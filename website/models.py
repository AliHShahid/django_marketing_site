from django.db import models

class Lead(models.Model):
    PACKAGE_CHOICES = [
        ('1000', '1000 items'),
        ('2000', '2000 items'),
        ('3000', '3000 items'),
        ('custom', 'Custom items'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True)
    package = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

