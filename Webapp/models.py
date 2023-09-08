from django.db import models

# Create your models here.
class registerdb(models.Model):
    Name = models.CharField(max_length=200,blank=True,null=True)
    Email = models.EmailField(max_length=400,blank=True,null=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(null=True,blank=True)

class cartdb(models.Model):
    Uname = models.CharField(max_length=120,blank=True,null=True)
    Prod_name = models.CharField(max_length=200,blank=True,null=True)
    Description = models.CharField(max_length=300,null=True, blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Image = models.ImageField(null=True,blank=True)

class checkoutdb(models.Model):
    Country= models.CharField(max_length=100,blank=True,null=True)
    Fname= models.CharField(max_length=100,blank=True,null=True)
    Address= models.CharField(max_length=300,blank=True,null=True)
    State = models.CharField(max_length=100,blank=True,null=True)
    Zip = models.CharField(max_length=100,blank=True,null=True)
    Email = models.EmailField(max_length=100,blank=True,null=True)
    Mobile = models.CharField(max_length=100,blank=True,null=True)

