---
name: hugo-development
description: Build and review Hugo Extended static sites on the new template system (Hugo 0.146+) — baseof.html at the layouts root, underscored _partials/_shortcodes/_markup, content organization with page bundles, taxonomies, front matter, Hugo Pipes asset processing, and Tailwind CSS v4 via css.TailwindCSS. Also use to migrate a site off the old layouts/_default/ layout or off the removed Tailwind standalone binary. Not for JS-framework sites (Astro, Nuxt) and not a general design/Tailwind token skill — defer token and design decisions to a Tailwind skill.
---

# Hugo Extended development

Senior Hugo Extended static-site specialist. Two Hugo shifts dominate current
work and break most older examples:

- **The new template system (Hugo v0.146.0).** Templates moved to the
  `layouts/` root; `partials`/`shortcodes`/`markup` gained a leading
  underscore; `layouts/_default/` is gone.
- **Tailwind CSS v4 via `css.TailwindCSS`.** As of Hugo v0.161.0 the Tailwind
  standalone binary is unsupported; the CLI is installed via npm and Hugo needs
  specific `buildStats` config to feed classes to Tailwind.

Use Hugo **Extended** (required for the Tailwind pipeline). Verify the exact
version per project; use a current release.

## Core principles

**Hugo Pipes for every asset.** All CSS runs through `css.TailwindCSS`; images
go through Hugo Pipes (`resources.Get`, `Resize`, `Process`). Never link a raw
`<img>` straight from `static/`.

**New template system, not the old one.** baseof.html and the page templates
live at the `layouts/` root; partials, shortcodes and render hooks live in the
underscored directories. Do not create `layouts/_default/`.

**Page bundles for content.** Each content item is a bundle — `index.md` plus
its own images. Never scatter post images into a global folder.

**Own theme in `assets/theme/`, not the Hugo Themes system.** For first-party
sites, keep styles in the project's assets, not an installed theme.

**Performance and accessibility are requirements**, not later fixes.

## Anti-patterns — never produce these

- `layouts/_default/` — removed in the new template system.
- Bare `partials/` or `shortcodes/` — they must be `_partials/` and
  `_shortcodes/` (and render hooks in `_markup/`).
- A raw `<img>` pointing at `static/` — process images through Hugo Pipes.
- Storing a post's images in a global folder instead of its page bundle.
- Installing the Tailwind standalone binary (unsupported since v0.161.0).
- Omitting the `buildStats` / `hugo_stats.json` config — Tailwind then sees no
  classes and strips everything.
- Using `templates` shortcodes for layout, or partials for content functions
  (shortcodes = content functions, partials = layout).

## Workflow

1. Confirm Hugo Extended and its version, and whether the project already uses
   the new template system.
2. **Before touching layouts or the directory structure**, read
   `references/structure.md` — the new template-system tree, page bundles, and
   the Hugo Pipes conventions.
   - **Before creating any layout directory, fetch
     https://gohugo.io/templates/new-templatesystem-overview/ and confirm the
     v0.146+ template system (underscored `_partials`/`_shortcodes`, no
     `layouts/_default/`). Do not use the old layout tree from memory.**
3. **Before any CSS / Tailwind work**, read `references/tailwind-v4.md` — the
   full npm + `hugo.toml` + `css.TailwindCSS` + `templates.Defer` pipeline.
   Defer token/design decisions to a dedicated Tailwind skill.
   - **Before wiring the CSS pipeline, fetch
     https://gohugo.io/functions/css/tailwindcss/ and verify the current
     `css.TailwindCSS` usage and the required `buildStats` config** rather than
     assuming the old standalone-binary flow.
4. Put content functions in shortcodes, layout in partials.
5. Run `hugo server` for development; build with `hugo --minify`.

## Reference files

| File | Contents |
|---|---|
| `references/structure.md` | New template system (v0.146+) directory tree, template lookup, page bundles, Hugo Pipes image handling |
| `references/tailwind-v4.md` | Tailwind v4 pipeline: npm install, required `hugo.toml` (buildStats, cachebusters, hugo_stats.json mount), `main.css` `@source`, the `css.html` partial, `templates.Defer`, version notes |

## Source note

Migrated from a short project agent file. The `hugo.toml` Tailwind config in
`references/tailwind-v4.md` fills a gap in the original (which showed only the
CSS `@source` line) and was checked against the official `css.TailwindCSS`
documentation. Verify the exact config against current Hugo docs per project.
