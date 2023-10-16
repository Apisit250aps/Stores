from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

import json
import random

from . import models
from . import serializers
from .method import *
# Create your views here.

# Authentication

@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def shopUser(request):
    user = User.objects.get(username=request.user.username)
    try :
        shop = models.ShopData.objects.filter(user=user)
        shopSerializer = serializers.ShopDataSerializer(shop, many=True)
        dataSerialized = shopSerializer.data
        data = []
        for item in dataSerialized:
            item = dict(item)
            item['user'] = User.objects.get(id=int(item['user'])).username
            item['product_type'] = models.ProductTypeData.objects.get(id=int(item['product_type'])).product_type
            item['shop_area'] = models.AreaData.objects.get(id=int(item['shop_area'])).area_name
            
            data.append(item)
              
    except Exception as err:
        print(err)
        data = None

    return Response(
        {
            "status":True,
            "data":data,
        }
    )


@csrf_exempt
@api_view(["POST", ])
@permission_classes((AllowAny,))
def shopRegister(request):
    # Auth
    user = User.objects.get(username=request.user.username)
    
    
    # response
    status = True
    message = ""
    
    # request data
    shop_product_type = request.data['shop_product_type']
    shop_name = request.data['shop_name']
    shop_contact = f"{request.data['fname']} {request.data['lname']}"
    area = request.data['shop_area']
    shop_address = request.data['shop_address']
    shop_sub_district = request.data['shop_sub_district']
    shop_district = request.data['shop_district']
    shop_province = request.data['shop_province']
    shop_zip = request.data['shop_zip']
    shop_tel = request.data['shop_tel']
    shop_fax = request.data['shop_fax']
    shop_email = request.data['shop_email']
    shop_remark = request.data['shop_remark']
    
    product_type = models.ProductTypeData.objects.get(id=int(shop_product_type))
    shop_area = models.AreaData.objects.get(id=int(area))
    
    
    
    try :
        if (models.ShopData.objects.filter(user=user).count() == 0):
            shop = models.ShopData.objects.create(
                user=user,
                product_type=product_type,
                shop_name=shop_name,
                shop_contact=shop_contact,
                shop_area=shop_area,
                shop_address=shop_address,
                shop_sub_district=shop_sub_district,
                shop_district=shop_district,
                shop_province=shop_province,
                shop_zip=shop_zip,
                shop_tel=shop_tel,
                shop_fax=shop_fax,
                shop_email=shop_email,
                shop_remark=shop_remark,
            )
            print(ShopCode(shop_product_type, area, shop.id))
            if shop:
                models.ShopData.objects.filter(id=shop.id).update(shop_code=ShopCode(shop_product_type, area, shop.id))
                message = "success"
            else :
                message = "fail"
                status = False
        else :
            status = False
            message = "You have a shop!"

    except Exception as err:
        status = False
        message = "something is error!"
        print(err)
    
    return Response(
        {
            "status":status,
            "message":message
        }
    )

# General API Shop
@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def getProductTypeData(request):
    product_type = models.ProductTypeData.objects.all()
    productTypeSerializer = serializers.ProductTypeDataSerializer(product_type, many=True)
    data = productTypeSerializer.data
    
    return Response(
        {
            "status":True,
            "data":data
        }
    )

@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def getAreaData(request):
    area = models.AreaData.objects.all()
    areaSerializer = serializers.AreaDataSerializer(area, many=True)
    data = areaSerializer.data
    
    return Response(
        {
            "status":True,
            "data":data,
        }
    )










# Address
@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def getProvince(request):
    data = {}
    msg = 'already get thai province'
    

    # get thai province file
    result = finders.find('data/json/thai_province.json')
    with open(result, encoding='utf8') as f:
        province = json.load(f)

    data['province'] = province.keys()

    return Response({'status': True, 'message': msg, 'data': data})


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def getDistrict(request):
    data = {}
    msg = 'already get thai district'
    

    # get thai province file
    result = finders.find('data/json/thai_province.json')
    with open(result, encoding='utf8') as f:
        province = json.load(f)

    province_selected = request.data['province']
    data['district'] = province[province_selected].keys()

    return Response({'status': True, 'message': msg, 'data': data})


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def getTambon(request):
    data = {}
    msg = 'already get thai tambon'
    

    # get thai province file
    result = finders.find('data/json/thai_province.json')
    with open(result, encoding='utf8') as f:
        province = json.load(f)

    province_selected = request.data['province']
    district_selected = request.data['district']

    data['tambon'] = province[province_selected][district_selected]

    return Response({'status': True, 'message': msg, 'data': data})
