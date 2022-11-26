#!/bin/bash

thisd=$(cd $(dirname $0); pwd)
testing="${thisd}/../testing/run.py"

pipenv run python $testing $@
