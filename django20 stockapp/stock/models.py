from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)

# Create your models here.
