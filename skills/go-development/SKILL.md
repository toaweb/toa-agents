---
name: go-development
description: Build and review Go services, APIs and CLIs — modern net/http routing (method + wildcard ServeMux patterns, Go 1.22+), log/slog structured logging, context propagation, error wrapping with errors.Is/As, generics where they earn their place, table-driven tests, module hygiene and cmd/ + internal/ project layout. Also use to modernize legacy patterns (ioutil, GOPATH-era layout, interface{} instead of any, third-party routers where the stdlib mux suffices, goroutines without a cancellation path). Not for non-Go backends — defer Python API work to the FastAPI skill — and not a database-design skill; defer schema and query design to the Postgres skill.
---

# Go development

Senior Go specialist. Go 1.26 is the current line (released February 2026;
Green Tea GC on by default, `new(expr)`, goroutine leak detection). Go's
compatibility promise means old code still runs — but plenty of pre-1.22
*patterns* are obsolete, and training-data Go skews old. Verify the project's
version from the `go` directive in `go.mod`.

## Core principles

**Stdlib first.** Since Go 1.22, `net/http.ServeMux` routes by method and
wildcard (`mux.HandleFunc("GET /posts/{id}", ...)`). Reach for a third-party
router only for a concrete missing need (middleware ecosystems, route groups)
— never by reflex.

**Errors are values, and every one is handled.** Wrap with
`fmt.Errorf("...: %w", err)`, branch with `errors.Is` / `errors.As`. `_ = err`
is a bug you wrote on purpose. `panic` is for programmer errors, never
control flow.

**Context flows down.** `ctx context.Context` is the first parameter of
anything that blocks, calls I/O, or can be cancelled. Never stored in a
struct.

**Every goroutine has an exit plan.** A goroutine without a cancellation or
completion path is a leak. Go 1.26's leak detection helps find them; design
prevents them.

**Interfaces live with the consumer.** Accept interfaces, return concrete
types. Define the interface where it is *used*, sized to what that consumer
needs — not next to the implementation as a mirror of it.

**`log/slog` for logs.** Structured, leveled, one logger configured at the
entrypoint and passed or wrapped — not `fmt.Println` and not global
third-party loggers by default.

**Small packages, `internal/` by default.** Export only what another module
genuinely needs.

## Anti-patterns — never produce these

- `io/ioutil` — deprecated; use `io` and `os` equivalents.
- `interface{}` where `any` reads better (1.18+), or reflection where
  generics do the job — and generics where a plain interface does.
- A third-party router for routes the 1.22+ ServeMux handles.
- Ignored errors, `panic` as control flow, or `fmt.Errorf` without `%w` when
  the cause should stay inspectable.
- Goroutines with no cancellation path; `time.Sleep` as synchronization
  (tests included) — use channels, `sync`, or `context`.
- Global mutable state and `init()` doing real work.
- GOPATH-era layout or a `pkg/` directory by cargo cult; use `cmd/` +
  `internal/`.
- Storing a `context.Context` in a struct field.

## Workflow

1. Confirm the Go version from `go.mod` and the module layout before writing
   code.
   - **Before relying on any feature from a recent release, fetch
     https://go.dev/doc/devel/release and the relevant release notes
     (e.g. https://go.dev/doc/go1.26) and confirm it against the project's
     `go` directive** — do not assume the newest toolchain from memory.
2. **Before scaffolding a service, handlers, logging or tests**, read
   `references/patterns.md` — project layout, the `net/http` server baseline
   with graceful shutdown, ServeMux routing, `slog` setup, error-handling and
   table-driven-test patterns, and the tooling commands.
   - **Before writing routing code, fetch https://pkg.go.dev/net/http and
     verify ServeMux pattern syntax (method, wildcards, precedence) against
     the current docs** rather than reproducing a third-party router's API
     from memory.
3. Handlers thin, business logic in packages under `internal/`; the database
   layer follows the Postgres skill.
4. Run `gofmt` (or `goimports`), `go vet`, and the project's linter after
   changes.
5. Verify: `go build ./...` and `go test -race ./...` before calling it done.

## Reference files

| File | Contents |
|---|---|
| `references/patterns.md` | Project layout, http server baseline (ServeMux patterns, timeouts, graceful shutdown), `slog` setup, error handling, table-driven tests, tooling commands, version notes |

## Source note

Written July 2026, verified against the official Go release notes
(go.dev/doc/go1.26; Go 1.26 released February 2026) and pkg.go.dev for the
1.22+ ServeMux routing surface. Re-verify the toolchain version per project.
