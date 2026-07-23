---
name: nuxt-development
description: Build and review Nuxt 4 + Vue 3 frontends — components, pages, layouts, composables, Pinia stores, plugins, nuxt.config, SSR/SSG, routing, SSR-safe state management and data fetching. Also use to modernize legacy patterns (Options API, code outside app/, @nuxtjs/tailwind, direct process.env, module-scoped refs that leak across SSR requests). Not for non-Nuxt frontends (Astro, a plain Vue SPA without Nuxt) and not a general Tailwind design skill — defer token and design decisions to a Tailwind skill.
---

# Nuxt 4 + Vue 3 development

Senior Nuxt 4 and Vue 3 specialist. Nuxt 4 is the current line (Nuxt 3 reached
end of life in July 2026). Application code lives in `app/`, and several Vue 2 /
Options-API / Nuxt 3-root habits are wrong here. Verify exact versions per
project.

## Core principles

**`app/` is where code lives.** Pages, layouts, components, composables, stores,
plugins and middleware live under `app/`, not the project root.

**Composition API only.** Every component is `<script setup lang="ts">`. No
Options API.

**Auto-imports are the default.** Never manually import `ref`, `computed`,
`useState`, `useFetch`, composables, or components. Rely on Nuxt's auto-import.

**Runtime config, not `process.env`.** Read configuration through
`useRuntimeConfig()`; never touch `process.env` directly in app code.

**SSR-safe state.** Use `useState` for simple shared values and Pinia for
complex domain logic. Never a module-scoped `ref` — it leaks state across
requests in SSR.

**One API layer.** All server calls go through `app/lib/api/`. Components and
stores call that layer, never raw `$fetch` inline.

**Performance and accessibility are requirements**, not later fixes.

## Anti-patterns — never produce these

- Options API, or `<script>` without `setup lang="ts"`.
- Application code at the project root instead of `app/`.
- A module-scoped `ref`/`reactive` for shared state (SSR cross-request leak).
- Reading `process.env` directly instead of `useRuntimeConfig()`.
- Manually importing `ref`, `computed`, `useState`, composables or components.
- `@nuxtjs/tailwind` — deprecated. Use the `@tailwindcss/vite` plugin.
- Raw `$fetch` calls scattered through components instead of `app/lib/api/`.
- Monolithic stores — use one Pinia store per domain.
- `useFetch`/`useAsyncData` for imperative event-handler actions (use `$fetch`),
  or `$fetch` for SSR-aware initial loads (use `useFetch`/`useAsyncData`).

## Workflow

1. Confirm Nuxt (4.x), Vue (3.5+) and Pinia (current major) versions before
   writing code.
2. Check `app/components/` for existing patterns before adding new ones.
3. **Before scaffolding config, stores, data fetching or the API layer**, read
   `references/patterns.md` — it holds the stack baseline, project structure,
   `nuxt.config.ts` baseline, the state/data-fetching decision rules, and the
   API-layer pattern.
4. Keep styling decisions in a dedicated Tailwind skill; this skill owns
   structure, state and data flow.
5. One Pinia store per domain; no monolithic stores.
6. Run the project's typecheck (e.g. `nuxi typecheck`) after changes.

## Reference files

| File | Contents |
|---|---|
| `references/patterns.md` | Stack baseline & versions, `app/` project structure, `nuxt.config.ts` baseline, state vs data-fetching rules, the `app/lib/api/` layer, typecheck |

## Source note

Migrated from a short project agent file. Stack versions in
`references/patterns.md` were checked against the npm registry and Nuxt release
notes at migration time — re-verify per project.
