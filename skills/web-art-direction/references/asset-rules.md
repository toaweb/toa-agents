# Asset rules — web visuals

Craft rules per asset type. Brand-neutral: apply the project's own brand source
on top of these.

## Web hero images

- Design for responsive cropping first: desktop wide, tablet, and mobile portrait.
  Specify a crop-safe zone that survives all three.
- Keep the subject away from critical text overlays unless a deliberate scrim or
  a separate text-safe area is specified.
- Specify **LCP intent** when the image is the first visible image on the page —
  it is likely the Largest Contentful Paint element and must be prioritised and
  correctly sized.
- Prefer real product / place / object / state where inspection matters; avoid
  generic atmospheric art that says nothing.
- Provide meaningful `alt` text for informative images and `alt=""` for purely
  decorative ones.

## OG and social images

- Produce a clear **1200×630** composition unless the project has a stricter
  local requirement. (1200×630 is the standard Open Graph size.)
- Keep core text and marks inside a central safe area — platforms crop edges
  differently.
- Use fewer words than a hero; social thumbnails are scanned at small sizes.
- Treat these as metadata assets, exported separately from in-page content
  images — their text/alt policy is different from content-image alt policy.

## Logos and marks

- Start with concept directions and vector-ready structure: geometry, wordmark
  treatment, spacing, monochrome viability, and small-size behaviour.
- Test the mark in one-colour, reversed, and favicon-scale contexts before
  committing to it.
- **Do not finalise a logo as a raster-only image** — a mark needs a vector /
  source file.
- For favicons, follow the project's monogram / small-icon system unless the
  user asks for a brand exception. Verify the mark stays legible at 16–32px.

## Generated images

- A prompt must specify: **subject, composition, medium, lighting, palette
  relationship, crop, aspect ratio, and an avoid list.** A prompt missing any of
  these will drift.
- Avoid generated text inside images unless the tool is explicitly reliable for
  typography; add text in code / design tools instead, where it stays crisp and
  editable.
- Avoid photoreal people unless the user requested it and rights/privacy are clear.
- Do not imply generated images are real photos, screenshots, or official
  product art. Label concept renders as such.
- State source/licensing risk for any reference or generated asset before hand-off.
