#Pull base image
FROM python:3.10

#set environment variables
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

#set work directory
WORKDIR /code

#Install dependendcies
COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

#Copy project
COPY . /code/