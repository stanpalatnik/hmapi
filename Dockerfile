FROM python:latest
ENV LANG C.UTF-8

MAINTAINER Stanislav Palatnik "stan@spalatnik.com"

RUN mkdir /restapi

ADD requirements.txt /restapi/requirements.txt
RUN pip install -r /restapi/requirements.txt

WORKDIR /restapi

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 hmapi.wsgi