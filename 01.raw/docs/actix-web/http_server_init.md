---
title: "HTTP Server Initialization"
type: docs
source: https://actix.rs/docs/http_server_init
site: actix.rs
project: actix-web
section: Diagrams
created: 2026-06-06
tags:
  - clippings/docs
  - actix-web
  - rust
  - diagram
---

**Source URL**: https://actix.rs/docs/http_server_init

> 본 파일은 actix.rs 다이어그램 페이지를 GitHub 원본 + mermaid `.mmd` 소스로 재구성한 verbatim 캡처다. 렌더 SVG 대신 mermaid 소스를 보존한다.

# Architecture overview

Below is a diagram of HttpServer initialization, which happens on the following code

```rust
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/", web::to(|| HttpResponse::Ok()))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

```mermaid
sequenceDiagram

participant HttpServer
participant ServerBuilder
participant Worker
participant StreamNewService
participant HttpService
participant HttpServiceResponse
participant Tokio

HttpServer-->>HttpService: build...
HttpServer->>ServerBuilder: listen(addr,Fn->HttpService)
ServerBuilder->>StreamNewService: create(addr,Fn->HttpService)
HttpServer->>ServerBuilder: start()
ServerBuilder->>Worker: start(StreamNewService)

Worker->>StreamNewService: InternalServiceFactory::create()
StreamNewService->>HttpService: new_service()
HttpService->>HttpServiceResponse: HttpServiceResponse::new()
HttpService->>StreamNewService: HttpServiceResponse as Future
StreamNewService->>Worker: StreamService(HttpServiceResponse) as Future
Worker-->>Tokio: spawn(StreamService(HttpServiceResponse)).map(Worker))
Tokio-->>HttpServiceResponse: poll()
HttpServiceResponse-->>Tokio: Ready(Worker(HttpServiceHandler))

loop Worker process messages
	Tokio-->>Worker: poll->Pending...
	activate Worker
	Note over Worker: pull messages
	deactivate Worker
end
```
