from django.db import models

# Create your models here.
class category(models.Model):
  category_name = models.CharField(max_length=100, unique = True)
  slug = models.CharField(max_length=100, unique = True)
  discription = models.TextField(max_length= 225)
  cat_image = models.ImageField(upload_to="Photos/categories",blank = True)