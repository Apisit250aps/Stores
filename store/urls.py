from django.urls import path

from . import views as api

urlpatterns = [
    
    # shop
    path('user/get', api.shopUser, name='shop-user-api'),
    path('create/', api.shopRegister, name='shop-create-api'),
    
    
    # generals API
    path('data/area', api.getAreaData, name='get-area-api'),
    path('data/product-type', api.getProductTypeData, name='get-product-type-api'),
    
    
    # address
   
    
]
