# Flat & Elevated Product UI Treatment 2026

> A visual-treatment guide for authenticated application interfaces.

## 1. Purpose

Flat UI reduces ornamental depth and emphasizes typography, color, spacing, borders, and direct interaction.

Elevated UI adds depth selectively to communicate overlapping or temporary layers.

The strongest product interfaces typically combine both.

## 2. Flat UI strengths

Flat UI supports:

- dense tables;
- toolbars;
- navigation;
- settings;
- enterprise workflows;
- fast scanning;
- consistent responsive behavior.

## 3. Flat UI risks

Purely flat design can weaken affordance when buttons, labels, text, and selectable rows appear too similar.

Use:

- clear control shapes;
- state changes;
- borders;
- underlines;
- icons;
- placement;
- focus.

## 4. Elevated UI strengths

Elevation helps distinguish:

- menus;
- flyouts;
- dialogs;
- drag previews;
- transient panels;
- sticky content crossing a surface.

## 5. Elevated UI risks

Excessive elevation creates:

- card clutter;
- false importance;
- unclear hierarchy;
- visual noise;
- poor dark-mode behavior.

## 6. Recommended combination

```text
Base workspace: flat
Forms: bordered or tonal
Cards: outlined/filled when bounded
Menus/dialogs: elevated
Selected row: tonal + marker
Drag state: elevated
```

## 7. Cards

Material 3 distinguishes elevated, filled, and outlined cards. Use the type that reflects actual grouping and hierarchy.

Do not use cards for every paragraph or table region.

## 8. Actions

Primary buttons may be filled. Secondary actions may be outlined or textual. Dense toolbars may use flat icon buttons with labels or tooltips.

## 9. Navigation

Use tonal selected states, marker lines, or filled navigation items. Do not rely only on shadow.

## 10. Forms

Inputs need visible boundaries. A flat field with only a placeholder is not acceptable.

## 11. Dark mode

Replace weak shadows with tone and border. Verify that raised surfaces remain distinguishable.

## 12. Accessibility

Affordance must remain clear in keyboard focus, forced colors, and touch contexts.

## 13. Anti-patterns

Avoid invisible links, text-only destructive actions without distinction, every object in an elevated card, and shadow as the only separation cue.

## 14. Agent rules

An AI agent should use flat structure by default, add elevation only for real overlap or temporary hierarchy, and preserve explicit interaction cues.

## 15. Checklist

- [ ] Flat base
- [ ] Clear affordance
- [ ] Elevation purpose
- [ ] Card type justified
- [ ] Form boundaries
- [ ] Selected/focus states
- [ ] Dark-mode treatment
- [ ] Forced-colors behavior


## Research basis

Primary and current references:

- W3C, Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- Apple Human Interface Guidelines, Dark Mode: https://developer.apple.com/design/human-interface-guidelines/dark-mode
- Apple Human Interface Guidelines, Materials: https://developer.apple.com/design/human-interface-guidelines/materials
- Material Design 3, Elevation: https://m3.material.io/styles/elevation
- Material Design 3, Color Roles: https://m3.material.io/styles/color/roles
- Microsoft Fluent, Acrylic: https://learn.microsoft.com/en-us/windows/apps/design/style/acrylic
- Microsoft Fluent, Mica: https://learn.microsoft.com/en-us/windows/apps/design/style/mica
- Microsoft Fluent, Materials: https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/materials
- IBM Carbon Design System: https://carbondesignsystem.com/

