from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class User(models.Model):
    login_name = models.CharField(max_length=200)
    login_password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    photo = models.ImageField()
    user_created = models.TimeField (blank=False, null=False, default=datetime.datetime.now())
    other = models.CharField(max_length=200)

class Roles(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE())
    roll_type = models.CharField(max_length=200)