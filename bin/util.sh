TMPD="$(cd $(dirname $0); pwd)/../tmp"
mkdir -p $TMPD

log() {
    echo "$@" 1>&2
}
