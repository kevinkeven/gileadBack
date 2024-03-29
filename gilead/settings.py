"""
Django settings for gilead project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import django_on_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# ADMINS = config("ADMINS", cast=lambda v: [s.strip() for s in v.split(",")])

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config("DEBUG", cast=bool, default=False)

ALLOWED_HOSTS = ["*"]


CSRF_TRUSTED_ORIGINS = [
    "https://api.gileadsummitholidays.com",
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 2,
}

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"]
}


# Application definition
SITE_ID = config("SITE_ID", cast=bool)

INSTALLED_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "drf_multiple_model",
    "corsheaders",
    "authemail",
    "accounts",
    "blog",
    "enquire",
    "accommodation",
    "destination",
    "itineraries",
    "search",
    "shared",
    "experiences",
    # "django.contrib.sites",
    # "django.contrib.sitemaps",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "gilead",
        "USER": "gilead",
        "PASSWORD": "gilead",
        "HOST": "localhost",
        "PORT": 5432,
    }
}
ROOT_URLCONF = "gilead.urls"


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTH_EMAIL_VERIFICATION = False
WSGI_APPLICATION = "gilead.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

if not DEBUG:
    EMAIL_BCC = "admin@gilead.com"
    EMAIL_FROM = "gileadsummitholidays@gmail.com"
    EMAIL_HOST = "smtp.sendgrid.net"
    EMAIL_PORT = 25
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = "apikey"
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", cast=str, default="api")
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

CORS_ALLOW_ALL_ORIGINS = True

AUTH_USER_MODEL = "accounts.User"
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    )
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"
STATIC_URL = "static/"
STATIC_ROOT = "staticfiles/"

if not DEBUG:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID", cast=str, default="api")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY", cast=str, default="apii")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME", cast=str, default="api")
AWS_QUERYSTRING_AUTH = config("AWS_QUERYSTRING_AUTH", cast=str, default="apii")
AWS_S3_REGION_NAME = "eu-north-1"

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_S3_SIGNATURE_VERSION = "s3v4"

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

django_on_heroku.settings(locals())
