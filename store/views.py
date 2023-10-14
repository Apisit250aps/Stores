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
# Create your views here.

# Authentication

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
    product_type = request.data['product_type']
    shop_name = request.data['shop_name']
    shop_contact = request.data['shop_contact']
    shop_area = request.data['shop_area']
    shop_address = request.data['shop_address']
    shop_sub_district = request.data['shop_sub_district']
    shop_district = request.data['shop_district']
    shop_province = request.data['shop_province']
    shop_zip = request.data['shop_zip']
    shop_tel = request.data['shop_tel']
    shop_fax = request.data['shop_fax']
    shop_email = request.data['shop_email']
    shop_remark = request.data['shop_remark']
    
    try :
        shop = models.ShopData.objects.create(
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

        if shop:
            message = "success"
        else :
            message = "fail"
            status = False

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
