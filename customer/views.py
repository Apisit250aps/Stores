from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, 'customer/home.html')

def account(request):
    
    return render(request, 'customer/account.html')

def shop(request):
    
    return render(request, 'customer/shop.html')

def cart(request):
    
    return render(request, 'customer/cart.html')

def order(request):
    
    return render(request, 'customer/order.html')

