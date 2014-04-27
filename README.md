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

## VirtualEnv

`sudo pip install virtualenv`

`cd /path/to/project/dir`

`virtualenv venv`

Always activate the virtualenv when installing things

`. venv/bin/activate`


## Installing dependencies
`export CFLAGS=-Qunused-arguments`

`export CPPFLAGS=-Qunused-arguments`

`pip install --allow-external argparse --upgrade -r requirements.txt`

