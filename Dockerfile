FROM python:3.7-alpine
MAINTAINER Maria_Jose

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# Instala el cliente de Postgres
RUN apk add --update --no-cache postgresql-client
# dependencias temporales
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# elimina los requisitos temporales
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user