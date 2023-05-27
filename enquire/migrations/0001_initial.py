# Generated by Django 4.2 on 2023-05-27 11:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquire',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('travel_date', models.DateField()),
                ('travel_duration', models.IntegerField()),
                ('travel_type', models.CharField(choices=[('Luxury', 'Luxury'), ('Midrange', 'Midrange'), ('Budget', 'Budget')], default='Midrange', max_length=10)),
                ('adults', models.IntegerField(default=0)),
                ('children', models.IntegerField(blank=True, default=0, null=True)),
                ('special_request', models.TextField()),
                ('travel_destination', models.ManyToManyField(related_name='yourtrip', to='shared.country')),
            ],
            options={
                'verbose_name_plural': 'Enquiries',
            },
        ),
    ]