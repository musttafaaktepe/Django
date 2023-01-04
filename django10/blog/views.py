from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Blog

from .serializers import CategorySerializer, BlogSerializer

class CategoryView(ModelViewSet):  # crud
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
