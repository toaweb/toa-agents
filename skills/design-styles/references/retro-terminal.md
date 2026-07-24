# Retro terminal / BBS — style definition

Version: 1.0. Brand-neutral: bind the roles below to the project's own
tokens. Where this file says "phosphor", it means the project's primary
accent, whatever hue that is.

## Definition

Phosphor-era computing — hardware terminals, BBSes, early consoles — treated
as a design language rather than a costume. The interface presents itself as
a machine session: monospace type, prompt idioms, status labels, a dark
canvas with one or two glowing-adjacent accents. The craft lies in
restraint: evoking the era through structure and language, not through
piling on CRT effects.

## Principles

1. **The session metaphor carries the identity.** Prompts (`$`, `>`),
   status codes, bracketed labels (`[OK]`, `[LOADING]`), path-like
   navigation. Use the metaphor consistently or not at all.
2. **Monospace is structural, not decorative.** Alignment, columns and
   ASCII/box-drawing structure exploit the fixed grid. If nothing aligns,
   monospace is wasted.
3. **Dark canvas, luminous ink.** A near-black canvas with a bright primary
   text color. Light-mode terminal (paper teletype) is a valid variant —
   pick one.
4. **Effects have a budget.** Scanlines, glow, flicker, typing animations:
   choose at most ONE ambient effect and keep it subtle. The style dies by
   accumulation.
5. **Modern usability under the retro skin.** Real focus states, real
   contrast (WCAG 2.2 AA), real responsive behavior, reduced-motion respect.
   The metaphor never costs a user task.

## Layout

- Column grid derived from the character grid — widths in `ch` where natural.
- Boxed sections using border or box-drawing characters; single-line rules as
  separators.
- Density is period-appropriate: information-rich, little decorative
  whitespace. Group with boxes and rules, not with floating space.
- A persistent status/header line (host-style branding, section, state) is a
  strong signature element.

## Typography

- **Everything monospace is legitimate** in this style — the rare exception
  where body-in-mono is correct. If body text runs long (articles), a
  readable mono at ≥1rem with line length ≤70ch, or a deliberate hybrid
  (mono UI + humanist body) declared up front.
- Uppercase for labels and status only; sentence case for content.
- ASCII art / figlet-style display type as a signature, used sparingly and
  always with an accessible text alternative.

## Color roles (neutral)

- `canvas` — near-black (or paper for the teletype variant).
- `phosphor` — the primary luminous text/accent color (project's primary).
- `phosphor-dim` — same hue, reduced, for secondary text; must still meet AA.
- `alert` — one warm contrast color for errors/warnings (project's
  secondary), used only semantically.
- No third accent. Hue variety is not part of this style; intensity levels
  of the phosphor are.

## Components

- **Buttons/links:** bracketed (`[ RUN ]`) or prompt-prefixed; inversion or
  fill on hover/focus; underline acceptable for inline links.
- **Forms:** flat fields with visible borders, mono input, blinking-caret
  affordance optional (one place, respects `prefers-reduced-motion`).
- **Tables/lists:** ruled or box-drawn; column alignment exact — this style
  showcases tabular data better than almost any other.
- **Progress/status:** ASCII progress bars, spinner glyph cycles, `[####--]`
  idioms — with `aria` equivalents.
- **Code blocks:** need a distinguishing treatment (rule, label, or dim
  background) since the whole page is already mono.

## Effects budget (pick at most one ambient)

- Subtle scanline overlay (≤3–4% opacity), OR
- faint text glow on headings only (small blur, same hue), OR
- a single typing animation on the hero line (once, skippable).

Flicker, curvature/barrel distortion, heavy noise: never — they harm
readability and accessibility for costume value.

## Anti-patterns — never produce these

- Effect stacking: scanlines + glow + flicker + noise together.
- Neon rainbow palettes — this is a one-phosphor style.
- Mixing the metaphor arbitrarily: prompt idioms on one page, none on the
  next.
- Fake "hacking" content, scrolling gibberish, or Matrix rain as filler.
- Animation that ignores `prefers-reduced-motion`.
- Dim-on-dark text below AA because "terminals were low contrast".
- Proportional fonts inside aligned ASCII structures (breaks the grid).
- Tiny mono body text (<1rem) because terminals were small.

## Verify before delivering

One canvas variant; one phosphor + one alert only; ≤1 ambient effect;
alignment exact on every boxed/ruled structure; AA contrast including
dimmed text; reduced-motion honored; text alternatives for ASCII art.
