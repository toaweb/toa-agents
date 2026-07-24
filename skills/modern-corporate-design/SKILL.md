---
name: modern-corporate-design
description: Design system for corporate, B2B, consulting, professional services, industrial, logistics, maritime, SaaS, finance, legal and institutional websites. Combines minimal discipline with one deliberate identity signal so the result does not read as a template. Use when building or reviewing sites where credibility, clarity and conversion matter more than visual expression, or when the user asks for a corporate, professional, B2B, institutional or "expressive minimalism" style. Not for consumer products, gaming, entertainment, creative portfolios or brutalist and retro directions.
---

# Modern Corporate / Expressive Minimalism

Brand-neutral design system. It defines the style and its rules — never a
specific company's colors, fonts, logo, tone of voice or content.

## Core formula

```
Clear content architecture
+ disciplined layout
+ restrained component system
+ one strong identity idea
= expressive corporate minimalism
```

Minimalism is not the removal of useful information. It is the removal of
unnecessary competition.

## Strategic principles

**Clarity before decoration.** The page explains the business before it tries
to impress. Every page answers: Where am I? What is offered? Is this relevant
to me? Why should I trust it? What happens next?

**Proof before claims.** Prefer client outcomes, numbers with context,
certifications, case studies, named capabilities, documented processes.
Never write "world-class", "cutting-edge", "market-leading", "innovative
solutions", "trusted partner" without evidence on the page. Never invent
statistics.

**Restraint with identity.** Choose ONE dominant identity mechanism plus a
small supporting set. Typography, color, imagery, motion, texture, 3D and
decorative geometry must not all compete.

**Systems over one-off compositions.** Pages feel individually composed but
are built from reusable rules: grid, spacing, type scale, color roles, image
ratios, component anatomy, border rules, interaction states.

**Human confidence.** Direct language, authentic photography, visible
expertise, editorial judgment, specific details. Not machine-generated,
not emotionally empty.

**Performance is part of the design.** Fast loading, stable layout and
accessible interaction are visual-quality requirements, not later fixes.

## Style spectrum — pick one before designing

| Direction | Characteristics |
|---|---|
| Conservative | Symmetrical, neutral, familiar, restrained type, strong proof |
| Editorial | Large type, asymmetric grids, strong photography, narrative |
| Technical | Data, diagrams, specifications, modular panels, precise labels |
| Human | Warm imagery, softer colors, approachable type, people-led |
| Premium | Large spacing, refined type, limited palette, art-directed imagery |
| Bold | Strong color fields, oversized text, sharp composition |

## Anti-patterns — never produce these

- Centered hero + gradient orb + three floating cards
- Generic blue-purple gradients as a default
- Rounded cards for every section
- Meaningless abstract 3D shapes filling empty space
- The same icon inside a colored circle for every feature
- Invented statistics
- Generic stock photos presented as proof
- Identical layouts applied to unrelated content
- Weak messaging hidden behind oversized typography
- Artificial asymmetry that breaks alignment
- "AI-style" glowing grids unless the context genuinely requires it
- Every section at full viewport height
- Decorative dashboards on non-software businesses

## Workflow

1. Identify company type and primary audience.
2. State the page goal.
3. Select one direction from the style spectrum.
4. Build the content hierarchy before any visual styling.
5. Identify the primary evidence the page will rest on.
6. Choose one dominant identity mechanism.
7. Read `references/design-system.md` for grid, spacing, type, color,
   borders and component anatomy before writing markup or CSS.
8. Read `references/visual-assets.md` before specifying photography,
   illustration, icons, charts, diagrams or maps.
9. Design responsive behavior explicitly — do not leave it implied.
10. Preserve WCAG 2.2 AA throughout. **When a contrast, target-size or
    non-text-contrast requirement is in doubt, check it against
    https://www.w3.org/TR/WCAG22/ — it is normative; do not rely on memory.**
11. Verify against the anti-patterns above before delivering.

## Brand values

This skill contains no brand values. `assets/tokens.css` holds the token
architecture with placeholder values only.

Look for a brand token file in the project — commonly `brand.json`,
`brand/tokens.css` or a path the user names. Use those values in place of
the placeholders. If none exists and the work needs brand values, ask.
Never invent brand rules, colors, fonts or logos.

## Constraints

Do not:

- use arbitrary trendy decoration
- create generic template sections without purpose
- substitute visual polish for content strategy
- ship inaccessible low-contrast minimalism
- mix unrelated visual languages
- embed important content in raster graphics
- make assumptions about regulated claims
- build decorative UI that implies functionality that does not exist

## Reference files

| File | Contents |
|---|---|
| `references/design-system.md` | Full system: IA, grid, spacing, typography, color, borders, components, motion, responsive, accessibility, performance, tokens, sector adaptations, production checklist |
| `references/visual-assets.md` | Photography, stock policy, image treatment and composition, illustration, icons, borders, separators, connectors, motifs, patterns, charts, diagrams, maps, logos, badges, screenshots, video, asset delivery, file formats |
| `assets/tokens.css` | Token architecture, placeholder values |
| `scripts/check_compliance.py` | Mechanical check against the anti-patterns |
