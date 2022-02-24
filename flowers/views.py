from django.shortcuts import render

from api.models import Products

# Create your views here.
def index(request):
    products    = Products.objects.all()
    print('\n', products, '\n')
    # flw = {'пионы', 'гвоздики'}
    context     = {"products": products}
    return render(request, 'flowers/index.html', context)