FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#RUN pip install --upgrade -r /app/requirements.txt

COPY . .
