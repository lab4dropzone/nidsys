from django.contrib import admin
from django.urls import path
from nidsys import views
from django.urls import re_path as url

urlpatterns = [  
    url(r'^newlist_url$', views.NewList, name='newlist'),
    url(r'^(\d+)/$', views.ViewList, name='viewlist'),
    url(r'^(\d+)/addList$', views.AddList, name='addlist'),
    
    # path('', views.MainPage, name='mainpage'),
    # url(r'^nidsys/viewlist_url/$', views.ViewList, name='viewlist'),
]
