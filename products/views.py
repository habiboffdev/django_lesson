from django.shortcuts import render
from django.http.response import HttpResponse as response
from .models import Product
# Create your views here.

def hello_world(request, ism):
    return response(f"Hello, {ism}")      

def print_products(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'all_products': all_products,'variable': 'this is sent'})
# url qo'shilar - products/available - bunda sotuvda borlarini
# url qo'shilar - products/not_available - bunda sotuvda yoq
# photo_link degan xususiyatini yozing
# 