from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin, name='login'),
    path('register/', views.register, name='register'),
    path('driver', views.driver, name='driver'),
    path('logindriver', views.logindriver, name='logindriver'),  
    path('signup', views.handlesignup, name='handlesignup'),
    path('driversignup', views.handledriversignup, name='handledriversignup'),  
    path('login', views.handleLogin, name='handleLogin'),
    path('driverlogin', views.handledriverLogin, name='handledriverLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
]