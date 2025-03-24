from django.shortcuts import render

#create your views here.
from django.http import HttpResponse

def home(request):
     return render(request,'index.html')
def resume(request):
     return render(request,'Resume.html')




