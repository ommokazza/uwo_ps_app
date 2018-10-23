#!/bin/bash -eu

FILE_DIR=$(dirname `readlink -f ${BASH_SOURCE[0]}`)
# FILE_DIR=$(dirname `pwd`)/scripts
SCRIPTS_DIR=$(dirname $FILE_DIR)
BASE_DIR=$(dirname $SCRIPTS_DIR)
VENV_DIR=$BASE_DIR/venv

. $VENV_DIR/bin/activate
