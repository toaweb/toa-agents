# Mobile Product UI/UX 2026

> Rules for mobile-first and native mobile applications across iOS, Android, and responsive product surfaces.

## 1. Purpose

Mobile UI should support tasks that benefit from portability, touch, camera, location, notifications, offline use, or rapid review.

Do not shrink desktop software into a phone.

## 2. Platform conventions

Respect current Apple HIG and Material guidance for navigation, system bars, back behavior, sheets, permissions, typography, and controls.

Use shared product identity without erasing platform expectations.

## 3. Navigation

Choose based on hierarchy:

- tab/bottom bar for a few primary areas;
- navigation stack for drill-down;
- drawer for larger secondary structures;
- search for broad collections;
- modal/sheet for focused tasks.

Do not overload bottom navigation.

## 4. One-handed use

Place frequent actions within practical reach where possible. Do not put every critical action at the top edge.

## 5. Touch

Use practical target size and separation. Provide alternatives to swipe, drag, pinch, and long press.

## 6. Safe areas

Respect status bars, camera cutouts, home indicators, browser bars, and virtual keyboards.

## 7. Forms

Use suitable keyboard types, autofill, scanning, pickers, and step progression. Preserve entered data when the keyboard, app, or network changes state.

## 8. Camera and scanning

Explain permission and purpose before the system prompt. Provide manual entry and file alternatives.

Show capture quality, crop, retry, upload, and privacy.

## 9. Offline

Define:

```text
available offline
queued changes
sync status
conflict
failed sync
last updated
```

Do not show stale data as current.

## 10. Notifications

Ask for notification permission after value and context are clear. Provide granular preferences and deep-link to the relevant object.

## 11. Biometrics

Use biometrics for convenience with secure fallback. Do not make biometric use mandatory when another valid method exists.

## 12. Sheets and dialogs

Use sheets for focused, reversible tasks and compact choices. Use alerts for critical decisions.

Avoid stacking several modals or sheets.

## 13. Lists and tables

Use priority data, grouped lists, horizontal table only when necessary, and detail screens for full records.

## 14. Orientation and larger screens

Support rotation where task benefits. Tablet and foldable layouts may introduce panes rather than merely scaling.

## 15. Accessibility

Support Dynamic Type/font scaling, screen readers, switch control, voice access, reduced motion, high contrast, captions, and platform focus behavior.

## 16. Performance and battery

Avoid continuous background work, excessive location updates, heavy animation, and unnecessary network refresh.

## 17. Permissions

Request only when needed. Explain denied and limited states and provide a route to settings.

## 18. Destructive actions

Use undo for reversible actions. Confirm irreversible actions with object identity and consequence.

## 19. Anti-patterns

Avoid hamburger menus for a few primary areas, gesture-only actions, tiny top-corner controls, permission prompts on launch, desktop tables scaled down, and required network for tasks that should work offline.

## 20. Agent rules

An AI agent must identify platform, task, input mode, offline need, permission timing, touch alternatives, and tablet/foldable adaptation.

## 21. Checklist

- [ ] Platform conventions
- [ ] Navigation model
- [ ] One-handed use
- [ ] Touch targets/alternatives
- [ ] Safe areas/keyboard
- [ ] Camera/scanning
- [ ] Offline/sync
- [ ] Notifications
- [ ] Biometrics fallback
- [ ] Accessibility
- [ ] Battery/network
- [ ] Tablet/foldable


## Research basis

Primary references:

- W3C, WCAG 2.2: https://www.w3.org/TR/WCAG22/
- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- Material Design 3: https://m3.material.io/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines
- IBM Carbon Design System: https://carbondesignsystem.com/
- Atlassian Design System: https://atlassian.design/
- GitHub Primer: https://primer.style/
- Shopify Polaris: https://polaris.shopify.com/
- GOV.UK Design System: https://design-system.service.gov.uk/
- U.S. Web Design System: https://designsystem.digital.gov/

