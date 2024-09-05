#!/bin/sh
python manage.py make   migrations
python manage.py migrate
python manage.py loaddata sample.json   
gunicorn garage.wsgi:application --bind 0.0.0.0:8000