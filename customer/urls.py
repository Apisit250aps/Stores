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
from . import views as api

urlpatterns = [

    # authentications
    path('login', api.userLogin, name='login-api'),
    path('logout', api.userLogout, name='logout-api'),
    path('register', api.userRegister, name='register-api'),
    
    
    # customers
    path('auth/edit', api.editCustomer, name='customer-edit-api'),
    path('auth/create', api.registerCustomer, name='customer-register-api'),
    path('auth/data', api.getUserCustomer, name='customer-user-api')
    
]
