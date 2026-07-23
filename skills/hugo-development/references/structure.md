# Hugo — new template system & structure reference

Verified against the official "New template system in Hugo v0.146.0" overview.

## What changed in v0.146.0

Hugo re-implemented Go template handling. Structural changes:

- Templates live at the **`layouts/` root**, not in `layouts/_default/`.
- `partials` → `_partials`, `shortcodes` → `_shortcodes`, `markup` → `_markup`
  (leading underscore). `_partials`, `_shortcodes` and `_markup` can appear at
  any level of the tree.
- `hugo new theme` scaffolds: `baseof.html`, `home.html`, `page.html`,
  `section.html`, `taxonomy.html`, `term.html`.
- The old `_internal/` templates concept is gone — load former internal
  templates as normal partials, e.g. `{{ partial "twitter_cards.html" . }}`.

## Canonical project tree

```
assets/
├── css/main.css              single CSS entry point (@import "tailwindcss"; @source ...)
└── theme/{tokens,styles}/    @theme tokens; globals, prose, utilities
layouts/
├── baseof.html               HTML shell; calls the css partial via templates.Defer
├── home.html                 front page
├── page.html                 single pages
├── section.html              section / list pages
├── taxonomy.html             taxonomy list (optional)
├── term.html                 term list (optional)
├── _partials/
│   ├── css.html              css.TailwindCSS processing
│   └── theme/                reusable UI partials
├── _shortcodes/              content functions only
└── _markup/                  render hooks (render-link, render-image, render-codeblock)
content/                      page bundles (index.md + its images)
data/                         navigation.yaml, site.yaml, etc.
static/                       unprocessed files only (favicon, OG images)
```

- **Partials** = layout building blocks (`layouts/_partials/`).
- **Shortcodes** = content functions callable from Markdown (`layouts/_shortcodes/`).
- **Render hooks** = Markdown output control (`layouts/_markup/`:
  `render-link.html`, `render-image.html`, `render-codeblock.html`).

## Page bundles (always)

```
content/blog/my-post/
├── index.md
├── cover.webp
└── screenshot.webp
```

Keep each post's images inside its bundle. Never store post images in a single
global folder.

## Hugo Pipes for images

Process images through Hugo Pipes rather than linking raw files from `static/`:

```go-html-template
{{ with .Resources.GetMatch "cover.*" }}
  {{ $img := .Process "resize 1200x webp q80" }}
  <img src="{{ $img.RelPermalink }}" width="{{ $img.Width }}" height="{{ $img.Height }}" alt="...">
{{ end }}
```

`static/` is only for files that must ship byte-for-byte (favicon, robots.txt,
pre-made OG images).
