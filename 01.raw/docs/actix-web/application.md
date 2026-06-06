---
title: "Application"
type: docs
source: https://actix.rs/docs/application
site: actix.rs
project: actix-web
section: Basics
created: 2026-06-06
tags:
  - clippings/docs
  - actix-web
  - rust
---

**Source URL**: https://actix.rs/docs/application

> 본 파일은 actix.rs 렌더링 페이지를 pandoc 으로 변환한 verbatim 캡처다. 코드 블록·산문 원문 보존, 네비게이션·앵커 노이즈만 제거.

# Writing an Application

`actix-web` provides various primitives to build web servers and
applications with Rust. It provides routing, middleware, pre-processing
of requests, post-processing of responses, etc.

All `actix-web` servers are built around the
[`App`](https://docs.rs/actix-web/4/actix_web/struct.App.html) instance.
It is used for registering routes for resources and middleware. It also
stores application state shared across all handlers within the same
scope.

An application's
[`scope`](https://docs.rs/actix-web/4/actix_web/struct.Scope.html) acts
as a namespace for all routes, i.e. all routes for a specific
application scope have the same url path prefix. The application prefix
always contains a leading "/" slash. If a supplied prefix does not
contain leading slash, it is automatically inserted. The prefix should
consist of value path segments.

> For an application with scope `/app`, any request with the paths
> `/app`, `/app/`, or `/app/test` would match; however, the path
> `/application` would not match.

```rust
use actix_web::{web, App, HttpServer, Responder};

async fn index() -> impl Responder {
    "Hello world!"
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().service(
            // prefixes all resources and routes attached to it...
            web::scope("/app")
                // ...so this handles requests for `GET /app/index.html`
                .route("/index.html", web::get().to(index)),
        )
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

In this example, an application with the `/app` prefix and an
`index.html` resource is created. This resource is available through the
`/app/index.html` url.

> For more information, check the [URL
> Dispatch](https://actix.rs/docs/url-dispatch#using-an-application-prefix-to-compose-applications)
> section.

## State

Application state is shared with all routes and resources within the
same scope. State can be accessed with the
[`web::Data<T>`](https://docs.rs/actix-web/4/actix_web/web/struct.Data.html)
extractor where `T` is the type of the state. State is also accessible
for middleware.

Let's write a simple application and store the application name in the
state:

```rust
use actix_web::{get, web, App, HttpServer};

// This struct represents state
struct AppState {
    app_name: String,
}

#[get("/")]
async fn index(data: web::Data<AppState>) -> String {
    let app_name = &data.app_name; // <- get app_name
    format!("Hello {app_name}!") // <- response with app_name
}
```

Next, pass in the state when initializing the App and start the
application:

```rust
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .app_data(web::Data::new(AppState {
                app_name: String::from("Actix Web"),
            }))
            .service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

Any number of state types could be registered within the application.

## Shared Mutable State

`HttpServer` accepts an application factory rather than an application
instance. An `HttpServer` constructs an application instance for each
thread. Therefore, application data must be constructed multiple times.
If you want to share data between different threads, a shareable object
should be used, e.g. `Send` + `Sync`.

Internally,
[`web::Data`](https://docs.rs/actix-web/4/actix_web/web/struct.Data.html)
uses `Arc`. So in order to avoid creating two `Arc`s, we should create
our Data before registering it using
[`App::app_data()`](https://docs.rs/actix-web/4/actix_web/struct.App.html#method.app_data).

In the following example, we will write an application with mutable,
shared state. First, we define our state and create our handler:

```rust
use actix_web::{web, App, HttpServer};
use std::sync::Mutex;

struct AppStateWithCounter {
    counter: Mutex<i32>, // <- Mutex is necessary to mutate safely across threads
}

async fn index(data: web::Data<AppStateWithCounter>) -> String {
    let mut counter = data.counter.lock().unwrap(); // <- get counter's MutexGuard
    *counter += 1; // <- access counter inside MutexGuard

    format!("Request number: {counter}") // <- response with count
}
```

and register the data in an `App`:

```rust
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Note: web::Data created _outside_ HttpServer::new closure
    let counter = web::Data::new(AppStateWithCounter {
        counter: Mutex::new(0),
    });

    HttpServer::new(move || {
        // move counter into the closure
        App::new()
            .app_data(counter.clone()) // <- register the created data
            .route("/", web::get().to(index))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

Key takeaways:

- State initialized *inside* the closure passed to `HttpServer::new` is
  local to the worker thread and may become de-synced if modified.
- To achieve *globally shared state*, it must be created **outside** of
  the closure passed to `HttpServer::new` and moved/cloned in.

## Using an Application Scope to Compose Applications

The
[`web::scope()`](https://docs.rs/actix-web/4/actix_web/web/fn.scope.html)
method allows setting a resource group prefix. This scope represents a
resource prefix that will be prepended to all resource patterns added by
the resource configuration. This can be used to help mount a set of
routes at a different location than the original author intended while
still maintaining the same resource names.

For example:

```rust
#[actix_web::main]
async fn main() {
    let scope = web::scope("/users").service(show_users);
    App::new().service(scope);
}
```

In the above example, the `show_users` route will have an effective
route pattern of `/users/show` instead of `/show` because the
application's scope argument will be prepended to the pattern. The route
will then only match if the URL path is `/users/show`, and when the
[`HttpRequest.url_for()`](https://docs.rs/actix-web/4/actix_web/struct.HttpRequest.html#method.url_for)
function is called with the route name `show_users`, it will generate a
URL with that same path.

## Application guards and virtual hosting

You can think of a guard as a simple function that accepts a *request*
object reference and returns *true* or *false*. Formally, a guard is any
object that implements the
[`Guard`](https://docs.rs/actix-web/4/actix_web/guard/trait.Guard.html)
trait. Actix Web provides several guards. You can check the [functions
section](https://docs.rs/actix-web/4/actix_web/guard/index.html#functions)
of the API docs.

One of the provided guards is
[`Host`](https://docs.rs/actix-web/4/actix_web/guard/fn.Host.html). It
can be used as a filter based on request header information.

```rust
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(
                web::scope("/")
                    .guard(guard::Host("www.rust-lang.org"))
                    .route("", web::to(|| async { HttpResponse::Ok().body("www") })),
            )
            .service(
                web::scope("/")
                    .guard(guard::Host("users.rust-lang.org"))
                    .route("", web::to(|| async { HttpResponse::Ok().body("user") })),
            )
            .route("/", web::to(HttpResponse::Ok))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

## Configure

For simplicity and reusability both
[`App`](https://docs.rs/actix-web/4/actix_web/struct.App.html#method.configure)
and
[`web::Scope`](https://docs.rs/actix-web/4/actix_web/struct.Scope.html#method.configure)
provide the `configure` method. This function is useful for moving parts
of the configuration to a different module or even library. For example,
some of the resource's configuration could be moved to a different
module.

```rust
use actix_web::{web, App, HttpResponse, HttpServer};

// this function could be located in a different module
fn scoped_config(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::resource("/test")
            .route(web::get().to(|| async { HttpResponse::Ok().body("test") }))
            .route(web::head().to(HttpResponse::MethodNotAllowed)),
    );
}

// this function could be located in a different module
fn config(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::resource("/app")
            .route(web::get().to(|| async { HttpResponse::Ok().body("app") }))
            .route(web::head().to(HttpResponse::MethodNotAllowed)),
    );
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .configure(config)
            .service(web::scope("/api").configure(scoped_config))
            .route(
                "/",
                web::get().to(|| async { HttpResponse::Ok().body("/") }),
            )
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

The result of the above example would be:

```rust
/         -> "/"
/app      -> "app"
/api/test -> "test"
```

Each
[`ServiceConfig`](https://docs.rs/actix-web/4/actix_web/web/struct.ServiceConfig.html)
can have its own `data`, `routes`, and `services`.
