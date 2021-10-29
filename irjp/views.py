from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'Home.html')
   
def Register(request):
    return render(request, 'Register.html')

def login2(request): 
    return render(request, 'T-login.html')

def table(request):
    return render(request, 'table.html')

