from django.db import models

class Inquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    business_email = models.EmailField()
    company_name = models.CharField(max_length=200)
    state_region = models.CharField(max_length=100, blank=True, null=True)
    country_region = models.CharField(max_length=100, blank=True, null=True)
    inquiry = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.first_name} {self.last_name}"
