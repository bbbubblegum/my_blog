# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:56:06 2019

@author: 蘇
"""

"""wakanda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

#具体app下的url 配置
urlpatterns = [
    #正则表达式，注意其实和结束符之间的‘/’！！
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_id,name='article_id'),
    url(r'^login/', views.login,name='login'),
#    url(r'^tools/scripts/(?P<script_id>[0-9]+)$',views.script_id,name='scripts')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #没有这一句无法显示上传的图片
app_name = 'wakanda_forever'