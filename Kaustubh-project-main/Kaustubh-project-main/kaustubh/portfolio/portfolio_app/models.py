from django.db import models
from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')  # can be PDF or image

    def __str__(self):
        return self.title

# Create your models here.
