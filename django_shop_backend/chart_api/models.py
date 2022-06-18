from django.db import models

# Create your models here.
class Financial(models.Model):
    month = models.CharField(max_length=32)
    revenue = models.IntegerField()
