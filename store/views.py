from django.shortcuts import get_object_or_404, render
from store.models import Product
from category.models import category  

def store(request, category_url=None):
    print('category_url : ', category_url)
    categories = None  
    
    if category_url is not None:
        print("printing category : ", category.category_name)
        categories = get_object_or_404(category, slug=category_url)
        print("printing products :::", categories)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True)
    
        product_count = products.count()
    
    context = {
        "products": products,
        "product_count": product_count,
        "category_url": category_url,
        "categories": categories,
    }
    
    return render(request, "store.html", context)