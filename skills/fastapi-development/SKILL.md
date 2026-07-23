---
name: fastapi-development
description: Build and review FastAPI + Python backends — async route handlers, Pydantic v2 models, SQLAlchemy 2.0 async ORM, dependency injection, database sessions, Alembic migrations, and a layered router/service/repository architecture. Also use to modernize legacy patterns (Pydantic orm_mode, SQLAlchemy Column() style, @app.on_event startup hooks). Not for non-Python backends and not a database-design skill — defer schema and query design to a Postgres skill.
---

# FastAPI backend development

Senior FastAPI and Python backend specialist. FastAPI is still pre-1.0 and
releases frequently — **verify the current version** (`uv pip show fastapi` or
PyPI) rather than assuming a pinned baseline. Target Pydantic v2 and
SQLAlchemy 2.0; both have modern APIs that supersede common older examples.

## Core principles

**Async all the way.** Route handlers are `async def`. The DB layer uses an
async engine and `AsyncSession`. Don't mix sync DB calls into async handlers.

**Strict layering.** Router → service → repository, one direction only:
- **Router** is thin: parse/validate input, call a service, shape the response.
- **Service** holds business logic. It never writes SQL.
- **Repository** is the only layer that touches the database.

**Versioned from day one.** All routes live under `/api/v1/`.

**Least privilege in the database.** The app connects as a dedicated
application role, never as the Postgres superuser.

**Typed and validated.** Pydantic v2 schemas at the edges, SQLAlchemy 2.0
`Mapped[T]` models in the ORM, type hints on every signature.

## Anti-patterns — never produce these

- Business logic inside a router, or raw SQL inside a service.
- `orm_mode = True` — use `model_config = {"from_attributes": True}` (Pydantic v2).
- Old `Column(...)` model style — use `Mapped[T]` + `mapped_column(...)`.
- `@app.on_event("startup"/"shutdown")` — deprecated. Use a `lifespan`
  async context manager.
- Repeating `Depends(get_db)` everywhere — define one `Annotated` alias and reuse it.
- Unversioned routes mounted at `/`.
- Connecting to Postgres as a superuser.
- Blocking / synchronous I/O inside an async handler.

## Workflow

1. Confirm FastAPI, Pydantic (v2), SQLAlchemy (2.0) and Python versions before
   writing code.
2. **Before writing models, schemas, sessions, or the app entrypoint**, read
   `references/patterns.md` — it holds the canonical project structure, the
   SQLAlchemy 2.0 and Pydantic v2 syntax, the `lifespan` and DB-dependency
   patterns, and the package/migration commands.
3. Keep routers thin; put logic in services; keep SQL in repositories.
4. After any model change, autogenerate an Alembic revision and **review it**
   before applying.
5. Verify: run the test suite and start the dev server before calling it done.

## Reference files

| File | Contents |
|---|---|
| `references/patterns.md` | Project structure, SQLAlchemy 2.0 models, Pydantic v2 schemas, `lifespan`, DB dependency alias, package management (uv) and Alembic commands, current stack baselines |

## Source note

Migrated from a short project agent file. The stack baselines in
`references/patterns.md` were checked against PyPI and the official FastAPI /
PostgreSQL release notes; treat them as "current at migration time" and
re-verify versions per project.
