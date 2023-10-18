from django.urls import path

from . import views as api

urlpatterns = [

    # shop
    path('user/get', api.shopUser, name='shop-user-api'),
    path('create/', api.shopRegister, name='shop-create-api'),


    # generals API
    path('data/area', api.getAreaData, name='get-area-api'),
    path('data/product-type', api.getProductTypeData,
         name='get-product-type-api'),
    path('data/product-category', api.getProductCategory,
         name='get-product-category-api'),

    # InputData
    path('create/input-data', api.createInputData, name='create-input-data-api'),
    path('get/input-invoice', api.getInputData, name='get-input-invoice-api'),


    # products 
    path('product/all', api.allProduct, name='product-all-api'),
    
    # address


]
