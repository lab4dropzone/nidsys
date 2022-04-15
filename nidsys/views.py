from django.shortcuts import render, redirect
from django.http import HttpResponse

from nidsys.models import Registration

def MainPage(request):
  if request.method == 'POST':
    Registration.objects.create(sname=request.POST['surname'],fname=request.POST['firstname'],
      mname=request.POST['middlename'],bdate=request.POST['bdate'],
      address=request.POST['address'],contactno=request.POST['contactno'])
    return redirect('/')

  reglist = Registration.objects.all()
  return render(request,'mainpage.html',{'registered':reglist})

  # return render(request,'mainpage.html',{'newSurname':request.POST.get('surname'),
  #  'newFirstname':request.POST.get('firstname'),'newMiddlename':request.POST.get('middlename'),
  #  'newAddress':request.POST.get('address'),'newContactNo':request.POST.get('contactno'),})

   # return render(request, 'mainpage.html', {'newSurname':request.POST.get('surname',''),})

   # if request.method == "POST":
   #    return HttpResponse(request.POST['surname'])
   # return render(request, 'mainpage.html')
   

