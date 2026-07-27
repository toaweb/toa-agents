# Product UI Motion & Iconography 2026

> Shared rules for motion, transition, feedback, icons, symbols, and visual cues.

## 1. Motion purpose

Motion may communicate:

- state change;
- hierarchy;
- spatial relationship;
- progress;
- feedback;
- continuity;
- attention.

Do not animate merely to make the product feel modern.

## 2. Motion categories

Define tokens for:

```text
instant feedback
small transition
navigation transition
content reveal
progress
ambient motion
```

Control interactions should feel immediate. Spatial changes may use slightly longer durations.

## 3. Easing

Use a small set of easing functions. Entrances, exits, and direct manipulation may need different curves, but each component should not invent its own physics.

## 4. Distance and scale

Keep routine movement small. Large translations and zooms can cause disorientation and motion sensitivity.

## 5. Reduced motion

Design intentional alternatives:

```text
slide → immediate state or fade
parallax → static layers
auto-play → poster and play control
morph → discrete state change
```

Reduced motion must preserve content and function.

## 6. Pause, stop, and hide

Provide controls for qualifying moving, blinking, scrolling, or auto-updating content. Avoid continuous ambient motion near reading.

## 7. Loading and progress

Use:

- progress bar for measurable work;
- spinner for short localized work;
- skeleton where structure is known;
- background job status for long work.

Do not show fake progress or indefinite loading without recovery.

## 8. Motion performance

Prefer transform and opacity. Use care with blur, filters, layout-changing properties, many fixed layers, and continuous scroll listeners.

Pause offscreen animation.

## 9. Icon purpose

Icons support recognition, orientation, and compactness. They should not replace clear text for unfamiliar actions.

## 10. Icon system

Define:

```text
grid
stroke or fill
caps and joins
corner treatment
optical alignment
sizes
minimum rendered size
mirroring
status semantics
```

## 11. Functional icons

Use familiar symbols for search, close, menu, download, filter, sort, expand, and navigation.

Pair ambiguous icons with labels.

## 12. Accessible icons

Functional icon controls need accessible names. Decorative icons should be hidden from assistive technology.

A tooltip alone is not the accessible name.

## 13. Status and official symbols

Status icons require labels and stable meanings.

Use official safety, regulatory, and platform symbols accurately. Do not redraw them casually or use them decoratively.

## 14. Directionality

Mirror directional icons for RTL where appropriate. Do not mirror culturally stable, brand-specific, or media-control symbols automatically.

## 15. Icon containers

Use no container by default. Add a container only for grouping, selection, touch target, or identity.

Avoid icons in colored circles as the universal feature-card formula.

## 16. Anti-patterns

Avoid bouncing controls, long exit animations, animated focus rings, mixed icon packs, ambiguous sparkles, decorative official symbols, and motion that masks latency.

## 17. Agent rules

An AI agent must state motion purpose, reduced-motion behavior, icon label requirements, and avoid adding a new symbol when text is clearer.

## 18. Checklist

- [ ] Motion purpose
- [ ] Duration/easing tokens
- [ ] Distance/scale limits
- [ ] Reduced-motion variant
- [ ] Pause/stop
- [ ] Loading/recovery
- [ ] Icon grid
- [ ] Accessible names
- [ ] RTL behavior
- [ ] Status labels
- [ ] Official-symbol review


## Research basis

Primary references:

- W3C, Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- GOV.UK Design System: https://design-system.service.gov.uk/
- U.S. Web Design System: https://designsystem.digital.gov/
- IBM Carbon Design System: https://carbondesignsystem.com/
- Material Design 3: https://m3.material.io/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines
- Atlassian Design System: https://atlassian.design/
- GitHub Primer: https://primer.style/
- Adobe Spectrum: https://spectrum.adobe.com/
- Shopify Polaris: https://polaris.shopify.com/

