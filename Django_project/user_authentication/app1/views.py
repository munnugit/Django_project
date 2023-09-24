from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('Username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
       

        print(uname,email,pass1,pass2)
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        Username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(Username,pass1)
    return render(request,'login.html')