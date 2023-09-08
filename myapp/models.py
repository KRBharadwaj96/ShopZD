from django.db import models

# Create your models here.
class categorydb(models.Model):
    Name = models.CharField(max_length=200,null=True,blank=True)
    Image = models.ImageField(null=True,blank=True)
    Description = models.CharField(max_length=500,null=True,blank=True)

class productdb(models.Model):
    Select = models.CharField(max_length=300,null=True,blank=True)
    Product = models.CharField(max_length=200,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=500,null=True,blank=True)
    Brand = models.CharField(max_length=100,blank=True,null=True)
    Image = models.ImageField(null=True,blank=True)

class contactdb(models.Model):
    Fname = models.CharField(max_length=100,null=True,blank=True)
    Lname = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Subject = models.CharField(max_length=200, null=True, blank=True)
    Message = models.CharField(max_length=1000, null=True, blank=True)


