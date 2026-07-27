# Forms & Validation Patterns 2026

> Rules for data entry, form structure, validation, review, saving, submission, and recovery.

## 1. Purpose

A form should help users understand what is required, enter valid information, preserve effort, review consequences, and recover from mistakes.

## 2. Ask only what is needed

Every field creates cost, privacy exposure, validation, support, and maintenance. Ask only for information required at the current stage.

## 3. Structure

Recommended order:

```text
purpose
context
logical sections
fields
review
primary action
secondary action
```

Use one column by default. Use two columns only for short, strongly related values.

## 4. Labels and help

Use persistent labels. Explain format and reason before errors occur.

Do not use placeholders as labels or hide required guidance in tooltips.

## 5. Required and optional

Choose a consistent convention based on which state is less common. Explain conditional requirements.

## 6. Input choice

Match control to data. Prefer native text, number, date, checkbox, radio, and select behavior unless a custom pattern offers clear benefit.

Use autocomplete and input-purpose metadata where appropriate.

## 7. Validation timing

Validate:

- on input for tightly constrained values;
- after field completion for normal fields;
- on dependency changes;
- on submission for full consistency;
- on server response for authoritative rules.

Do not show an error before the user has had a reasonable chance to answer.

## 8. Error messages

State what is wrong and how to correct it.

Bad:

```text
Invalid value
```

Better:

```text
Enter the UN number using four digits, for example 3481.
```

## 9. Error summary

For longer forms, provide a summary linked to each invalid field. Move focus to the summary after failed submission while retaining inline errors.

## 10. Preservation

Never erase valid values because one field failed. Protect unsaved work during navigation, timeout, network failure, and authentication renewal.

## 11. Autosave and drafts

Show:

```text
saving
saved
save failed
offline draft
conflict
```

Do not claim “Saved” before authoritative persistence when it matters.

## 12. Multi-step forms

Use steps when order, dependency, risk, or review requires them. Do not split a short form merely to reduce visual height.

Show progress without implying an inaccurate completion percentage.

## 13. Review

Use review before high-impact submissions. Show entered data in readable sections with edit links.

## 14. Submission

Prevent duplicate submission, preserve action width during loading, announce success, and provide a reference or next step.

## 15. Conditional fields

Reveal fields only when relevant. Maintain logical focus and explain why they appeared.

## 16. Dates and units

Show locale and time-zone context. Place units adjacent to input. Avoid ambiguous date formats.

## 17. File attachments

Show allowed types, limits, scanning status, upload progress, failure, retry, remove, and confidentiality context.

## 18. Accessibility

Use native form semantics, programmatic labels, descriptions, fieldsets, legends, error relationships, and keyboard order.

## 19. Anti-patterns

Avoid placeholder labels, premature errors, disabled submit buttons with no explanation, unnecessary steps, erased data, and forms in small modals.

## 20. Agent rules

An AI agent must define field purpose, validation authority, error recovery, draft behavior, review, and accessible relationships before implementation.

## 21. Checklist

- [ ] Necessary fields only
- [ ] Logical sections
- [ ] Persistent labels
- [ ] Validation timing
- [ ] Error summary
- [ ] Data preservation
- [ ] Draft/autosave
- [ ] Review
- [ ] Submission state
- [ ] Accessibility


## Research basis

Primary references:

- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/patterns/
- GOV.UK Design System patterns: https://design-system.service.gov.uk/patterns/
- U.S. Web Design System components: https://designsystem.digital.gov/components/overview/
- IBM Carbon patterns: https://carbondesignsystem.com/patterns/overview/
- Material Design 3 components: https://m3.material.io/components
- Atlassian Design System: https://atlassian.design/
- Shopify Polaris: https://polaris.shopify.com/

