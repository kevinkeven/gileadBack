#!/bin/sh
python manage.py collectstatic --no-input
python manage.py migrate
gunicorn -c gunicorndev.py --bind=0.0.0.0:80