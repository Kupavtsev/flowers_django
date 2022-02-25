from multiprocessing import context
from django.shortcuts import render

from api.models import Products, Rubric

# Create your views here.
def index(request):
    products    = Products.objects.all()
    # print('\n', products, '\n')
    # flw = {'пионы', 'гвоздики'}
    context     = {"products": products}
    return render(request, 'flowers/index.html', context)

def by_rubric(request, rubric_id):
    products    = Products.objects.filter(rubric=rubric_id)
    rubrics     = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'products': products, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'flowers/products.html', context)