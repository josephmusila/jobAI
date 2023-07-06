from django.contrib import admin
from . import models

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    model   = models.Job
    list_display =('id', 'job_name', 'job_description','job_responsibilities','job_requirements')


admin.site.register(models.Job, JobAdmin)




