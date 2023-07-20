
# new docker

FROM python:3.8-slim-buster

# Install Git
RUN apt-get update && apt-get install -y git redis

WORKDIR /flask_app

# WORKDIR /usr/src/app/flask_app
RUN apt-get -y install gcc
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# Expose the necessary port(s)
EXPOSE 5000

# # command out the below if running docker-compose
# CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]




# backup flask



# FROM python:3.8-slim-buster

# # Install Git
# RUN apt-get update && apt-get install -y git

# WORKDIR /flask_app/projects

# # WORKDIR /usr/src/app/flask_app

# COPY requirements.txt requirements.txt

# RUN pip3 install -r requirements.txt

# COPY . .
# # command out the below if running docker-compose
# CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]


# CMD gunicorn --workers $WORKERS \
# --threads $THREAD \
# --bind 0.0.0.0:$PORT_APP \
# --log-level DEBUG \
# app:app


