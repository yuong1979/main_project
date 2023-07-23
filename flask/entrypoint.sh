#!/bin/sh
# If the FLASK env variable is set, run gunicorn core.wsgi:application --bind 0.0.0.0:8080
# Otherwise, run celery -A core worker -B -l INFO

if [ "$FLASK" = "true" ]; then
    gunicorn --bind 0.0.0.0:8080 --workers 4 --threads 4 run:app
else
    celery -A celery_worker.celery worker --loglevel=info --concurrency=2
fi
