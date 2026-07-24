# Go — patterns & reference

Verified July 2026 against the official Go release notes and pkg.go.dev.
Go 1.26 is current (February 2026). Re-verify the `go` directive per project.

## Version notes

- **1.22** — ServeMux method + wildcard routing (`GET /posts/{id}`), loop
  variables scoped per iteration.
- **1.23** — iterator functions (`range` over func).
- **1.25** — Green Tea GC opt-in experiment.
- **1.26** — Green Tea GC **on by default**; `new(expr)` takes an expression
  (initial value); goroutine leak detection; cgo overhead ~30% lower.

## Project layout

```
.
├── cmd/
│   └── <appname>/main.go     entrypoint only: wire config, logger, server
├── internal/
│   ├── server/               http handlers + routing
│   ├── <domain>/             business logic, one package per domain
│   └── store/                database access (follow the Postgres skill)
├── go.mod                    module path + go directive = source of truth
└── go.sum
```

- `main.go` stays tiny: read config, build dependencies, call `run(ctx)`.
- No `pkg/` unless code is genuinely consumed by other modules.
- One package = one responsibility; avoid `utils`.

## HTTP server baseline

```go
func run(ctx context.Context, logger *slog.Logger) error {
	mux := http.NewServeMux()
	mux.HandleFunc("GET /healthz", handleHealthz)
	mux.HandleFunc("GET /api/v1/posts/{id}", handleGetPost)
	mux.HandleFunc("POST /api/v1/posts", handleCreatePost)

	srv := &http.Server{
		Addr:              ":8080",
		Handler:           mux,
		ReadHeaderTimeout: 5 * time.Second,   // never ship zero timeouts
		ReadTimeout:       10 * time.Second,
		WriteTimeout:      30 * time.Second,
		IdleTimeout:       120 * time.Second,
	}

	errCh := make(chan error, 1)
	go func() { errCh <- srv.ListenAndServe() }()

	select {
	case err := <-errCh:
		return err
	case <-ctx.Done(): // e.g. signal.NotifyContext(ctx, os.Interrupt, syscall.SIGTERM)
		shutdownCtx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		defer cancel()
		return srv.Shutdown(shutdownCtx)
	}
}
```

- Path values: `r.PathValue("id")` (1.22+).
- Wildcard forms: `{id}`, trailing `{path...}`, exact-match `{$}`.
- Middleware is just `func(http.Handler) http.Handler` — compose by wrapping;
  no framework needed for logging/recovery/request-ID.

## Structured logging (`log/slog`)

```go
logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{
	Level: slog.LevelInfo,
}))
slog.SetDefault(logger)

logger.Info("post created", "post_id", id, "author", author)
logger.Error("store failed", "err", err)
```

- One handler configured at the entrypoint; text handler in dev, JSON in prod.
- Attach request-scoped attrs with `logger.With(...)`, not global state.

## Error handling

```go
var ErrNotFound = errors.New("not found")

func (s *Store) Post(ctx context.Context, id string) (*Post, error) {
	p, err := s.query(ctx, id)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			return nil, fmt.Errorf("post %s: %w", id, ErrNotFound)
		}
		return nil, fmt.Errorf("querying post %s: %w", id, err)
	}
	return p, nil
}

// Caller branches on the sentinel, not on string matching:
if errors.Is(err, store.ErrNotFound) { http.NotFound(w, r); return }
```

- Wrap with `%w` when the caller may need the cause; add context every hop.
- `errors.As` for typed errors; never `strings.Contains(err.Error(), ...)`.

## Table-driven tests

```go
func TestSlugify(t *testing.T) {
	t.Parallel()
	tests := []struct {
		name, in, want string
	}{
		{"spaces", "Hello World", "hello-world"},
		{"unicode", "Blåbær", "blabaer"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := Slugify(tt.in); got != tt.want {
				t.Errorf("Slugify(%q) = %q, want %q", tt.in, got, tt.want)
			}
		})
	}
}
```

- `t.Parallel()` by default; `t.Cleanup` over manual teardown.
- Synchronize with channels/`context`, never `time.Sleep`.

## Tooling

```bash
go build ./...
go vet ./...
go test -race ./...
gofmt -l .            # or goimports
go mod tidy           # after dependency changes
go fix ./...          # apply automated modernizations (improved in 1.26)
```

A project-configured `golangci-lint` runs on top of, never instead of,
`go vet`.
