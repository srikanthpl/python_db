from django.db import models

# Create your models here.
class Product(models.Model):
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=30,unique="True")
    Price=models.IntegerField()
    Quantity=models.IntegerField()
    
    class Meta:
        db_table="product"