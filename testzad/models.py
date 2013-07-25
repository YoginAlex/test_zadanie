# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone
from likedislike.decorator import likedecor

@likedecor
class Testzad(models.Model):
    datetime_add = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now, verbose_name="Дата внесения в базу")
    text = models.TextField(blank=True, verbose_name="Комментарий к объекту")

    def __unicode__(self):
        return u'%s - %s' % (self.datetime_add, self.text)
