# By Jeckonia Onyango <jeckonia49>

[![Build Status](https://travis-ci.org/jeckonia49/jeckonia49.svg?branch=master)](https://travis-ci.org/jeckonia49/jeckonia49)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

This is a api framework build ontop of django rest with ninja. Check out the project's [documentation](http://jeckonia49.github.io/jeckonia49/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development
create vertual environment
### python -m venv <environment_name>

Install the requirements 

### pip install -r requirements.txt
create a superuser 

#### based on user name

## This config assumen your are using windows


### Bellow are not neeed to run this app

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
