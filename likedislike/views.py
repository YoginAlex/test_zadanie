# -*- coding: utf-8 -*-
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import traceback
from likedislike.models import *

def setlike(request):
    """Пишем в базу like/dislike"""
    #Тут лучше всего делать через Ajax
    if request.method == 'GET':
        #тут надо добавить больше проверок
        #но на минуту представим, что всё ОК
        like_model = request.GET['model']
        like_obj_id = int(request.GET['obj_id'])
        try:
            #ищем запись
            likedislike = LikeDisLike.objects.filter(model_name=like_model).filter(obj_id=like_obj_id).order_by('-datetime_add')[0]
        except:
            #если нет еще записи
            likedislike = LikeDisLike(model_name=like_model, obj_id=like_obj_id, like_dislike='like')
            likedislike.save()
        else:
            #тут тоже надо добавить много проверок
            if likedislike.like_dislike == 'like':
                likedislike.like_dislike = 'dislike'
                likedislike.save()
            else:
                likedislike.like_dislike = 'like'
                likedislike.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

