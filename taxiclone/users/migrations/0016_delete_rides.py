# Generated by Django 3.0.3 on 2020-03-03 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_rides_ride_no'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rides',
        ),
    ]