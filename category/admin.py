from django.contrib import admin
from . models import category

class categoryAdmin(admin.ModelAdmin):
  list_display = ("category_name",'slug','discription')
  prepopulated_fields = {'slug': ('category_name',)}

# Register your models here.
admin.site.register(category,categoryAdmin)
