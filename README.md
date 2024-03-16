# By Jeckonia Onyango <jeckonia49>

[![Build Status](https://travis-ci.org/jeckonia49/jeckonia49.svg?branch=master)](https://travis-ci.org/jeckonia49/jeckonia49)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django)

This is a api framework build ontop of django rest with ninja. Check out the project's [documentation](http://jeckonia49.github.io/jeckonia49/).

# Prerequisites
## NOTE {Above} This config assumen your are using windows
- [Docker](https://docs.docker.com/docker-for-mac/install/)  # optional

## HOW TO RUN 

### Option 1:

create vertual environment

### python -m venv <environment_name>

Install the requirements 

### pip install -r requirements.txt
create a superuser 

#### based on user name

create a post gress database for it
:default connection str: postgres://kwasa:1234@localhost:5432/alvan1



### option 2: using docker
# need docker desktop to run 

### follow the commands

pull the latest image

*docker pull dandelionxxx/alvan:latest*

run the image on local machine

*docker run -e PORT=8000 -p 8000:8000*




