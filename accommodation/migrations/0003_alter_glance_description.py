# Generated by Django 4.2.2 on 2023-07-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0002_remove_glance_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glance',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
