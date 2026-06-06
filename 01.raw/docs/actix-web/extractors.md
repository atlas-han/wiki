---
title: "Extractors"
type: docs
source: https://actix.rs/docs/extractors
site: actix.rs
project: actix-web
section: Basics
created: 2026-06-06
tags:
  - clippings/docs
  - actix-web
  - rust
---

**Source URL**: https://actix.rs/docs/extractors

> 본 파일은 actix.rs 렌더링 페이지를 pandoc 으로 변환한 verbatim 캡처다. 코드 블록·산문 원문 보존, 네비게이션·앵커 노이즈만 제거.

# Type-safe Request Information Extraction

Actix Web provides a facility for type-safe request information access
called *extractors* (i.e., `impl FromRequest`). There are lots of
built-in extractor implementations (see
[implementors](https://docs.rs/actix-web/latest/actix_web/trait.FromRequest.html#implementors)).

An extractor can be accessed as an argument to a handler function. Actix
Web supports up to 12 extractors per handler function.

In most cases, argument position does not matter. However, if an
extractor **takes** the body (i.e., it reads *any* bytes from the
request body stream), then only the first extractor will succeed. If you
need fallback behavior such as "read body as JSON or just give me the
raw bytes if that fails", then use the
[`Either`](https://docs.rs/actix-web/4/actix_web/enum.Either.html)
extractor (e.g., `Either<Json<T>, Bytes>`).

Some other specific use cases where request bodies need reading twice
can be supported:

- For body (any extractor) + it's hash/digest, see [the `actix-hash`
  crate](https://docs.rs/actix-hash).
- For body (any extractor) + custom request signature scheme: see [the
  `RequestSignature`
  extractor](https://docs.rs/actix-web-lab/0.21/actix_web_lab/extract/struct.RequestSignature.html)
  from `actix-web-lab`.

Simple example showing extraction of two positional dynamic path
segments and a JSON body:

```rust
async fn index(path: web::Path<(String, String)>, json: web::Json<MyInfo>) -> impl Responder {
    let path = path.into_inner();
    format!("{} {} {} {}", path.0, path.1, json.id, json.username)
}
```

## Path

[*Path*](https://docs.rs/actix-web/4/actix_web/dev/struct.Path.html)
provides information that is extracted from the request's path. Parts of
the path that are extractable are called "dynamic segments" and are
marked with curly braces. You can deserialize any variable segment from
the path.

For instance, for resource that registered for the
`/users/{user_id}/{friend}` path, two segments could be deserialized,
`user_id` and `friend`. These segments could be extracted as a tuple in
the order they are declared (e.g., `Path<(u32, String)>`).

```rust
use actix_web::{get, web, App, HttpServer, Result};

/// extract path info from "/users/{user_id}/{friend}" url
/// {user_id} - deserializes to a u32
/// {friend} - deserializes to a String
#[get("/users/{user_id}/{friend}")] // <- define path parameters
async fn index(path: web::Path<(u32, String)>) -> Result<String> {
    let (user_id, friend) = path.into_inner();
    Ok(format!("Welcome {}, user_id {}!", friend, user_id))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(index))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}
```

It is also possible to extract path information to a type that
implements the `Deserialize` trait from `serde` by matching dynamic
segment names with field names. Here is an equivalent example that uses
a deserialization struct using `serde` (make sure to enable its `derive`
feature) instead of a tuple type.

```rust
use actix_web::{get, web, Result};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
    user_id: u32,
    friend: String,
}

/// extract path info using serde
#[get("/users/{user_id}/{friend}")] // <- define path parameters
async fn index(info: web::Path<Info>) -> Result<String> {
    Ok(format!(
        "Welcome {}, user_id {}!",
        info.friend, info.user_id
    ))
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

As a non-type-safe alternative, it's also possible to query (see
[`match_info`
docs](https://docs.rs/actix-web/latest/actix_web/struct.HttpRequest.html#method.match_info))
the request for path parameters by name within a handler:

```rust
#[get("/users/{user_id}/{friend}")] // <- define path parameters
async fn index(req: HttpRequest) -> Result<String> {
    let name: String = req.match_info().get("friend").unwrap().parse().unwrap();
    let userid: i32 = req.match_info().query("user_id").parse().unwrap();

    Ok(format!("Welcome {}, user_id {}!", name, userid))
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

## Query

The
[`Query<T>`](https://docs.rs/actix-web/4/actix_web/web/struct.Query.html)
type provides extraction functionality for the request's query
parameters. Underneath it uses `serde_urlencoded` crate.

```rust
use actix_web::{get, web, App, HttpServer};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
    username: String,
}

// this handler gets called if the query deserializes into `Info` successfully
// otherwise a 400 Bad Request error response is returned
#[get("/")]
async fn index(info: web::Query<Info>) -> String {
    format!("Welcome {}!", info.username)
}
```

## JSON

[`Json<T>`](https://docs.rs/actix-web/4/actix_web/web/struct.Json.html)
allows deserialization of a request body into a struct. To extract typed
information from a request's body, the type `T` must implement
`serde::Deserialize`.

```rust
use actix_web::{post, web, App, HttpServer, Result};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
    username: String,
}

/// deserialize `Info` from request's body
#[post("/submit")]
async fn submit(info: web::Json<Info>) -> Result<String> {
    Ok(format!("Welcome {}!", info.username))
}
```

Some extractors provide a way to configure the extraction process. To
configure an extractor, pass its configuration object to the resource's
`.app_data()` method. In the case of *Json* extractor it returns a
[*JsonConfig*](https://docs.rs/actix-web/4/actix_web/web/struct.JsonConfig.html).
You can configure the maximum size of the JSON payload as well as a
custom error handler function.

The following example limits the size of the payload to 4kb and uses a
custom error handler.

```rust
use actix_web::{error, web, App, HttpResponse, HttpServer, Responder};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
    username: String,
}

/// deserialize `Info` from request's body, max payload size is 4kb
async fn index(info: web::Json<Info>) -> impl Responder {
    format!("Welcome {}!", info.username)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        let json_config = web::JsonConfig::default()
            .limit(4096)
            .error_handler(|err, _req| {
                // create custom error response
                error::InternalError::from_response(err, HttpResponse::Conflict().finish())
                    .into()
            });

        App::new().service(
            web::resource("/")
                // change json extractor configuration
                .app_data(json_config)
                .route(web::post().to(index)),
        )
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

## URL-Encoded Forms

A URL-encoded form body can be extracted to a struct, much like
`Json<T>`. This type must implement `serde::Deserialize`.

[*FormConfig*](https://docs.rs/actix-web/4/actix_web/web/struct.FormConfig.html)
allows configuring the extraction process.

```rust
use actix_web::{post, web, App, HttpServer, Result};
use serde::Deserialize;

#[derive(Deserialize)]
struct FormData {
    username: String,
}

/// extract form data using serde
/// this handler gets called only if the content type is *x-www-form-urlencoded*
/// and the content of the request could be deserialized to a `FormData` struct
#[post("/")]
async fn index(form: web::Form<FormData>) -> Result<String> {
    Ok(format!("Welcome {}!", form.username))
}
```

If the form body is optional, or you want to handle invalid input
yourself, wrap the extractor in `Option` and check for `None` in your
handler.

```rust
use actix_web::{post, web, App, HttpServer, Result};
use serde::Deserialize;

#[derive(Deserialize)]
struct FormData {
    username: String,
}

/// accept form data when it is present and valid
#[post("/maybe")]
async fn maybe(form: Option<web::Form<FormData>>) -> Result<String> {
    let Some(form) = form else {
        return Ok("Missing or invalid form data.".to_string());
    };

    Ok(format!("Welcome {}!", form.username))
}
```

## Other

Actix Web also provides many other extractors, here's a few important
ones:

- [`Data`](https://docs.rs/actix-web/4/actix_web/web/struct.Data.html) -
  For accessing pieces of application state.
- [`HttpRequest`](https://docs.rs/actix-web/4/actix_web/struct.HttpRequest.html) -
  `HttpRequest` is itself an extractor, in case you need access to other
  parts of the request.
- `String` - You can convert a request's payload to a `String`. [*An
  example*](https://docs.rs/actix-web/4/actix_web/trait.FromRequest.html#impl-FromRequest-for-String)
  is available in the rustdoc.
- [`Bytes`](https://docs.rs/actix-web/4/actix_web/web/struct.Bytes.html) -
  You can convert a request's payload into *Bytes*. [*An
  example*](https://docs.rs/actix-web/4/actix_web/trait.FromRequest.html#impl-FromRequest-5)
  is available in the rustdoc.
- [`Payload`](https://docs.rs/actix-web/4/actix_web/web/struct.Payload.html) -
  Low-level payload extractor primarily for building other extractors.
  [*An
  example*](https://docs.rs/actix-web/4/actix_web/web/struct.Payload.html)
  is available in the rustdoc.

## Application State Extractor

Application state is accessible from the handler with the `web::Data`
extractor; however, state is accessible as a read-only reference. If you
need mutable access to state, it must be implemented.

Here is an example of a handler that stores the number of processed
requests:

```rust
use actix_web::{web, App, HttpServer, Responder};
use std::cell::Cell;

#[derive(Clone)]
struct AppState {
    count: Cell<usize>,
}

async fn show_count(data: web::Data<AppState>) -> impl Responder {
    format!("count: {}", data.count.get())
}

async fn add_one(data: web::Data<AppState>) -> impl Responder {
    let count = data.count.get();
    data.count.set(count + 1);

    format!("count: {}", data.count.get())
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let data = AppState {
        count: Cell::new(0),
    };

    HttpServer::new(move || {
        App::new()
            .app_data(web::Data::new(data.clone()))
            .route("/", web::to(show_count))
            .route("/add", web::to(add_one))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

Although this handler will work, `data.count` will only count the number
of requests handled *by each worker thread*. To count the number of
total requests across all threads, one should use shared `Arc` and
[atomics](https://doc.rust-lang.org/std/sync/atomic/).

```rust
use actix_web::{get, web, App, HttpServer, Responder};
use std::{
    cell::Cell,
    sync::atomic::{AtomicUsize, Ordering},
    sync::Arc,
};

#[derive(Clone)]
struct AppState {
    local_count: Cell<usize>,
    global_count: Arc<AtomicUsize>,
}

#[get("/")]
async fn show_count(data: web::Data<AppState>) -> impl Responder {
    format!(
        "global_count: {}\nlocal_count: {}",
        data.global_count.load(Ordering::Relaxed),
        data.local_count.get()
    )
}

#[get("/add")]
async fn add_one(data: web::Data<AppState>) -> impl Responder {
    data.global_count.fetch_add(1, Ordering::Relaxed);

    let local_count = data.local_count.get();
    data.local_count.set(local_count + 1);

    format!(
        "global_count: {}\nlocal_count: {}",
        data.global_count.load(Ordering::Relaxed),
        data.local_count.get()
    )
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let data = AppState {
        local_count: Cell::new(0),
        global_count: Arc::new(AtomicUsize::new(0)),
    };

    HttpServer::new(move || {
        App::new()
            .app_data(web::Data::new(data.clone()))
            .service(show_count)
            .service(add_one)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

**Note**: If you want the *entire* state to be shared across all
threads, use `web::Data` and `app_data` as described in [Shared Mutable
State](https://actix.rs/docs/application#shared-mutable-state).

Be careful when using blocking synchronization primitives like `Mutex`
or `RwLock` within your app state. Actix Web handles requests
asynchronously. It is a problem if the [*critical
section*](https://en.wikipedia.org/wiki/Critical_section) in your
handler is too big or contains an `.await` point. If this is a concern,
we would advise you to also read [Tokio's advice on using blocking
`Mutex` in async
code](https://tokio.rs/tokio/tutorial/shared-state#on-using-stdsyncmutex).
