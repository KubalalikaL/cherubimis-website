#!/bin/sh
set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate --noinput

# Start Gunicorn
gunicorn cherubimis_website.wsgi:application --preload --bind 0.0.0.0:8000