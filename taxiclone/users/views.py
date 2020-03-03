from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import User as CusUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def signin(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def driver(request):
    return render(request, 'user/driver.html')

def logindriver(request):
    return render(request, 'user/driverlogin.html')



def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['mobile']
        loginpassword = request.POST['password']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            #request.session[‘id’] = id
            messages.success(request,"successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials, please try again")
            return redirect('home')

    return HttpResponse('404- Not Found')

def handledriverLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['mobile']
        loginpassword = request.POST['password']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"successfully logged in")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid credentials, please try again")
            return redirect('dashboard')

    return HttpResponse('404- Not Found')


def handleLogout(request):
        logout(request)
        messages.success(request,"successfully logout")
        return redirect('login')


#def handlesignup(request):
 #   if request.method == 'POST':
  #     username = request.POST['mobile']
   #     fname = request.POST['fullName']
    #    pass1 = request.POST['password']        
    #   email = request.POST['email']
        # lname = request.POST['lname']
        # pass2 = request.POST['pass2']
     #   myuser = User.objects.create_user(username, email, pass1)
      #  myuser.first_name = fname
        # myuser.last_name = lname
       # myuser.save()
        #messages.success(request, "your taxiclone accound has been successfully created")
        #return redirect('home')
    #else:
     #   return HttpResponse('404 - Not found')

def handlesignup(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        fname = request.POST['fullName']
        password = request.POST['password']        
        #email = request.POST['email']
        myuser = CusUser.objects.create_user(mobile, password, fname)
        #myuser.name = fname
        myuser.save()
        messages.success(request, "your taxiclone accound has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not found')



def handledriversignup(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        fname = request.POST['fullName']
        password = request.POST['password']
        vehicle_type = request.POST['vehicle']        
        #email = request.POST['email']
        myuser = CusUser.objects.create_driver(mobile, password, fname, vehicle_type)
        #myuser.name = fname
        myuser.save()
        messages.success(request, "your taxiclone accound has been successfully created")
        return redirect('dashboard')
    else:
        return HttpResponse('404 - Not found')