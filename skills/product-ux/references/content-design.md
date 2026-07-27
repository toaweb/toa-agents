# Product UI Content Design 2026

> Rules for labels, instructions, errors, empty states, onboarding, warnings, confirmations, terminology, localization, and AI-generated content.

## 1. Purpose

Interface content helps users predict what will happen, complete tasks, avoid errors, understand state, and recover.

Content is part of component behavior, not placeholder copy added after design.

## 2. Voice and tone

Define a stable voice. Adjust tone to context:

```text
routine
success
warning
error
sensitive
destructive
urgent
```

Do not use humor in high-risk or distressing situations unless research supports it.

## 3. Terminology

Maintain a canonical glossary for objects, actions, roles, status, and regulated terms.

Use one name for one concept. Do not alternate between project, workspace, account, and organization when they mean the same thing.

## 4. Labels

Use concrete nouns and verbs.

Good:

```text
Create shipment
Download report
Archive project
```

Weak:

```text
Continue
Manage
Submit
```

Labels should remain understandable outside visual context.

## 5. Headings

A heading should identify the page or section when read out of context. Preserve logical heading levels.

## 6. Instructions

Give instructions before the user needs them. Put required format and constraints near the control.

Do not hide essential help only in tooltips.

## 7. Errors

State:

1. what happened;
2. how to fix it;
3. what remains saved;
4. where to get help.

Avoid blame, vague “invalid input,” and raw technical codes without explanation.

## 8. Empty states

Differentiate:

- first use;
- no results;
- completed queue;
- permission restriction;
- loading failure;
- unavailable feature;
- missing setup.

The action must match the cause.

## 9. Confirmations

Confirm high-impact actions with object identity and consequence.

Prefer:

```text
Delete project “Nordhavn”?
This removes 14 saved reports and cannot be undone.
```

Avoid generic “Are you sure?”

## 10. Notifications

Include source, time, reason, object, and action where useful. Separate urgent alerts from background completion.

Avoid alert fatigue.

## 11. Dates, numbers, and units

Use locale-aware formats. Include time zone where operationally relevant. Avoid ambiguous numeric dates.

Use consistent units and precision.

## 12. Onboarding

Explain value through real tasks. Prefer contextual guidance and sample work over long forced tours.

Allow dismissal and later access.

## 13. Sensitive content

Use respectful, direct language. Avoid euphemism that hides consequences and emotional language that pressures users.

## 14. AI-generated content

Label generated output. Show source, uncertainty, and editable status where relevant.

Do not describe generated interpretation as confirmed fact.

## 15. Translation and localization

Design source copy for translation. Avoid concatenated fragments, idioms, and word-order assumptions.

Allow labels, buttons, and errors to wrap.

## 16. Governance

Document:

- owner;
- glossary;
- prohibited terms;
- regulated wording;
- translation status;
- last review;
- source;
- AI involvement.

## 17. Anti-patterns

Avoid vague CTAs, placeholder instructions, cheerful errors, inconsistent object names, unexplained acronyms, false urgency, and generated content without disclosure.

## 18. Agent rules

An AI agent must use canonical terminology, write specific labels, preserve regulated wording, and avoid inventing facts, status, or consequences.

## 19. Checklist

- [ ] Glossary
- [ ] Voice/tone
- [ ] Labels
- [ ] Headings
- [ ] Instructions
- [ ] Errors
- [ ] Empty states
- [ ] Confirmations
- [ ] Locale formats
- [ ] AI disclosure
- [ ] Translation
- [ ] Ownership


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

