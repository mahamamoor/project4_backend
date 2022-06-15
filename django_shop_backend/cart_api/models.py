from django.db import models

# Create your models here.
class Cart(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=50)
    image = models.TextField(default='')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
