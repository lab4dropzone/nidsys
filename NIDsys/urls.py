from django.contrib import admin
from django.urls import path
from nidsys import views
from django.urls import re_path as url

urlpatterns = [
    path('', views.MainPage, name='mainpage'),
    url(r'^nidsys/viewlist_url/$', views.ViewList, name='viewlist'),
]
