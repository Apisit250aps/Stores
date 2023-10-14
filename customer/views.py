
from django.shortcuts import render, redirect
import json
import pytz
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.db.models import Q
from django.views.decorators.http import require_POST

import random

from . import models
from . import serializers

# Create your views here.


@csrf_exempt
@api_view(["POST",])
@permission_classes((AllowAny,))
def userLogin(request):

    username = request.data['username']
    password = request.data['password']

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:
        if user.is_active:
            status = True
            msg = 'user is logined'
            login(request, user)
        else:
            status = False
            msg = 'Currently, This user is not active'
    else:
        status = False
        msg = 'Error wrong username/password'

    return Response({'status': status, 'message': msg})


@csrf_exempt
@api_view(["GET",])
@permission_classes((AllowAny, IsAuthenticated))
def userLogout(request):
    logout(request)
    return redirect("index")


@csrf_exempt
@api_view(["POST", ])
@permission_classes((AllowAny,))
def userRegister(request):
    email = request.data['email']
    username = request.data['username']
    password = request.data['password']

    try:
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )

        if user:
            status = True
            message = "Register Successfully!"
        else:
            status = False
            message = "Register Fail!"

    except Exception as err:
        status = False
        message = "Something is error!"

        print(err)

    return Response(
        {
            "status": status,
            "message": message
        }
    )


# Customers

@csrf_exempt
@api_view(["POST",])
@permission_classes((AllowAny, IsAuthenticated))
def registerCustomer(request):
    status = True
    message = ""
    user = User.objects.get(username=request.user.username)
    customer_fname = request.data['fname']
    customer_lname = request.data['lname']
    customer_tel = request.data['tel']
    customer_fax = request.data['fax']
    customer_email = request.data['email']
    customer_remark = request.data['remark']
    customer_province = request.data['province']
    customer_district = request.data['district']
    customer_sub_district = request.data['sub_district']
    customer_zip = request.data['zip']
    customer_address = request.data['address']

    customer_contact = customer_fname+" "+customer_lname
    customer_code = "TEMP"

    try:
        customer = models.CustomerData.objects.create(
            user=user,
            customer_code=customer_code,
            customer_contact=customer_contact,
            customer_address=customer_address,
            customer_sub_district=customer_sub_district,
            customer_district=customer_district,
            customer_province=customer_province,
            customer_zip=customer_zip,
            customer_tel=customer_tel,
            customer_fax=customer_fax,
            customer_email=customer_email,
            customer_remark=customer_remark,
        )
        if customer:
            id = int(customer.id)
            num = 10000
            cha = 'CT'
            code = cha+str(num+id)
            models.CustomerData.objects.filter(id=id).update(customer_code=code)
            status = True
            message = "Success"
        else :
            status = False
            message = "Error"
        
    except Exception as err:
        models.CustomerData.objects.get(id=id).delete()
        print(err)
        status = False
        message = "Error"

    return Response(
        {
            "status": status,
            "message": message
        }
    )

@csrf_exempt
@api_view(["POST",])
@permission_classes((AllowAny, IsAuthenticated))
def editCustomer(request):
    status = True
    message = ""
    user = User.objects.get(username=request.user.username)
    customer_fname = request.data['fname']
    customer_lname = request.data['lname']
    customer_tel = request.data['tel']
    customer_fax = request.data['fax']
    customer_email = request.data['email']
    customer_remark = request.data['remark']
    customer_province = request.data['province']
    customer_district = request.data['district']
    customer_sub_district = request.data['sub_district']
    customer_zip = request.data['zip']
    customer_address = request.data['address']

    customer_contact = customer_fname+" "+customer_lname
    

    try:
        customer = models.CustomerData.objects.filter(user=user).update(
            customer_contact=customer_contact,
            customer_address=customer_address,
            customer_sub_district=customer_sub_district,
            customer_district=customer_district,
            customer_province=customer_province,
            customer_zip=customer_zip,
            customer_tel=customer_tel,
            customer_fax=customer_fax,
            customer_email=customer_email,
            customer_remark=customer_remark,
        )
        
        if customer:
            status = True
            message = "Success"
        else :
            status = False
            message = "Error"
        
    except Exception as err:
        print(err)
        status = False
        message = "Error"

    return Response(
        {
            "status": status,
            "message": message
        }
    )

@csrf_exempt
@api_view(["GET",])
@permission_classes((AllowAny, IsAuthenticated))
def getUserCustomer(request):
    user = User.objects.get(username=request.user.username)
    print(user)
    try:
        customer = models.CustomerData.objects.filter(user=user)
        customerSerializer = serializers.CustomerDataSerializer(
            customer, many=True)
        data = customerSerializer.data[0]
    except Exception as err:
        print(err)
        data = None

    return Response(
        {
            "status": True,
            "data": data
        }
    )
