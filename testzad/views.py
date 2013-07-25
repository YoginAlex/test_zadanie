# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.template import RequestContext
import traceback
from testzad.models import *

def home(request):
    try:
        obj = Testzad.objects.all()
    except:
        obj = {}
        # print traceback.format_exc()

    return render_to_response(
    'home.html', 
    {
        'obj': obj,
    },
    context_instance=RequestContext(request))    
