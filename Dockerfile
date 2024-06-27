FROM python:3.8-slim-buster
RUN apt-get update
RUN apt-get install procps -y
RUN apt-get install vim -y
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY config/nats.conf config/nats.conf
COPY . .