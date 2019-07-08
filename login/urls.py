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

#具体app下的url 配置

urlpatterns = [
    #正则表达式，注意其实和结束符之间的‘/’！！
    url(r'^$', views.login,name='login'),
    url(r'^register/', views.register,name='register'),
    url(r'^logout/', views.logout,name='logout'),
]
app_name = 'login'