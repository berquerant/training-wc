#!/bin/bash

thisd=$(cd $(dirname $0); pwd)
source "${thisd}/util.sh"

e2e="${thisd}/e2e.sh"
select="${thisd}/select.sh"

log "Build executables"
make

for x in go python clojure zig rust c ; do
    log "Start test for ${x}..."
    $e2e $($select $x)
done
