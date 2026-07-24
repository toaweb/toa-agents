---
name: design-styles
description: Catalogue of named web design styles with full, versioned definitions — brutalism / neo-brutalism, retro terminal / BBS / phosphor. Use whenever the user names a design style ("make it brutalist", "terminal look", "retro style") or asks which styles exist, so the style is designed to its documented definition instead of from memory. Each style is brand-neutral — project brand values are applied on top. For corporate / B2B / expressive minimalism use the modern-corporate-design skill instead; this catalogue covers the expressive directions.
---

# Design styles catalogue

This skill is a **router**. It holds no design rules itself — every style has
its own full definition in `references/`, and that definition is the single
source of truth for the style. Never design a named style from memory: style
definitions are versioned documents here precisely because a model's
recollection of "brutalism" or "Y2K" is vague and drifts.

## Workflow

1. Identify which style the user is asking for. If the request is ambiguous
   between styles ("retro" can mean several), name the candidates from the
   catalogue below and ask.
2. **Read the style's reference file in full** before producing any design,
   markup, CSS or art direction.
3. Apply the project's brand values (colors, fonts, logo) **on top of** the
   style. A style is method; a brand is identity. Look for the project's
   brand source (`brand.json`, token files, or a path the user names); if the
   work needs brand values and none exists, ask — never invent them.
4. Follow the style's own anti-pattern list before delivering, and defer
   implementation mechanics to the framework/Tailwind skills as usual.

## Catalogue

| Style | Reference | One-line definition |
|---|---|---|
| Brutalism / neo-brutalism | `references/brutalist.md` | Raw structure shown, not hidden: hard borders, unapologetic type, honest layout |
| Retro terminal / BBS | `references/retro-terminal.md` | Phosphor-era computing as a design language: monospace, scanline restraint, prompt idioms |
| Modern corporate / expressive minimalism | → use the `modern-corporate-design` skill | Large enough to carry its own scripts/assets; lives as its own skill |

Adding a style = adding one reference file + one row here. The reference must
be complete enough to design from without external lookups: definition,
principles, layout, type, color roles (neutral), components, anti-patterns.

## Reference files

| File | Contents |
|---|---|
| `references/brutalist.md` | Full brutalism / neo-brutalism definition: principles, layout, typography, color roles, components, motion, anti-patterns |
| `references/retro-terminal.md` | Full retro terminal / BBS definition: principles, layout, typography, color roles, components, effects budget, anti-patterns |
