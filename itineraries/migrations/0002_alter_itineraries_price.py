# Generated by Django 4.2.2 on 2023-07-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraries',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
