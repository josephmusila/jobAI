from django.db import models

# Create your models here.

class Job(models.Model):
    job_name = models.CharField(max_length=255)
    job_description = models.TextField(max_length=3000)
    job_requirements=models.TextField(max_length=3000)
    job_responsibilities=models.TextField(max_length=3000)


