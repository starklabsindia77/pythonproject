from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Rides
from random import randint
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request, 'home/home.html')


@csrf_exempt
def add_ride(request):
  current_date = timezone.now()
  Start = request.POST["start"]
  End = request.POST["end"]
  ride = randint(1000, 9999)
  querySet = Rides.objects.create(From=Start, to=End, created_at=current_date, ride_no=ride)
  return render(request, 'home/home.html')

