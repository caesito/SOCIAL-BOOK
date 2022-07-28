from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
