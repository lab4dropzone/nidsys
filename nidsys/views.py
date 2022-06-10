from django.shortcuts import render,redirect
from django.http import HttpResponse
from nidsys.models import Registration,PreviousAddr

def MainPage(request):
  reglist = Registration.objects.all()
  return render(request,'mainpage.html')

def ViewList(request,rId):
  regId = Registration.objects.get(id=rId)
  # addrlist = PreviousAddr.objects.filter(regid=regId)
  # return render(request,'listpage.html',{'addrList':addrlist})
  return render(request,'listpage.html',{'regId':regId})


def NewList(request):
  vsname = request.POST['surname']
  vfname = request.POST['firstname']
  vmname = request.POST['middlename']
  vbdate = request.POST['bdate']
  vaddress = request.POST['address']
  vcontactno = request.POST['contactno']
  newReg = Registration.objects.create(sname=vsname,fname=vfname,mname=vmname,bdate=vbdate,
    address=vaddress,contactno=vcontactno)
  return redirect(f'/nidsys/{newReg.id}/')

def AddList(request,rId):
  newReg = Registration.objects.get(id=rId)
  vprevaddr = request.POST['prevaddr']
  vfromdate = request.POST['fromdate']
  vtodate = request.POST['todate']
  PreviousAddr.objects.create(regid=newReg,prevaddr=vprevaddr,fromdate=vfromdate,todate=vtodate)
  return redirect(f'/nidsys/{newReg.id}/')



