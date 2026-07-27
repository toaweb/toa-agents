# Tables, Data Grids & Bulk Actions 2026

> Rules for comparison, operational records, large datasets, selection, editing, and batch work.

## 1. Choose the representation

Use a table when users compare fields across records. Use a list when one label dominates. Use cards when visual recognition matters more than comparison.

## 2. Table anatomy

```text
title/context
toolbar
active filters
column headers
rows
selection/bulk bar
result count
pagination
```

## 3. Columns

Keep the identifying column visible. Include units in headers. Right-align numerical values and use tabular numerals.

Prioritize columns by task, not database order.

## 4. Sorting

Show active direction. Support only meaningful sortable columns. Preserve sorting during navigation.

## 5. Selection

Distinguish:

```text
select visible rows
select current page
select all matching results
```

Show count and clear action.

## 6. Bulk actions

Bulk actions must show scope, consequences, incompatible records, progress, partial success, failure detail, and recovery.

Do not claim all items succeeded if some failed.

## 7. Row actions

Expose the common action; move rare actions to overflow. Avoid many unlabeled icons.

## 8. Clickable rows

Use only when destination is unambiguous. Preserve keyboard access and avoid nested click conflicts.

## 9. Inline editing

Use for low-risk independent values. Show edit, validation, saving, success, failure, and conflict.

Avoid inline editing for regulated or highly dependent fields.

## 10. Expansion

Use expanded rows for supporting detail, not a second full application inside the table.

## 11. Pinning and resizing

Allow when wide datasets require it. Preserve user configuration and provide reset.

## 12. Pagination and virtualization

Use pagination when position, exact count, export, and revisiting matter. Virtualization must not destroy keyboard, screen-reader, find-in-page, or print behavior.

## 13. Responsive behavior

On compact screens use priority columns, row detail pages, horizontal tables with a stable identifier, or structured cards. Do not shrink every column.

## 14. Empty and error states

Differentiate no data, no results, permission, partial load, stale data, and server failure.

## 15. Accessibility

Use semantic tables for ordinary data. Complex grids require the complete APG grid model, including keyboard navigation and focus strategy.

Do not apply `role="grid"` merely for styling.

## 16. Export

Exports must include filter context, units, time zone, source, and visible or explicitly selected columns.

## 17. Anti-patterns

Avoid tables used for layout, hidden units, color-only status, horizontal scrolling for simple data, row action icon clutter, and destructive bulk actions without scope.

## 18. Agent rules

An AI agent must define comparison tasks, column priority, selection scope, bulk partial failure, mobile transformation, and semantic table versus interactive grid behavior.

## 19. Checklist

- [ ] Correct representation
- [ ] Column priority/units
- [ ] Sorting/filter state
- [ ] Selection scope
- [ ] Bulk partial failure
- [ ] Row actions
- [ ] Editing/conflict
- [ ] Pagination/virtualization
- [ ] Mobile alternative
- [ ] Semantic accessibility


## Research basis

Primary references:

- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/patterns/
- GOV.UK Design System patterns: https://design-system.service.gov.uk/patterns/
- U.S. Web Design System components: https://designsystem.digital.gov/components/overview/
- IBM Carbon patterns: https://carbondesignsystem.com/patterns/overview/
- Material Design 3 components: https://m3.material.io/components
- Atlassian Design System: https://atlassian.design/
- Shopify Polaris: https://polaris.shopify.com/

