# from django.contrib import admin
# from django.urls import path
from django.urls import re_path as url

from nidsys import views as nidsys_views
from nidsys import urls as nidsys_urls
from django.conf.urls import include

urlpatterns = [
    url(r'^$', nidsys_views.MainPage, name='mainpage'),
    url(r'^nidsys/', include(nidsys_urls)),

    # path('', views.MainPage, name='mainpage'),
    # url(r'^nidsys/viewlist_url/$', views.ViewList, name='viewlist'), 
    # url(r'^nidsys/newlist_url$', views.NewList, name='newlist'),
    # url(r'^nidsys/(\d+)/$', views.ViewList, name='viewlist'),
    # url(r'^nidsys/(\d+)/addList$', views.AddList, name='addlist'),
]
