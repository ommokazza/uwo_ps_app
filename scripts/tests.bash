#!/bin/bash -eu

FILE_DIR=$(dirname `readlink -f ${BASH_SOURCE[0]}`)
# FILE_DIR=$(dirname `pwd`)/scripts
SCRIPTS_DIR=$FILE_DIR
BASE_DIR=$(dirname $SCRIPTS_DIR)

TESTS_DIR=$BASE_DIR/tests

pushd $BASE_DIR
python -m unittest tests.formatter_test
python -m unittest tests.towns_table_test
# python -m unittest tests.game_screen_monitor_test
popd
