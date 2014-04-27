cse-190-server
==============

# Setup
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

`sudo pip install virtualenv`

`cd /path/to/project/dir`

`virtualenv venv`

Always activate the virtualenv when installing things for this project.

`. venv/bin/activate`


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



