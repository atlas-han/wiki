---
title: "Serde"
type: entity
category: tool
tags: [serde, rust, serialization]
created: 2026-06-06
updated: 2026-06-06
links: [https://serde.rs, https://docs.rs/serde]
sources: [actix-web-official-docs]
---

# Serde

Rust의 **직렬화/역직렬화** 프레임워크. `#[derive(Serialize, Deserialize)]`로 구조체를 JSON·URL-encoded form 등 다양한 포맷과 상호 변환한다.

[[actix-web]]의 [[actix-web-extractors|extractor]]가 serde에 의존한다 — `web::Json<T>`는 요청 본문을 `T`로 역직렬화하고, `web::Form<T>`는 `serde_urlencoded`로 폼을 파싱하며, `web::Query<T>`는 쿼리스트링을 매핑한다. 응답 측에서도 [[actix-web-handlers-responders|Responder]]가 `serde_json`으로 직렬화한다.

## References

- <https://serde.rs>
