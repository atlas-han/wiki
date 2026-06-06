---
title: "Responses"
type: docs
source: https://actix.rs/docs/response
site: actix.rs
project: actix-web
section: Advanced
created: 2026-06-06
tags:
  - clippings/docs
  - actix-web
  - rust
---

**Source URL**: https://actix.rs/docs/response

> 본 파일은 actix.rs 렌더링 페이지를 pandoc 으로 변환한 verbatim 캡처다. 코드 블록·산문 원문 보존, 네비게이션·앵커 노이즈만 제거.

# Response

A builder-like pattern is used to construct an instance of
`HttpResponse`. `HttpResponse` provides several methods that return a
`HttpResponseBuilder` instance, which implements various convenience
methods for building responses.

> Check the
> [documentation](https://docs.rs/actix-web/4/actix_web/struct.HttpResponseBuilder.html)
> for type descriptions.

The methods `.body`, `.finish`, and `.json` finalize response creation
and return a constructed *HttpResponse* instance. If this methods is
called on the same builder instance multiple times, the builder will
panic.

```rust
use actix_web::{http::header::ContentType, HttpResponse};

async fn index() -> HttpResponse {
    HttpResponse::Ok()
        .content_type(ContentType::plaintext())
        .insert_header(("X-Hdr", "sample"))
        .body("data")
}
```

## JSON Response

The `Json` type allows to respond with well-formed JSON data: simply
return a value of type `Json<T>` where `T` is the type of a structure to
serialize into *JSON*. The type `T` must implement the `Serialize` trait
from *serde*.

For the following example to work, you need to add `serde` to your
dependencies in `Cargo.toml`:

```toml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
```

```rust
use actix_web::{get, web, Responder, Result};
use serde::Serialize;

#[derive(Serialize)]
struct MyObj {
    name: String,
}

#[get("/a/{name}")]
async fn index(name: web::Path<String>) -> Result<impl Responder> {
    let obj = MyObj {
        name: name.to_string(),
    };
    Ok(web::Json(obj))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    use actix_web::{App, HttpServer};

    HttpServer::new(|| App::new().service(index))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}
```

Using the `Json` type this way instead of calling the `.json` method on
a `HttpResponse` makes it immediately clear that the function returns
JSON and not any other type of response.

## Content encoding

Actix Web can automatically *compress* payloads with the [*Compress
middleware*](https://docs.rs/actix-web/4/actix_web/middleware/struct.Compress.html).
The following codecs are supported:

- Brotli
- Gzip
- Deflate
- Identity

A response's `Content-Encoding` header defaults to
`ContentEncoding::Auto`, which performs automatic content compression
negotiation based on the request's `Accept-Encoding` header.

```rust
use actix_web::{get, middleware, App, HttpResponse, HttpServer};

#[get("/")]
async fn index() -> HttpResponse {
    HttpResponse::Ok().body("data")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .wrap(middleware::Compress::default())
            .service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

Explicitly disable content compression on a handler by setting
`Content-Encoding` to an `Identity` value:

```rust
use actix_web::{
    get, http::header::ContentEncoding, middleware, App, HttpResponse, HttpServer,
};

#[get("/")]
async fn index() -> HttpResponse {
    HttpResponse::Ok()
        // v- disable compression
        .insert_header(ContentEncoding::Identity)
        .body("data")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .wrap(middleware::Compress::default())
            .service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

When dealing with an already compressed body (for example, when serving
pre-compressed assets), set the `Content-Encoding` header on the
response manually to bypass the middleware:

```rust
use actix_web::{
    get, http::header::ContentEncoding, middleware, App, HttpResponse, HttpServer,
};

static HELLO_WORLD: &[u8] = &[
    0x1f, 0x8b, 0x08, 0x00, 0xa2, 0x30, 0x10, 0x5c, 0x00, 0x03, 0xcb, 0x48, 0xcd, 0xc9, 0xc9,
    0x57, 0x28, 0xcf, 0x2f, 0xca, 0x49, 0xe1, 0x02, 0x00, 0x2d, 0x3b, 0x08, 0xaf, 0x0c, 0x00,
    0x00, 0x00,
];

#[get("/")]
async fn index() -> HttpResponse {
    HttpResponse::Ok()
        .insert_header(ContentEncoding::Gzip)
        .body(HELLO_WORLD)
}
```
