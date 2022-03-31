from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
   return HttpResponse('<html><title>National ID System</title></html>')
