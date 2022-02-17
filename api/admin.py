from django.contrib import admin
from .models import Products
# Register your models here.

class ProductsAdmin( admin.ModelAdmin ):
    list_display        = ( 'name', 'price' )
    list_display_links  = ( 'name', 'price' )
    search_fields       = ( 'name', 'price' )

admin.site.register( Products, ProductsAdmin )