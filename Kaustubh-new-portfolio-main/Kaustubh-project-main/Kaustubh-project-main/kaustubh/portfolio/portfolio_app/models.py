from django.db import models
from django.db import models

from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issued_by = models.CharField(max_length=255)  # Fixed field name
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')  # Stores PDF or images

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=255)
    applicant = models.CharField(max_length=255)
    updated_date = models.DateField()
    resume_file = models.FileField(upload_to='resume/')  # can be PDF or image

    def __str__(self):
        return self.title
# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
