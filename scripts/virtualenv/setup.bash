#!/bin/bash -eu

FILE_DIR=$(dirname `readlink -f ${BASH_SOURCE[0]}`)
# FILE_DIR=$(dirname `pwd`)/scripts
SCRIPTS_DIR=$(dirname $FILE_DIR)
BASE_DIR=$(dirname $SCRIPTS_DIR)
VENV_DIR=$BASE_DIR/venv

#if [ $# -lt 1 ]; then echo "usage: $0 <VENV_DIR>"; exit; fi
#VENV_DIR=$1

SUDO_PIP="sudo pip3"
SYSTEM_PIP=/usr/bin/pip3

if [ ! -z ${VIRTUAL_ENV+x} ]; then deactivate; fi

sudo apt-get -y install python3-pip
$SUDO_PIP install virtualenv
# $SYSTEM_PIP install virtualenv

# ECLIPSE - TURN OFF BEFORE HERE
mkdir $VENV_DIR
virtualenv -p python3 $VENV_DIR

# HACK FIX
# https://github.com/pypa/virtualenv/issues/1029
if [ ! -f $VENV_DIR/activate.original ]; then
    mkdir -p $VENV_DIR/backup
    cp $VENV_DIR/bin/activate $VENV_DIR/backup/activate.original
fi

cat $VENV_DIR/backup/activate.original | sed 's/$PS1/${PS1-}/g' > $VENV_DIR/bin/activate
. $FILE_DIR/activate.bash

