---
name: tailwind-styling
description: Style UIs with Tailwind CSS v4 and design tokens — CSS-first config with @theme, three-tier token systems (primitive → semantic → role), data-attribute theming (mode × brand) instead of dark: variants, @custom-variant, mobile-first responsive utilities, container queries, and animations. Also use to migrate off tailwind.config.js or the deprecated @astrojs/tailwind / @nuxtjs/tailwind plugins. Owns styling mechanics and token wiring; defer brand values, component logic and page structure to a design-system or framework skill.
---

# Tailwind CSS v4 styling

Senior Tailwind CSS and UI specialist. Tailwind v4 is CSS-first: configuration
lives in CSS via `@theme`, not in `tailwind.config.js`. Integrate through
`@tailwindcss/vite` — never `@astrojs/tailwind` or `@nuxtjs/tailwind` (both
deprecated). Verify the installed Tailwind version per project.

## Core principles

**CSS-first configuration.** Tokens live in `@theme` blocks. Every `@theme`
variable becomes both a CSS custom property and a Tailwind utility. There is no
`tailwind.config.js` and no `content` array.

**Tokens, never raw values.** Markup references semantic / role tokens
(`bg-surface`, `text-primary`), never a raw hex or a magic number (`#123456`,
`27px`). No hardcoded values anywhere in markup.

**Three-tier token architecture.** primitive (raw palette, no meaning) →
semantic (what it means: surfaces, text, lines) → role/alias (what it's used
for). Markup binds to the role/semantic layer.

**Theme by data-attribute, not `dark:`.** Re-point role/semantic tokens under
`[data-mode="…"]` / `[data-theme="…"]` on `<html>`. Two axes (mode × brand)
combine orthogonally. Avoid scattering `dark:` variants through markup.

**Mobile-first, always.** Unprefixed utilities are the mobile base; `sm: md:
lg: xl:` expand upward. Never start from a desktop layout.

**Composition over `@apply`.** Extract repeated class patterns into components
rather than reaching for `@apply`.

## Anti-patterns — never produce these

- A `tailwind.config.js` for token config in a v4 project — use `@theme`.
- `@astrojs/tailwind` or `@nuxtjs/tailwind` — use `@tailwindcss/vite`.
- Raw hex, rgb, or magic-number values in markup instead of tokens.
- `dark:` / `light:` variants scattered through markup instead of data-attribute
  token re-pointing.
- Desktop-first classes with `md:`/`lg:` walking the layout back down.
- `@apply` used to paper over what should be a component.
- Plain `@theme` for a token that must change at runtime (use `@theme inline`).
- Touch targets under 44px, or form inputs below `text-base` (iOS zoom).

## Workflow

1. Confirm the project uses Tailwind v4 and where its theme/token files live.
2. **Before any token, theme, or dark-mode work**, read
   `references/theming.md` — the three-tier model, `@theme` vs `@theme inline`,
   data-attribute theming, `@custom-variant`, and the theme folder structure.
   - **Before writing any `@theme` block or token config, fetch
     https://tailwindcss.com/docs/theme and confirm the v4 CSS-first syntax. Do
     not emit a `tailwind.config.js` token config from memory** — that is the v3
     pattern.
   - **Before using `@theme inline`, `@custom-variant`, or any `@`-directive,
     fetch https://tailwindcss.com/docs/functions-and-directives and verify the
     directive against the current docs.**
3. **Before writing responsive markup**, read `references/mobile-first.md` —
   mobile-first rules, touch targets, form-input sizing, and container queries.
4. Check the existing `theme/tokens/` before inventing any new value.
5. Test the mobile viewport first, then desktop.
6. Before finishing, grep the changed files for stray `<style>` blocks, inline
   `style=` attributes, and arbitrary-value color classes — none should slip in.

## Reference files

| File | Contents |
|---|---|
| `references/theming.md` | v4 CSS-first config, three-tier tokens, `@theme` vs `@theme inline` (precise semantics), data-attribute theming, `@custom-variant`, theme folder structure |
| `references/mobile-first.md` | Mobile-first rules, 44px touch targets, `text-base` inputs, `touch-action`, container queries |

## Source note

Migrated from a project agent file. The Tailwind v4 directives were checked
against the official docs and issue tracker; brand-specific example values were
replaced with neutral placeholders. Apply the project's own brand tokens on top.
