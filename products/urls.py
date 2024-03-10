from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.listproducts, name='listproducts'),
    path('edit/', views.editproducts, name='editproducts'),
]
    