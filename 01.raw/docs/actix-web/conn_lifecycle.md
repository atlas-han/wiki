---
title: "Connection Lifecycle"
type: docs
source: https://actix.rs/docs/conn_lifecycle
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

**Source URL**: https://actix.rs/docs/conn_lifecycle

> 본 파일은 actix.rs 다이어그램 페이지를 GitHub 원본 + mermaid `.mmd` 소스로 재구성한 verbatim 캡처다. 렌더 SVG 대신 mermaid 소스를 보존한다.

# Architecture overview

After Server has started listening to all sockets, [`Accept`][accept] and [`Worker`][worker] are two main loops responsible for processing incoming client connections.

Once connection accepted Application level protocol processing happens in a protocol specific [`Dispatcher`][dispatcher] loop spawned from [`Worker`][worker].

    Please note, below diagrams are outlining happy-path scenarios only.

```mermaid
sequenceDiagram

participant ServerBuilder
participant Accept
participant WorkerClient
participant Worker
participant Dispatcher

ServerBuilder->>Accept: start(socks, workers)

Note over Accept: accept Connections
loop poll connections on sockets
	activate Accept
	Accept-->>Accept: poll() --> Conn
	Note over Accept: backpressure logic
	Accept->>WorkerClient: send(Conn)
end
deactivate Accept

Note over Worker: process Connections
loop Worker as Future::poll
	activate Worker
	Worker->>WorkerClient: rx.poll_next()
	Note over Worker: Service factories
	Worker-->>Dispatcher: new(stream)
end
deactivate Worker

Note over Dispatcher: process Requests
loop Dispatcher::poll
	activate Dispatcher
	Dispatcher-->>Dispatcher: Dispatch requests
end
deactivate Dispatcher
```

## Accept loop in more detail

```mermaid
sequenceDiagram

participant ServerBuilder
participant mio
participant Accept
participant WorkerClient

ServerBuilder->>Accept: start(socks, workers)
loop Continuous: poll
	Accept->>mio: mio::Poll::poll()
	alt poll() -> TIMER | CMD
		Accept-->>Accept: process_*
	else poll() -> NOTIFY
		Accept->>Accept: backpressure
	else poll() -> OTHER(token)
		Accept-->>Accept: accept_one(Conn)
		loop while exist WorkerClient
			Accept->>WorkerClient: send(Conn)
			alt send(Conn) -> Ok(_)
				Note over Accept: break loop
			else send(Conn) -> Err(_)
				Accept->>ServerBuilder: worker_faulted(idx)
				Accept->>Accept: remove worker, get next worker				
			end
		end
	end
end
```

Most of code implementation resides in [`actix-server`][server] crate for struct [`Accept`][accept].

## Worker loop in more detail

```mermaid
sequenceDiagram

participant ServerBuilder
participant WorkerClient
participant Worker
participant StreamService
participant HttpServiceHandler
participant Tokio

ServerBuilder-->>Tokio: spawn(Worker)

Tokio-->>Worker: poll()
alt WorkerState::Available
	loop
		Worker->>WorkerClient: rx.poll_next()
		WorkerClient->>Worker: WorkerCommand(Conn)
		Worker->>Worker: check_readiness()
		alt check_readiness() -> Ok(true)
			Note over Worker,StreamService: Worker::services[Conn.token]
			Worker-->>StreamService: call(ServerMessage::Connect(stream))
			StreamService->>HttpServiceHandler: call(stream)
			HttpServiceHandler->>StreamService: HttpServiceHandlerResponse as Future
			StreamService->>Tokio: spawn(HttpServiceHandlerResponse)

		else check_readiness() -> Ok(false)
			Worker-->>Worker: WorkerState::Unavailable
		else check_readiness() -> Err(token,idx)
			Worker-->>Worker: WorkerState::Restarting
		end
	end
end

Note over HttpServiceHandler: process connection
```

Most of code implementation resides in [`actix-server`][server] crate for struct [`Worker`][worker].

## Request loop roughly

```mermaid
sequenceDiagram

participant HttpServer
participant HttpServiceHandler
participant HSHR
participant State
participant Dispatcher
participant Tokio

Note over HSHR, State: HttpServiceHandlerResponse

HttpServer-->>HttpServiceHandler: eventually build...
alt Protocol::HTTP1
HttpServiceHandler->>Dispatcher: H1::Dispatcher::new()
HttpServiceHandler->>State: State::H1(Dispatcher)
else Protocol::HTTP2
HttpServiceHandler->>State: State::H2Handshake
end
HttpServiceHandler->>HSHR: HttpServiceHandlerResponse::new(State)
HttpServiceHandler-->>Tokio: StreamService->Tokio::spawn(HttpServiceHandlerResponse as Future)

Tokio->>HSHR: poll()
alt State::H2Handshake
HSHR->>Dispatcher: H2::Dispatcher::new(stream,services)
HSHR->>HSHR: poll()
else 
HSHR->>Dispatcher: poll()
end
Note over Dispatcher: requests loop
```

Most of code implementation for request loop resides in [`actix-web`][web] and [`actix-http`][http] crates.

[server]: https://crates.io/crates/actix-server
[web]: https://crates.io/crates/actix-web
[http]: https://crates.io/crates/actix-http
[accept]: https://github.com/actix/actix-net/blob/master/actix-server/src/accept.rs
[worker]: https://github.com/actix/actix-net/blob/master/actix-server/src/worker.rs
[dispatcher]: https://github.com/actix/actix-web/blob/master/actix-http/src/h1/dispatcher.rs
