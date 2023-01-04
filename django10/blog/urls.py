from django.urls import path, include

from .views import CategoryView
from rest_framework import routers
from .views import CategoryView, BlogView

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('blog', BlogView)



urlpatterns = [
    path('',  include(router.urls))
]