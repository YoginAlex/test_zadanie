# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import traceback
from likedislike.models import *

def likedecor(cls):
    """Выбираем все лайки для данной модели
    """
    cls.likedislike = LikeDisLike.objects.filter(model_name=cls.__name__)
    return cls