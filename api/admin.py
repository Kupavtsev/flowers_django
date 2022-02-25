from django.contrib import admin
from .models import Products, Rubric
# Register your models here.

class ProductsAdmin( admin.ModelAdmin ):
    list_display        = ( 'name', 'price', 'rubric' )
    list_display_links  = ( 'name', 'price', 'rubric' )
    search_fields       = ( 'name', 'price', 'rubric' )

admin.site.register( Products, ProductsAdmin )
admin.site.register(Rubric)