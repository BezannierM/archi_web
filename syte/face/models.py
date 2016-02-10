import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)