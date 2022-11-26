#!/bin/bash

thisd=$(cd $(dirname $0); pwd)

cd $thisd && lein run
