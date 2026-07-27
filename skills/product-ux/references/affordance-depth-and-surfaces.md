# Affordance, Depth & Surface System 2026

> A foundation for authenticated product interfaces, admin panels, user portals, control panels, dashboards, and SaaS applications.

## 1. Purpose

Affordance communicates what can be interacted with and what action is possible. Depth and surfaces communicate grouping, hierarchy, layering, selection, interruption, and spatial relationship.

A product UI should never require users to guess whether an element is:

- clickable;
- editable;
- draggable;
- selected;
- disabled;
- floating;
- temporary;
- behind another layer.

## 2. Surface hierarchy

Use a small, deliberate surface model:

```text
Canvas
Primary workspace
Secondary pane
Raised panel
Transient surface
Modal overlay
```

Most product screens need no more than four visible surface levels.

## 3. Affordance cues

Interactive elements may use:

- shape;
- border;
- fill;
- shadow;
- label;
- icon;
- cursor;
- placement;
- motion;
- state change.

Use multiple cues for unfamiliar or high-risk controls.

## 4. Flat, bordered, and elevated controls

### Flat

Suitable for familiar navigation, text actions, toolbars, and dense environments.

Flat controls need clear labels, spacing, hover, focus, active, and selected states.

### Bordered

Suitable for forms, secondary actions, grouped data, technical panels, and operational interfaces.

Borders should be strong enough to identify control boundaries.

### Elevated

Suitable for temporary surfaces, menus, dialogs, drag state, and selected objects that overlap other content.

Do not use elevation for every card.

## 5. Elevation semantics

Elevation should represent a relationship, not prestige.

Typical elevation order:

```text
Base content
Sticky or selected surface
Menu/flyout
Dialog
Critical interruption
```

Material Design defines elevation as z-axis distance. Fluent materials similarly use depth and material to distinguish long-lived and transient surfaces.

## 6. Shadows

Shadows should be:

- consistent with one virtual light source;
- subtle at low elevation;
- stronger only for real overlap;
- tested in dark mode;
- replaced or supported by borders in high-contrast contexts.

Avoid shadow-only boundaries.

## 7. Tonal surfaces

Modern UI systems increasingly use surface color roles rather than only shadow levels. Material 3 separates tone-based surface roles from elevation.

Use tonal differences for:

- section grouping;
- persistent panes;
- selected regions;
- read-only areas.

Do not create many nearly identical gray surfaces.

## 8. Interactive states

Every interactive surface must define:

```text
default
hover
focus
active
selected
disabled
read-only
loading
error
```

The selected state must remain visible without hover.

## 9. Pressed and toggled states

Pressed is temporary. Selected or toggled is persistent.

Do not use the same visual treatment for both.

## 10. Drag affordance

Use drag handles, cursor change, preview, target indicators, and keyboard alternatives.

Do not make arbitrary areas draggable without a cue.

## 11. Touch

Touch interfaces cannot rely on hover. Controls need visible default affordance, adequate targets, and feedback after contact.

## 12. High contrast and forced colors

Meaningful boundaries must survive forced-colors mode. Use real borders or platform semantics where possible.

## 13. Surface selection guide

| Context | Recommended base |
|---|---|
| Dense data table | flat/bordered |
| Form | bordered/tonal |
| Dashboard module | tonal or outlined |
| Menu | raised/transient |
| Dialog | elevated/overlay |
| Navigation rail | tonal persistent |
| Media overlay | translucent only when legible |
| Critical warning | opaque, high contrast |

## 14. Anti-patterns

Avoid:

- every section in a floating card;
- shadow-only inputs;
- invisible flat buttons;
- decorative elevation;
- unclear read-only states;
- selected states that depend on color alone;
- glass effects behind dense data;
- neumorphic controls with no border.

## 15. Agent rules

An AI agent must define the semantic purpose of every surface level, preserve focus and state cues, avoid redundant cards, and choose the simplest treatment that makes interaction understandable.

## 16. Checklist

- [ ] Surface hierarchy
- [ ] Interactive cues
- [ ] State matrix
- [ ] Persistent versus transient
- [ ] Touch behavior
- [ ] Drag alternatives
- [ ] Dark mode
- [ ] Forced colors
- [ ] No shadow-only meaning
- [ ] No decorative elevation


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

