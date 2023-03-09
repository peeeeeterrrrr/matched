from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=11,validators=[MinLengthValidator(11), MaxLengthValidator(11)],  unique=True, blank=False)
    userrealname = models.CharField(max_length=10, unique=False, blank=False)
    email = models.EmailField(max_length=25, unique=True, blank=False)

    def annonymusname(self):
        string_name = str(self.userrealname)
        return string_name[0] + '*' + string_name[-1]
    def annonymusphone(self):
        string_phone = str(self.username)
        return '010-' + string_phone[0] + '***-***' + string_phone[-1]