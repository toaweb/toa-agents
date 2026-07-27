# Modern Enterprise UI / Operational Minimalism Design System

> Brand-neutral reference for admin panels, enterprise applications, SaaS back offices, operations systems, ERP, logistics tools, regulated workflows, and data-heavy web applications.
>
> This document defines the visual and structural UI system. Workflow rules belong in `ux-workflows.md`; dashboards and data presentation belong in `data-visualization.md`.

---

## 1. Purpose

Modern Enterprise UI is designed for software people use repeatedly to complete real work. The interface must make complex tasks understandable, efficient, accurate, predictable, accessible, auditable, and resilient.

```text
Clear structure
+ controlled information density
+ predictable interaction
+ visible system state
+ strong data components
+ restrained visual identity
= operational minimalism
```

Minimal does not mean sparse. Enterprise interfaces may be dense while still being visually ordered.

---

## 2. Priority order

1. Correctness
2. Task completion
3. Clarity
4. System feedback
5. Accessibility
6. Efficiency
7. Consistency
8. Visual identity
9. Decoration

A visual decision must never weaken a higher priority.

---

## 3. 2026 direction

Recommended characteristics:

- role-based workspaces;
- action-oriented dashboards;
- saved views and personalization;
- compact, scalable data interfaces;
- accessibility-first components;
- clear loading, empty, error, offline, stale, and permission states;
- progressive disclosure;
- consistent cross-device behavior;
- integrated but reviewable AI assistance;
- restrained visual character rather than decorative spectacle.

AI may assist with explanation, extraction, classification, and recommendations, but it must not make the primary workflow unpredictable.

---

## 4. Application shell

A standard desktop shell should contain:

```text
Global header
Primary navigation
Page context
Local navigation
Main workspace
Optional contextual panel
System feedback layer
```

Example:

```text
┌────────────────────────────────────────────────────────────┐
│ Product   Global search     Status   Help   Alerts   User │
├──────────────┬─────────────────────────────────────────────┤
│ Primary nav  │ Breadcrumb / workspace context              │
│              │ Page title                    Primary action│
│ Main areas   │ Local tabs / toolbar                        │
│ Favorites    ├─────────────────────────────────────────────┤
│ Recent       │                                             │
│              │ Main workspace                              │
│ Admin        │                                             │
└──────────────┴─────────────────────────────────────────────┘
```

### Shell rules

- Keep global and local navigation distinct.
- Preserve the same shell across related product areas.
- Do not place page actions inside global navigation.
- Keep system-wide alerts separate from local validation.
- Let data workspaces use available width.
- Do not force every page into a narrow marketing-site container.
- Support zoom, reflow, keyboard navigation, and responsive transformation.

---

## 5. Navigation

### Primary navigation

- Use concrete labels.
- Show the current location.
- Keep item order stable.
- Separate administration from everyday work.
- Use icons as support, not as the sole label.
- Allow favorites and recent items where useful.
- Avoid vague labels such as “Explore” or “Manage” when specific names exist.

### Side navigation

Use when the product has several destinations, nested structures, or frequent switching.

Supported states:

```text
Expanded
Compact
Overlay
Hidden for focused work
```

Rules:

- Remember the selected state.
- Provide tooltips in icon-only mode.
- Keep active state visible without color alone.
- Prefer no more than two visible hierarchy levels.
- Do not automatically reorder items based on inferred behavior.

### Breadcrumbs

Use for hierarchical entities, nested settings, folders, and detail pages reached from several lists. Breadcrumbs do not replace the page title.

### Tabs

Use for sibling views of the same context:

```text
Overview | Packages | Documents | History
```

Do not use tabs for sequential steps or unrelated destinations.

---

## 6. Page anatomy

A standard data-management page:

```text
Breadcrumb or workspace label
Page title and description
Primary action
Status or context
Local navigation
Search and filter toolbar
Active filters
Main table, list, form, or workspace
Result summary and pagination
```

The title area may contain object status, key metadata, one primary action, and a secondary overflow menu. Avoid several equally strong primary actions.

---

## 7. Layout

Example tokens:

```css
:root {
  --sidebar-expanded: 16rem;
  --sidebar-compact: 4rem;
  --reading-width: 72rem;
  --page-gutter: clamp(1rem, 2vw, 2rem);
  --grid-gap: clamp(0.75rem, 1.5vw, 1.5rem);
}
```

Approved layout modes:

- full-width data workspace;
- reading-width settings or documentation;
- split master-detail;
- form with side guidance;
- dashboard grid;
- focused modal or side panel;
- builder or canvas.

Rules:

- Use full width for wide data tables.
- Use reading width for explanatory content.
- Align controls and data consistently.
- Preserve logical DOM order.
- Recompose split views at smaller widths.

---

## 8. Density

Recommended modes:

| Mode | Use |
|---|---|
| Comfortable | occasional users, onboarding, touch-heavy work |
| Default | general enterprise use |
| Compact | experts, high-volume operations, large tables |

Density may affect row height, control height, cell padding, toolbar spacing, and metadata spacing. It must not reduce text readability, focus visibility, pointer targets, or state recognition.

---

## 9. Spacing

```css
:root {
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
}
```

- Use tighter spacing inside a component than between groups.
- Keep label-to-field spacing consistent.
- Preserve extra separation around destructive actions.
- Do not use cards to compensate for unclear spacing.
- Align toolbars and table edges.

---

## 10. Typography

The primary UI font should have:

- clear rendering at small sizes;
- distinguishable `0/O`, `1/l/I`;
- tabular numerals;
- sufficient language support;
- robust medium and semibold weights;
- readable symbols and punctuation.

Recommended scale:

```text
Page title: 24–32 px
Section title: 18–24 px
Component title: 15–18 px
Body/UI: 14–16 px
Table text: 13–15 px
Metadata: 12–13 px
```

Rules:

- Use sentence case.
- Use tabular numerals for aligned data.
- Right-align numbers in tables.
- Avoid thin weights and decorative fonts in controls.
- Use monospace only when the data benefits from it.
- Do not reduce body text merely to show more rows.

---

## 11. Color

Define semantic roles:

```text
Canvas
Base surface
Raised surface
Selected surface
Strong text
Default text
Muted text
Subtle border
Strong border
Brand action
Focus
Information
Success
Warning
Error
Disabled
```

Rules:

- Use brand color mainly for action and active state.
- Keep status meanings stable.
- Pair color with text, icon, or shape.
- Avoid low-contrast gray-on-gray UI.
- Do not use gradients for critical state.
- Test dark mode independently rather than simply inverting colors.
- Use a separate accessible palette for charts.

---

## 12. Borders, surfaces, radii, shadows

### Borders

Use borders for grouping and control boundaries, not around every container.

```css
--border-subtle: 1px;
--border-default: 1px;
--border-strong: 2px;
```

### Surfaces

Limit elevation:

```text
Canvas
Base surface
Raised surface
Overlay
```

### Radius

```text
Small controls: 4–6 px
Buttons and fields: 4–8 px
Panels: 6–12 px
Dialogs: 8–16 px
Pills: tags and compact filters only
```

### Shadows

Use mainly for overlays, dialogs, menus, drag states, and sticky content moving over other content. Use borders and surface contrast for normal structure.

---

## 13. Actions

Hierarchy:

1. Primary
2. Secondary
3. Tertiary or text
4. Destructive
5. Icon-only

Rules:

- One dominant action per decision area.
- Use specific verb-based labels.
- Keep common actions visible.
- Put rare actions in an overflow menu.
- Show hover, active, focus, disabled, and loading states.
- Keep button width stable during loading.
- Icon-only buttons require accessible names and usually tooltips.

---

## 14. Fields and controls

Every control needs:

- persistent label;
- instructions when needed;
- required or optional state;
- focus state;
- validation;
- error state;
- clear read-only and disabled behavior.

Rules:

- Placeholder is not a label.
- Read-only must not look disabled.
- Place units adjacent to values.
- Use native input behavior where possible.
- Make date, locale, and time-zone context explicit.
- Do not hide identifiers users need to compare.

---

## 15. Tables and lists

Visual requirements:

- stable row height;
- clear header distinction;
- visible sort state;
- aligned numeric values;
- consistent status treatment;
- persistent selection;
- clear hover without implying selection;
- sticky headers where useful;
- visible keyboard focus;
- robust overflow handling.

Avoid zebra striping unless it materially improves tracking across wide tables.

---

## 16. Cards and panels

Use cards for bounded object summaries, dashboard modules, configuration groups, selectable templates, and status summaries.

Do not:

- wrap every section in a card;
- nest cards without a strong reason;
- give static and clickable cards identical behavior;
- build a dashboard only from identical KPI cards.

---

## 17. Side panels and dialogs

### Side panels

Use to inspect or edit limited context while preserving the list or workspace behind it.

Avoid for very wide content, long high-risk forms, complex tables, or multi-step tasks.

### Dialogs

Use for short decisions, confirmations, conflict resolution, or small forms.

Dialogs require:

- focus trapping and restoration;
- clear title;
- safe escape behavior;
- primary and secondary actions;
- responsive sizing;
- correct scroll containment.

Do not place complex workflows or data tables in modals unless unavoidable.

---

## 18. System states

Every substantial page and component should define:

```text
Initial
Loading
Loaded
Empty
No results
Partial
Stale
Offline
Error
Permission denied
Disabled
Read-only
Success
Conflict
Archived
Deleted
```

### Loading

- Use skeletons when the layout is known.
- Use progress indicators for measurable work.
- Use spinners for short localized operations.
- Preserve prior content during refresh where safe.
- Do not replace an entire page with a spinner for a local update.

### Empty states

Distinguish no data, no filter results, incomplete setup, permission restrictions, and failed loading. Each needs a different message and next action.

---

## 19. Feedback

Use:

- inline validation for fields;
- section banners for local problems;
- page banners for page-wide problems;
- global banners for system incidents;
- toasts for short non-critical confirmation;
- dialogs for high-impact decisions;
- notification center for persistent history.

A toast must not be the only record of a critical failure.

---

## 20. Responsive behavior

### Large screens

- persistent navigation;
- master-detail;
- wide tables;
- multi-panel workspaces.

### Medium screens

- collapsible navigation;
- fewer supporting columns;
- priority columns;
- contextual side panels.

### Compact screens

- overlay navigation;
- object lists rather than wide tables;
- separate detail pages;
- focused forms;
- simplified filters;
- sticky primary actions where appropriate.

Do not merely shrink the desktop interface.

---

## 21. Accessibility

Target WCAG 2.2 AA as a minimum.

Required:

- semantic landmarks;
- logical heading hierarchy;
- complete keyboard support;
- visible focus;
- sufficient text and non-text contrast;
- practical pointer targets;
- zoom and reflow;
- labels and descriptions;
- accessible dialogs;
- understandable errors;
- status not communicated by color alone;
- reduced-motion support;
- screen-reader announcements for dynamic changes;
- accessible tables.

---

## 22. AI-assisted UI

Suitable uses:

- summarize;
- extract;
- classify;
- suggest;
- explain;
- detect anomalies;
- draft;
- translate;
- natural-language search.

AI output should show:

- that it is generated;
- source or basis where possible;
- uncertainty where relevant;
- editable result;
- accept/reject controls;
- expected consequence;
- audit record for important actions;
- human confirmation for irreversible operations.

Do not automatically rearrange critical navigation or hide controls based on inferred behavior.

---

## 23. Performance

Design for:

- responsive application shell;
- stable layout;
- fast common interactions;
- large datasets;
- cancellable requests;
- safe optimistic updates;
- clear slow-operation feedback;
- partial failure;
- offline or degraded states;
- controlled third-party dependencies.

The visual design must account for latency rather than assume instant responses.

---

## 24. Anti-patterns

Avoid:

- dashboards made only from KPI cards;
- excessive glassmorphism;
- low-contrast gray UI;
- rounded cards around everything;
- icon-only navigation without labels;
- hidden critical actions;
- several equal primary buttons;
- excessive modal use;
- animations that delay work;
- fake AI insights;
- hover-only information;
- status indicated only by color;
- permanent loading spinners;
- vague empty states;
- dark mode created by simple inversion.

---

## 25. AI-agent instructions

An AI agent must:

1. identify user roles and frequent tasks;
2. identify high-risk actions;
3. define the application shell;
4. define stable navigation;
5. define density requirements;
6. define page templates;
7. define all component states;
8. define responsive transformations;
9. define accessibility requirements;
10. distinguish global, page, and object actions;
11. preserve auditability;
12. design for latency and partial failure;
13. avoid invented data and permissions;
14. use reusable tokens and components.

The agent must not optimize only for screenshots or remove required information in the name of minimalism.

---

## 26. Production checklist

### Foundation

- [ ] Roles and tasks identified
- [ ] Navigation documented
- [ ] Application shell documented
- [ ] Density modes decided
- [ ] Page templates defined
- [ ] Token system defined

### Components

- [ ] Buttons and actions
- [ ] Inputs and selectors
- [ ] Tables and lists
- [ ] Tabs
- [ ] Side panels
- [ ] Dialogs
- [ ] Notifications
- [ ] Loading states
- [ ] Empty states
- [ ] Permission states
- [ ] Error states

### Responsive and accessibility

- [ ] Large, medium, and compact layouts tested
- [ ] Navigation transformation defined
- [ ] Tables have compact alternatives
- [ ] Keyboard paths tested
- [ ] Focus visible
- [ ] Contrast verified
- [ ] Zoom and reflow tested
- [ ] Dynamic announcements defined

### Performance

- [ ] Large datasets handled
- [ ] Slow operations provide feedback
- [ ] Layout remains stable
- [ ] Partial and failed requests handled

---

## 27. Research basis

- IBM Carbon Design System: https://carbondesignsystem.com/
- Carbon data tables: https://carbondesignsystem.com/components/data-table/usage/
- Carbon empty states: https://carbondesignsystem.com/patterns/empty-states-pattern/
- Carbon dashboard guidance: https://v10.carbondesignsystem.com/data-visualization/dashboards/
- Atlassian Design System: https://atlassian.design/
- Atlassian dynamic table: https://atlassian.design/components/dynamic-table
- Material Design 3: https://m3.material.io/
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Fuselab, Enterprise UX Design Guide 2026: https://fuselabcreative.com/enterprise-ux-design-guide-2026-best-practices/
- Hashbyt, Enterprise UI Design in 2026: https://hashbyt.com/blog/enterprise-ui-design

---

## 28. Final rule

A modern enterprise interface should disappear into the work. Users should spend their attention on decisions, exceptions, and outcomes—not on discovering how the interface behaves.
