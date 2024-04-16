from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.CharField(max_length=500)
    phoneno=models.IntegerField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    catigory=models.CharField(max_length=100,default="")
    price=models.IntegerField()
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name
    
    