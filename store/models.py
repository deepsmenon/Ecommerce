from django.db import models
from category.models import category

# Create your models here.
class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=100, unique=True)
    discription     = models.TextField(max_length=500, blank=True)
    price           = models.FloatField()
    images          = models.ImageField(upload_to="photos/Products")
    stock           = models.IntegerField()  # quantity of the products
    category        = models.ForeignKey(category, on_delete=models.CASCADE)
    created_date    = models.DateField(auto_now_add=True)
    modified_date   = models.DateField(auto_now=True)  # Use auto_now for modified date
    is_available    = models.BooleanField(default=True)

    quantity        = models.IntegerField(default=0)

    class Meta():
      verbose_name = "Products"
      verbose_name_plural = "Products"


    def __str__(self):
        return self.product_name


