# Generated by Django 3.0.3 on 2020-03-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_driver', models.BooleanField(default=False, verbose_name='driver status')),
                ('is_customer', models.BooleanField(default=False, verbose_name='customer status')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
