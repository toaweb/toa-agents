# PostgreSQL — patterns & reference

Verified at migration time (July 2026) against the PostgreSQL 18 release
material. Re-verify the server version per project.

## Version baseline

- PostgreSQL 18 preferred (works with 17+). PG 18 is stable (since Sept 2025).
- Native `uuidv7()` requires PG 18 (no extension needed on 18+).
- scram-sha-256 is the default auth method (since PG 14).
- Drivers: `asyncpg` by default; **switch to `psycopg3` behind PgBouncer in
  transaction-pooling mode** — asyncpg relies on server-side prepared
  statements which break under transaction pooling. (Alternative mitigation:
  disable asyncpg's statement cache, e.g. `statement_cache_size=0`.)

## Naming conventions

```
Tables:       snake_case, plural       users, blog_posts, guild_members
Columns:      snake_case               user_id, is_active, created_at
Primary key:  always "id"              id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
Timestamps:   on every table           created_at, updated_at TIMESTAMPTZ
Indexes:      idx_<table>_<column>     idx_users_email
Foreign key:  fk_<table>_<ref>         fk_blog_posts_users
```

## ID strategy

- **Internal primary keys:** `BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY`.
- **Publicly exposed / distributed IDs:** `uuidv7()` (Postgres 18 native,
  time-ordered so new keys land at the right edge of the B-tree — index-friendly,
  unlike random `uuidv4`/`gen_random_uuid`).

```sql
CREATE TABLE posts (
  id UUID PRIMARY KEY DEFAULT uuidv7(),
  ...
);
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

Always `Mapped[T]` + `mapped_column`. Never the old untyped `Column(...)` style.
Put `TimestampMixin` (created_at / updated_at) on every model.

## App role setup (init.sql)

DDL is owned by the migration role; the app role gets DML only.

```sql
CREATE ROLE myapp_app WITH LOGIN PASSWORD 'from_env';
GRANT CONNECT ON DATABASE myapp TO myapp_app;
GRANT USAGE ON SCHEMA public TO myapp_app;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myapp_app;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO myapp_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myapp_app;
```

`ALTER DEFAULT PRIVILEGES` applies to objects created later **by the role that
runs it** — run it as the same role Alembic uses for DDL, so new tables are
automatically granted to the app role.

## Common fix: missing password on app role

scram-sha-256 login fails if the role has no password. Creating the role does
not set one automatically.

```sql
ALTER ROLE myapp_app WITH LOGIN PASSWORD 'set_password_here';
```

## Alembic workflow

```bash
uv run alembic revision --autogenerate -m "add users table"
uv run alembic upgrade head
uv run alembic current
uv run alembic downgrade -1
```

- Always **read** the generated migration before running — autogenerate misses
  some changes (e.g. some constraint/type edits) and guesses others.
- Never edit a migration that has already been applied; add a new one.

## Optimization checklist

- Index all foreign-key columns and frequent WHERE/JOIN/ORDER BY columns.
- `EXPLAIN (ANALYZE, BUFFERS)` on slow queries before adding indexes blindly.
- Watch for N+1 access patterns from the ORM; batch with `selectinload` /
  explicit joins where needed.
