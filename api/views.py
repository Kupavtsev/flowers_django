# from django.shortcuts import render
from django.http import JsonResponse
from .models import Products
from .serializers import ProductsSerializer

# Create your views here.
def api_products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)