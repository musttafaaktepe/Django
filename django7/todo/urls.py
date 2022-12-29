from django.urls import path, include
from rest_framework import routers

from .views import (    
    todo_list_create,   
)

urlpatterns = [
    path('list-create/', todo_list_create),
    
]