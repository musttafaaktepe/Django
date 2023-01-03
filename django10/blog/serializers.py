from rest_framework.viewsets import ModelViewSet


from .models import Category
from .serializers import CategorySerializer, BlogSerializer



class CategoryView(ModelViewSet):  # crud
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



