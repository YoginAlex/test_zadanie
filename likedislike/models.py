# -*- coding: utf-8 -*-
import datetime
from functools import wraps
from django.db import models
from django.utils import timezone

class LikeDisLike(models.Model):
    LIKEDISLIKE = (
        ('like', 'like'),
        ('dislike', 'dislike'),
    )

    datetime_add = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now(), verbose_name="Дата внесения в базу")
    model_name = models.TextField(blank=False, verbose_name="Класс объекта")
    obj_id = models.IntegerField(blank=False, null=False, verbose_name="ID объекта")
    like_dislike = models.CharField(choices=LIKEDISLIKE, blank=False, max_length=10)

    def __unicode__(self):
        return u'%s' % (self.model_name)