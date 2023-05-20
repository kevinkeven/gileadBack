from django.db import models
from authemail.models import EmailAbstractUser, EmailUserManager


class User(EmailAbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    objects = EmailUserManager()
