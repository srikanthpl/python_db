from django.db import models

# Create your models here.
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eloc=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ename}"