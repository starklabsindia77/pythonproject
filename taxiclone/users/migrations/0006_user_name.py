# Generated by Django 3.0.3 on 2020-03-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200302_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='none', max_length=13),
        ),
    ]
