from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'email', 'service', 'website', 'created_at')
    search_fields = ('business_name', 'email', 'website')
    list_filter = ('created_at',)