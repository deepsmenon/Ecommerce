

from django.urls import include, path

from . import views


urlpatterns = [
    
    
    
    path('', views.store),
    path('Products/',include('products.urls')),
    
] 