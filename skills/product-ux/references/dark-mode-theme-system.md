# Dark Mode & Theme System 2026

> Rules for light/dark appearance, adaptive themes, user preferences, semantic colors, assets, charts, code, and system integration.

## 1. Purpose

Dark mode is a system appearance, not a simple inversion and not a standalone design style.

Apple describes Dark Mode as a systemwide appearance intended to provide a comfortable viewing experience in low-light environments.

## 2. Theme architecture

Define semantic roles once:

```text
canvas
surface
raised surface
text
muted text
border
action
focus
selection
status
overlay
chart
code
```

Resolve those roles independently for light and dark themes.

## 3. User control

Support:

```text
System
Light
Dark
```

Remember the user's explicit choice. System preference should be the default only until a user chooses otherwise.

## 4. Contrast

Test every state in both appearances. Apple explicitly recommends checking minimum contrast in both light and dark modes.

Do not use pure white for all dark-theme text. Use a hierarchy of strong, default, muted, and disabled values.

## 5. Surfaces

Dark themes need visible surface separation through:

- tone;
- border;
- elevation;
- material;
- spacing.

Do not use many nearly identical near-black values.

## 6. Elevation in dark mode

Shadows are less effective on dark backgrounds. Use tonal elevation, borders, or controlled highlights.

Material guidance emphasizes checking foreground contrast as elevated surfaces change.

## 7. Images

Prepare rules for:

- transparent logos;
- screenshots;
- illustrations;
- photography;
- charts;
- maps;
- code blocks.

Do not invert photographs or customer logos automatically.

## 8. Product screenshots

When showing application screenshots inside the application or documentation, label whether the image is from light or dark mode.

Avoid placing a dark screenshot on a dark surface without a visible frame.

## 9. Charts

Create theme-specific chart palettes. Preserve:

- series identity;
- contrast;
- grid visibility;
- selected state;
- muted state;
- status meaning.

## 10. Code and syntax

Define syntax colors separately for dark mode. Verify comments, errors, selection, current line, and diff states.

## 11. Focus

Focus indicators must remain visible on every dark surface and selected state.

## 12. Disabled and read-only

Disabled content must remain perceivable. Read-only controls should remain legible and distinct from disabled controls.

## 13. OLED and black

Pure black can reduce power use on some OLED displays but should not override legibility, surface structure, or visual comfort.

## 14. Theme transition

Avoid dramatic full-screen animation. Theme changes should be fast and should not trigger motion discomfort.

## 15. System integration

Use system-provided adaptive colors and symbols where appropriate. Apple notes that system colors and symbols can adapt to appearance and accessibility settings.

## 16. Forced colors

Dark mode does not replace forced-colors or high-contrast support.

## 17. Testing

Test:

- system/light/dark;
- browser zoom;
- high contrast;
- reduced transparency;
- screenshots;
- charts;
- video controls;
- forms;
- disabled/read-only;
- selected/focus combinations.

## 18. Anti-patterns

Avoid simple color inversion, pure white everywhere, hidden borders, dark gradients behind text, unreadable muted content, and theme-specific changes to product meaning.

## 19. Agent rules

An AI agent must use semantic tokens, provide all three theme settings, test every state, preserve user choice, and never generate a dark theme by blindly inverting values.

## 20. Checklist

- [ ] Semantic mapping
- [ ] System/light/dark
- [ ] User persistence
- [ ] Contrast by state
- [ ] Surface hierarchy
- [ ] Theme-specific assets
- [ ] Charts/code
- [ ] Focus
- [ ] Forced colors
- [ ] No meaning changes


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

