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
from django.conf.urls import url,include
from django.contrib import admin
from wakanda_forever import views
from django.conf.urls.static import static
from django.conf import settings


#项目Url的总路径
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wakanda/',include('wakanda_forever.urls',namespace='wakanda_forever')),
    url(r'^$',views.index ,name='index'),
    url(r'^comments/', include('comment.urls',namespace='comment')),
    url(r'^login/',include('login.urls',namespace='login')),
    url(r'ckeditor/', include('ckeditor_uploader.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #没有这一句无法显示上传的图片

