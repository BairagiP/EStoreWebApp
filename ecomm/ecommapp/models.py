from django.db import models

# Create your models here.
class Product(models.Model):
    CAT=((1,'Mobile'),(2,"Shoes"),(3,"Clothes"))
    name=models.CharField(max_length=20)
    price=models.FloatField(max_length=30)
    category=models.IntegerField(choices=CAT)
    pdeatils=models.CharField(max_length=50)
    is_Active=models.BooleanField(default=True,verbose_name='Available')
    def __str__(self):
        return self.name