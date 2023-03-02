from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=10, unique=True, blank=False)
    userrealname = models.CharField(max_length=10, unique=False, blank=False)
    email = models.EmailField(max_length=25, unique=True, blank=False)
    phone_number = models.CharField(max_length=20, unique=True, blank=False, null=False)
