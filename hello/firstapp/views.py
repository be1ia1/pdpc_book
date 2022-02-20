from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('Hello, World!')
    return HttpResponse('<h2>Головна</h2>')

def about(request):
    # return HttpResponse('Hello, World!')
    return HttpResponse('<h2>Про сайт</h2>')

def contacts(request):
    # return HttpResponse('Hello, World!')
    return HttpResponse('<h2>Контакти</h2>')

def products(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2>Продукт № {0}</h2>'.format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Max')
    output = "<h2>Користувач</h2><h3>id: {0} \
                  Ім\'я: {1} </h3>".format(id, name)
    return HttpResponse(output)