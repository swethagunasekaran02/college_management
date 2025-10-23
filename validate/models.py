from django.db import models

# Create your models here.
class validation(models.Model):
    
    name=models.CharField(max_length=222)
    age=models.IntegerField(default=0)
    address=models.CharField(max_length=220)
