from django.db import models

class Lead(models.Model):
    SERVICE_CHOICES = [
        ('google_ads', 'Google Ads'),
        ('meta_ads', 'Meta Ads'),
        ('linkedin_ads', 'Linked in Ads'),
        ('seo_aeo', 'SEO/AEO'),
        ('web_development', 'Web Development'),
        ('landing_page_optimization', 'Landing page Optimization'),
        ('go_high_level_automation', 'Go High Level Automation'),
    ]

    business_name = models.CharField(max_length=150)
    website = models.URLField(blank=True)
    email = models.EmailField()
    service = models.CharField(max_length=40, choices=SERVICE_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business_name} - {self.email}"

