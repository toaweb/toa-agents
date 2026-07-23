# Tailwind v4 — tokens & theming reference

Verified against the official Tailwind CSS v4 docs and issue tracker. v4 is
CSS-first (released Jan 2025): config lives in CSS, not `tailwind.config.js`.

## CSS-first config

```css
@import "tailwindcss";

@theme {
  /* Example placeholder values — replace with the project's brand tokens. */
  --color-primary:   #7c3aed;
  --color-text:      #1a1a1a;
  --font-sans:       ui-sans-serif, system-ui, sans-serif;
  --spacing-section: 4rem;
}
```

- `@import "tailwindcss"` is the entry point.
- Every `@theme` variable becomes **both** a CSS custom property **and** a
  Tailwind utility (e.g. `--color-primary` → `bg-primary`, `text-primary`).
- No `tailwind.config.js`, no `content` array.

## Three-tier token architecture

1. **Primitive** — raw palette / scale, no meaning (`--red-500`, `--space-4`).
2. **Semantic** — what it means (`--color-surface`, `--color-text`,
   `--color-border`).
3. **Role / alias** — what it's used for at a specific spot.

Markup binds to the **semantic / role** layer, never to a primitive or a raw
value. This is what makes re-theming a token-level change, not a markup edit.

A single brand with one light/dark pair can use a flatter one-tier `@theme` plus
a `[data-theme]` override. Go three-tier when scaling across multiple
themes/brands/apps.

## `@theme` vs `@theme inline` — the key distinction

The naming is counterintuitive; what matters is the emitted CSS:

- **Plain `@theme`** — utilities bake in the token's **literal value** at build
  time. `.bg-primary` emits `background-color: #7c3aed;`. Smaller output; best
  for static, single-brand setups where the value never changes at runtime.
- **`@theme inline`** — utilities emit a **`var()` reference** instead of the
  literal. `.bg-primary` emits `background-color: var(--color-primary);`. Because
  the utility points at the variable, re-pointing that variable at runtime (e.g.
  a `[data-theme]` cascade change) updates the utility **live**.

**Rule:** use `@theme inline` whenever a token references another variable or
must change at runtime (theme/brand switching, external CSS integration). Use
plain `@theme` only for static one-brand setups.

## Data-attribute theming (not `dark:`)

Re-point semantic/role tokens under a data attribute on `<html>`, so the whole
UI re-themes without `dark:` variants in markup:

```css
:root { --color-surface: white;  --color-text: #1a1a1a; }
[data-mode="dark"] { --color-surface: #111; --color-text: #f5f5f5; }
```

Two orthogonal axes (mode × brand) combine cleanly:
`[data-mode="dark"][data-brand="…"]`.

## `@custom-variant` — when you genuinely need a variant

If you do need a real variant selector (e.g. to support a `dark:` utility driven
by a data attribute):

```css
@custom-variant dark (&:where([data-mode="dark"] *));
```

Then `dark:bg-surface` resolves under `[data-mode="dark"]`. Prefer token
re-pointing first; reach for `@custom-variant` only when a variant is actually
required.

## Theme folder structure

```
theme/
├── tokens/
│   ├── colors.css      @theme { --color-* }
│   ├── typography.css  @theme { --font-* }
│   ├── spacing.css     @theme { --spacing-* }
│   └── animations.css
└── styles/
    ├── main.css        single global entry (@import "tailwindcss" + all tokens)
    ├── prose.css       markdown / long-form typography
    └── utilities.css   project-specific utilities
```

## Design principles

- No hardcoded values — always `@theme` tokens or the Tailwind scale.
- No magic numbers (`27px`, `#123456`).
- Repeated class patterns → extract to a component, not `@apply`.
