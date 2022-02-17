from django.shortcuts import render

# Create your views here.
def index(request):
    # bbs             = Bb.objects.all()
    # rubrics         = Rubric.objects.all()
    # context         = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'flowers/index.html')