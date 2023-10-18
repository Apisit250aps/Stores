from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Customer
@login_required
def index(request):

    return render(request, 'customer/home.html')


@login_required
def account(request):

    return render(request, 'customer/account.html')


@login_required
def shop(request):

    return render(request, 'customer/shop.html')


@login_required
def cart(request):

    return render(request, 'customer/cart.html')


@login_required
def order(request):

    return render(request, 'customer/order.html')




# Store
def Product(request):
    
    return render(request, 'store/products.html')

def addProduct(request):
    
    return render(request, 'store/add-product.html')


def invoice(request):
    
    return render(request, 'store/invoice.html')

# Auth

def login(request):

    return render(request, 'auth/login.html')

def register(request):

    return render(request, 'auth/register.html')
