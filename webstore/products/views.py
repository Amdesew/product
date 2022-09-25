from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

def products(request):
    products = Products.objects.all()
    return render(request, 'index.html',
                  {'products': products})