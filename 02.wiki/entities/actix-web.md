---
title: "Actix Web"
type: entity
category: tool
tags: [actix-web, rust, web-framework, async]
created: 2026-06-06
updated: 2026-06-06
links: [https://actix.rs, https://docs.rs/actix-web, https://github.com/actix/actix-web]
sources: [actix-web-official-docs]
---

# Actix Web

**Rust**의 강력하고 실용적인 **비동기 웹 프레임워크**. async/await + [[tokio]] 런타임 위에 구축되며, HTTP/1.1·HTTP/2·TLS를 네이티브 지원한다. 타입 안전한 **extractor** 패턴, 조합 가능한 **미들웨어**, 코어당 워커 스레드를 띄우는 멀티스레드 **HttpServer**가 특징. stable Rust(MSRV 1.72)에서 동작하며 nightly가 필요 없다.

이 페이지는 actix-web 지식의 **허브** — 아래 "주요 개념"이 개별 가이드 페이지로 연결된다.

## actor 프레임워크와의 관계

> 한때 actix-web은 [[actix-actor-framework|actix actor 프레임워크]] 위에 구축됐으나, 지금은 *"largely unrelated to the actor framework"* (공식 문서 *What is Actix Web*). actor는 현재 WebSocket 엔드포인트 등 일부에서만 선택적으로 쓰인다. 코어 웹 처리는 tokio 기반.

## 생태계 (주요 crate)

- `actix-web` — 코어 프레임워크
- `actix-files` — 정적 파일 서빙 (`NamedFile`, `Files`)
- `actix-web-actors` / `actix-ws` — WebSocket
- `actix-cors` — CORS 미들웨어 · `actix-session` — 세션 미들웨어 · `actix-multipart` — multipart 파싱
- 직렬화는 [[serde]], TLS는 `rustls`/`openssl`에 의존

## 주요 개념 (사용 가이드)

### 요청 처리
- [[actix-web-extractors]] — `FromRequest`·`web::Path/Query/Json/Form/Data`로 타입 안전 추출
- [[actix-web-handlers-responders]] — 핸들러 시그니처·`Responder` trait·스트리밍 응답
- [[actix-web-routing]] — URL dispatch, 패턴 매칭, scope, guard, URL 생성

### 애플리케이션·서버
- [[actix-web-application-state]] — `App`·`app_data`·`web::Data` 공유 상태 (워커 클로저 함정)
- [[actix-web-http-server]] — `HttpServer` 워커 모델·TLS/HTTP2·graceful shutdown·정적 파일
- [[actix-web-connection-lifecycle]] — Accept/Worker/Dispatcher 루프 (내부 동작 다이어그램)

### 횡단 관심사
- [[actix-web-middleware]] — `Transform`+`Service`, 로깅·CORS·세션·압축
- [[actix-web-error-handling]] — `ResponseError` trait, 커스텀 에러 응답

### 통합·테스트
- [[actix-web-testing]] — `TestRequest`·`init_service` 통합 테스트
- [[actix-web-websockets]] — `actix-ws` WebSocket 핸들링
- [[actix-web-databases]] — `web::block`(Diesel 동기) · SeaORM(async) · r2d2 풀

## 개발 워크플로 메모

- 핸들러에서 절대 블로킹 금지(`std::thread::sleep` 등) — 동기 작업은 [[actix-web-databases|web::block]]로 오프로드.
- 개발 중 자동 재컴파일은 `watchexec`(예: `watchexec -e rs -r cargo run`) 사용.

## References

- 공식 문서: <https://actix.rs/docs> ([[actix-web-official-docs]])
- API: <https://docs.rs/actix-web/4>
