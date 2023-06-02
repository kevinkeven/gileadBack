#!/bin/sh
gunicorn gilead.wsgi:application --bind 0.0.0.0:80