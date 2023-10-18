"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # customer
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('order', views.order, name='order'),
    
    # account
    path('account', views.account, name='account'),
    path('shop', views.shop, name='shop'),
    
    # auth
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    
    
    # store
    path('store/products', views.Product, name='products'),
    path('store/add-product', views.addProduct, name='add-product'),
    path('store/invoice', views.invoice, name='invoice'),
    
    
]
