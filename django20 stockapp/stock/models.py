from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=25, unique= True)
    image = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=23, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="b_products")
    stock = models.PositiveSmallIntegerField(blank=True, default=0)
    createds = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Firm(models.Model):
    name = models.CharField(max_length=23, unique=True)
    phone = models.CharField(max_length=25)
    adress = models.CharField(max_length=252)
    image = models.TextField()

    def __str__(self):
        return self.name

class Purchases(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firm=models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, related_name="purchases")
    brand=models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name="b_purchases")
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,  related_name="purchase")
    quantity=models.PositiveSmallIntegerField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    price_total=models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return f'{self.product}-{self.quantity}'
    
class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='b_sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sale')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
        return f'{self.product} - {self.quantity}'