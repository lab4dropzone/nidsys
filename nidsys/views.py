from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
  return render(request,'mainpage.html',{'newSurname':request.POST.get('surname'),
   'newFirstname':request.POST.get('firstname'),'newMiddlename':request.POST.get('middlename'),
   'newAddress':request.POST.get('address'),'newContactNo':request.POST.get('contactno'),})

   # return render(request, 'mainpage.html', {'newSurname':request.POST.get('surname',''),})

   # if request.method == "POST":
   #    return HttpResponse(request.POST['surname'])
   # return render(request, 'mainpage.html')
   

