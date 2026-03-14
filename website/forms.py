from django import forms
from django.db import DatabaseError, connection

from .models import Lead


DEFAULT_SERVICE_CHOICES = [
    ("google_ads", "Google Ads"),
    ("meta_ads", "Meta Ads"),
    ("linkedin_ads", "Linked in Ads"),
    ("seo_aeo", "SEO/AEO"),
    ("web_development", "Web Development"),
    ("landing_page_optimization", "Landing page Optimization"),
    ("go_high_level_automation", "Go High Level Automation"),
]


def get_lead_service_choices():
    model_choices = getattr(Lead, "SERVICE_CHOICES", None)
    if model_choices:
        return model_choices

    try:
        service_field = Lead._meta.get_field("service")
        field_choices = getattr(service_field, "choices", None)
        if field_choices:
            return field_choices
    except Exception:
        pass

    return DEFAULT_SERVICE_CHOICES


class LeadCaptureForm(forms.Form):
    SERVICE_CHOICES = get_lead_service_choices()

    # Keep legacy field names so existing templates continue to post correctly.
    business_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField()
    service = forms.ChoiceField(choices=SERVICE_CHOICES, required=False)

    # Legacy aliases still used by older templates.
    name = forms.CharField(max_length=150, required=False)
    contact_name = forms.CharField(max_length=150, required=False)
    package = forms.ChoiceField(choices=SERVICE_CHOICES, required=False)

    phone = forms.CharField(max_length=20, required=False)
    date = forms.DateField(required=False)
    message = forms.CharField(required=False, widget=forms.Textarea)
    website = forms.URLField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        # Normalize company/name input from either new or legacy templates.
        business_name = (
            cleaned_data.get("business_name")
            or cleaned_data.get("contact_name")
            or cleaned_data.get("name")
            or ""
        ).strip()
        if not business_name:
            self.add_error("business_name", "This field is required.")
        else:
            cleaned_data["business_name"] = business_name

        # Normalize service input from either new or legacy templates.
        service = cleaned_data.get("service") or cleaned_data.get("package")
        if not service:
            self.add_error("service", "Please select a service.")
        else:
            cleaned_data["service"] = service

        return cleaned_data

    def _build_lead_values(self):
        business_name = self.cleaned_data["business_name"]
        contact_name = (self.cleaned_data.get("contact_name") or "").strip()
        service = self.cleaned_data["service"]
        website = self.cleaned_data.get("website", "")
        message = self.cleaned_data.get("message", "")
        phone = self.cleaned_data.get("phone", "")

        return {
            "business_name": business_name,
            "name": contact_name or business_name,
            "email": self.cleaned_data["email"],
            "service": service,
            "package": service,
            "website": website,
            "company": business_name,
            "message": message,
            "phone": phone,
        }

    def _save_with_model_fields(self, lead_values):
        lead_field_names = {
            field.name
            for field in Lead._meta.fields
            if getattr(field, "concrete", False)
        }

        lead_data = {
            field_name: value
            for field_name, value in lead_values.items()
            if field_name in lead_field_names
        }

        return Lead.objects.create(**lead_data)

    def _save_with_database_columns(self, lead_values):
        table_name = Lead._meta.db_table

        with connection.cursor() as cursor:
            table_description = connection.introspection.get_table_description(cursor, table_name)

        database_columns = {column.name for column in table_description}
        insertable_columns = [
            column_name
            for column_name, value in lead_values.items()
            if column_name in database_columns
        ]

        if not insertable_columns:
            raise DatabaseError("No compatible Lead columns were found in the database.")

        quoted_table_name = connection.ops.quote_name(table_name)
        quoted_columns = ", ".join(
            connection.ops.quote_name(column_name)
            for column_name in insertable_columns
        )
        placeholders = ", ".join(["%s"] * len(insertable_columns))
        values = [lead_values[column_name] for column_name in insertable_columns]

        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO {quoted_table_name} ({quoted_columns}) VALUES ({placeholders})",
                values,
            )

        return lead_values

    def save(self):
        if not self.is_valid():
            raise ValueError("Cannot save an invalid LeadCaptureForm")

        lead_values = self._build_lead_values()

        try:
            return self._save_with_model_fields(lead_values)
        except (DatabaseError, TypeError):
            return self._save_with_database_columns(lead_values)
