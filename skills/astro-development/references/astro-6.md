# Astro 6 — Content Layer API & migration reference

Verified against the official Astro v6 upgrade guide and content collection
references (docs.astro.build). Astro 6.0 stable: March 2026.

## Runtime requirements

- **Node 22.12.0 or newer.** Node 18 and Node 20 support was dropped.
- **Zod 4.** Astro 6 upgrades from Zod 3. Some string-format helpers moved to
  top-level namespace methods — e.g. `z.string().email()` → `z.email()`.
  `z.coerce.date()`, `z.string()`, `z.array()`, `z.boolean().default()` still
  work. Error-message config changed from `message` to `error`.

## Content Layer API (required in v6)

Legacy content collections are **removed**. There is no `type: 'content'` /
`type: 'data'`; every collection declares an explicit `loader`. Config lives at
`src/content.config.ts` (the old `src/content/config.ts` is no longer read).

```typescript
// src/content.config.ts
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const blog = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    categories: z.array(z.string()).default([]),
    feature_image: z.string().optional(),
    draft: z.boolean().default(false),
    // Do NOT add `slug` — it throws ContentSchemaContainsSlugError.
  }),
});

export const collections = { blog };
```

### Loaders
- `glob({ pattern, base })` and `file()` are the built-in loaders, imported
  from `astro/loaders`.
- Built-in `glob()` IDs are slugified from the file path.
- Third-party / custom loaders are supported via the Content Loader API.

### Reading and rendering

```typescript
import { getCollection, getEntry, render } from 'astro:content';

const posts = await getCollection('blog');
const post = await getEntry('blog', 'my-post');

// In a component:
const { Content } = await render(post);   // NOT post.render()
```

### Entry shape
- `entry.id` — the collection identifier (a slug from the file path).
  There is no `entry.slug` anymore.
- `entry.filePath` — the source file path, if you need the original filename.
- `entry.data` — the parsed, schema-validated frontmatter.

## Astro 5 → 6 breaking-change checklist

| Removed / changed | Replacement |
|---|---|
| Legacy collections (`type: 'content'`/`'data'`) | Content Layer API with `loader` |
| `src/content/config.ts` | `src/content.config.ts` |
| `slug` field in schema | none — use `entry.id`; original path via `entry.filePath` |
| `entry.slug` | `entry.id` |
| `entry.render()` | `render(entry)` from `astro:content` |
| `z` from `astro:content` | `z` from `astro/zod` |
| `Astro.glob()` | `import.meta.glob()` (sync, `{ eager: true }`) |
| `<ViewTransitions />` | `<ClientRouter />` |
| `emitESMImage()` | removed |
| Zod 3 | Zod 4 |
| Node 18 / 20 | Node 22.12.0+ |
| `@astrojs/tailwind` (deprecated) | `@tailwindcss/vite` plugin |

## Astro 6 surface worth knowing

- **Server islands** — defer server-rendered fragments per component.
- **`astro:env`** — typed, validated environment variables (client vs server).
- **View transitions** via `<ClientRouter />`.
- Built-in APIs for CSP, fonts, and live content collections (new in v6).

## Migration order (from Astro 5)

1. Bump Node to 22.12.0+.
2. Upgrade Zod to 4 and adjust any deprecated schema helpers.
3. Move `src/content/config.ts` → `src/content.config.ts`; convert every
   collection to a `loader`.
4. Remove any `slug` schema fields; replace `entry.slug` → `entry.id` and
   `entry.render()` → `render(entry)`.
5. Replace `Astro.glob()` with `import.meta.glob()`.
6. Rename `<ViewTransitions />` → `<ClientRouter />`.
7. Run `astro check`, then `astro build`.
