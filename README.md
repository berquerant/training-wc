# training-wc

## Initialize

    $ pipenv install
    $ pipenv shell

## Run

e.g.

    $ make
    $ bin/testing.sh run -c `bin/select.sh go` < SOME_FILE

## Testing

    $ bin/e2e_all.sh

See [e2e_all.sh](bin/e2e_all.sh)

## Benchmark

e.g.

    $ bin/testing.sh bench -c `./bin/select.sh go` -i 100 -l 100 -n 100 | jq -r .mean

See [testing](testing/run.py).

## Requirements

- macOS 13
- pipenv
- [clojure](clojure-wc/README.md)
- [golang](go-wc/README.md)
- [rust](rust-wc/README.md)
- [python](py-wc/README.md)
- [zig](zig-wc/README.md)
