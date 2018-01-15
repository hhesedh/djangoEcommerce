# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import Product

# Create your views here.
def product_list(request):
    return render(request, 'catalog/product_list.html')
