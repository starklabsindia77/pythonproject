# Generated by Django 3.0.3 on 2020-03-03 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_driver',
            new_name='admin',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_customer',
            new_name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='none', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
