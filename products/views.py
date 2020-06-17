# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products} )