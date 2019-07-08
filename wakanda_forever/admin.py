# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:23:26 2019

@author: 蘇
"""

from django.contrib import admin
from wakanda_forever.models import Tag,Author,Article
 
# Register your models here.
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Article)