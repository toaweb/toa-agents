# Brutalist Web Design System

> A brand-neutral, framework-neutral reference for designing accessible and usable brutalist websites.

**Status:** normative style resource  
**Scope:** visual language, color, typography, layout, components, interaction, responsiveness, accessibility, and performance  
**Companion resource:** `images-and-graphics.md`

---

## 1. Purpose

This document defines a repeatable brutalist web design language. It is intended for designers, developers, and AI agents creating websites in the style.

The system must remain independent of any specific company, product, color palette, font family, framework, or technology stack. Project-specific identity should be applied as a separate layer.

The goal is not to make a website look unfinished. The goal is to expose structure, prioritize content, and create deliberate tension through typography, contrast, framing, and layout.

### Normative language

- **Must** means required.
- **Should** means the default unless a documented reason justifies an exception.
- **May** means optional.

---

## 2. Definition

Web brutalism treats the native materials of the web as visible design elements:

- text
- links
- buttons
- forms
- borders
- grids
- tables
- images
- browser states
- loading and error messages

It rejects unnecessary visual disguise. Structure is allowed to look structural. Controls are allowed to look functional. Content is allowed to dominate the interface.

### Common branches

| Branch | Characteristics |
|---|---|
| Classical web brutalism | Native controls, system fonts, direct links, minimal decoration |
| Editorial brutalism | Large typography, visible grids, captions, numbering, strong image treatment |
| Neo-brutalism | Heavy outlines, saturated accents, hard offset shadows, simplified geometry |
| Technical brutalism | Monospace labels, diagrams, tables, coordinates, system readouts |

A project may combine branches, but it should establish one dominant direction.

---

## 3. Core principles

### 3.1 Function before decoration

The user must understand the page before appreciating its style. Navigation, hierarchy, controls, and status must remain obvious.

### 3.2 Visible structure

Grids, borders, dividers, columns, labels, and captions may be visible. Structure should communicate organization rather than becoming empty decoration.

### 3.3 Typography as architecture

Hierarchy is built primarily through scale, weight, width, spacing, and alignment. Typography should carry more of the composition than ornamental graphics.

### 3.4 Controlled contrast

Brutalism relies on strong differences:

- large versus small
- black versus white
- dense versus empty
- aligned versus deliberately offset
- polished information versus rough material texture

Contrast should direct attention, not make every element compete.

### 3.5 Honest interaction

Links must look like links. Buttons must look clickable. Form fields must look editable. Disabled, selected, loading, success, and error states must be visible.

### 3.6 Deliberate imperfection

Misalignment, asymmetry, collage, crop, and print wear may be used, but they must be repeatable decisions. Randomness is not a system.

### 3.7 Performance as part of the aesthetic

The style should not depend on heavy animation, excessive client-side scripting, or oversized media. Fast delivery supports the principle of directness.

---

## 4. Non-negotiable rules

### Must

- use square corners as the default
- use clear visual hierarchy
- maintain usable navigation
- use semantic HTML and real text
- provide visible keyboard focus
- support mobile and zoomed layouts
- distinguish interactive and non-interactive elements
- provide all relevant component states
- meet WCAG 2.2 AA as a minimum target

### Must not

- use soft glassmorphism, frosted panels, or backdrop blur
- use decorative gradients as a default surface treatment
- use soft ambient shadows
- round every card, field, and button
- hide essential controls behind hover-only behavior
- use texture behind body text when it reduces readability
- bake important interface text into raster images
- break expected navigation behavior for visual novelty
- apply glitch, rotation, or collage to every element

### Should

- use only two or three dominant brutalist devices on one page
- establish an orderly grid before breaking it
- use one primary accent at a time
- reserve the strongest contrast for the most important content
- alternate dense and open sections to create rhythm

---

## 5. Color system

Brutalism has no official palette. Its most common color logic is monochrome or near-monochrome with one saturated accent.

### 5.1 Palette structures

#### Classical monochrome

- black ink
- white or warm off-white paper
- middle gray for secondary information

#### Monochrome plus signal

- black and paper base
- one saturated red, yellow, blue, green, or orange accent
- semantic colors reserved for status

#### High-color neo-brutalism

- black outlines
- white or light neutral background
- two or three flat saturated colors
- no gradients or translucent layering

High-color palettes require more discipline because every saturated surface competes for attention.

### 5.2 Neutral example tokens

These values illustrate roles, not a required palette:

```css
:root {
  --color-canvas: #f2f0e8;
  --color-surface: #ffffff;
  --color-ink: #000000;
  --color-muted: #555555;
  --color-line: #000000;
  --color-accent: #ff3b00;
  --color-success: #087f5b;
  --color-warning: #9a6700;
  --color-danger: #c92a2a;
}
```

Projects should replace these values while preserving the semantic roles.

### 5.3 Distribution

A useful starting ratio is:

- 75–85% neutral canvas, surface, ink, and gray
- 10–20% primary accent
- no more than 5% secondary signal or semantic status colors

### 5.4 Color rules

- Use flat color fields.
- Use accent color to signal priority, selection, or action.
- Do not use color as the only state indicator.
- Test all text and control boundaries for contrast.
- Avoid large areas of multiple saturated colors unless high-color neo-brutalism is the chosen branch.

---

## 6. Typography

Brutalist typography is based on role and contrast, not one mandatory font list.

### 6.1 Type roles

| Role | Suitable categories | Use |
|---|---|---|
| Display | heavy grotesk, condensed sans, slab serif, heavy system sans | heroes and section titles |
| Body | readable sans or serif | paragraphs, articles, help text |
| Utility | monospace or technical sans | metadata, labels, timestamps, code |

### 6.2 Font selection rules

- Use one primary family plus one contrasting utility family when possible.
- Use system fonts when speed and rawness are priorities.
- Self-host web fonts when a specific typeface is essential.
- Load only required weights and styles.
- Always define robust fallbacks.
- Do not use more than three type families without a strong editorial reason.

### 6.3 Hierarchy

```css
:root {
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-body: 1rem;
  --text-lead: clamp(1.125rem, 1rem + 0.5vw, 1.5rem);
  --text-heading: clamp(2rem, 1.25rem + 3vw, 4.5rem);
  --text-display: clamp(3.25rem, 1.5rem + 8vw, 9rem);
}
```

- Display headings may use uppercase.
- Body copy should normally use mixed case.
- Heading line-height may be tight: `0.85–1.0`.
- Body line-height should normally be `1.5–1.75`.
- Long-form line length should normally remain within `55–75ch`.
- Utility text must remain readable; small metadata is not exempt from contrast requirements.

### 6.4 Typographic tension

Approved techniques include:

- extreme scale contrast
- cropped display letters
- mixed alignment
- narrow uppercase labels beside large headings
- mono metadata against expressive display type
- repeated words used as texture when they are decorative and hidden from assistive technology

Do not compromise the reading order or semantic heading structure.

---

## 7. Spacing and rhythm

Use a consistent base unit. A 4px or 5px base works well.

```css
:root {
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-24: 6rem;
  --space-32: 8rem;
}
```

### Rhythm rules

- Use tight spacing inside information clusters.
- Use large gaps between major sections.
- Alternate dense and open compositions.
- Do not distribute all elements evenly by default.
- Whitespace is an active brutalist material, not unused space.

---

## 8. Grid and layout

### 8.1 Base grid

- mobile: 4 columns
- tablet: 6 columns
- desktop: 12 columns
- use consistent gutters
- allow visible column dividers where they explain structure

```css
.layout-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
}

@media (min-width: 48rem) {
  .layout-grid {
    grid-template-columns: repeat(12, minmax(0, 1fr));
  }
}
```

### 8.2 Composition patterns

Approved patterns:

- asymmetric two-column split
- oversized heading paired with a narrow metadata rail
- full-width statement followed by a dense grid
- visible sidebar or index column
- image or figure extending beyond the text column
- alternating paper and ink sections
- numbered editorial sequence
- contact-sheet grid

### 8.3 Grid breaking

A component may overlap, offset, crop, or extend beyond the base grid when:

- the base grid is already understandable
- the reading order remains logical
- important content is not covered
- keyboard focus remains visible
- the mobile layout has a deliberate alternative
- the page does not create unintended horizontal scrolling

Use one dominant grid break per section rather than many small disruptions.

### 8.4 Section rhythm

Alternate among:

1. **Statement sections:** large type, low content density.
2. **Evidence sections:** projects, products, data, lists, or imagery.
3. **Reading sections:** restrained typography and generous line length.

Repeated identical card grids weaken the style.

---

## 9. Borders, surfaces, and shadows

### 9.1 Borders

```css
:root {
  --border-hairline: 1px;
  --border-standard: 2px;
  --border-strong: 4px;
  --radius: 0;
}
```

- Use 1px for secondary dividers.
- Use 2px for controls and standard cards.
- Use 4px for featured frames, heroes, dialogs, and major separators.
- Keep corners square.
- Use dashed or dotted lines only for technical or editorial meaning.

### 9.2 Surfaces

Surfaces should be flat and visibly bounded. Use color inversion, border strength, or spacing to create hierarchy instead of translucent layers.

### 9.3 Hard offset shadows

```css
.hard-shadow {
  box-shadow: 8px 8px 0 currentColor;
}
```

Rules:

- blur must be zero
- offset direction should remain consistent within a section
- standard offset: 4–10px
- large featured elements: 10–18px
- not every component should have a shadow

---

## 10. Components

### 10.1 Header and navigation

- Use a full-width structural bar or clearly bounded header.
- Mark the active destination with underline, inversion, block color, or a strong border.
- Keep labels visible.
- Do not rely on icons alone for primary navigation.
- Avoid floating pill-shaped navigation as the default.
- Mobile navigation must use a clear button and logical reading order.

### 10.2 Hero

A strong brutalist hero normally contains:

1. section code, eyebrow, or category label
2. one dominant heading
3. a short explanation
4. one primary action and optional secondary link
5. one figure, image, or structural graphic
6. caption, number, or meaningful metadata

The value proposition and action must remain understandable before media loads.

### 10.3 Buttons

```css
.button {
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border: 2px solid currentColor;
  border-radius: 0;
  background: var(--color-accent);
  color: var(--color-ink);
  font-weight: 800;
  text-transform: uppercase;
}

.button:active {
  transform: translate(2px, 2px);
}
```

- Primary: solid accent.
- Secondary: transparent with strong border.
- Tertiary: visible text link, often underlined or paired with an arrow.
- Provide hover, focus, active, disabled, loading, success, and error states where relevant.

### 10.4 Cards

- Use a visible frame or divider.
- Provide one clear primary action.
- Give metadata a consistent position.
- Keep media ratios consistent within one card set.
- Use hard shadow only on featured cards.
- Do not wrap every content block in a card.

### 10.5 Links

- Underline body links by default.
- Use clear hover and focus changes.
- Do not make non-links look like links.
- External-link icons must not replace accessible text.

### 10.6 Tags and badges

- Use square corners and 1–2px borders.
- Use compact uppercase or monospace text.
- Limit visible tags to meaningful categories.
- Clickable tags should have generous target size.
- Status badges must include text, not color alone.

### 10.7 Forms

- Labels must remain visible.
- Placeholder text must not replace labels.
- Inputs require strong borders and clear focus.
- Errors should appear next to the relevant field.
- Required fields must be communicated in text.
- Native input types should be used when possible.
- Submission must expose loading, success, and failure states.

### 10.8 Tables and data interfaces

- Use strong row and column structure.
- Keep headers visible and unambiguous.
- Use tabular numbers where alignment matters.
- Do not decorate data cells with unnecessary texture.
- Provide a deliberate small-screen strategy: reflow, scroll, or alternate summary.

### 10.9 Dialogs

- Use a strong frame and flat backdrop.
- Avoid blur and glass effects.
- Move focus into the dialog and restore it when closed.
- Support Escape unless the action is intentionally blocking.
- State destructive consequences clearly.

### 10.10 Footer

The footer may use a technical or editorial end-plate treatment, but it must still contain real navigation, contact, legal, and status information in readable form.

---

## 11. Interaction and motion

Motion should be immediate, mechanical, and functional.

Approved:

- instant color inversion
- underline or block changes
- 1–3px active displacement
- short reveal for state changes
- progress and loading indicators

Avoid:

- scroll-jacking
- decorative parallax
- automatic marquees without controls
- continuous glitch animation
- long floating transitions
- staggered entrance animation for every section

Typical transitions should remain within `0–120ms`. The interface must remain understandable when animation is removed.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 12. Responsive behavior

- Design mobile first.
- Convert desktop asymmetry into logical document flow on small screens.
- Remove overlaps that reduce readability or target size.
- Preserve metadata instead of hiding it.
- Adjust heading size, line breaks, and wording where necessary.
- Avoid clipping text to force a desktop composition onto mobile.
- Do not use `overflow-x: hidden` to conceal layout defects.
- Test at 320px and with large text settings.

Breakpoints should be introduced when the content needs them, not for named device models.

---

## 13. Accessibility and usability

Brutalism is not permission to reduce usability.

### Minimum requirements

- semantic landmarks and heading hierarchy
- skip link
- complete keyboard operation
- visible focus indicator
- text contrast of at least 4.5:1 for normal text
- contrast of at least 3:1 for large text and meaningful non-text graphics
- pointer targets of at least 24×24 CSS pixels; 44×44 is preferred
- no state communicated by color alone
- content usable at 200% text zoom and 400% page zoom
- correct labels, errors, and instructions for forms
- useful alternative text for informative images
- empty `alt=""` for purely decorative images
- support for reduced motion

### Focus standard

```css
:focus-visible {
  outline: 3px solid var(--color-accent);
  outline-offset: 4px;
}
```

Strong focus treatment is visually compatible with brutalism and should be considered part of the style.

---

## 14. Performance

Recommended targets:

| Metric or resource | Target |
|---|---:|
| Largest Contentful Paint | ≤ 2.5s at the 75th percentile |
| Cumulative Layout Shift | ≤ 0.1 |
| Interaction to Next Paint | ≤ 200ms |
| Third-party scripts | none by default |

Implementation principles:

- deliver primary content as HTML
- use client-side code only for real interaction
- make the LCP resource discoverable in initial markup
- do not lazy-load the likely LCP image
- reserve media dimensions to prevent layout shift
- load below-the-fold media lazily
- avoid animation libraries for basic state changes
- minimize font weights, tracking scripts, and decorative media

---

## 15. Anti-patterns

Reject a design when it:

- looks like a generic template with a thick border added afterward
- has no underlying grid or spacing logic
- uses large type without a readable mobile solution
- adds meaningless terminal text or fake system data
- uses multiple competing accent colors in one component
- gives every card, button, and image a hard shadow
- uses too many typefaces to appear raw
- makes metadata too faint or too small
- prioritizes asymmetry over logical reading and focus order
- hides essential content in hover, animation, or marquee
- confuses visual aggression with useful hierarchy

---

## 16. Quality checklist

### Visual system

- [ ] The selected brutalist branch is identifiable.
- [ ] Color roles are consistent.
- [ ] Corners are square by default.
- [ ] Borders follow a small defined scale.
- [ ] Hard shadows are selective.
- [ ] Each section has one dominant focal point.
- [ ] Metadata is meaningful.
- [ ] Dense and open sections create rhythm.

### Responsive design

- [ ] No accidental horizontal scrolling at 320px.
- [ ] Headings are not clipped.
- [ ] Desktop asymmetry becomes logical mobile flow.
- [ ] Interactive targets are large enough.
- [ ] Sticky elements do not cover content or focus.

### Accessibility

- [ ] Heading structure and landmarks are correct.
- [ ] All functions work with keyboard input.
- [ ] Focus is visible on every surface.
- [ ] Contrast has been measured.
- [ ] Forms expose labels, errors, and status.
- [ ] Color is not the only status indicator.
- [ ] Reduced motion is respected.
- [ ] Zoom and reflow are tested.

### Performance

- [ ] The LCP image is not lazy-loaded.
- [ ] Media has intrinsic dimensions.
- [ ] Below-the-fold images are lazy-loaded.
- [ ] Client-side code is limited to real interaction.
- [ ] Third-party scripts are justified.
- [ ] Unused font weights are removed.

---

## 17. Instructions for AI agents

```text
Design and implement the page according to `design-system.md` and
`images-and-graphics.md`.

Treat both resources as brand-neutral style rules. Do not infer a company,
product, framework, font family, or color identity from the examples. Apply the
project's separate identity only after the brutalist structure is established.

Use semantic HTML, visible hierarchy, square corners, flat surfaces, strong
borders, selective hard shadows, clear interaction states, and a deliberate
grid. Do not add glass, blur, soft shadows, decorative gradients, or rounded
card systems.

Validate mobile layout, keyboard focus, contrast, zoom, reduced motion, media
dimensions, and loading performance before considering the work complete.
```

---

## 18. Research references

- [Brutalist Web Design — David Bryant Copeland](https://brutalist-web.design/)
- [Brutalist Design Principles — nat.io](https://nat.io/blog/brutalist-design-principles)
- [WCAG 2.2 — W3C](https://www.w3.org/TR/WCAG22/)
- [Contrast Minimum — W3C WAI](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum)
- [Non-text Contrast — W3C WAI](https://www.w3.org/WAI/WCAG21/understanding/non-text-contrast.html)
- [Focus Appearance — W3C WAI](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)
- [Target Size Minimum — W3C WAI](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [Optimize Largest Contentful Paint — web.dev](https://web.dev/articles/optimize-lcp)
- [Optimize Cumulative Layout Shift — web.dev](https://web.dev/articles/optimize-cls)
- [prefers-reduced-motion — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)

