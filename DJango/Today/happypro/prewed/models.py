from django.db import models

# Create your models here.

class Customer(models.Model):
    Name=models.CharField(max_length=30)
    Number=models.IntegerField()
    Address=models.IntegerField()
    
    class Meta:
        db_table="prewed"