FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN apt-get update && \
    apt-get -qy install python3-dev default-libmysqlclient-dev gcc


ADD requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

ADD . /app/
