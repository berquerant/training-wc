GO_DIR = go-wc
ZIG_DIR = zig-wc
RUST_DIR = rust-wc
C_DIR = c-wc


.PHONY: build
build: build-go build-zig build-rust build-c

.PHONY: build-go
build-go:
	cd $(GO_DIR) && go build -o dist/wc ./main.go

.PHONY: build-zig
build-zig:
	cd $(ZIG_DIR) && zig build -Drelease-fast=true

.PHONY: build-rust
build-rust:
	cd $(RUST_DIR) && cargo build --release

.PHONY: build-c
build-c:
	cd $(C_DIR) && mkdir -p dist && zig cc -o dist/wc main.c
