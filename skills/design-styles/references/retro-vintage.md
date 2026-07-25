# Retro & Vintage Website Design System

> A general-purpose reference for designers, developers, and AI agents creating retro- or vintage-inspired websites.
>
> This document defines the design language only. It is intentionally brand-neutral and does not include project-specific colors, fonts, components, or identity rules.

---

## 1. Purpose

Retro and vintage web design uses visual references from earlier periods while preserving modern usability, accessibility, responsiveness, and performance.

The objective is **not** to reproduce the technical limitations of an old website. The objective is to evoke a recognizable era through typography, composition, color, ornament, texture, imagery, and interaction without degrading the user experience.

Use this system to:

- establish an era-specific visual direction;
- guide page layout, typography, color, components, and motion;
- prevent inconsistent mixing of unrelated historical styles;
- give designers and AI agents explicit implementation rules;
- maintain modern accessibility and responsive behavior.

---

## 2. Core definitions

### Vintage

A style that appears genuinely old, collected, printed, worn, archival, or inherited. It often references real historical objects and production methods.

Typical signals:

- aged paper;
- faded pigments;
- letterpress or screen-print imperfections;
- engraving and etching;
- ornamental frames;
- old editorial layouts;
- period-specific typography;
- restrained, timeworn surfaces.

### Retro

A contemporary reinterpretation of an earlier visual era. Retro may be brighter, cleaner, more playful, or deliberately exaggerated.

Typical signals:

- bold period palettes;
- geometric shapes;
- nostalgic display typography;
- simplified illustrations;
- old technology references;
- decorative patterns;
- stylized rather than realistically aged surfaces.

### Retro-futurism

A historical vision of the future, such as space-age 1950s graphics, 1980s computer interfaces, chrome typography, neon grids, or analog science-fiction imagery.

### Rule

Do not use “retro” as a random collection of old-looking effects. Select a defined historical direction and build a coherent system around it.

---

## 3. Select an era before designing

A retro or vintage site should be based on one primary era. A secondary influence may be added only when the relationship is deliberate.

| Era or movement | Common visual characteristics |
|---|---|
| 1880s–1910s / Victorian | Decorative borders, engraved illustrations, serif and ornamental lettering, dense composition, labels, flourishes |
| 1890s–1910s / Art Nouveau | Organic curves, botanical motifs, asymmetry, decorative display lettering, muted natural colors |
| 1920s–1930s / Art Deco | Symmetry, stepped geometry, metallic accents, high contrast, tall display type, luxury and precision |
| 1930s–1950s / Industrial print | Utility labels, stamps, condensed type, limited inks, diagrams, catalog structures |
| 1940s–1960s / Mid-century | Bold geometry, simple palettes, collage, flat illustration, clean sans-serif type, optimistic composition |
| 1950s / Diner and advertising | Script lettering, badges, cream/red/aqua palettes, chrome, checker patterns, product illustration |
| 1960s / Mod and psychedelic | Optical patterns, rounded forms, saturated color, warped lettering, poster-like composition |
| 1970s | Warm earth colors, chunky serif type, rounded geometry, stripes, sunbursts, handmade graphics |
| 1980s | Neon, black backgrounds, grids, chrome, gradients, Memphis geometry, arcade and synth references |
| 1990s print / grunge | Photocopy texture, distressed type, collage, rough alignment, zines, high-energy contrast |
| Early web / 1990s–2000s | System fonts, browser chrome, pixel graphics, beveled controls, tiled backgrounds, visible interface metaphors |

### Era selection rule

Before producing a design, document:

1. primary era;
2. secondary influence, if any;
3. emotional objective;
4. historical references;
5. modern constraints;
6. elements that must not be used.

Example:

```text
Primary era: 1970s editorial advertising
Secondary influence: mid-century product catalogs
Mood: warm, tactile, optimistic
Avoid: neon, chrome, pixel art, Victorian ornament
Modern constraints: WCAG 2.2 AA, mobile-first, fast loading
```

---

## 4. Design principles

### 4.1 Authenticity over decoration

Use a small number of historically credible signals repeatedly. One coherent palette, type system, border language, and texture treatment is stronger than many unrelated effects.

### 4.2 Modern structure, historical surface

Build the underlying experience with modern standards:

- semantic HTML;
- responsive grids;
- clear hierarchy;
- predictable navigation;
- accessible controls;
- scalable typography;
- optimized assets.

Apply retro character through:

- typography;
- color;
- borders;
- textures;
- illustration;
- icon treatment;
- labels;
- composition;
- controlled motion.

### 4.3 Controlled imperfection

Imperfection should look intentional.

Allowed:

- slightly uneven print texture;
- subtle registration offset;
- mild distress;
- paper grain;
- irregular border details;
- imperfect halftone coverage.

Avoid:

- random distortion on every component;
- damage that reduces readability;
- fake aging applied uniformly;
- low-resolution text;
- excessive visual noise.

### 4.4 Hierarchy before nostalgia

A user should understand the page before noticing the historical styling.

The hierarchy should clearly distinguish:

1. page purpose;
2. primary action;
3. section structure;
4. supporting information;
5. decorative material.

### 4.5 One dominant visual idea

Each page should have one dominant retro concept, such as:

- a magazine spread;
- a product catalog;
- a cinema poster;
- an archive card system;
- a diner menu;
- a terminal interface;
- a record sleeve;
- a travel brochure.

Do not make every section imitate a different artifact.

---

## 5. Color system

## 5.1 General color characteristics

Retro and vintage palettes commonly use:

- muted pigments;
- warm off-whites instead of pure white;
- ink-like dark colors instead of pure black;
- limited spot-color logic;
- complementary accent colors;
- era-specific saturation;
- faded or slightly yellowed neutrals.

Pure white and pure black may be used, but they often create a more contemporary result.

## 5.2 Era-based palette directions

### Victorian and archival

- parchment;
- sepia;
- oxblood;
- forest green;
- navy;
- charcoal;
- antique gold.

### Art Deco

- black;
- ivory;
- emerald;
- burgundy;
- cobalt;
- brass or gold;
- silver-gray.

### Mid-century

- mustard;
- tomato red;
- teal;
- cream;
- olive;
- burnt orange;
- dark brown.

### 1970s

- avocado;
- rust;
- ochre;
- chocolate;
- tan;
- warm cream;
- dusty blue.

### 1980s

- black;
- electric cyan;
- magenta;
- violet;
- acid green;
- chrome gray;
- deep navy.

### 1990s grunge

- dirty white;
- black;
- faded red;
- army green;
- photocopy gray;
- washed purple;
- industrial yellow.

## 5.3 Palette construction

Use a controlled palette:

```text
1 background family
1 ink/text family
1 primary accent
1 secondary accent
1 optional signal color
```

Recommended distribution:

- 60–75% background and neutral surfaces;
- 15–25% text, borders, and structural color;
- 5–15% primary accent;
- less than 5% signal or highlight color.

## 5.4 Color rules

- Use color to communicate hierarchy, not only atmosphere.
- Preserve sufficient contrast even when colors are faded.
- Do not place distressed textures directly behind small text.
- Do not rely on color alone for state, errors, selection, or status.
- Metallic colors should normally be represented as flat color or restrained gradients, not noisy fake foil everywhere.
- Neon palettes need dark neutral space to avoid visual fatigue.
- Test color combinations in normal, hover, focus, active, disabled, and visited states.

## 5.5 Accessibility requirement

For WCAG 2.2 Level AA:

- normal text should reach at least 4.5:1 contrast;
- large text should reach at least 3:1;
- meaningful UI boundaries and focus indicators should remain visible;
- text should normally remain real HTML text rather than text embedded in images.

---

## 6. Typography

## 6.1 Typography roles

Use no more than three primary type roles:

1. **Display** — headings, hero statements, posters, labels;
2. **Body** — paragraphs, navigation, forms, long reading;
3. **Utility or accent** — metadata, captions, dates, stamps, code-like labels.

A two-family system is usually sufficient.

## 6.2 Typeface categories

### Serif

Appropriate for:

- editorial vintage;
- newspapers;
- book-inspired layouts;
- Victorian or archival work;
- traditional luxury;
- 1970s display design.

Useful characteristics:

- old-style serifs;
- slab serifs;
- high-contrast Didone forms;
- soft, rounded serifs;
- condensed editorial serifs.

### Sans serif

Appropriate for:

- industrial labels;
- Swiss and mid-century design;
- transport graphics;
- 1980s modernism;
- catalog and technical layouts.

Useful characteristics:

- grotesque sans;
- geometric sans;
- humanist sans;
- condensed sans;
- wide display sans.

### Script and sign-painter styles

Appropriate for:

- diner aesthetics;
- packaging;
- badges;
- automotive or leisure themes;
- 1940s–1960s advertising.

Use sparingly. Never use decorative script for long paragraphs, form labels, or dense navigation.

### Monospace and pixel type

Appropriate for:

- terminals;
- early computing;
- receipts;
- typewriters;
- technical documentation;
- early-web references.

Use a readable modern monospace for body-sized text. Pixel fonts should usually be limited to large labels or decorative headings.

### Decorative display type

Use for short, high-impact text only. It must not become the default interface font.

## 6.3 Pairing principles

Good pairing usually comes from contrast:

- expressive serif + neutral sans;
- condensed display + humanist body;
- geometric sans + warm serif;
- script accent + sturdy sans;
- pixel display + readable monospace or sans.

Avoid pairing two highly decorative families that compete for attention.

## 6.4 Type scale

Use a clear scale rather than arbitrary sizes.

Example fluid scale:

```css
--text-xs: clamp(0.75rem, 0.72rem + 0.12vw, 0.82rem);
--text-sm: clamp(0.875rem, 0.84rem + 0.16vw, 0.96rem);
--text-base: clamp(1rem, 0.96rem + 0.2vw, 1.125rem);
--text-lg: clamp(1.2rem, 1.1rem + 0.45vw, 1.5rem);
--text-xl: clamp(1.5rem, 1.28rem + 1vw, 2.15rem);
--text-2xl: clamp(2rem, 1.55rem + 2vw, 3.4rem);
--text-3xl: clamp(2.8rem, 1.9rem + 4vw, 5.8rem);
```

## 6.5 Typographic rules

- Body text should normally be at least `1rem`.
- Use relative units such as `rem`, `em`, and `clamp()`.
- Body line height should usually fall between `1.45` and `1.75`.
- Headlines may use tighter line height, typically `0.9` to `1.15`.
- Keep long text lines near 45–75 characters.
- Avoid excessive all-caps in long text.
- Increase letter spacing carefully for small uppercase labels.
- Do not apply strong distress effects to live body text.
- Use fallback fonts with similar proportions.
- Limit downloaded weights and styles.
- Prefer variable fonts where they reduce file count without harming rendering.

---

## 7. Layout and composition

## 7.1 Grid philosophy

Retro design may appear irregular, but it should still be based on a grid.

Possible structures:

- editorial columns;
- poster grid;
- modular card system;
- catalog rows;
- asymmetric mid-century composition;
- centered Art Deco symmetry;
- dense zine collage;
- early-web window or panel layout.

## 7.2 Recommended layout model

Use a modern container and intentional internal grid.

```css
.page-shell {
  width: min(100% - 2rem, 80rem);
  margin-inline: auto;
}

.section-grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: clamp(1rem, 2vw, 2rem);
}
```

The visual style may break the grid selectively, but navigation, reading order, and controls should remain predictable.

## 7.3 Composition techniques

- oversized title typography;
- framed sections;
- inset labels;
- side notes;
- captions and folio numbers;
- overlapping image and type;
- visible rules and dividers;
- stamps and badges;
- radial bursts;
- geometric crop shapes;
- catalog numbering;
- ornamental corners;
- asymmetric negative space;
- controlled collage.

## 7.4 Density

Choose one density model:

### Editorial

Moderate density, strong columns, long-form reading, visible captions.

### Poster

Low information density, oversized type, bold image, one primary action.

### Catalog

High structure, repeated modules, labels, prices, specifications, comparison.

### Zine or grunge

High visual density, overlapping material, rough texture, intentionally broken alignment.

### Early interface

Compact spacing, panels, tabs, toolbars, status indicators, system-like controls.

Do not mix all density models on one page.

## 7.5 Spacing

Even vintage-inspired layouts require a consistent spacing scale.

```css
--space-1: 0.25rem;
--space-2: 0.5rem;
--space-3: 0.75rem;
--space-4: 1rem;
--space-6: 1.5rem;
--space-8: 2rem;
--space-12: 3rem;
--space-16: 4rem;
--space-24: 6rem;
```

Use decorative overlap as an exception, not as the spacing system itself.

---

## 8. Surfaces, borders, and texture

## 8.1 Surface vocabulary

Appropriate surface references include:

- paper;
- cardboard;
- painted metal;
- enamel;
- fabric;
- vinyl;
- newsprint;
- photocopy;
- CRT glass;
- old plastic;
- wood;
- screen print;
- letterpress.

Select one or two dominant material references.

## 8.2 Texture rules

Texture should:

- support the selected era;
- be subtle beneath text;
- scale correctly on high-density screens;
- avoid visible tiling;
- not significantly increase page weight;
- not interfere with controls;
- be reduced or removed in high-contrast modes where needed.

Preferred implementation:

- lightweight compressed raster overlay;
- CSS gradients for simple grain or pattern;
- SVG for repeatable line patterns;
- pseudo-elements with low opacity;
- separate texture layer rather than baking texture into every asset.

## 8.3 Borders

Possible border languages:

- thin editorial rules;
- thick screen-print frames;
- double-line Art Deco borders;
- hand-drawn outlines;
- ticket perforations;
- dotted receipt rules;
- beveled early-web panels;
- ornamental corners.

Use one primary border language across the product.

## 8.4 Shadows

Retro shadow styles may include:

- hard offset print shadow;
- long geometric shadow;
- subtle paper lift;
- inset panel shadow;
- neon glow;
- beveled interface highlight.

Avoid mixing soft modern SaaS shadows with strong print-style offset shadows unless deliberately contrasted.

---

## 9. Components

## 9.1 Buttons

Buttons may resemble:

- printed labels;
- tickets;
- enamel signs;
- hardware controls;
- arcade buttons;
- underlined editorial links;
- early GUI buttons.

Requirements:

- obvious clickable state;
- minimum practical touch target;
- clear hover and focus states;
- visible disabled state;
- text label, not icon alone for critical actions;
- no texture that obscures the label.

## 9.2 Cards

Possible card concepts:

- archive card;
- catalog item;
- matchbox label;
- record sleeve;
- newspaper clipping;
- polaroid;
- ticket;
- terminal panel.

Each card family should have consistent:

- padding;
- border;
- media ratio;
- heading position;
- metadata treatment;
- interaction behavior.

## 9.3 Navigation

Retro styling must not reduce discoverability.

Recommended:

- clearly named primary links;
- visible current-page state;
- restrained decorative separators;
- mobile navigation with real controls;
- keyboard-accessible menus;
- no hidden navigation solely for aesthetic reasons.

## 9.4 Forms

Forms may use vintage labels, rules, stamps, or panel treatments, but must include:

- persistent labels;
- instructions outside placeholders;
- visible focus;
- accessible error messages;
- sufficient control size;
- semantic grouping;
- clear required/optional status;
- readable entered values.

## 9.5 Tables and data

Suitable historical references:

- ledgers;
- inventory sheets;
- timetables;
- receipts;
- technical manuals;
- product catalogs.

Preserve real table semantics and mobile readability.

---

## 10. Iconography and illustration

Icon styles may include:

- engraving;
- line art;
- simplified geometric symbols;
- hand-painted sign icons;
- pixel icons;
- technical diagrams;
- pictograms;
- rubber stamps;
- mid-century flat illustration.

Rules:

- use one icon family;
- match stroke weight to borders and type;
- do not mix detailed engraving with minimal line icons;
- keep functional icons recognizable;
- include text labels where ambiguity is possible;
- avoid decorative icons in place of semantic HTML.

---

## 11. Motion and interaction

## 11.1 Appropriate motion concepts

- film flicker;
- mechanical slide;
- page turn;
- marquee movement;
- CRT scan;
- stamp impact;
- carousel rotation;
- analog dial;
- typewriter reveal;
- poster layer shift.

## 11.2 Motion rules

- Motion should explain state or reinforce the selected era.
- Avoid constant background movement.
- Avoid simulated damage or flicker that impairs reading.
- Keep interaction response immediate.
- Do not delay navigation for decorative transitions.
- Support `prefers-reduced-motion`.
- Allow users to pause moving or auto-updating content where required.
- Never rely on animation alone to communicate status.

Example:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 12. Responsive behavior

Do not treat the desktop composition as a poster that is merely scaled down.

### Desktop

- complex editorial grids;
- overlap and side notes;
- wider decorative frames;
- multi-column storytelling;
- larger background motifs.

### Tablet

- reduce overlap;
- simplify secondary ornament;
- preserve hierarchy;
- keep two-column structures only when readable.

### Mobile

- use a clear single-column reading order;
- turn side notes into inline metadata;
- crop images intentionally;
- reduce or remove nonessential textures;
- keep decorative type within the viewport;
- preserve comfortable touch targets;
- avoid horizontal scrolling except for intentional data regions.

Responsive decisions should preserve the concept, not every desktop detail.

---

## 13. Accessibility and usability

Historical appearance must never be used as justification for poor accessibility.

Required:

- semantic landmarks and heading order;
- full keyboard navigation;
- visible focus;
- sufficient contrast;
- text resizing without loss of content;
- responsive reflow;
- descriptive alternative text;
- captions where needed;
- accessible form errors;
- no critical text embedded only in images;
- no color-only state communication;
- reduced-motion support;
- readable link states;
- logical DOM order despite visual overlap.

### Early-web exception

A site may visually imitate early web design, but it should not recreate inaccessible HTML practices such as:

- layout tables;
- blinking text;
- inaccessible image maps;
- autoplay audio;
- tiny fixed fonts;
- keyboard traps;
- unlabeled frames;
- text stored as raster images.

---

## 14. Performance

Retro design frequently relies on images, fonts, and textures, so asset discipline is essential.

### Rules

- use modern image formats where appropriate;
- serve responsive image sizes;
- specify image width and height;
- lazy-load below-the-fold media;
- preload only critical assets;
- subset fonts;
- load only required font weights;
- avoid large looping GIFs;
- use CSS or SVG for simple patterns;
- compress grain and texture overlays;
- reserve layout space to prevent shift;
- test on slow mobile connections.

A vintage page may look heavy while remaining technically lightweight.

---

## 15. Design tokens

Example neutral token structure:

```css
:root {
  /* Colors should be replaced by the selected era palette */
  --color-paper: #f0e4c8;
  --color-ink: #211d18;
  --color-muted-ink: #5f5548;
  --color-accent: #a6432f;
  --color-accent-2: #2f6b68;
  --color-line: color-mix(in srgb, var(--color-ink) 45%, transparent);

  --font-display: "Chosen Display", serif;
  --font-body: "Chosen Body", sans-serif;
  --font-utility: "Chosen Utility", monospace;

  --radius-none: 0;
  --radius-small: 0.2rem;
  --border-thin: 1px;
  --border-heavy: 3px;

  --shadow-print: 0.35rem 0.35rem 0 var(--color-ink);
  --shadow-paper: 0 0.5rem 1.5rem rgb(0 0 0 / 0.14);

  --content-width: 76rem;
  --reading-width: 68ch;
}
```

These values are examples, not a universal palette.

---

## 16. Era-specific implementation recipes

## 16.1 Mid-century editorial

- geometric sans display;
- readable serif or humanist sans body;
- cream background;
- two or three bold spot colors;
- flat shapes;
- strong image crops;
- asymmetric 6- or 12-column grid;
- minimal texture;
- hard-edged dividers.

## 16.2 1970s commercial

- warm cream and brown base;
- rust, mustard, avocado, or dusty blue accents;
- rounded or chunky display serif;
- stripes and sunburst motifs;
- product photography with warm cast;
- soft corners used selectively;
- large decorative headlines.

## 16.3 Art Deco luxury

- symmetrical grid;
- black or deep jewel-tone background;
- ivory text;
- brass or gold accent;
- thin geometric borders;
- tall display type;
- restrained ornament;
- centered composition;
- controlled animation.

## 16.4 1980s digital

- dark base;
- cyan, magenta, violet, or acid accents;
- grid or scan-line motifs;
- geometric sans or techno display;
- chrome used sparingly;
- strong contrast;
- panel-based layout;
- brief glow effects;
- no uncontrolled neon haze behind body text.

## 16.5 1990s grunge and zine

- black, dirty white, faded spot colors;
- photocopy imagery;
- condensed or distressed display;
- neutral body font;
- collage and torn-edge masks;
- rough alignment within a hidden grid;
- highly controlled texture;
- simple, reliable navigation.

## 16.6 Early-web revival

- system or bitmap-inspired type;
- visible panels, status bars, tabs, and underlined links;
- tiled or patterned surfaces;
- small pixel icons;
- playful browser metaphors;
- modern semantic markup underneath;
- accessible text size and contrast;
- responsive behavior replacing fixed-width historical limitations.

---

## 17. Common failures

Avoid:

- combining Victorian ornament, 1980s neon, and 1990s grunge without a clear concept;
- adding grain to every surface;
- making all text distressed;
- using script for body copy;
- replacing buttons with ambiguous decoration;
- embedding important text in poster images;
- sacrificing contrast for a faded look;
- using fixed desktop dimensions;
- loading many decorative fonts;
- reproducing obsolete usability problems;
- confusing “vintage” with brown filters alone;
- treating random aging as historical authenticity;
- overusing badges, ribbons, stamps, and starbursts;
- making every section visually compete with the hero.

---

## 18. AI-agent design instructions

When an AI agent creates a retro or vintage website, it must:

1. identify the selected historical era;
2. state the design concept in one sentence;
3. choose a limited color system;
4. define display, body, and optional utility typography;
5. establish a responsive grid;
6. select one border and texture language;
7. define component states;
8. preserve WCAG 2.2 AA requirements;
9. use real HTML text for meaningful content;
10. optimize fonts and images;
11. support reduced motion;
12. document what is intentionally excluded.

The agent must not:

- invent brand colors unless requested;
- combine unrelated eras by default;
- use decorative fonts for long reading;
- use texture as a substitute for composition;
- produce desktop-only layouts;
- imitate inaccessible historical web practices;
- apply random distress effects;
- create visual complexity without clear hierarchy.

---

## 19. Production checklist

### Direction

- [ ] Primary era selected
- [ ] Historical references documented
- [ ] Mood and audience defined
- [ ] Excluded styles listed
- [ ] One dominant visual concept selected

### Visual system

- [ ] Limited palette defined
- [ ] Text contrast tested
- [ ] Type roles defined
- [ ] Grid defined
- [ ] Spacing scale defined
- [ ] Border language defined
- [ ] Texture strategy defined
- [ ] Icon or illustration family defined

### Components

- [ ] Navigation is obvious
- [ ] Buttons have all states
- [ ] Forms have persistent labels
- [ ] Focus styles are visible
- [ ] Cards use consistent structure
- [ ] Tables remain usable on mobile

### Responsive design

- [ ] Mobile layout designed independently
- [ ] Decorative overlap simplified on small screens
- [ ] Text does not overflow
- [ ] Touch targets are usable
- [ ] Reading order remains logical

### Accessibility

- [ ] WCAG 2.2 AA contrast
- [ ] Keyboard navigation
- [ ] Correct heading hierarchy
- [ ] Alternative text
- [ ] Reduced motion
- [ ] Text can resize
- [ ] No essential image-only text
- [ ] Status is not color-only

### Performance

- [ ] Responsive images
- [ ] Correct image dimensions
- [ ] Modern compressed formats
- [ ] Font files minimized
- [ ] Below-the-fold media lazy-loaded
- [ ] Texture assets optimized
- [ ] Layout shift checked

---

## 20. Research basis

This guide synthesizes historical graphic-design conventions with modern web standards.

Key references:

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*: https://www.w3.org/TR/WCAG22/
- W3C, *How to Meet WCAG 2.2*: https://www.w3.org/WAI/WCAG22/quickref/
- web.dev, *Responsive Web Design Basics*: https://web.dev/articles/responsive-web-design-basics
- web.dev, *Typography*: https://web.dev/learn/design/typography
- web.dev, *Optimize Web Fonts*: https://web.dev/learn/performance/optimize-web-fonts
- MDN, *Variable Fonts*: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts
- LogRocket, *Retro UX design best practices*: https://blog.logrocket.com/ux-design/retro-ux-design-best-practices/
- Stuff & Nonsense, *What 90s web design can teach us today*: https://stuffandnonsense.co.uk/blog/retro-reboot-what-90s-web-design-can-teach-us-today/
- Tilda Education, *Popular Web Design Styles*: https://tilda.education/en/web-design-styles
- Awwwards, *Retro Website Examples*: https://www.awwwards.com/websites/retro/

---

## 21. Final rule

A successful retro or vintage website should feel historically informed at first glance and modern in use. The visitor may notice paper, type, color, ornament, or old-interface references, but navigation, reading, accessibility, responsiveness, and performance must behave like a well-built contemporary website.
