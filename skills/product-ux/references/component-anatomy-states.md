# Product UI Component Anatomy & States 2026

> Rules for component APIs, anatomy, behavior, states, composition, accessibility, documentation, and maturity.

## 1. Purpose

A component is a reusable contract, not only a styled shape. It includes anatomy, content rules, interaction, states, accessibility semantics, responsive behavior, analytics events, and implementation constraints.

## 2. Required specification

Every component document should define:

```text
purpose
when to use
when not to use
anatomy
variants
states
content rules
keyboard behavior
screen-reader behavior
responsive behavior
tokens
events
analytics
examples
anti-patterns
owner
maturity
```

A visual screenshot alone is not documentation.

## 3. Anatomy

Name internal parts consistently. Define which parts are required, optional, repeatable, or mutually exclusive.

Expose only slots and properties users need. Avoid APIs that permit arbitrary combinations without guardrails.

## 4. State model

Consider:

```text
default
hover
focus
active
selected
disabled
read-only
loading
empty
error
warning
success
partial
stale
offline
permission denied
```

Not every component uses every state, but absence must be intentional.

## 5. Disabled and read-only

Disabled means unavailable for interaction and may be removed from keyboard navigation. Read-only means the value remains available and often selectable or copyable.

Do not style them identically. Explain why an action is unavailable when that information helps the user proceed.

## 6. Loading

Loading states should:

- preserve dimensions;
- prevent duplicate submission;
- retain context;
- announce meaningful progress;
- expose retry or cancellation when appropriate.

Use skeletons only when the approximate structure is known. Do not show fake progress.

## 7. Empty and no-result states

Differentiate:

- no data exists;
- filters returned no results;
- setup is incomplete;
- permission prevents access;
- loading failed;
- work is complete.

The message and action must match the actual cause.

## 8. Errors

Errors should identify what happened, which content is affected, what remains safe, and how to recover.

Component errors must integrate with form or page-level summaries where relevant.

## 9. Native semantics

Use native HTML controls first. Native semantics usually provide better keyboard, form, focus, and platform behavior.

ARIA does not add behavior automatically. Complex widgets must implement the complete interaction model described by WAI-ARIA APG.

## 10. Keyboard behavior

Document exact keys. Use platform conventions. Avoid custom shortcuts that conflict with browsers, assistive technology, or operating systems.

## 11. Focus management

Move focus only when context changes, such as opening a modal, moving to an error summary, or completing a destructive flow.

Restore focus to a logical origin after overlays close.

## 12. Content resilience

Test:

- long labels;
- translation;
- missing metadata;
- duplicated names;
- large numbers;
- unknown state;
- text spacing;
- browser zoom;
- user-generated content.

Do not use fixed heights for text-dependent components.

## 13. Composition

Define whether the parent or child owns padding, borders, headings, and actions.

Avoid card-inside-card nesting, duplicated focus rings, and stacked interactive elements with ambiguous targets.

## 14. Variants

Variants should represent real semantic, behavioral, density, or platform differences.

Avoid a new variant created for one page. Prefer composition or a documented extension.

## 15. Events and analytics

Define high-level events such as opened, submitted, selected, completed, failed, and dismissed.

Do not instrument every pointer movement by default. Analytics must not alter behavior or block accessibility.

## 16. Maturity

Use:

```text
experimental
beta
stable
deprecated
retired
```

Document owner, version, known limitations, testing context, and replacement.

## 17. Quality gates

A component is not stable until it has:

- production usage;
- complete states;
- accessibility review;
- content review;
- responsive testing;
- API review;
- automated tests;
- documented limitations.

## 18. Anti-patterns

Avoid visual-only specs, unlimited variants, custom controls duplicating native elements, undocumented focus changes, hidden error behavior, and state names that mean different things across components.

## 19. Agent rules

An AI agent must use stable components first, follow documented anatomy and states, avoid ad hoc variants, preserve native semantics, and flag missing keyboard, loading, empty, error, or permission behavior.

## 20. Checklist

- [ ] Purpose and alternatives
- [ ] Anatomy
- [ ] Required/optional parts
- [ ] Complete state model
- [ ] Native semantics
- [ ] Keyboard behavior
- [ ] Focus management
- [ ] Responsive behavior
- [ ] Content stress tests
- [ ] Tokens and events
- [ ] Maturity and owner


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

