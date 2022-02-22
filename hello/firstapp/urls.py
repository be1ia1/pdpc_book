from django.urls import path
# from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('details/', views.details),
    path('m404', views.m404)
    # path('', views.index, name='firstapp'),
    # re_path(r'^about', views.about, name='about'),
    # re_path(r'^contacts', views.contacts, name='contacts'),
    # path('products/', views.products),
    # path('products/<int:productid>/', views.products, name='products'),
    # path('users/', views.users),
    # path('users/<int:id>/<str:name>/', views.users, name='users'),
    # path('details/', views.details, name='details')
    # re_path(r'^products/$', views.products, name='dproducts'),
    # re_path(r'^products/(?P<productid>\d+)', views.products, name='products'),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)', views.users, name='users')
]