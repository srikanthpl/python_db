from django.db import models

# Create your models here.
class Product(models.Model):
    pid=models.IntegerField
    pname=models.CharField(44)
    price=models.FloatField()
    
    