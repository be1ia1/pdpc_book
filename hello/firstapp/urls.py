from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='firstapp'),
    re_path(r'^about', views.about, name='about'),
    re_path(r'^contacts', views.contacts, name='contacts'),
    path('products/', views.products),
    path('products/<int:productid>/', views.products, name='products'),
    path('users/', views.users),
    path('users/<int:id>/<str:name>/', views.users, name='users')
    # re_path(r'^products/$', views.products, name='dproducts'),
    # re_path(r'^products/(?P<productid>\d+)', views.products, name='products'),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)', views.users, name='users')
]