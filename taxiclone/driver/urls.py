from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path('dashboard', views.dashboard, name='dashboard'),
     path('confirm_ride/<int:ride_id>/', views.confirm_ride, name='confirm_ride'),
     path('delete_ride/<int:ride_id>/', views.delete_ride, name='delete_ride'),
    #path('bookCab', views.add_ride, name='bookCab'),
]