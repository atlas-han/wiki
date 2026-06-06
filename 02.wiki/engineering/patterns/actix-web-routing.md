---
title: "Actix Web — URL Dispatch & Routing"
type: engineering
category: pattern
tags: [actix-web, rust, routing, url-dispatch, guards]
created: 2026-06-06
updated: 2026-06-06
related: [actix-web-extractors, actix-web-application-state, actix-web-handlers-responders]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

# Actix Web — URL Dispatch & Routing

[[actix-web]]의 URL dispatch는 간단한 패턴 매칭 언어로 URL path를 핸들러에 매핑한다. 요청 path가 등록된 패턴 중 하나에 매칭되면 해당 핸들러가 호출되고, 어디에도 매칭되지 않으면 *NOT FOUND*가 반환된다. 매칭은 **route가 등록된 순서대로** 검사되며 첫 매칭이 채택된다.

## Resource 등록: route() vs service()

가장 간단한 방법은 `App::route(path, route)`로 단일 route를 등록하는 것이다. 같은 path에 여러 번 호출할 수 있지만, **첫 매칭이 사용되므로** HTTP method나 guard가 다르지 않으면 첫 번째만 동작한다.

```rust
use actix_web::{web, App, HttpResponse, HttpServer};

async fn index() -> HttpResponse {
    HttpResponse::Ok().body("Hello")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/", web::get().to(index))
            .route("/user", web::post().to(index))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

완전한 resource 설정(이름, 여러 route, guard)이 필요하면 `App::service(web::resource(...))`를 쓴다. `web::get()`/`web::post()`는 method guard가 붙은 route를 만든다.

```rust
use actix_web::{guard, web, App, HttpResponse};

async fn index() -> HttpResponse {
    HttpResponse::Ok().body("Hello")
}

pub fn main() {
    App::new()
        .service(web::resource("/prefix").to(index))
        .service(
            web::resource("/user/{name}")
                .name("user_detail")
                .guard(guard::Header("content-type", "application/json"))
                .route(web::get().to(HttpResponse::Ok))
                .route(web::put().to(HttpResponse::Ok)),
        );
}
```

resource는 route를 등록 순서대로 검사한다. 한 *Route*는 guard를 몇 개든 가질 수 있지만 handler는 하나뿐이다.

## 패턴 문법: 동적 세그먼트 · tail · 정규식

- **동적 세그먼트** `{identifier}`: 다음 slash 전까지의 문자를 받아 `match_info`의 키로 저장. 내부 정규식은 `[^{}/]+` (slash 아닌 1+ 문자).
- 세그먼트 안에서 매칭은 첫 비영숫자 문자까지만 진행된다. `foo/{name}.html`은 `/foo/biz.html`에 매칭되어 `Params {'name': 'biz'}`. `foo/{name}.{ext}`는 `biz.html`을 `name=biz, ext=html`로 분해.
- **정규식 제약**: `{foo:\d+}`처럼 콜론 뒤에 정규식을 지정. 기본은 `{foo}` == `{foo:[^/]+}`.
- **tail match**: `foo/{bar}/{tail:.*}` → `foo/abc/def/a/b/c`가 `tail='def/a/b/c'`로 나머지 전부를 흡수.
- 세그먼트는 최소 1글자가 있어야 매칭된다. `/abc/`에 대해 `/abc/{foo}`는 매칭 실패, `/{foo}/`는 매칭.
- path는 매칭 전에 URL-decode 된다. `/foo/La%20Pe%C3%B1a` → `Params {'bar': 'La Peña'}`. 패턴 리터럴에는 디코딩된 값을 쓴다(`/Foo Bar/{baz}`, not `/Foo%20Bar/{baz}`).

## Route matching 순서가 중요한 이유

요청이 들어오면 actix는 `App::service()`로 **선언된 순서대로** 각 resource 패턴을 검사한다. route의 모든 guard가 `true`여야 그 route가 채택된다. 하나라도 `false`면 그 route를 건너뛰고 다음으로 진행한다. 첫 매칭에서 멈추므로, **더 구체적인 패턴을 먼저** 등록해야 한다(넓은 패턴이 앞에 있으면 뒤의 구체적 route가 영영 닿지 않음).

## 중첩 스코프 (web::scope)

`web::scope("/users")`는 그 안 모든 resource 패턴에 prefix를 붙인다. scope는 중첩 가능하다. 아래에서 `show_users`의 실효 패턴은 `/users/show`가 되고, `url_for("show_users", ...)`도 같은 path를 생성한다.

```rust
#[get("/show")]
async fn show_users() -> HttpResponse {
    HttpResponse::Ok().body("Show users")
}

#[get("/show/{id}")]
async fn user_detail(path: web::Path<(u32,)>) -> HttpResponse {
    HttpResponse::Ok().body(format!("User detail: {}", path.into_inner().0))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().service(
            web::scope("/users")
                .service(show_users)
                .service(user_detail),
        )
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

스코프 단위로 별도 state를 둘 수 있다 → [[actix-web-application-state]].

## Guards: Header · Method · Not / Any / All

guard는 *request* 참조를 받아 `true`/`false`를 반환하는 `Guard` trait 구현체다. request를 읽을 수만 있고 수정은 못 한다(필요하면 request extensions에 정보 저장 가능).

```rust
use actix_web::{
    guard::{Guard, GuardContext},
    http, HttpResponse,
};

struct ContentTypeHeader;

impl Guard for ContentTypeHeader {
    fn check(&self, req: &GuardContext) -> bool {
        req.head().headers().contains_key(http::header::CONTENT_TYPE)
    }
}
```

조합 guard:

- `guard::Not(guard::Get())` — GET이 아닌 모든 method.
- `guard::Any(guard::Get()).or(guard::Post())` — 하나라도 매칭.
- `guard::All(guard::Get()).and(guard::Header("content-type", "plain/text"))` — 전부 매칭.

가상 호스팅은 `guard::Host("www.rust-lang.org")`처럼 호스트 헤더로 scope를 분기한다.

## match_info / Path 추출

매칭된 동적 세그먼트는 `HttpRequest::match_info()`로 직접 꺼내거나, 타입 안전한 `web::Path` 추출기로 받는다. tuple은 패턴 세그먼트와 1:1 대응해야 하고, struct는 serde `Deserialize`를 구현해야 한다.

```rust
use actix_web::{get, web, App, HttpServer, Result};

#[get("/{username}/{id}/index.html")] // <- define path parameters
async fn index(info: web::Path<(String, u32)>) -> Result<String> {
    let info = info.into_inner();
    Ok(format!("Welcome {}! id: {}", info.0, info.1))
}
```

추출기 일반론(`Path`/`Query`/`Json` 등)은 → [[actix-web-extractors]], 응답 변환은 → [[actix-web-handlers-responders]].

## 명명 리소스 + url_for로 URL 생성

resource에 `.name("foo")`를 주면 `HttpRequest::url_for("foo", segments)`로 패턴 기반 URL을 생성할 수 있다(명명되지 않은 resource는 에러). `external_resource()`로 매칭에는 안 쓰이고 URL 생성에만 쓰이는 외부 URL도 등록 가능.

```rust
use actix_web::{get, guard, http::header, HttpRequest, HttpResponse, Result};

#[get("/test/")]
async fn index(req: HttpRequest) -> Result<HttpResponse> {
    let url = req.url_for("foo", ["1", "2", "3"])?; // <- generate url for "foo" resource

    Ok(HttpResponse::Found()
        .insert_header((header::LOCATION, url.as_str()))
        .finish())
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    use actix_web::{web, App, HttpServer};

    HttpServer::new(|| {
        App::new()
            .service(
                web::resource("/test/{a}/{b}/{c}")
                    .name("foo") // <- set resource name, then it could be used in `url_for`
                    .guard(guard::Get())
                    .to(HttpResponse::Ok),
            )
            .service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

## NormalizePath와 ⚠️ POST→GET 데이터 손실

`middleware::NormalizePath`는 trailing slash 추가, 중복 slash 병합 등으로 path를 정규화하고, 정규화된 경로로 **redirect** 한다(예: `//resource///` → `/resource/`).

> 문서 경고: 이 메커니즘으로 *POST* 요청을 redirect 해서는 안 된다. slash-appending *Not Found* redirect는 **POST 요청을 GET으로 바꿔 원래의 POST 데이터를 잃는다**.

따라서 정규화 redirect는 GET에만 거는 것이 안전하다.

```rust
use actix_web::{http::Method, middleware, web, App, HttpServer};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .wrap(middleware::NormalizePath::default())
            .service(index)
            .default_service(web::route().method(Method::GET))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

## 기본 Not Found 응답 변경

매칭되는 resource/route가 없으면 default resource가 쓰이며 기본은 *NOT FOUND*. `App::default_service()`로 이를 덮어쓸 수 있다(예: GET 외 method에 `MethodNotAllowed` 반환).

## References

- [[actix-web-official-docs]] — URL Dispatch (Resource configuration, Route matching, Pattern syntax, Scoping, Guards, `url_for`, NormalizePath, default_service)
- 추출기: [[actix-web-extractors]]
- 핸들러·응답: [[actix-web-handlers-responders]]
- 스코프 상태: [[actix-web-application-state]]
