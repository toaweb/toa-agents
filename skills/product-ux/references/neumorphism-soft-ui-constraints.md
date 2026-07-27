# Neumorphism / Soft UI Constraints 2026

> A constrained treatment guide for authenticated product interfaces.
>
> Classification: experimental and limited. Default recommendation: do not use neumorphism for core controls or critical workflows.

## 1. Purpose

Neumorphism creates raised and inset surfaces using paired shadows and closely related background colors. It can create a soft, tactile appearance but often weakens affordance, state visibility, and contrast.

The purpose of this guide is primarily to prevent unsafe use.

## 2. Appropriate use

Potentially acceptable for:

- noncritical media controls;
- decorative dashboard modules;
- demo interfaces;
- low-density personal tools;
- visual themes where an opaque bordered fallback exists.

## 3. Avoid for

Do not use for:

- form fields;
- primary buttons;
- warnings;
- authentication;
- permissions;
- tables;
- dense navigation;
- regulated workflows;
- operational control;
- accessibility settings.

## 4. Surface model

A neumorphic surface usually uses:

```text
base surface color
light shadow
dark shadow
optional border
pressed/inset state
focus ring
```

The virtual light direction must remain consistent.

## 5. Affordance

Raised appearance alone is insufficient. Add:

- label;
- icon;
- border;
- state change;
- shape;
- visible focus.

## 6. Pressed state

Pressed states must not depend only on changing shadow direction. Use an additional fill, border, icon, or label state.

## 7. Contrast

Neumorphism commonly fails because controls and backgrounds are too similar.

All meaningful text, icons, boundaries, focus, and state indicators must meet contrast requirements.

## 8. Focus

Focus must use a separate, strong indicator. Never attempt to represent keyboard focus through a subtle change in soft shadow.

## 9. Disabled and read-only

Do not reduce already weak contrast further. Read-only content must remain fully legible.

## 10. Dark mode

Dark neumorphism is especially difficult because shadow contrast and surface separation collapse. Use explicit borders or replace the treatment.

## 11. Forced colors

Provide native semantics and real boundaries so controls remain visible when shadows disappear.

## 12. Motion

Avoid animated shadow movement. It is visually expensive and may make state harder to interpret.

## 13. Testing gate

A neumorphic implementation must pass:

- default-state recognition without hover;
- keyboard focus;
- selected state;
- dark mode;
- forced colors;
- grayscale;
- low-quality display;
- touch;
- zoom.

If any state is ambiguous, replace it with flat, outlined, or elevated UI.

## 14. Anti-patterns

Avoid shadow-only buttons, inset text fields, monochrome warning states, soft toggle switches with no text, and neumorphic card grids around dense data.

## 15. Agent rules

An AI agent must treat neumorphism as constrained, preserve borders and semantic states, and reject its use for core, high-risk, or dense controls.

## 16. Checklist

- [ ] Noncritical context
- [ ] Explicit affordance
- [ ] Border fallback
- [ ] Strong focus
- [ ] Persistent selected state
- [ ] Dark-mode replacement
- [ ] Forced-colors behavior
- [ ] Touch recognition
- [ ] No critical workflow use


## Research basis

Primary and current references:

- W3C, Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines
- Material Design 3: https://m3.material.io/
- Microsoft Windows App Design Guidelines: https://learn.microsoft.com/en-us/windows/apps/design/
- IBM Carbon Design System: https://carbondesignsystem.com/
- GOV.UK Design System: https://design-system.service.gov.uk/
- U.S. Web Design System: https://designsystem.digital.gov/

