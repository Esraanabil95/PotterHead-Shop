# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.



def maps(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'maps.html', { 'mapbox_access_token': mapbox_access_token })

