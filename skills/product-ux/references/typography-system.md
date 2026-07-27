# Product UI Typography System 2026

> Rules for readable, scalable, multilingual, data-capable typography in product interfaces.

## 1. Purpose

Product typography must support repeated use, dense information, forms, navigation, tables, errors, code, and help content.

## 2. Roles

Define a limited role set:

```text
display
page title
section title
component title
body
label
metadata
data
code
```

Avoid size tokens without semantic roles.

## 3. Typeface requirements

The primary UI family should provide:

- clear small-size rendering;
- distinguishable `0/O`, `1/l/I`;
- tabular numerals;
- broad language support;
- useful punctuation and symbols;
- sufficient weights;
- stable metrics;
- readable italics.

## 4. Size and line height

Body/UI text usually remains in a 14–18px equivalent range, with long reading at 16px or higher.

Body line height generally falls between 1.45 and 1.7. Dense tables may be tighter without clipping.

## 5. Measure

Long-form text should usually remain near 45–75 characters per line. Settings pages and dialogs should not stretch prose across the viewport.

## 6. Numbers and units

Use tabular numerals for aligned data. Define locale-aware decimals, separators, dates, time, currency, percentages, negatives, and units.

Prevent numbers and units from breaking apart when this harms interpretation.

## 7. Labels

Labels should be persistent, concise, and sentence case by default. Uppercase is reserved for short technical metadata.

## 8. Hierarchy

Use size, weight, spacing, position, and color together. Do not rely on size alone.

## 9. Responsive typography

Use `clamp()` carefully. Test translation, browser zoom, user font scaling, split-screen, and narrow containers.

Components may adapt to their container rather than only the global viewport.

## 10. User text preferences

Support increased line, paragraph, letter, and word spacing. Avoid fixed-height labels and clipped headings.

## 11. Multilingual and bidirectional content

Test real scripts, shaping, line breaks, fallback, mirrored layout, numerals, and truncation.

## 12. Truncation

Do not truncate identity, status, errors, or actions. When unavoidable, provide the full value and preserve searchability.

## 13. Code and identifiers

Use monospace where alignment or character distinction adds value. Long IDs need wrapping, copying, or expansion.

## 14. Font performance

Use WOFF2, subsetting, metric-compatible fallback, and intentional `font-display`. Avoid large families that delay first content.

## 15. Anti-patterns

Avoid tiny metadata everywhere, thin weights, placeholder-only labels, centered long-form text, fixed-height text, all-caps paragraphs, and decorative fonts in forms.

## 16. Agent rules

An AI agent must use established roles, respect localization, avoid hardcoded sizes when tokens exist, and test wrapping in every state.

## 17. Checklist

- [ ] Type roles
- [ ] Font licensing
- [ ] Language coverage
- [ ] Numeral behavior
- [ ] Responsive scale
- [ ] Text-spacing tolerance
- [ ] Truncation policy
- [ ] Fallback metrics
- [ ] Zoom/reflow
- [ ] Code/data styles


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

