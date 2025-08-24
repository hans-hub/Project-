from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=[
            ('applied', 'Applied'),
            ('interview', 'Interview'),
            ('offer', 'Offer'),
            ('rejected', 'Rejected'),
        ],
        default='applied'
    )
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} at {self.company_name}"

class Note(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name="notes")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.application}"
