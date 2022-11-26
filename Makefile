GO_DIR = go-wc
ZIG_DIR = zig-wc
RUST_DIR = rust-wc


.PHONY: build
build: build-go build-zig build-rust

.PHONY: build-go
build-go:
	cd $(GO_DIR) && go build -o dist/wc ./main.go

.PHONY: build-zig
build-zig:
	cd $(ZIG_DIR) && zig build -Drelease-fast=true

.PHONY: build-rust
build-rust:
	cd $(RUST_DIR) && cargo build --release
