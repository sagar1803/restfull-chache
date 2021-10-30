FROM python:latest

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirement.txt /app/requirement.txt

RUN pip install -r requirement.txt

COPY . /app

CMD python manage.py runserver 0.0.0.0:8001