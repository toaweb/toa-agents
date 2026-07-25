# Images and Graphics in Brutalist Web Design

> A brand-neutral, framework-neutral production guide for photography, illustration, icons, borders, separators, textures, diagrams, and graphic treatments in brutalist websites.

**Status:** normative visual-media resource  
**Scope:** image selection, editing, framing, collage, iconography, graphic devices, accessibility, responsiveness, and performance  
**Companion resource:** `design-system.md`

---

## 1. Purpose

In brutalist web design, an image is not anonymous decoration. It is a structural object that may be framed, cropped, labeled, numbered, copied, screened, torn, or deliberately misregistered.

The result must still be intentional, legible, responsive, accessible, and technically efficient.

This resource is independent of any specific brand, project, palette, font family, or software stack. Color examples describe common brutalist techniques rather than a fixed identity.

---

## 2. Core principles

### 2.1 Every visual needs a role

An image or graphic should do at least one of the following:

- document a person, place, object, or event
- establish atmosphere or context
- explain a process or relationship
- create hierarchy
- provide evidence
- act as a deliberate interruption in the layout
- support navigation or status

Do not add imagery only because a region feels empty.

### 2.2 Raw does not mean random

Rough texture, asymmetry, harsh crop, halftone, collage, and photocopy effects must be controlled. The page should establish visual order before it breaks that order.

### 2.3 Consistency matters more than the number of effects

Choose two or three recurring treatments for most visuals. For example:

1. high-contrast monochrome
2. 3px solid frame
3. one hard offset shadow

Use halftone, torn paper, color separation, and glitch as occasional accents.

### 2.4 The subject must survive the treatment

A strong source image normally has:

- one clear focal point
- a recognizable silhouette
- usable local contrast
- enough resolution for crop and texture
- composition that tolerates asymmetry
- details that remain understandable at small sizes

---

## 3. Photography direction

### Prefer

- documentary photography
- direct portraits
- hard flash or directional light
- visible material texture
- architecture, infrastructure, workshops, streets, tools, and real environments
- natural moments rather than staged corporate gestures
- close crops and unusual viewpoints
- strong shadow shapes
- honest imperfections

### Avoid by default

- generic stock-business photography
- staged handshakes and artificial group poses
- soft pastel lifestyle imagery
- excessive beauty retouching
- generic shallow-depth-of-field backgrounds
- exaggerated HDR
- synthetic lens flare
- scenes with many competing micro-details
- inconsistent camera and lighting styles without a unifying treatment

### Portraits

Brutalist portraits often use:

- direct eye contact
- hard flash
- tight crop
- black-and-white or duotone
- visible grain
- contact-sheet numbering
- registration marks
- asymmetric placement

Do not distort identity, obscure the eyes without reason, or use texture that erases important facial information.

---

## 4. Color and tonal treatments

Brutalism has no official image palette. The common logic is restrained color and strong tonal separation.

### 4.1 High-contrast monochrome

Use when the source has a clear subject and good midtone detail.

```css
.image-monochrome {
  filter: grayscale(1) contrast(1.3) brightness(0.95);
}
```

Do not crush all shadow detail. Dark clothing, dark skin tones, night scenes, and textured backgrounds may need individual adjustment.

### 4.2 Duotone

Combine black or a dark ink color with one saturated project accent.

Suitable methods:

- pre-rendered duotone for consistent results
- gradient map in an image editor
- CSS blend mode for controlled, non-critical cases

```css
.duotone {
  background: var(--visual-accent, #ff3b00);
  overflow: hidden;
}

.duotone img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: grayscale(1) contrast(1.4);
  mix-blend-mode: multiply;
}
```

CSS blending varies with the source. Pre-render important editorial images when consistent output is required.

### 4.3 Restrained color

Natural color may remain when:

- the subject depends on color
- color provides evidence or context
- the source already matches the page's tonal direction
- a hard frame and layout treatment provide enough consistency

Reduce saturation or normalize contrast rather than applying an effect automatically.

### 4.4 Photocopy treatment

Typical characteristics:

- blown highlights
- dense black shadows
- dust and scan lines
- uneven toner
- damaged or imperfect edges
- repeated-copy degradation

The source must remain identifiable. Texture should be adjustable as a separate layer.

### 4.5 Halftone

Halftone imitates newspaper or screen printing.

- use finer dots for small cards
- use larger dots for hero or poster-scale work
- protect faces and fine text
- test at real rendered size
- check for moiré after responsive scaling
- prefer pre-rendering when consistent print behavior matters

### 4.6 Color separation and misregistration

A small channel offset can reference imperfect printing.

- limit the offset to a few pixels
- use it on selected edges or subjects
- do not apply it to body text
- avoid continuous animation
- ensure the subject remains readable

---

## 5. Composition and crop

### 5.1 Focal hierarchy

Each image should have one dominant subject. Supporting texture, labels, or graphic fragments must not compete with it.

### 5.2 Hard crop

Approved:

- subject leaving the frame
- partial head or body crop
- extreme close-up
- asymmetrical placement
- architecture without full context
- large negative space for adjacent type

Avoid accidental cuts through eyes, hands, product controls, diagrams, or other information-bearing details.

### 5.3 Protective positioning

Use `object-position`, focal-point metadata, art direction, or separate mobile crops to protect the subject.

```css
.media-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: var(--focal-x, 50%) var(--focal-y, 50%);
}
```

### 5.4 Negative space

Negative space may hold HTML typography, metadata, or navigation. Do not add empty space only to mimic an editorial template.

---

## 6. Image presentation patterns

### 6.1 Hard frame

```css
.media-frame {
  border: 3px solid currentColor;
  border-radius: 0;
  overflow: hidden;
}
```

- standard frame: 2–4px
- major feature or hero: 4–6px
- keep corners square
- do not combine every frame with a shadow

### 6.2 Hard offset shadow

```css
.media-offset {
  border: 3px solid currentColor;
  box-shadow: 10px 10px 0 var(--visual-accent, currentColor);
}
```

- blur must be zero
- keep direction consistent within a section
- common offset: 6–12px
- large feature: 12–20px
- preserve space so the shadow is not clipped

### 6.3 Inset print border

An image may use an outer paper border and inner ink rule to resemble a print, slide, evidence card, or contact sheet.

### 6.4 Captioned figure

Use semantic `<figure>` and `<figcaption>`.

```html
<figure class="editorial-figure">
  <img src="example.webp" alt="Useful description of the subject">
  <figcaption>Fig. 03 — Place, date, or relevant context</figcaption>
</figure>
```

Captions may include:

- figure number
- date
- location
- source
- technical detail
- editorial note

Do not invent metadata only to make the page look technical.

### 6.5 Solid text plate

When text overlaps an image, place it on a solid plate unless contrast has been verified for every responsive crop.

```css
.image-label {
  position: absolute;
  inset-inline-start: 1rem;
  inset-block-end: 1rem;
  padding: 0.3em 0.45em;
  border: 2px solid currentColor;
  background: var(--label-bg, #ffffff);
  color: var(--label-ink, #000000);
  font-weight: 900;
  text-transform: uppercase;
}
```

Important text should remain HTML rather than being permanently embedded in the raster image.

### 6.6 Controlled collage

A practical collage may contain:

- one main image
- one cut-out subject or secondary crop
- one headline or text plate
- one number, label, or stamp
- one torn-paper or color block
- one arrow, line, or registration mark

Keep the total to roughly three to five layers. One element must remain dominant.

### 6.7 Torn paper

Torn edges should be used as masks, separators, or small corner treatments.

- avoid covering controls
- keep body text on a stable surface
- use a reusable mask rather than random new edges everywhere
- provide a clean mobile fallback when the tear creates awkward gaps

---

## 7. Icons

Brutalist iconography should be direct, geometric, and structurally consistent.

### 7.1 Suitable icon styles

- simple line icons with strong stroke
- filled geometric symbols
- arrows, crosses, squares, circles, and registration marks
- technical pictograms
- bitmap or low-resolution symbols when intentionally selected
- native Unicode symbols when they render consistently and remain accessible

### 7.2 Icon rules

- Use one icon family per interface.
- Keep stroke widths consistent.
- Prefer square bounding boxes.
- Avoid soft, overly detailed, or decorative illustration icons.
- Do not place every icon inside a rounded container.
- Do not use an icon as the only label for unfamiliar actions.
- Mark decorative icons as hidden from assistive technology.
- Give interactive icons an accessible name and sufficient target size.

### 7.3 Icon sizing

Common visible sizes:

- 16px: dense utility context
- 20–24px: normal interface controls
- 32–48px: feature or navigation symbol

The clickable target should normally be at least 44×44px even when the visible icon is smaller.

---

## 8. Borders and separators

Borders are part of the composition, not an afterthought.

### 8.1 Line hierarchy

| Weight | Use |
|---:|---|
| 1px | secondary divider, table rule, metadata rail |
| 2px | standard component, input, button, card |
| 4px | major section, feature, hero, dialog |
| 6px+ | rare poster-scale statement |

### 8.2 Separator types

Approved:

- solid horizontal rule
- double rule
- dashed technical cut line
- dotted registration line
- repeated index marks
- numbered divider
- alternating blocks of ink and paper

Use one dominant separator language per page.

### 8.3 Structural meaning

Separators should indicate:

- section change
- content grouping
- reading order
- active or selected region
- process step
- boundary between data areas

Do not add lines that imply structure where no relationship exists.

---

## 9. Graphic devices

### 9.1 Labels and stamps

Suitable treatments:

- solid rectangular label
- outlined issue plate
- date stamp
- category marker
- approval/rejection mark
- figure code
- version number

Text must be meaningful and readable.

### 9.2 Arrows and connectors

- Use thick, simple arrows.
- Keep arrow style consistent.
- Connect elements only when a real sequence or relationship exists.
- Avoid decorative arrows pointing nowhere.

### 9.3 Registration marks

Crop marks, crosses, circles, and calibration bars may reinforce a print-production aesthetic.

- keep them outside critical content
- use them sparingly
- mark them decorative for assistive technology
- do not let them resemble controls

### 9.4 Numbering

Numbers can establish sequence, hierarchy, or editorial rhythm.

Use consistent formats such as:

- `01`, `02`, `03`
- `FIG. 01`
- `STEP 1/4`
- `ISSUE 004`

Do not number unrelated components solely as decoration.

### 9.5 Technical metadata

Coordinates, dimensions, dates, file names, response times, and version labels may be used when they are real and relevant. Fake data weakens the visual language.

---

## 10. Texture and pattern

### 10.1 Suitable textures

- paper grain
- photocopy noise
- ink bleed
- toner streaks
- halftone dots
- scan lines
- coarse bitmap dithering
- concrete, metal, cardboard, tape, or fabric scans

### 10.2 Suitable patterns

- square grid
- dot grid
- stripes
- checkerboard
- repeated type
- hatch lines
- calibration bars

### 10.3 Texture rules

- Texture must not reduce body-text readability.
- Keep texture on a separate layer where possible.
- Use lower contrast behind content.
- Avoid random texture packs with unrelated material qualities.
- Reuse a small approved texture set.
- Test compression; fine noise may create very large files.
- Provide a clean fallback for small screens when necessary.

### 10.4 CSS texture

Simple vector-like patterns may be generated in CSS, but avoid decorative gradients when the chosen brutalist direction rejects them. Repeating linear or radial gradients may be used only as a technical method for a flat grid, stripe, or dot pattern—not as soft color blending.

---

## 11. Illustration

Suitable illustration styles include:

- technical diagrams
- exploded views
- cutaway drawings
- instruction-manual line art
- blocky geometric compositions
- screen-print forms
- photocopied sketches
- bitmap diagrams
- raw browser or interface schematics

Rules:

- Use a limited stroke and color system.
- Keep labels in HTML when possible.
- Preserve logical relationships.
- Avoid decorative complexity that imitates a stock illustration library.
- Use arrows, lines, and numbering consistently with the rest of the page.

---

## 12. Data graphics

Charts and scorecards can use brutalist styling without sacrificing accuracy.

- Use flat fills and strong axes.
- Label values directly where possible.
- Use patterns or symbols in addition to color.
- Avoid 3D charts, glow, glass, and decorative perspective.
- Keep grid lines purposeful.
- Use monospace or tabular numerals for aligned values.
- Provide a table or textual summary for complex data.
- Never distort scale for visual drama.

---

## 13. Aspect ratios and use cases

| Use case | Common ratio | Notes |
|---|---:|---|
| Wide hero | 16:9 or 3:2 | protect focal point; consider separate mobile crop |
| Portrait hero | 4:5 or 3:4 | useful for editorial portrait or poster composition |
| Article lead | 3:2 | stable documentary format |
| Card media | 4:3 or 3:2 | keep one ratio within a card set |
| Portrait | 3:4 or 4:5 | allow direct crop and caption rail |
| Icon/graphic tile | 1:1 | useful for geometric systems |
| Social preview | platform-specific | keep critical content inside safe area |

Aspect ratios are compositional defaults, not mandatory rules.

---

## 14. Responsive behavior

- Use separate crops when one crop cannot protect the subject on all screens.
- Test images at 320–400px rendered width.
- Reduce or remove collage overlap on small screens.
- Move captions into normal flow when overlay becomes cramped.
- Preserve labels and metadata; do not hide context without reason.
- Use `object-position` to protect focal points.
- Prevent shadows and torn edges from causing horizontal scrolling.
- Check halftone and thin-line patterns for moiré at each breakpoint.

---

## 15. Accessibility

### Alternative text

- Describe the subject and purpose in context.
- Do not describe every visual filter.
- Use empty `alt=""` for purely decorative textures and marks.
- Do not repeat nearby captions word for word unless necessary.
- Complex diagrams need a textual explanation.

### Text and contrast

- Keep important text in HTML.
- Use solid text plates over busy images.
- Normal text requires at least 4.5:1 contrast.
- Large text and meaningful graphics require at least 3:1.
- Do not rely on color alone in diagrams or status graphics.

### Motion

- Animated glitch, scan, marquee, or noise must stop under reduced-motion preferences.
- Avoid flashing content.
- Provide pause controls for non-essential continuous motion.

---

## 16. Performance and file delivery

### Preferred formats

- AVIF or WebP for photographs
- SVG for simple diagrams, icons, frames, and patterns
- PNG for transparency when lossless raster is required
- JPEG only when compatibility or workflow requires it

### Delivery rules

- provide intrinsic width and height
- use `srcset` and `sizes` for responsive raster images
- do not lazy-load the likely LCP image
- lazy-load below-the-fold media
- preload only a verified critical image
- compress textures carefully
- avoid embedding large base64 images in CSS
- remove unused metadata when appropriate
- do not ship source-resolution images to small cards

Important editorial images should have art-directed crops rather than relying entirely on automatic center cropping.

---

## 17. Automation guidance

Automated processing may standardize a mixed image library, but it cannot make every source equally suitable.

### Safe automated steps

- crop to approved aspect ratios
- normalize exposure
- convert to monochrome
- apply a restrained contrast curve
- add a standard frame
- add a consistent paper border
- generate responsive sizes
- compress to modern formats

### Steps requiring review

- face crop
- heavy thresholding
- halftone scale
- duotone mapping
- torn masks
- collage layout
- text placement
- object removal or generative extension

### Generic transformation prompt

```text
Transform the supplied image into a brand-neutral brutalist editorial visual.
Preserve the subject, identity, factual content, and important details.

Use high-contrast documentary treatment, controlled monochrome or one-color
duotone, coarse print grain, restrained halftone, square framing, and a hard
editorial crop. Add only minimal registration marks or paper wear when they
support the composition.

Do not add company names, logos, slogans, product text, fake metadata, rounded
corners, gradients, glow, glass, soft blur, or unrelated objects. Do not alter
faces, products, diagrams, or factual information.
```

---

## 18. Anti-patterns

Reject a visual treatment when it:

- applies the same extreme filter to every source
- uses generic stock photography under a rough overlay
- obscures the main subject
- places important text directly over uncontrolled detail
- combines halftone, glitch, torn paper, duotone, shadow, and stamps on every image
- uses random arrows, codes, or fake technical labels
- clips faces or products without intent
- creates moiré at responsive sizes
- uses decorative texture that dominates the content
- creates a different visual language for every section

---

## 19. Quality checklist

### Source and subject

- [ ] The image has a clear purpose.
- [ ] The focal point is obvious.
- [ ] The subject survives the treatment.
- [ ] The crop protects important details.
- [ ] The source is licensed and credited where required.

### Style consistency

- [ ] The approved tonal treatment is used.
- [ ] Frames follow the defined border scale.
- [ ] Shadow direction is consistent.
- [ ] Texture comes from the approved set.
- [ ] Labels and numbering are meaningful.
- [ ] Collage has one dominant element.

### Responsive behavior

- [ ] Mobile crop has been reviewed.
- [ ] No shadow or mask causes horizontal overflow.
- [ ] Halftone and line patterns avoid moiré.
- [ ] Caption remains readable.
- [ ] Focal point remains visible.

### Accessibility

- [ ] Informative images have useful alt text.
- [ ] Decorative images use empty alt text.
- [ ] Important text remains HTML.
- [ ] Text-over-image contrast is verified.
- [ ] Diagrams have textual explanation.
- [ ] Color is not the only information channel.

### Performance

- [ ] Correct output format is used.
- [ ] Intrinsic dimensions are present.
- [ ] Responsive sources are generated.
- [ ] LCP media is not lazy-loaded.
- [ ] Below-the-fold media is lazy-loaded.
- [ ] File size is appropriate for rendered size.

---

## 20. Instructions for AI agents

```text
Use `images-and-graphics.md` as a brand-neutral production standard.

First determine the purpose of every visual. Select or create imagery with a
clear subject, documentary or structural value, and enough contrast to survive
the chosen treatment. Apply only the small set of recurring effects defined for
the project.

Keep important text in HTML. Use square frames, flat color, meaningful captions,
controlled crop, limited texture, and selective hard offset shadows. Icons,
separators, arrows, labels, diagrams, and registration marks must follow one
consistent graphic language.

Do not infer or add a company palette, logo, font, slogan, technology stack, or
fake metadata. Validate responsive crop, accessibility, moiré, contrast, alt
text, intrinsic dimensions, and file size before completion.
```

---

## 21. Research references

- [Brutalist Web Design — David Bryant Copeland](https://brutalist-web.design/)
- [Brutalist Design Principles — nat.io](https://nat.io/blog/brutalist-design-principles)
- [WCAG 2.2 — W3C](https://www.w3.org/TR/WCAG22/)
- [Contrast Minimum — W3C WAI](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum)
- [Non-text Contrast — W3C WAI](https://www.w3.org/WAI/WCAG21/understanding/non-text-contrast.html)
- [Images Tutorial — W3C WAI](https://www.w3.org/WAI/tutorials/images/)
- [Responsive Images — web.dev](https://web.dev/articles/serve-responsive-images)
- [Optimize Largest Contentful Paint — web.dev](https://web.dev/articles/optimize-lcp)

