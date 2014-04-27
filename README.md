cse-190-server
==============

# Table of Contents
1. [Setup](#setup)
2. [Running](#running)
3. [Deployment](#deploy)
3. [Running Unit Tests](#tests)

# <a name="setup"></a>Setup 
Here are local environment instructions for MAC

Clone the repository onto your computer. Doesn't matter where.

`cd /path/to/your/project`

`git clone git@github.com:jsandvik/cse-190-server.git .`

## Homebrew
I'm using homebrew on my mac. If you don't have it yet, you can find installation instructions [here](http://brew.sh)

`brew install python mysql`

I also updated pip and setuptools

`pip install --upgrade setuptools`

`pip install --upgrade pip`

Run mysql using the provided commands from homebrew or use 

`mysql.server start`

Create the database by logging into mysql and creating the schema.

`mysql -u root`

`create schema appDB;`

## VirtualEnv
Some instructions on virtualenv with Flask [here](http://flask.pocoo.org/docs/installation/)

`sudo pip install virtualenv`

`cd /path/to/project/dir`

`virtualenv venv`

Always activate the virtualenv when installing things for this project.

`. venv/bin/activate`

Update the setuptools in the venv. Make sure you activated the venv

`pip install --upgrade setuptools`


## Installing dependencies
Run these in order to install the dependencies.

`export CFLAGS=-Qunused-arguments`

`export CPPFLAGS=-Qunused-arguments`

`pip install --allow-external argparse --upgrade -r requirements.txt`

## Updating the database
SQLAlchemy can create the database for us based on the models we create. If you can't connect to the database, make sure the database connection info refers to your local version.

open a python shell by running `python` from the command line

`from project import db`

`db.drop_all()` will drop all tables in the database

`db.create_all()` will create the tables

# <a name="running"></a>Running the app 

`cd /path/to/project/`

`python project.py`

If there are no errors, the app should show up when you visit [localhost:5000](http://localhost:5000)

# <a name="deploy"></a>Deploying the app to the server 

Going to use [Fabric](http://flask.pocoo.org/docs/patterns/fabric/) and [Distribute](http://flask.pocoo.org/docs/patterns/distribute/#distribute-deployment) to deploy to the server. Working on this now more info coming soon. - DD 4/26

# <a name="tests"></a>Running unit tests 

`cd /path/to/project/`

`python tests.py`

This will run all of the tests located in tests.py. You can add more tests by adding more functions to test.py, but they must begin with the word 'test'.

In order for unit tests to run, you will need to create another seperate database in mysql, called testDB:

`mysql -u root`

`create schema testDB;`

