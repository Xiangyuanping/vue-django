from django.db import models

# Create your models here.

class User(models.Model):
    UserName=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
