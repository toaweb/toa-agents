# Brutalism / neo-brutalism — style definition

Version: 1.0. Brand-neutral: apply the project's own colors, fonts and marks
on top of these rules. Where this file says "accent", it means the project's
accent token, not a specific color.

## Definition

Web brutalism shows the structure instead of hiding it. It descends from
béton brut — material honesty — not from ugliness. Two registers:

- **Raw brutalism** — near-unstyled HTML energy: system fonts, default-blue
  links, visible document structure, minimal CSS. Best for personal sites,
  manifestos, archives.
- **Neo-brutalism** — the commercial evolution: thick borders, hard offset
  shadows, flat saturated color fields, oversized type, playful but rigid.
  Best for products, editorial, portfolios that want energy with usability.

Pick ONE register per project and state it before designing.

## Principles

1. **Honesty of structure.** The grid is visible or clearly inferable.
   Sections are separated by borders, not by whitespace fog.
2. **No simulated depth.** No gradients-as-lighting, no glassmorphism, no
   soft ambient shadows. Depth, where used (neo), is a hard offset shadow —
   solid color, no blur.
3. **Type does the heavy lifting.** Oversized headings, tight leading,
   unapologetic weight jumps. Hierarchy through size and weight, not through
   decoration.
4. **Function is legible.** Buttons look pressable, links look like links.
   Brutalism exaggerates affordances; it never hides them.
5. **Deliberate roughness, disciplined execution.** Misalignment, if any, is
   designed misalignment on a real grid. Accessibility (WCAG 2.2 AA) is
   non-negotiable — raw is not an excuse for illegible.

## Layout

- Hard-edged grid; cells divided by visible borders (2–4px solid).
- Asymmetry allowed but anchored: every "broken" element aligns to at least
  one real grid line.
- Density over airiness: brutalism tolerates — wants — more per screen than
  minimalism. Whitespace exists but is allocated in blocks, not gradients.
- Full-bleed color fields for section changes instead of soft transitions.

## Typography

- Roles, not families (bind to project fonts): **display** — heavy, condensed
  or mono, set large (clamp from ~2.5rem to ~6rem); **body** — highly
  readable, generous size (≥1rem, often 1.125rem); **data/label** — mono,
  uppercase tolerated for short labels only.
- Underlines on links, always. Hover states are blunt: inversion, background
  fill, or offset jump — not opacity fades.
- No letter-spacing tricks on body text; no justified text.

## Color roles (neutral)

- `canvas` — one flat page color (paper-white, near-black, or a bold field).
- `ink` — maximum-contrast text color against canvas.
- `accent` — ONE loud accent for interaction and emphasis. Neo-brutalism may
  add a second field color for section blocking; never more than two accents.
- `border` — usually pure ink; borders are structure, not decoration.
- All pairs meet WCAG 2.2 AA contrast; the loud accent still needs a
  compliant text pairing.

## Components

- **Buttons:** rectangular, 2–3px border, flat fill, hard offset shadow
  (e.g. `4px 4px 0 0` ink) in neo; active state moves the block onto its
  shadow. No rounded pills, no gradients.
- **Cards:** bordered boxes. Radius 0 (raw) or a small uniform radius ≤4px
  (neo, optional). Shadow rules as buttons.
- **Forms:** visible borders on every field, oversized labels above (never
  placeholder-as-label), blunt focus style (thick outline or fill change).
- **Tables:** embraced, fully ruled. Brutalism is one of the few styles where
  a ruled table is a feature.
- **Navigation:** flat list, visible, no hamburger on desktop. Mobile nav may
  collapse but stays high-contrast and bordered.

## Motion

Almost none. Instant state changes or ≤120ms steps. No easing theatrics, no
scroll-triggered reveals, no parallax. A cursor or marquee element is a
single deliberate signature, if used at all.

## Anti-patterns — never produce these

- Soft/blurred shadows, gradients-as-depth, glassmorphism.
- Rounded-everything (radius >4px anywhere in neo; any radius in raw).
- Pastel "brutalism-lite" with low contrast — contrast IS the style.
- Decorative misalignment that breaks reading order or tab order.
- Illegible type as an aesthetic; failing AA and calling it raw.
- Mixing registers: raw HTML energy on one section, polished neo cards on
  the next.
- More than two accent colors.
- Scroll-jacking or long animated transitions.

## Verify before delivering

Structure visible; one register throughout; borders consistent (one weight
system); ≤2 accents; AA contrast everywhere; links underlined; focus states
blunt and visible; zero soft shadows/gradients.
