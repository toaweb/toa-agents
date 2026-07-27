# Product UI Spacing, Layout & Adaptive Design 2026

> Rules for spatial systems, application shells, pane layouts, responsive behavior, density, and cross-device adaptation.

## 1. Purpose

Layout must help users understand hierarchy, preserve context, and complete tasks across resizable windows, touch devices, split-screen, zoom, and different input modes.

## 2. Spacing scale

Use a small base scale, commonly 4px with 8px as the major rhythm.

Define semantic spacing for:

- control inset;
- component gap;
- form row;
- section;
- page gutter;
- pane gap;
- touch separation.

Do not patch screens with arbitrary values.

## 3. Density

Support comfortable, default, and compact modes where useful. Density changes spacing and row height, not information meaning.

Compact mode must preserve focus, pointer targets, and legibility.

## 4. Application shell

Define stable areas:

```text
global navigation
workspace navigation
page header
local toolbar
main workspace
contextual panel
system feedback
```

Do not move global actions between pages.

## 5. Canonical layouts

Useful patterns include:

- list-detail;
- supporting pane;
- feed;
- dashboard;
- focused form;
- canvas;
- comparison;
- settings.

Select based on task, not visual novelty.

## 6. Adaptive classes

Use compact, medium, expanded, and large classes based on available space. Do not treat “mobile” as one device category.

## 7. Recomposition

Responsive design may change navigation container, pane visibility, table representation, action placement, filters, image crop, spacing, and density.

It must not change meaning, permissions, or workflow state.

## 8. Mobile

Prioritize the main task. Replace multi-pane layouts with navigable screens while preserving back context, selection, filters, and unsaved work.

## 9. Touch and pointer

Provide practical targets and spacing. Hover information needs focus and touch alternatives.

## 10. Safe areas and system UI

Respect notches, home indicators, virtual keyboards, browser chrome, and orientation.

## 11. Zoom and reflow

At zoom, avoid two-dimensional scrolling for normal reading. Fixed headers and footers must not consume short viewports.

## 12. Container queries

Use container queries for reusable components whose layout depends on actual pane or card width.

## 13. Empty space

Whitespace communicates grouping. Excessive emptiness in operational products can hide relationships and increase scrolling.

## 14. Anti-patterns

Avoid desktop layouts merely scaled down, fixed viewport heights, uncontrolled sticky panels, nested scrolling, hidden actions, and device-specific hardcoded breakpoints.

## 15. Agent rules

An AI agent must identify task and available space, define adaptive transformations, preserve DOM order, and specify compact alternatives for tables, forms, and multi-pane views.

## 16. Checklist

- [ ] Spacing scale
- [ ] Density modes
- [ ] Shell regions
- [ ] Canonical layout
- [ ] Adaptive classes
- [ ] Mobile recomposition
- [ ] Touch/pointer
- [ ] Safe areas
- [ ] Zoom/short viewport
- [ ] Container queries


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

