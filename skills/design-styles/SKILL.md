---
name: design-styles
description: Catalogue of 14 named web design styles with full, versioned, brand-neutral definitions — brutalist, editorial, swiss / international typographic, premium minimalism / quiet luxury, warm minimalism, typography-driven, data-driven SaaS, industrial / technical, immersive storytelling, organic / human-centered, retro / vintage, Y2K / digital nostalgia, retro terminal / BBS, and modern corporate / expressive minimalism. Use whenever the user names a design style or aesthetic direction ("make it brutalist", "quiet luxury feel", "Y2K look", "terminal style") or asks which styles exist, so the style is designed to its documented definition instead of from memory. Each style is brand-neutral — project brand values are applied on top. For admin panels, dashboards and product UX patterns use the product-ux skill instead.
---

# Design styles catalogue

This skill is a **router**. It holds no design rules itself — every style has
a full normative definition (`<style>.md`) and, for most styles, a companion
imagery/asset guide (`<style>-assets.md`) in `references/`. Those documents
are the single source of truth for the style. Never design a named style
from memory: definitions are versioned here precisely because a model's
recollection of a style is vague and drifts.

**Do not** use legacy `toa-rules/design/styles*` files as the style catalogue.
Those are historical trend notes. **This skill is canonical.**

## Workflow

1. Identify which style the user is asking for. If the request is ambiguous
   between styles ("retro" spans retro-vintage, Y2K, and retro-terminal;
   "minimal" spans premium, warm, and swiss), name the candidates from the
   catalogue and ask.
2. **Read the style's `references/<style>.md` in full** before producing any
   design, markup, CSS or art direction. Read `<style>-assets.md` as well
   whenever the task involves imagery, illustration, photography or
   graphic assets.
3. Apply the project's brand values (colors, fonts, logo, voice) **on top
   of** the style. A style is method; a brand is identity. Prefer **toa-mcp**
   tools `get_brand` / `get_token_scale` when the brand MCP is connected;
   otherwise `brand.json`, token files, or a path the user names. If brand
   values are required and none exist, ask — never invent them.
4. Respect each definition's normative language (must/should/may) and its
   accessibility and performance requirements — they are part of the style,
   not optional extras.
5. Defer implementation mechanics to the framework/Tailwind skills as usual.

## Catalogue

| Style | Definition | Asset guide |
|---|---|---|
| Brutalist / neo-brutalist | `references/brutalist.md` | `references/brutalist-assets.md` |
| Editorial | `references/editorial.md` | `references/editorial-assets.md` |
| Swiss / International Typographic | `references/swiss-international.md` | `references/swiss-international-assets.md` |
| Premium minimalism / quiet luxury | `references/premium-minimalism.md` | `references/premium-minimalism-assets.md` |
| Warm minimalism | `references/warm-minimalism.md` | `references/warm-minimalism-assets.md` |
| Typography-driven | `references/typography-driven.md` | `references/typography-driven-assets.md` |
| Data-driven SaaS | `references/data-driven-saas.md` | `references/data-driven-saas-assets.md` |
| Industrial / technical | `references/industrial-technical.md` | `references/industrial-technical-assets.md` |
| Immersive storytelling | `references/immersive-storytelling.md` | `references/immersive-storytelling-assets.md` |
| Organic / human-centered | `references/organic-human-centered.md` | `references/organic-human-centered-assets.md` |
| Retro / vintage | `references/retro-vintage.md` | `references/retro-vintage-assets.md` |
| Y2K / digital nostalgia | `references/y2k-digital-nostalgia.md` | `references/y2k-digital-nostalgia-assets.md` |
| Retro terminal / BBS (phosphor) | `references/retro-terminal.md` | — |
| Modern corporate / expressive minimalism | → use the `modern-corporate-design` skill | (bundled there) |

Modern corporate lives as its own full skill because it carries scripts and
token assets (compliance checker, tokens.css); this catalogue defers to it.

## Not in this catalogue

This catalogue covers **public** surfaces — websites, marketing, editorial.
Interfaces behind a login belong to the `product-ux` skill, and so do their
visual treatments: flat/elevated, glassmorphism, neumorphism and
skeuomorphic controls are documented there with the safety constraints a
product surface requires. Do not treat them as styles from this catalogue,
and do not apply a catalogue style to a product surface as a substitute for
the product-UX rules.

Adding a style = adding its definition (and asset guide) + one row here.
A definition must be complete enough to design from without external
lookups: purpose, principles, layout, typography, color roles (neutral),
components, interaction, accessibility, anti-patterns.
