---
title: "Databases"
type: docs
source: https://actix.rs/docs/databases
site: actix.rs
project: actix-web
section: Patterns
created: 2026-06-06
tags:
  - clippings/docs
  - actix-web
  - rust
---

**Source URL**: https://actix.rs/docs/databases

> 본 파일은 actix.rs 렌더링 페이지를 pandoc 으로 변환한 verbatim 캡처다. 코드 블록·산문 원문 보존, 네비게이션·앵커 노이즈만 제거.

# Async Options

We have several example projects showing use of async database adapters:

- [Postgres](https://github.com/actix/examples/tree/master/databases/postgres)
- [SQLite](https://github.com/actix/examples/tree/master/databases/sqlite)
- [MongoDB](https://github.com/actix/examples/tree/master/databases/mongodb)

# Diesel

The current versions of Diesel (v1/v2) does not support asynchronous
operations, so it is important to use the
[`web::block`](https://docs.rs/actix-web/4/actix_web/web/fn.block.html)
function to offload your database operations to the Actix runtime
thread-pool.

You can create action functions that correspond to all the operations
your app will perform on the database.

```rust
#[derive(Debug, Insertable)]
#[diesel(table_name = self::schema::users)]
struct NewUser<'a> {
    id: &'a str,
    name: &'a str,
}

fn insert_new_user(
    conn: &mut SqliteConnection,
    user_name: String,
) -> diesel::QueryResult<User> {
    use crate::schema::users::dsl::*;

    // Create insertion model
    let uid = format!("{}", uuid::Uuid::new_v4());
    let new_user = NewUser {
        id: &uid,
        name: &user_name,
    };

    // normal diesel operations
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

Now you should set up the database pool using a crate such as `r2d2`,
which makes many DB connections available to your app. This means that
multiple handlers can manipulate the DB at the same time, and still
accept new connections. Simply, the pool in your app state. (In this
case, it's beneficial not to use a state wrapper struct because the pool
handles shared access for you.)

```rust
type DbPool = r2d2::Pool<r2d2::ConnectionManager<SqliteConnection>>;

#[actix_web::main]
async fn main() -> io::Result<()> {
    // connect to SQLite DB
    let manager = r2d2::ConnectionManager::<SqliteConnection>::new("app.db");
    let pool = r2d2::Pool::builder()
        .build(manager)
        .expect("database URL should be valid path to SQLite DB file");

    // start HTTP server on port 8080
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

Now, in a request handler, use the `Data<T>` extractor to get the pool
from app state and get a connection from it. This provides an owned
database connection that can be passed into a
[`web::block`](https://docs.rs/actix-web/4/actix_web/web/fn.block.html)
closure. Then just call the action function with the necessary arguments
and `.await` the result.

This example also maps the error to an `HttpResponse` before using the
`?` operator but this is not necessary if your return error type
implements
[`ResponseError`](https://docs.rs/actix-web/4/actix_web/error/trait.ResponseError.html).

```rust
async fn index(
    pool: web::Data<DbPool>,
    name: web::Path<(String,)>,
) -> actix_web::Result<impl Responder> {
    let (name,) = name.into_inner();

    let user = web::block(move || {
        // Obtaining a connection from the pool is also a potentially blocking operation.
        // So, it should be called within the `web::block` closure, as well.
        let mut conn = pool.get().expect("couldn't get db connection from pool");

        insert_new_user(&mut conn, name)
    })
    .await?
    .map_err(error::ErrorInternalServerError)?;

    Ok(HttpResponse::Ok().json(user))
}
```

That's it! See the full example
[here](https://github.com/actix/examples/tree/master/databases/diesel).

# SeaORM

[SeaORM](https://www.sea-ql.org/SeaORM/) is a Rust ORM with full async
support. When used with Actix Web, unlike Diesel, it allows you to
perform database operations directly in an asynchronous manner without
needing to use `web::block`.

First, define your data models and functions for database operations.
Using `sea-orm-cli`, you can use a data model that is automatically
generated from an existing DB definition:

```rust
// Importing the existing entity modules
pub mod prelude;
pub mod users;
use crate::users::ActiveModel as UserActiveModel;

#[derive(Debug, Serialize)]
struct User {
    id: String,
    name: String,
}

async fn insert_new_user(
    conn: &DatabaseConnection,
    user_name: String,
) -> Result<User, sea_orm::DbErr> {
    // Create insertion model
    let uid = Uuid::new_v4().to_string();
    let new_user = UserActiveModel {
        id: Set(uid.clone()),
        name: Set(user_name),
        ..Default::default()
    };

    // Insert the user
    let user = new_user.insert(conn).await?;

    Ok(User {
        id: user.id,
        name: user.name,
    })
}
```

Next, set up the database connection as part of your application state.
SeaORM manages connection pools by default, so you don't need additional
pool configuration:

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
```

In your request handler, use the `web::Data<DatabaseConnection>`
extractor to get the database connection and perform async operations
directly:

```rust
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

For a full example, please refer to
[here](https://github.com/actix/examples/tree/master/databases/sea-orm).
