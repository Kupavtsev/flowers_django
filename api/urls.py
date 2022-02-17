from django.urls import path

from .views import api_products

urlpatterns = [
    path('api/products', api_products),
]