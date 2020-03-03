from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from customer.models import Rides
from django.http import HttpResponseRedirect

# Create your views here.
def dashboard(request):
    ride_items = Rides.objects.all().order_by("id")
    return render(request, 'driver/dashboard.html', {
      "ride_items": ride_items})



@csrf_exempt
def confirm_ride(request, ride_id):
  End=request.POST["to"]
  Rides.objects.filter(pk=ride_id).update(to=End)
  return HttpResponseRedirect("/")



@csrf_exempt
def delete_ride(request, ride_id):
  Rides.objects.get(id=ride_id).delete()
  return HttpResponseRedirect("/")