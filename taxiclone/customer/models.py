from django.db import models

# Create your models here.
    

class Rides(models.Model):
    ride_no = models.CharField(max_length=255, blank=True, null=True) 
    From = models.CharField(max_length=60)
    to = models.CharField(max_length=60)
    Assigned_to =models.CharField(max_length=255, blank=True, null=True)
    Start_status  =models.BooleanField(default=False)
    Finish_status =models.BooleanField(default=False) 
    created_at    = models.DateTimeField(auto_now_add=True)

 