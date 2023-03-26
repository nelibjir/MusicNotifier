ARG REGISTRY=docker.io
FROM $REGISTRY/python:3.8.13-slim-bullseye

# ----------- Install all dependencies -------------
RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && apt-get install -y libpq-dev iputils-ping vim systemctl

# Link Python to version 8
RUN ln -s /usr/bin/python3.8 /usr/bin/python

RUN systemctl reload

ENV APP_HOME /app
ENV PYTHONPATH ${APP_HOME}

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/app-data

WORKDIR $APP_HOME

# Install any needed packages specified in Pipfile
COPY ./src/Pipfile* ${APP_HOME}/
RUN pip install pipenv psycopg2
RUN pipenv install --system --deploy --ignore-pipfile

# --------------- APP OTHER ---------------

ARG ENVIRONMENT=develop
ARG POSTGRES_HOST=db
ARG POSTGRES_DB=karla
ARG POSTGRES_NAME=karla
ARG POSTGRES_USER=karla_user
ARG POSTGRES_PASSWORD=password
ARG POSTGRES_PORT=5432

# The environment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED=1

# This optimize the size and running of container
ENV PYTHONDONTWRITEBYTECODE 1


COPY ./src/entrypoint .


# copy project
COPY ./src/music_events_notifier $APP_HOME/music_events_notifier
COPY ./src/main.py $APP_HOME/main.py

#run entry point
#CMD ["/bin/bash", "-c", "${APP_HOME}/entrypoint ./main.py"]
CMD ["tail", "-f", "/dev/null"]

#ENTRYPOINT ["tail", "-f", "/dev/null"]
