---
title: "Actix (Actor Framework)"
type: docs
source: https://actix.rs/docs/actix
site: actix.rs
project: actix
section: Actix
created: 2026-06-06
tags:
  - clippings/docs
  - actix-actor
  - rust
---

**Source URL**: https://actix.rs/docs/actix

> 본 파일은 actix.rs 렌더링 페이지를 pandoc 으로 변환한 verbatim 캡처다. 코드 블록·산문 원문 보존, 네비게이션·앵커 노이즈만 제거.

# Quick start

Before you can start writing an actix application, you’ll need a version
of Rust installed. We recommend you use rustup to install or configure
such a version.

## Install Rust

Before we begin, we need to install Rust using the
[rustup](https://rustup.rs/) installer:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

If you already have rustup installed, run this command to ensure you
have the latest version of Rust:

```bash
rustup update
```

The actix framework requires Rust version 1.40.0 and up.

## Running Examples

The fastest way to start experimenting with actix is to clone the actix
repository and run the included examples in the examples/ directory. The
following set of commands runs the `ping` example:

```bash
git clone https://github.com/actix/actix
cd actix
cargo run --example ping
```

Check
[examples/](https://github.com/actix/actix/tree/master/actix/examples)
directory for more examples.
