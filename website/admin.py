from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','package', 'company','phone', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)