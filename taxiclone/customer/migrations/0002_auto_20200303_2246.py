# Generated by Django 3.0.3 on 2020-03-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='Assigned_to',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rides',
            name='ride_no',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
