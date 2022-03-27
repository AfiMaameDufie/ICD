#Pull base image
FROM python:3.8

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory
WORKDIR /code

#Install dependendcies
COPY Pipfile Pipfile.lock /project/
RUN pip install pipenv && pipenv install --system

#Copy project
COPY . /code/