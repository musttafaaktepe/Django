from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    bio=models.TextField(blank=True)
    image=models.ImageField(upload_to='profile', blank=True, null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    #cascade, setnull setDefault donothing protect

    def __str__(self):
        return self.user.username

class Address(models.Model):
    name= models.CharField(max_length=20)
    adress= models.CharField(max_length=150)
    city= models.CharField(max_length=20)
    phone= models.CharField(max_length=20)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=100)
    user= models.ManyToManyField(User)

    def __str__(self):
        return self.name
