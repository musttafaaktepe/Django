from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category

class CategoryView(ModelViewSet):
    querset=Category.objects.all()
    serializer_class=None