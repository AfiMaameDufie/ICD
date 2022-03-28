#Pull base image
FROM python:3.10

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory
WORKDIR /code

#Install dependendcies
COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

#Copy project
COPY . /code/