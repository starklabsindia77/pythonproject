from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from customer.models import Rides
from django.http import HttpResponseRedirect

# Create your views here.
def dashboard(request):
    #ride_items = Rides.objects.all().order_by("id")
    ride_items = Rides.objects.all().filter(Assigned_to__isnull=True).order_by("id")
    return render(request, 'driver/dashboard.html', {
      "ride_items": ride_items})



@csrf_exempt
def confirm_ride(request, ride_id):
  if request.method == 'POST':
    End=request.POST["to"]
    #print(End)
    Rides.objects.filter(id=ride_id).update(Assigned_to=End)
    return redirect('dashboard')
  else:
        return HttpResponse('404 - Not found')



@csrf_exempt
def delete_ride(request, ride_id):
  Rides.objects.get(id=ride_id).delete()
  return redirect('dashboard')