---
title: "What is Actix Web"
type: docs
source: https://actix.rs/docs/whatis
site: actix.rs
project: actix-web
section: Introduction
created: 2026-06-06
tags:
  - clippings/docs
  - actix-web
  - rust
---

**Source URL**: https://actix.rs/docs/whatis

> 본 파일은 actix.rs 렌더링 페이지를 pandoc 으로 변환한 verbatim 캡처다. 코드 블록·산문 원문 보존, 네비게이션·앵커 노이즈만 제거.

# Actix Web is part of an Ecosystem of Crates

Long ago, Actix Web was built on top of the `actix` actor framework.
Now, Actix Web is largely unrelated to the actor framework and is built
using a different system. Though `actix` is still maintained, its
usefulness as a general tool is diminishing as the
[futures](https://docs.rs/futures/latest/futures) and async/await
ecosystem matures. At this time, the use of `actix` is only required for
WebSocket endpoints.

We call Actix Web a powerful and pragmatic framework. For all intents
and purposes, it's a micro-framework with a few twists. If you are
already a Rust programmer, you will probably find yourself at home
quickly. But even if you are coming from another programming language,
you should find Actix Web easy to pick up.

An application developed with Actix Web will expose an HTTP server
contained within a native executable. You can either put this behind
another HTTP server like nginx or serve it up as-is. Even in the
complete absence of another HTTP server, Actix Web is powerful enough to
provide HTTP/1 and HTTP/2 support as well as TLS (HTTPS). This makes it
useful for building small services ready for production.

Most importantly: Actix Web runs on Rust 1.72 or later and it works with
stable releases.
