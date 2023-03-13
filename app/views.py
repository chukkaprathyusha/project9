from django.shortcuts import render

# Create your views here.
def jinja_first(request):
    d={'name':'prathyu'}
    return render(request,'jinja_first.html',context=d)
