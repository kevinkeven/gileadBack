from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "gilead",
        "USER": "gilead",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

ALLOWED_HOSTS = ["*"]
