from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def signin(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')



def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['mobile']
        loginpassword = request.POST['password']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials, please try again")
            return redirect('home')

    return HttpResponse('404- Not Found')


def handleLogout(request):
        logout(request)
        messages.success(request,"successfully logout")
        return redirect('login')


def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['mobile']
        fname = request.POST['fullName']
        pass1 = request.POST['password']        
        email = request.POST['email']
        # lname = request.POST['lname']
        # pass2 = request.POST['pass2']
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        # myuser.last_name = lname
        myuser.save()
        messages.success(request, "your taxiclone accound has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not found')