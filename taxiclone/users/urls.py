from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin, name='login'),
    path('register/', views.register, name='register'),  
    path('home', views.home, name='home'),
    path('signup', views.handlesignup, name='handlesignup'),  
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
]