from django.db import models


class Todolist(models.Model):
    data=models.CharField(max_length=40,blank=False,null=False)
    
    
    
    
