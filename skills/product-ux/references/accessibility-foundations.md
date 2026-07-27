# Product UI Accessibility Foundations 2026

> Accessibility rules for product interfaces beyond a checklist-only approach.

## 1. Purpose

Accessibility means people with different sensory, motor, cognitive, linguistic, and technological needs can perceive, understand, navigate, operate, and recover from the interface.

Target WCAG 2.2 AA as a minimum. Conformance alone does not guarantee usability.

## 2. Native HTML first

Use native controls and semantic elements before ARIA.

ARIA can expose roles, names, states, and relationships, but it does not create keyboard or interaction behavior. Complex widgets must implement the complete APG pattern.

## 3. Keyboard access

Every action must be available without a pointer.

Requirements:

- logical tab order;
- visible focus;
- expected arrow-key behavior in composite widgets;
- escape from overlays;
- no keyboard traps;
- no positive `tabindex` used to force visual order.

## 4. Focus management

Manage focus for:

- dialogs;
- menus;
- route changes;
- error summaries;
- inserted content;
- destructive confirmations;
- deleted items.

Avoid moving focus merely because data refreshed.

## 5. Accessible names and descriptions

Controls need stable accessible names. Help text, errors, units, and requirements need programmatic relationships.

Do not place essential names only in icons, placeholders, or tooltips.

## 6. Dynamic updates

Use live regions sparingly for meaningful events such as validation, background completion, result-count changes, and session warnings.

Avoid announcing every animation, keystroke, or visual decoration.

## 7. Contrast

Verify:

- text;
- icons;
- control boundaries;
- focus;
- selected state;
- charts;
- disabled/read-only differences;
- text over media.

Automation helps, but manual state-by-state review remains necessary.

## 8. Zoom, reflow, and text spacing

Test at 200% zoom and narrow widths. Support user overrides for line height, paragraph spacing, letter spacing, and word spacing.

Avoid fixed-height controls and labels that clip.

## 9. Motion and sensory safety

Support reduced motion. Avoid flashing, unexpected sound, uncontrolled auto-updating content, large parallax movement, and motion required for comprehension.

Provide pause, stop, or hide controls where WCAG requires them.

## 10. Cognitive accessibility

Use:

- clear language;
- stable structure;
- visible progress;
- examples;
- recognition rather than recall;
- error prevention;
- confirmation for high-impact actions;
- recovery;
- human support.

Avoid unexplained changes and memory-dependent workflows.

## 11. Authentication

Support password managers, paste, accessible MFA, recovery codes, and alternatives to cognitive-function tests.

Do not block copy/paste into password or one-time-code fields without a proven security reason.

## 12. Touch and motor access

Use practical targets, sufficient separation, alternatives to complex gestures, and no drag-only workflows.

Allow actions to be completed with a single pointer unless multipoint gestures are essential.

## 13. Data visualization

Provide:

- plain-language summary;
- direct labels;
- non-color cues;
- table access;
- keyboard exploration where interactive;
- source and period;
- meaningful focus order.

## 14. Documents and media

Provide accessible HTML summaries for critical PDFs. Videos need captions; important audio needs transcripts. Complex imagery may need detailed descriptions.

## 15. Testing strategy

Combine:

- automated checks;
- keyboard;
- screen readers;
- zoom/reflow;
- forced colors;
- reduced motion;
- mobile assistive technology;
- user testing with disabled people.

Document browser, OS, and assistive-technology versions.

## 16. Accessibility statement

Publish support contact, testing scope, known limitations, workarounds, and update date where appropriate.

## 17. Anti-patterns

Avoid accessibility overlays, separate reduced-content sites, icon-only workflows, disabled zoom, inaccessible CAPTCHA, and claims based only on automated scans.

## 18. Agent rules

An AI agent must preserve native semantics, follow APG for complex widgets, include keyboard and focus behavior, and never claim accessibility without evidence.

## 19. Checklist

- [ ] Semantics
- [ ] Keyboard
- [ ] Focus
- [ ] Names/states/relationships
- [ ] Contrast
- [ ] Zoom/reflow
- [ ] Text spacing
- [ ] Reduced motion
- [ ] Cognitive clarity
- [ ] Authentication
- [ ] Media/documents
- [ ] Real assistive-technology testing


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

