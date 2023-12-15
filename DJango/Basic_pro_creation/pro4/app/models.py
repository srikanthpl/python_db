from django.db import models

# Create your models here.
class Employee(models.Model):
    Ename=models.CharField(max_length=32)
    Eloc=models.CharField(max_length=32)
    Esal=models.FloatField()
