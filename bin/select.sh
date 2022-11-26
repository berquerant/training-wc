#!/bin/bash

thisd=$(cd $(dirname $0); pwd)
source "${thisd}/util.sh"

usage() {
    log "Usage: select.sh LANG"
    log
    log "Print a proper executable path."
}

thisd=$(cd $(dirname $0); pwd)
root="${thisd}/.."

go_wc="${root}/go-wc/dist/wc"
py_wc="${root}/py-wc/wc.sh"
clojure_wc="${root}/clojure-wc/wc.sh"
zig_wc="${root}/zig-wc/zig-out/bin/zig-wc"
rust_wc="${root}/rust-wc/target/release/rust-wc"
c_wc="${root}/c-wc/dist/wc"

case "$1" in
    "go" | "golang") echo $go_wc ;;
    "py" | "python") echo $py_wc ;;
    "clj" | "clojure") echo $clojure_wc ;;
    "zig") echo $zig_wc ;;
    "rust") echo $rust_wc ;;
    "c") echo $c_wc ;;
    *) usage
       exit 1
       ;;
esac
