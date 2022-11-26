#!/bin/bash

thisd=$(cd $(dirname $0); pwd)
source "${thisd}/util.sh"

usage() {
    log "Usage: e2e.sh WC"
    log
    log "Run e2e test"
}

check="${thisd}/check.sh"
# testing="${thisd}/testing.sh"
wc_command="$1"

if [ -z $wc_command ] ; then
    echo "Require command equivalent to wc at 1st argument"
    usage
    exit 1
fi

find "${thisd}/../testdata" -type f | while read line ; do
    testname=$(basename $line)
    echo "Test ${testname}"
    $check $wc_command $line
done

