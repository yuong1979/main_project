#!/bin/sh
# If the DJANGO env variable is set, run gunicorn core.wsgi:application --bind 0.0.0.0:8080
# Otherwise, run celery -A core worker -B -l INFO

if [ "$DJANGO" = "true" ]; then
    echo "Running Django"
    gunicorn core.wsgi:application --bind 0.0.0.0:8080
else
    echo "Running Celery"
    celery -A core worker -B -l INFO
fi