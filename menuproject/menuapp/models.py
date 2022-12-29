from unicodedata import name
from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name=models.CharField(max_length=200)

class Menu(models.Model):
    
    ad=models.CharField(max_length=100)
    mutfak=models.CharField(max_length=100)
    fiyat=models.IntegerField()
    kategori_id=models.ForeignKey(MenuCategory,on_delete=models.PROTECT, default=None)
    
    def __str__(self):
        return self.name + " : "+ self.cuisine

    