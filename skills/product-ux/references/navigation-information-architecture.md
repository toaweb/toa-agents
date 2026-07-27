# Navigation & Information Architecture Patterns 2026

> Rules for product structure, application shells, global/local navigation, tabs, breadcrumbs, and orientation.

## 1. Purpose

Navigation helps users know where they are, what is available, and how to move without losing context.

## 2. Model user tasks

Organize around user goals and objects rather than internal teams or database tables.

## 3. Navigation levels

Separate:

```text
global product navigation
workspace/organization navigation
local page navigation
object relationships
utility navigation
```

Do not mix page actions into global navigation.

## 4. Side navigation

Use for many stable destinations or nested product areas. Support expanded, compact, and overlay behavior.

Keep labels in expanded mode. Icon-only navigation needs tooltips and accessible names.

## 5. Top navigation

Use when primary destinations are few and shallow.

## 6. Tabs

Tabs represent sibling views of one context. They are not sequential steps and should not hide unrelated destinations.

Follow the APG tabs keyboard model for custom implementations.

## 7. Breadcrumbs

Use for real hierarchy, nested settings, documents, or object paths. Do not use breadcrumbs as the only page title.

## 8. Back behavior

Preserve list filters, selected object, scroll position, and unsaved work. Browser back should behave predictably.

## 9. Workspace switching

Show current workspace, organization, or account clearly. Switching must explain effect on data and permissions.

## 10. Favorites and recent items

Useful for complex products. Keep them user-controlled and distinguish personal from shared navigation.

## 11. Search and command palette

Global search and command palette supplement navigation; they do not replace discoverable structure.

## 12. Deep links

Important views, tabs, filters, and selected records should be linkable where security allows.

## 13. Mobile navigation

Choose bottom navigation for a few high-frequency destinations; drawers or hierarchical pages for larger structures. Preserve labels and state.

## 14. Permissions

Do not expose inaccessible destinations without a reason. Distinguish unavailable by role from unavailable by object state.

## 15. Accessibility

Provide landmarks, skip links, current-page state, logical focus, and expected keyboard behavior.

## 16. Anti-patterns

Avoid vague labels, constantly changing order, hidden desktop navigation, more than two visible nested levels, tabs as workflow steps, and icon-only primary navigation.

## 17. Agent rules

An AI agent must map tasks and hierarchy, identify navigation levels, preserve state, and document responsive transformation.

## 18. Checklist

- [ ] Task model
- [ ] Navigation levels
- [ ] Current location
- [ ] Stable labels/order
- [ ] Back/context preservation
- [ ] Deep links
- [ ] Workspace switching
- [ ] Mobile pattern
- [ ] Permission handling
- [ ] Keyboard/landmarks


## Research basis

Primary references:

- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/patterns/
- GOV.UK Design System patterns: https://design-system.service.gov.uk/patterns/
- U.S. Web Design System components: https://designsystem.digital.gov/components/overview/
- IBM Carbon patterns: https://carbondesignsystem.com/patterns/overview/
- Material Design 3 components: https://m3.material.io/components
- Atlassian Design System: https://atlassian.design/
- Shopify Polaris: https://polaris.shopify.com/

