from django.shortcuts import render, redirect
from django.http import HttpResponse

from nidsys.models import Registration

def MainPage(request):
  reglist = Registration.objects.all()
  return render(request,'mainpage.html')
  
def ViewList(request):
  # reglist = Registration.objects.all()
  reglist = Registration.objects.first()
  return render(request,'listpage.html',{'registered':reglist})

def NewList(request):
  Registration.objects.create(sname=request.POST['surname'],fname=request.POST['firstname'],
      mname=request.POST['middlename'],bdate=request.POST['bdate'],
      address=request.POST['address'],contactno=request.POST['contactno'])
  return redirect('/nidsys/viewlist_url/')