from django.db import models



class Account(models.Model):
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)