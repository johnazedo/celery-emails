# CeleryEmails
<a href="https://travis-ci.com/github/JohnAzedo/CeleryEmails">
  <img alt="Build" src="https://travis-ci.com/JohnAzedo/CeleryEmails.svg?branch=master">
</a>
<a href="https://github.com/JohnAzedo/CeleryEmails/blob/master/LICENSE">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg">
</a>

Just a simple django project to send non-motivational emails using Celery Async Tasks.

# What I learned?

List of all the technologies I learned from building this project.

- Use docker-compose to python projects;

- Do asynchronoues tasks using Celery;

- Use Django Messages Framework;

- Include Travis in a github repository;

- Config and use a mail server;

- Starting to study Selenium.

# Setup

Clone this repository

````sh
$ git clone git@github.com:JohnAzedo/CeleryEmails.git
````

### Run with Docker :whale:

````sh
$ docker-compose up
````

### Run on local env

Install requirements

````sh
$ pip install -r requirements.txt
````

Make migrations and send to database
````sh
$ python manage makemigrations
$ python manage migrate
`````
Run project

````sh
$ python manage runserver
````
