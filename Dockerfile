# pull official base image
FROM python:3.8-slim-buster

RUN mkdir /django
WORKDIR /django
# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /requirements.txt
COPY ./requirements.txt /tmp/
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

# copy project
ADD . /django
EXPOSE 8000
RUN python manage.py collectstatic --noinput
CMD gunicorn --workers 1 --log-level INFO --bind '0.0.0.0:8000' core.wsgi:application