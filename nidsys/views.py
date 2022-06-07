from django.shortcuts import render, redirect
from django.http import HttpResponse
from nidsys.models import Registration,PreviousAddr

def NewList(request):
  vregid = Registration.objects.create(idno="2022058712",fname="Ralph")
  vprevaddr = request.POST['mprevaddr']
  vfromdate = request.POST['mfromdate']
  vtodate = request.POST['mtodate']
  PreviousAddr.objects.create(regid=vregid,prevaddr=vprevaddr,fromdate=vfromdate,todate=vtodate)
  return redirect(f'/nidsys/{vregid.id}/')

def ViewList(request,rId):
  newReg = Registration.objects.get(id=rId)
  addrlist = PreviousAddr.objects.filter(regid=newReg)
  return render(request,'listpage.html',{'addrList':addrlist})

def MainPage(request):
  reglist = Registration.objects.all()
  return render(request,'mainpage.html')