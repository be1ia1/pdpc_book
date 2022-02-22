from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Create your views here.

from django.http import * 

def m304(request): 
    return HttpResponseNotModified() 

def m400(request): 
    return HttpResponseBadRequest("<h2>Bad Request</h2>") 

def m403(request): 
    return HttpResponseForbidden("<h2>ForЬidden</h2>") 

def m404(request): 
    return HttpResponseNotFound("<h2>Not Found</h2>") 

def m405(request): 
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>") 

def m410(request): 
    return HttpResponseGone("<h2>Content is no longer here</h2>") 

def m500(request): 
    return HttpResponseServerError("<h2>Something is wrong</h2>") 

def index(request):
    # return HttpResponse('Hello, World!')
    return HttpResponse('<h2>Головна</h2>')

def about(request):
    # return HttpResponse('Hello, World!')
    return HttpResponse('<h2>Про сайт</h2>')

def contacts(request):
    # return HttpResponse('Hello, World!')
    # return HttpResponse('<h2>Контакти</h2>')
    return HttpResponseRedirect('/about')

def details(request):
    return HttpResponsePermanentRedirect('/')

def products(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2>Продукт № {0} Категорія: {1}</h2>'.format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get('id', 1)
    name = request.GET.get('name', 'Max')
    output = "<h2>Користувач</h2><h3>id: {0} \
                  Ім\'я: {1} </h3>".format(id, name)
    return HttpResponse(output)