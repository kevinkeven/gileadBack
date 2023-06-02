#!/bin/sh
python manage.py collectstatic --no-input
python manage.py migrate
gunicorn -c gilead.wsgi:application --bind=0.0.0.0:80