
# pull official base image
FROM python:3.8-slim-buster
# install psycopg2 dependencies
#RUN apt-get update \
#    && apt-get install postgresql-dev gcc python3-dev musl-dev \
#    && apt-get -y autoremove \
#    && apt-get clean

RUN mkdir /django
WORKDIR /django
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
COPY ./requirements.txt /requirements.txt
COPY ./requirements.txt /tmp/
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

# copy project
ADD . /django
EXPOSE 8000
RUN python manage.py collectstatic
#RUN python manage.py runserver
CMD gunicorn --workers 1 --log-level INFO --bind '0.0.0.0:8000' core.wsgi:application