from django.urls import path
from .views import *

urlpatterns = [
    path('',todo_list,name='todo_list' ),
    path('add/',todo_add,name='todo_add' ),

]