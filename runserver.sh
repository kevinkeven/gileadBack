#!/bin/sh

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
gunicorn gilead.wsgi:application --bind 0.0.0.0:80