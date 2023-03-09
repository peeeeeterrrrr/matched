from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accountapp.models import CustomUser


class Baseinformation(models.Model):
    sexchoice=(('male', '남'), ('female', '여'),)
    militarychoice=(('done', '복무완료'), ('yet', '미복무'),)
    profileimage = models.ImageField(upload_to='profile', blank=True, default='')
    customuser = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='baseinformation')
    age= models.IntegerField(validators=[MinValueValidator(19), MaxValueValidator(30)], blank=False)
    sex= models.CharField(max_length=6, choices=sexchoice, blank=False)
    military = models.CharField(max_length=6, choices=militarychoice, blank=False)
    location = models.CharField(max_length=10, blank=False)
    introduction =models.TextField(max_length=200 ,null=True)

# Create your models here.
