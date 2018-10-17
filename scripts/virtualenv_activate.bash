#!/bin/bash -eu

if [ $# -lt 1 ]; then echo "usage: $0 <VENV_DIR>"; exit; fi

VENV_DIR=$1

SUDO_PIP="sudo pip3"
SYSTEM_PIP=/usr/bin/pip3

if [ ! -z ${VIRTUAL_ENV+x} ]; then deactivate; fi

sudo apt-get -y install python3-pip
$SUDO_PIP install virtualenv
# $SYSTEM_PIP install virtualenv

mkdir $VENV_DIR

# ECLIPSE - TURN OFF BEFORE HERE
virtualenv -p python3 $VENV_DIR

# HACK FIX
# https://github.com/pypa/virtualenv/issues/1029
if [ ! -f $VENV_DIR/activate.original ]; then
    mkdir -p $VENV_DIR/backup
    cp $VENV_DIR/bin/activate $VENV_DIR/backup/activate.original
fi

cat $VENV_DIR/backup/activate.original | sed 's/$PS1/${PS1-}/g' > $VENV_DIR/bin/activate
source $VENV_DIR/bin/activate

