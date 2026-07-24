# Hugo + Tailwind CSS v4 pipeline reference

Verified against the official Hugo `css.TailwindCSS` and `templates.Defer`
documentation.

## Versions

- Requires **Hugo Extended**.
- Use `css.TailwindCSS` with **Tailwind CSS v4.0+**.
- **As of Hugo v0.161.0 the Tailwind standalone binary is no longer supported** —
  install the CLI via npm. (A project may set a higher baseline, e.g. a recent
  0.16x release; verify per project.)

## 1. npm install

```bash
npm install --save-dev tailwindcss @tailwindcss/cli @tailwindcss/typography
```

## 2. hugo.toml — required config

Hugo must write `hugo_stats.json` (the class list Tailwind scans) and make it
available to the asset pipeline. Without this, Tailwind sees no classes and
purges everything.

```toml
[build]
  [build.buildStats]
    enable = true
  [[build.cachebusters]]
    source = 'assets/notwatching/hugo_stats\.json'
    target = 'css'
  [[build.cachebusters]]
    source = '(postcss|tailwind)\.config\.js'
    target = 'css'

[[module.mounts]]
  source = 'assets'
  target = 'assets'

[[module.mounts]]
  disableWatch = true
  source = 'hugo_stats.json'
  target = 'assets/notwatching/hugo_stats.json'
```

Note: if `hugo_stats.json` is in `.gitignore`, Tailwind will ignore it — the
`@source` directive below is what re-includes it explicitly.

## 3. assets/css/main.css — entry point

```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";  /* only if installed in step 1 — drop both together */
@source "hugo_stats.json";
```

The `@source` directive points Tailwind at Hugo's generated class list. A
plugin that is installed but never loaded with `@plugin` does nothing — keep
the npm dependency and the `@plugin` line in sync.

## 4. layouts/_partials/css.html — processing partial

```go-html-template
{{ with resources.Get "css/main.css" }}
  {{ $opts := dict "minify" (not hugo.IsDevelopment) }}
  {{ with . | css.TailwindCSS $opts }}
    <link rel="stylesheet" href="{{ .RelPermalink }}">
  {{ end }}
{{ end }}
```

## 5. baseof.html — call it via templates.Defer

`css.TailwindCSS` depends on `hugo_stats.json`, which is only complete after all
pages render. Defer the CSS partial so it runs last:

```go-html-template
{{ with (templates.Defer (dict "key" "global")) }}
  {{ partial "css.html" . }}
{{ end }}
```

`templates.Defer` "defer[s] the execution of a template until after all sites
and output formats have been rendered" — exactly what Tailwind's class scanning
needs.

## Build

```bash
hugo server            # development
hugo --minify          # production build
```
