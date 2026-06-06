---
title: "Actix Web — Databases (web::block & async ORM)"
type: engineering
category: pattern
tags: [actix-web, rust, database, diesel, seaorm, r2d2]
created: 2026-06-06
updated: 2026-06-06
related: [actix-web-application-state, actix-web-extractors, tokio]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

[[actix-web]]는 비동기 서버이므로 DB 접근 방식이 드라이버의 동기/비동기 여부에 따라 갈린다. 동기 드라이버(Diesel)는 `web::block`으로 스레드 풀에 오프로드하고, 비동기 ORM(SeaORM)은 네이티브 async/await라 그대로 `.await` 한다.

## ⚠️ 핵심 원칙: 핸들러에서 블로킹 금지

[[tokio]] 기반 이벤트 루프는 적은 수의 워커 스레드로 수많은 connection을 처리한다. 동기 DB 호출처럼 스레드를 점유하는 블로킹 연산을 핸들러에서 직접 호출하면 그 워커가 막혀 다른 요청까지 멈춘다. 따라서 **블로킹 작업은 반드시 별도 스레드 풀로 내보내야** 한다.

## 동기 드라이버 (Diesel) → web::block

Diesel v1/v2는 비동기를 지원하지 않으므로 `web::block(|| { ... }).await`로 Actix 런타임의 스레드 풀에 DB 연산을 오프로드한다. 먼저 DB 연산에 대응하는 action 함수를 작성한다.

```rust
fn insert_new_user(
    conn: &mut SqliteConnection,
    user_name: String,
) -> diesel::QueryResult<User> {
    use crate::schema::users::dsl::*;

    let uid = format!("{}", uuid::Uuid::new_v4());
    let new_user = NewUser {
        id: &uid,
        name: &user_name,
    };

    diesel::insert_into(users)
        .values(&new_user)
        .execute(conn)
        .expect("Error inserting person");

    let user = users
        .filter(id.eq(&uid))
        .first::<User>(conn)
        .expect("Error loading person that was just inserted");

    Ok(user)
}
```

### r2d2 커넥션 풀을 web::Data로 공유

`r2d2` 풀을 `App`의 상태에 `web::Data`로 넣어 모든 핸들러가 공유하게 한다 ([[actix-web-application-state]]). 풀은 내부적으로 공유 접근을 처리하므로 별도 래퍼 struct로 감쌀 필요가 없다.

```rust
type DbPool = r2d2::Pool<r2d2::ConnectionManager<SqliteConnection>>;

#[actix_web::main]
async fn main() -> io::Result<()> {
    let manager = r2d2::ConnectionManager::<SqliteConnection>::new("app.db");
    let pool = r2d2::Pool::builder()
        .build(manager)
        .expect("database URL should be valid path to SQLite DB file");

    HttpServer::new(move || {
        App::new()
            .app_data(web::Data::new(pool.clone()))
            .route("/{name}", web::get().to(index))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

### Canonical 핸들러: 풀 추출 + web::block

핸들러에서 `web::Data<DbPool>` 추출기로 풀을 받고 ([[actix-web-extractors]]), `web::block` 클로저 안에서 커넥션을 얻어 action 함수를 호출한다.

```rust
async fn index(
    pool: web::Data<DbPool>,
    name: web::Path<(String,)>,
) -> actix_web::Result<impl Responder> {
    let (name,) = name.into_inner();

    let user = web::block(move || {
        // 풀에서 커넥션을 얻는 것도 잠재적 블로킹 연산이므로
        // web::block 클로저 안에서 호출한다.
        let mut conn = pool.get().expect("couldn't get db connection from pool");

        insert_new_user(&mut conn, name)
    })
    .await?
    .map_err(error::ErrorInternalServerError)?;

    Ok(HttpResponse::Ok().json(user))
}
```

> 💡 `.await?`가 두 번 풀리는 구조: 바깥 `?`는 `web::block`의 `BlockingError`(스레드 풀 실패)를, 안쪽 `.map_err(...)?`는 action 함수의 DB 에러를 처리한다. 반환 에러 타입이 `ResponseError`를 구현하면 `map_err`는 생략 가능하다 (→ [[actix-web-error-handling]]).
>
> ⚠️ 풀에서 커넥션을 얻는 `pool.get()` 자체도 블로킹일 수 있으므로 **반드시 `web::block` 안에서** 호출한다.

## 비동기 ORM (SeaORM) → web::block 불필요

SeaORM은 full async를 지원해 핸들러에서 직접 `.await` 할 수 있다. 커넥션 풀도 SeaORM이 기본으로 관리하므로 추가 풀 설정이 필요 없다.

```rust
#[actix_web::main]
async fn main() -> io::Result<()> {
    let database_url = "sqlite:app.db";
    let conn = Database::connect(database_url)
        .await
        .expect("Failed to connect to database");

    HttpServer::new(move || {
        App::new()
            .app_data(web::Data::new(conn.clone()))
            .route("/{name}", web::get().to(index))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}

async fn index(
    conn: web::Data<DatabaseConnection>,
    name: web::Path<(String,)>,
) -> actix_web::Result<impl Responder> {
    let (name,) = name.into_inner();

    let user = insert_new_user(&conn, name)
        .await
        .map_err(error::ErrorInternalServerError)?;

    Ok(HttpResponse::Ok().json(user))
}
```

## 언제 무엇을 쓰나

| 드라이버 | async 지원 | 핸들러에서 |
|----------|-----------|-----------|
| Diesel (v1/v2) | ❌ | `web::block` + `r2d2` 풀 필수 |
| SeaORM | ✅ | 직접 `.await`, 자체 풀 관리 |
| sqlx, mongodb 등 | ✅ | 직접 `.await` |

원칙은 하나다 — **드라이버가 동기면 `web::block`, 비동기면 그대로 `.await`**. 어느 쪽이든 풀은 `web::Data`로 공유한다.

## References

- [[actix-web-official-docs]] — Databases (https://actix.rs/docs/databases)
- [[actix-web]] · [[actix-web-application-state]] · [[actix-web-extractors]] · [[tokio]] · [[actix-web-error-handling]]
