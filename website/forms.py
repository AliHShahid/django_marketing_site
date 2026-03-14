from django import forms

from .models import Lead


class LeadCaptureForm(forms.Form):
    # Keep legacy field names so existing templates continue to post correctly.
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20, required=False)
    date = forms.DateField(required=False)
    package = forms.ChoiceField(choices=Lead.SERVICE_CHOICES)
    message = forms.CharField(required=False, widget=forms.Textarea)
    website = forms.URLField(required=False)

    def save(self):
        if not self.is_valid():
            raise ValueError("Cannot save an invalid LeadCaptureForm")

        return Lead.objects.create(
            business_name=self.cleaned_data["name"],
            email=self.cleaned_data["email"],
            service=self.cleaned_data["package"],
            message=self.cleaned_data.get("message", ""),
            website=self.cleaned_data.get("website", ""),
        )
