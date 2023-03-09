from datetime import datetime

from django.db import models

from accountapp.models import CustomUser


# Create your models here.
class Scholarship(models.Model):
    statechoice = (
        ('attend', '재학'),
        ('quit', '제적/자퇴'),
        ('off', '휴학'),
        ('graduate', '졸업'),
    )
    state = models.CharField(max_length=10, choices=statechoice, blank=False)
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='scholarship')
    startdate = models.DateField(blank=False)
    enddate = models.DateField(blank=True, default=None)
    school = models.CharField(max_length=10, blank=False)
    major = models.CharField(max_length=10, blank=False)
    schoolverificationimage= models.ImageField(upload_to='schoolverification', blank= True, default='')