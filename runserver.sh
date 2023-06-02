#!/bin/sh
python manage.py collectstatic
python manage.py migrate
gunicorn gilead.wsgi:application --bind 0.0.0.0:80