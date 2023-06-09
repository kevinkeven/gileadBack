from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils import timezone
from shared.models import Month

@receiver(post_migrate)
def create_months(sender, **kwargs):
    if sender.name == 'shared':
        # Check if the Month table is empty
    # List of month names
        month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        # Create Month objects for each month name
        for month_name in month_names:
            Month.objects.create(name=month_name)

 # Generated by Django 4.2 on 2023-05-16 13:11

# from django.db import migrations

# def populate_months(apps, schema_editor):
#     Month = apps.get_model('shared', 'Month')

#     # List of month names
#     month_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#     # Create Month objects for each month name
#     for month_name in month_names:
#         Month.objects.create(name=month_name)

# class Migration(migrations.Migration):

#     dependencies = [
#     ]

#     operations = [
#         migrations.RunPython(populate_months),
#     ]
