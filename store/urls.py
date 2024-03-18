

from django.urls import path,include
from . import views

urlpatterns = [
    
    
    
    path('', views.store),
    path('<slug:category_url>',views.store, name="products_by_category"),
    path('Products/',include('products.urls')),
    
] 