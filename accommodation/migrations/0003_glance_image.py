# Generated by Django 4.2 on 2023-05-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0002_remove_glance_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='glance',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accommodation/glance_images/'),
        ),
    ]
