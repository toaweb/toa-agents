# Product UI Color System 2026

> Rules for accessible, semantic, adaptive color in product interfaces, dashboards, admin systems, and mobile applications.

## 1. Purpose

Color communicates hierarchy, action, state, grouping, selection, and data. It must never become the only carrier of meaning.

## 2. Semantic roles

Define separate roles for:

```text
canvas
surface
raised surface
overlay
text
icon
border
action
focus
selection
information
success
warning
error
disabled
data visualization
```

Do not use brand color for every active, selected, informational, and interactive state.

## 3. Surface hierarchy

Limit ordinary products to a small stack:

1. canvas;
2. base surface;
3. raised surface;
4. overlay.

Use spacing and borders before adding more similar gray surfaces.

## 4. Text hierarchy

Define strong, default, muted, placeholder, disabled, inverse, and link roles.

Muted text still needs sufficient contrast. Placeholder text must never replace a label.

## 5. Action colors

Primary action color should be scarce. Secondary and tertiary actions must remain recognizable without competing.

Define default, hover, active, focus, disabled, and loading states independently.

## 6. Focus

Focus must remain visible on every supported surface. Use a two-color or offset ring where a single color cannot maintain contrast.

## 7. Status

Each status needs at least two cues:

```text
color + text
color + icon
color + shape
```

Do not use red and green alone.

## 8. Dark mode

Dark mode is not inversion. Re-evaluate surface relationships, muted text, borders, shadows, focus, images, charts, disabled controls, code, and status colors.

Pure white on pure black can be harsh for long reading.

## 9. High contrast and forced colors

Test forced-colors and system high-contrast modes. Do not suppress system colors without a verified replacement. Focus, controls, and boundaries must remain perceivable.

## 10. Data visualization

Separate UI semantic colors from chart-series colors. Define categorical, sequential, and diverging palettes.

Charts also need direct labels, symbols or patterns, table equivalents, and clear selected/muted states.

## 11. Personalization

User-selected accents must pass contrast checks and must not change semantic status meaning.

## 12. Algorithmic palettes

A mathematical lightness scale is not automatically perceptually uniform or accessible. Validate generated palettes manually.

## 13. Testing

Test:

- light and dark;
- hover/focus/selected combinations;
- common color-vision deficiencies;
- grayscale;
- low-quality displays;
- forced colors;
- low brightness;
- dense charts.

## 14. Anti-patterns

Avoid gray-on-gray interfaces, pastel status systems, gradient text for critical content, transparent controls over media, color-only selection, and disabled states that disappear.

## 15. Agent rules

An AI agent must use semantic tokens, verify contrast, preserve non-color cues, and never infer status meaning from brand color.

## 16. Checklist

- [ ] Semantic roles
- [ ] Text hierarchy
- [ ] Action states
- [ ] Focus on every surface
- [ ] Status with non-color cues
- [ ] Dark mode
- [ ] Forced-colors testing
- [ ] Data palettes
- [ ] Media-overlay tests
- [ ] Manual contrast review


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

Validate all rules with the actual audience, platform, language, product risk, and regulatory context.

