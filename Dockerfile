# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
COPY .env /app/
RUN ls -a