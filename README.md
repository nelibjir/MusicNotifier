# Event notifier
The purpose of this application is to obtain data about nearby musical events from 
different online sources and compare it with my favourite artists from LastFM and 
save and display these events around me that contains my favourite artists.

## Install
- git clone ssh://git@github.com:nelibjir/MusicNotifier.git
- in src "pipenv install" will install all needed libraries
- pre-commit needs to be installed yet with command: pre-commit install

## How to run
- python main.py --reload
- the working directory is needed to be set from music_events_notifier


## DB

Create .env files:
```
cp .env.example .env
cd src/ && cp .env.docker .env
```


## Docker run

Run app with::

``docker-compose up``

## TODO
- save to DB
- docker
- precommit-tool set up
- save to noSql
