#!/bin/bash

thisd=$(cd $(dirname $0); pwd)
source "${thisd}/util.sh"

usage() {
    log "Usage: check.sh WC FILE"
    log
    log "Verify that the output of the command equivalent to wc is the same as wc."
}

testing="${thisd}/testing.sh"
wc_command="$1"

if [ -z $wc_command ] ; then
    echo "Require command equivalent to wc at 1st argument"
    usage
    exit 1
fi

input="$2"

if [ -z $input ] ; then
    echo "Require input file at 2nd argument"
    usage
    exit 1
fi

run() {
    cat $input | $testing run -c $1
}


wc_result="${TMPD}/original.result"
result="${TMPD}/target.result"
run "wc" > $wc_result
run $wc_command > $result

diff $wc_result $result
