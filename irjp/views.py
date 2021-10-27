from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
   # view table.html using render function
    return render(request, 'Home.html')


def Register(request):
 
    return render(request, 'Register.html')

def login2(request):
  
    return render(request, 'T-login.html')

def table(request):
    # render table.html using render function
    return render(request, 'table.html')

