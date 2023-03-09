from django.db import models

from accountapp.models import CustomUser


# Create your models here.
class Career(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='career')
    startdate = models.DateField(blank=False)
    enddate = models.DateField(blank=True, default=None)
    careercontent = models.CharField(max_length=10, blank=False)
    careertype = models.CharField(max_length=10, blank=False)
    careerinstitute = models.CharField(max_length=10, blank=False)
