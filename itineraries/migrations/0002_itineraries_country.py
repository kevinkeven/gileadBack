# Generated by Django 4.2 on 2023-05-24 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
        ('itineraries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itineraries',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to='shared.country'),
        ),
    ]