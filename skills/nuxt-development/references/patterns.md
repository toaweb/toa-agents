# Nuxt 4 + Vue 3 — patterns & stack reference

Stack baselines verified at migration time (July 2026) against the npm registry
and Nuxt release notes. Re-verify per project.

## Stack baseline

| Component | Notes |
|---|---|
| Nuxt | 4.x (4.5 at migration time). App code lives in `app/`. |
| Vue | 3.5+ (3.5.x). Composition API, `<script setup lang="ts">`. |
| State | Pinia — core is now v4 (peer `vue ^3.5.11`), installed via the `@pinia/nuxt` module. Note the module version (1.x) is decoupled from the Pinia core version. |
| Styling | Tailwind CSS v4 via `@tailwindcss/vite` (NOT `@nuxtjs/tailwind`, deprecated). |
| Common modules | `@nuxt/image`, `@nuxt/icon`, `nuxt-seo`, `@nuxt/eslint`. |
| TypeScript | First-class; run the project's typecheck. |

Don't hardcode a pinned Nuxt/Vue/Pinia version into project code — confirm the
installed versions.

## Project structure (app/)

```
app/
├── pages/                    routes
├── layouts/                  layouts
├── components/
│   ├── ui/                   generic reusable components
│   └── layout/               Container / Section / Stack / Grid
├── composables/              auto-imported composables
├── stores/                   Pinia, one file per domain
├── lib/api/                  ALL server calls live here
└── ...
theme/
└── styles/main.css           single CSS entry point
theme/tokens/                 @theme tokens
nuxt.config.ts
```

- `components/ui` — generic reusable components.
- `components/layout` — layout primitives (Container, Section, Stack, Grid).
- `stores` — one Pinia store per domain; no monolithic store.
- `lib/api` — the only place that calls the server.

## nuxt.config.ts baseline

```typescript
import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',   // set to a current date per project
  css: ['~/theme/styles/main.css'],
  vite: { plugins: [tailwindcss()] },
  modules: ['@pinia/nuxt', '@nuxt/image', 'nuxt-seo', '@nuxt/icon', '@nuxt/eslint'],
})
```

`compatibilityDate` opts into Nitro/Nuxt behavior as of that date — set it to a
recent date when starting a project, don't copy an old one blindly.

## State management

- **Simple shared values:** `useState('key', () => initial)` — SSR-safe.
- **Complex domain logic:** Pinia, one store per domain.
- **Never** a module-scoped `ref`/`reactive` for shared state — it is created
  once per server process and leaks data across requests in SSR.

## Data fetching

- **SSR-aware page/component loads:** `useFetch` / `useAsyncData`. These run on
  server and client, dedupe, and hydrate correctly.
- **Client-side actions & event handlers:** `$fetch`. Don't wrap an imperative
  button-click call in `useFetch`.

## API layer

All server calls go through `app/lib/api/` — never a raw `$fetch` inline in a
component or store.

```typescript
// app/lib/api/posts.ts
export const postsApi = {
  list: () => $fetch('/api/v1/posts'),
  get: (id: string) => $fetch(`/api/v1/posts/${id}`),
}
```

Components/stores import `postsApi` and call it; they never build request URLs
themselves.
