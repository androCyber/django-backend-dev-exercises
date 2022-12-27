from unicodedata import name
from django.db import models

# Create your models here.

class Menu(models.Model):
    
    ad=models.CharField(max_length=100)
    mutfak=models.CharField(max_length=100)
    fiyat=models.IntegerField()
    
    def __str__(self):
        return self.name + " : "+ self.cuisine

    