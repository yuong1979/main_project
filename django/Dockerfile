FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /django_app

# WORKDIR /usr/src/app/django_app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# gunicorn core.wsgi:application --bind 0.0.0.0:8080
ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

