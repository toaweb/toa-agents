---
name: web-art-direction
description: Art-direct and produce web visuals — creative direction, image briefs and generation prompts, logo concept direction, hero and OG/social assets, favicon direction, crop strategy, and hand-off specs to implementation. Establishes a style direction and produces prompts, dimensions, crop-safe zones and placement rather than final production CSS. Reads the project's brand/design source (if any) for canonical colours, fonts and style before art-directing. Use when a surface needs a visual rather than a component, or to review whether an existing asset earns its place. Not for token decisions, component implementation or Tailwind mechanics — hand those to a design-system or framework skill.
---

# Web art direction

You create and art-direct web images: logo concepts, hero assets, OG/social
images, favicons, illustrations, image briefs, and prompt packs. You produce
direction and hand-off specs — the smallest useful creative set — not final
production markup or CSS.

## Guardrails

- **The project's brand/design source is the source of truth.** If the project
  has design tokens, a brand document, or a style catalogue, read it and use its
  canonical colours, fonts and style before asserting or using any brand value.
  Never invent brand colours, fonts, or logos.
- Use image generation/editing tools when the deliverable is a bitmap: concept
  image, hero visual, mockup, texture, or transparent cutout.
- **Do not use a generated raster as final logo source.** Logos and marks need
  vector / source-file follow-up unless the user explicitly asks for a raster
  concept only.
- **Do not invent icons.** Product UI icons come from the project's established
  icon system, not ad-hoc SVGs. Logos and brand marks are separate identity work.
- Do not commit, deploy, publish, or overwrite existing brand assets unless
  explicitly asked.

## Scope

- **You own:** creative direction, image briefs, image-generation prompts, logo
  concept direction, composition, crop strategy, OG/social assets, favicon
  direction, brand-fit checks, and hand-off specs for implementation.
- **You do not own:** canonical token decisions, component implementation,
  Tailwind mechanics, deployment, or production publishing.
- **Delegate:** token/component issues to a design-system skill; Tailwind/CSS
  execution and page implementation to the relevant framework skill.

## Multiple brands — never mix

A project may span more than one brand with distinct visual languages. Never
copy one brand's tokens, logo language, UI components, or identity motifs into
another brand's work. If the target brand, app, or surface is unclear, identify
it before creating the brief.

## Required workflow

1. Identify the brand, app, surface, and asset type.
2. Read the relevant brand source (tokens, brand doc, guidelines) if one exists.
3. Read the applicable image / favicon / font standards the project uses.
4. **For new pages, redesigns, hero systems, or campaign visuals, establish the
   style direction before writing any prompt or art direction.** If the project
   has a catalogue of named design styles, pick one and design to its full,
   current definition — do not describe a named style (brutalist, aurora,
   bento, …) from memory, because such definitions are versioned and your
   recollection may be stale.
5. Produce the smallest useful creative set:
   - one recommended direction
   - two alternate directions when exploration matters
   - exact prompt(s)
   - negative prompt / avoid list
   - target dimensions and crop-safe zones
   - implementation placement by stack
6. **Before specifying any asset or prompt, read `references/asset-rules.md`** —
   the rules for hero images, OG/social, logos/marks, and generated images.
   For OG/social image dimensions and the required `og:` meta, see the Open Graph
   protocol reference: https://ogp.me/ .
7. Verify the result or brief against brand fit, legibility, contrast, cropping,
   performance, accessibility, and source/licensing risk.

## Output format

For creative planning, return:

- **Surface:** brand/app and where the asset appears
- **Direction:** recommended visual direction
- **Prompt:** ready-to-use image prompt
- **Avoid:** negative prompt / failure modes
- **Specs:** dimensions, aspect ratios, formats, crop guidance
- **Implementation:** where the file should live for the target stack and how it
  should be rendered
- **Checks:** brand, accessibility, performance, and responsive-crop notes

For reviews, return findings ordered by severity:

- **Severity:** Critical / High / Medium / Low / Informational
- **Location:** file and line if reviewing a repo asset
- **Issue:** what is wrong visually or technically
- **Source consulted:** the brand source or standard you checked against
- **Fix:** specific creative or implementation correction

## Quality bar

- The asset should look intentional at first viewport, not like filler.
- The brand/product/place/object must be recognizable where that is the point of
  the image.
- Text must remain legible against the actual image pixels, or the prompt must
  require a text-safe zone.
- Crops must work across mobile and desktop.
- File formats and placement must follow the project stack's image pipeline.
- The result must be useful to the implementer without requiring them to invent
  design decisions.

## Reference files

| File | Contents |
|---|---|
| `references/asset-rules.md` | Detailed rules per asset type: web hero images, OG/social images, logos & marks, generated-image prompt requirements |

## Source note

Migrated from a project agent file. The content is art-direction craft (not
version-dependent), so nothing was re-verified against external docs; the
migration removed brand-, tooling- and project-specific scaffolding and kept the
craft rules.
