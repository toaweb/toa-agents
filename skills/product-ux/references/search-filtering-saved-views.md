# Search, Filtering & Saved Views Patterns 2026

> Rules for finding objects, narrowing results, preserving query context, and saving repeatable workspaces.

## 1. Purpose

Search and filtering should help users reach relevant records quickly without requiring exact memory of system structure.

## 2. Search scope

Make scope visible:

```text
current list
current workspace
all objects
documents
commands
help
```

Allow users to change scope when useful.

## 3. Query behavior

Support exact identifiers, partial names, common formatting variants, synonyms, and recent queries.

Do not silently broaden a high-risk query.

## 4. Results

Show object type, primary name, identifier, status, context, matched term, and destination.

Differentiate no results, permission-restricted results, and search failure.

## 5. Filters

Use user language. Filters may be:

- quick filters;
- faceted filters;
- advanced conditions;
- date ranges;
- saved criteria.

Show active filters and result count.

## 6. Logic

Make AND/OR behavior understandable. Avoid hidden filter dependencies.

## 7. Filter values

Distinguish:

```text
blank
unknown
not applicable
zero
none selected
all
```

## 8. Date and time filters

Show time zone, inclusivity of bounds, and relative versus fixed periods.

## 9. Applied-filter display

Use removable chips or a clear summary. Provide reset without losing unrelated configuration.

## 10. Saved views

A saved view may include query, filters, sort, columns, density, grouping, timeframe, and layout.

Support personal and shared views, ownership, duplicate, rename, default, and delete.

## 11. Shared views

Do not overwrite silently. Show owner, scope, permissions, and last modified.

## 12. Persistence

Preserve search and filter state when users inspect a record and return.

## 13. URL state

Encode safe, shareable state in the URL where appropriate. Do not expose sensitive query values.

## 14. Performance

Debounce expensive queries, cancel superseded requests, show progress, and preserve prior results during safe refresh.

## 15. Accessibility

Search controls need labels. Result changes should be announced appropriately. Chips, filter menus, and comboboxes need complete keyboard behavior.

## 16. Anti-patterns

Avoid unsearchable long selects, filters hidden after application, reset that clears everything, infinite filter panels, no result count, and saved views with unclear ownership.

## 17. Agent rules

An AI agent must define scope, matching, filter logic, persistence, URL behavior, permissions, and no-result/error states.

## 18. Checklist

- [ ] Scope
- [ ] Identifier/synonym support
- [ ] Result anatomy
- [ ] Active filters
- [ ] AND/OR clarity
- [ ] Date/time semantics
- [ ] Saved views
- [ ] Ownership
- [ ] Persistence/deep link
- [ ] Accessibility/performance


## Research basis

Primary references:

- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/patterns/
- GOV.UK Design System patterns: https://design-system.service.gov.uk/patterns/
- U.S. Web Design System components: https://designsystem.digital.gov/components/overview/
- IBM Carbon patterns: https://carbondesignsystem.com/patterns/overview/
- Material Design 3 components: https://m3.material.io/components
- Atlassian Design System: https://atlassian.design/
- Shopify Polaris: https://polaris.shopify.com/

