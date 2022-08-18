from django.shortcuts import render
from django.http import HttpResponse
from .models import Place


# Create your views here.


# def intro(request):
#      return render(request,'yourhome.html')
#
# def view1(request):
#      return render(request,'view1.html')
#
# def view2(request):
#      return HttpResponse('white blind light')
def intro(request):
    obj=Place.objects.all()
    return render(request, 'index.html',{'result':obj})
