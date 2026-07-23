# FastAPI — patterns & stack reference

Stack baselines verified at migration time (July 2026) against PyPI and the
official FastAPI and PostgreSQL release notes. Re-verify per project — FastAPI
is pre-1.0 and moves fast.

## Stack baseline

| Component | Notes |
|---|---|
| FastAPI | Pre-1.0, frequent releases (0.139.x at migration time). Verify current version; don't hardcode. |
| Pydantic | v2 — validation & serialization. |
| SQLAlchemy | 2.0 async ORM with `Mapped[T]` / `mapped_column`. |
| Database | PostgreSQL 18 (stable since Sept 2025); works with 17+. Driver: `asyncpg`. |
| Migrations | Alembic. |
| Python | 3.12+ (FastAPI supports 3.10–3.14). |
| Packaging / runner | `uv`. `fastapi dev` / `fastapi run` come from `fastapi[standard]`. |

## Project structure

```
backend/app/
  api/v1/        thin routers
  services/      business logic
  repositories/  DB access only
  models/        SQLAlchemy ORM (Base, mixins)
  schemas/       Pydantic v2
  db/            session.py, base.py
  core/          config.py, security.py, deps.py
  main.py        app entrypoint + lifespan
```

## SQLAlchemy 2.0 model syntax

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class User(Base, TimestampMixin):
    __tablename__ = "users"
    id:        Mapped[int]  = mapped_column(primary_key=True)
    email:     Mapped[str]  = mapped_column(String(255), unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)
```

Use `Mapped[T]` annotations with `mapped_column(...)`. Do **not** use the old
untyped `Column(...)` attribute style.

## Pydantic v2 schema syntax

```python
from pydantic import BaseModel

class UserRead(BaseModel):
    id: int
    email: str
    model_config = {"from_attributes": True}   # v2 — replaces orm_mode = True
```

## Lifespan (startup / shutdown)

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup: create engine / pools, warm caches
    yield
    # shutdown: dispose engine, close connections

app = FastAPI(lifespan=lifespan)
```

Never use the deprecated `@app.on_event("startup")` / `("shutdown")` hooks.

## Database session dependency

```python
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

DbDep = Annotated[AsyncSession, Depends(get_db)]

# Reuse the alias in every handler instead of repeating Depends(get_db):
@router.get("/users/{user_id}")
async def read_user(user_id: int, db: DbDep):
    ...
```

## Security baseline

- The app connects with a dedicated application role, never the Postgres
  superuser. Grant only the privileges the app needs.
- Keep credentials in environment variables / secrets, never in code.

## Package management (uv)

```bash
uv sync                          # install all deps from the lockfile
uv add fastapi                   # add a runtime package
uv add --dev pytest              # add a dev dependency
uv run fastapi dev app/main.py   # dev server (auto-reload)
uv run fastapi run app/main.py   # production mode (no reload)
uv run alembic upgrade head      # apply migrations
```

## Migration flow

1. Change the SQLAlchemy models.
2. `uv run alembic revision --autogenerate -m "describe change"`.
3. **Read the generated migration** — autogenerate misses some changes and
   guesses others. Fix it by hand where needed.
4. `uv run alembic upgrade head` to apply.
