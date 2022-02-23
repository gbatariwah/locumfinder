# from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from martor.models import MartorField
from core.models import User

JOB_TYPES = (('locum', 'Locum'), ('permanent', 'Permanent'),)

# Create your models here.
REGIONS = (

    ("northern", "Northern"),
    ("ashanti", "Ashanti"),
    ("western", "Western"),
    ("volta", "Volta"),
    ("eastern", "Eastern"),
    ("upper west", "Upper West"),
    ("upper east", "Upper East"),
    ("greater accra", "Greater Accra"),
    ("savannah", "Savannah"),
    ("north east", "North East"),
    ("bono east", "Bono East"),
    ("oti", "Oti"),
    ("ahafo", "Ahafo"),
    ("western north", "Western North"),
     )


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = MartorField()
    name_of_facility = models.CharField(max_length=255)
    type = models.CharField(max_length=9, choices=JOB_TYPES)
    name_of_town_or_city = models.CharField(max_length=50)
    region = models.CharField(max_length=50, choices=REGIONS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = MartorField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        message = self.message
        return message if len(message) < 70 else message[:70]
