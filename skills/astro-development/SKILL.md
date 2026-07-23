---
name: astro-development
description: Build, review, and migrate Astro 6 sites — components, pages, layouts, content collections (Content Layer API), islands / partial hydration, SSR & SSG, integrations, and astro config. Also use when migrating an older Astro version or another framework to Astro 6, or when a code example uses removed Astro 5 patterns (entry.slug, entry.render(), Astro.glob(), legacy collections). Not for non-Astro frontends (standalone Vue/React/Nuxt apps) and not a general CSS/Tailwind skill — defer styling mechanics to a Tailwind skill.
---

# Astro 6 development

Senior Astro 6 framework specialist. Astro 6 is the current stable line
(6.0 released March 2026). Everything below targets Astro 6.x — several
Astro 5 patterns were **removed**, not just deprecated, so treat older
examples with suspicion.

## Core principles

**Zero JavaScript by default.** Astro ships no client JS unless you ask for
it. Reach for a `client:*` directive only when a component genuinely needs
interactivity. Prefer `client:visible` / `client:idle` over `client:load`.

**Islands, not SPAs.** Interactivity lives in isolated islands (Vue, React,
Svelte, Solid). The surrounding page stays static HTML. Don't hydrate a whole
layout to make one button work.

**TypeScript-first.** Type props, use typed env via `astro:env`, and run
`astro check` as part of every change.

**Content Layer API only.** All content collections use the Content Layer API
with an explicit `loader`. The legacy collections API is gone in v6.

**Performance and accessibility are design requirements.** Stable layout,
fast loads, and WCAG 2.2 AA are part of "done", not follow-ups.

## Anti-patterns — never produce these

- Legacy content collections (`type: 'content'` / `type: 'data'`, or config at
  `src/content/config.ts`). Removed in v6.
- A `slug` field in a collection schema — it throws
  `ContentSchemaContainsSlugError`. The entry identifier is `entry.id`; the
  source filename is `entry.filePath`.
- `entry.render()` — use the `render(entry)` function from `astro:content`.
- `Astro.glob()` — removed. Use `import.meta.glob()` (no longer returns a
  Promise; pass `{ eager: true }` for synchronous access).
- `<ViewTransitions />` — removed. Use `<ClientRouter />`.
- Importing `z` from `astro:content` — import it from `astro/zod`.
- `@astrojs/tailwind` — deprecated. Use the `@tailwindcss/vite` plugin.
- Hydrating components that render no interactive behavior.
- Running on Node < 22.12.0.

## Workflow

1. Confirm the Astro version and adapter (SSR vs static) before writing code.
2. For a new project, agree on the `src/` structure and package manager up
   front; don't assume one.
3. **Before writing or editing any content collection**, read
   `references/astro-6.md` — it holds the current Content Layer config,
   schema, rendering, and the v6 migration checklist.
4. Build content and page structure before styling. Defer Tailwind/CSS
   mechanics to a dedicated Tailwind skill.
5. Keep client JS minimal — justify every `client:*` directive.
6. Verify types with `astro check`.
7. Build and preview (`astro build && astro preview`) before calling it done.
8. Confirm with the user before adding MDX — it is not a default dependency.

## Reference files

| File | Contents |
|---|---|
| `references/astro-6.md` | Content Layer API config, schema, loaders, rendering; full Astro 5 → 6 breaking-change checklist with the removed APIs and their replacements |

## Source note

This skill was migrated from a short project agent file. The heavy content in
`references/astro-6.md` is the verified Astro 6 API surface and migration
checklist (checked against the official upgrade guide), not invented detail.
