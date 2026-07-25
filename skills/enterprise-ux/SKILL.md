---
name: enterprise-ux
description: Product UI/UX patterns for enterprise and admin interfaces — admin panels, dashboards, internal tools, SaaS product surfaces, data tables, complex forms, multi-step workflows, notifications, and data visualization. Use when designing or reviewing product UX (not marketing sites): "build an admin dashboard", "design this settings page", "how should this table/filter/bulk action work", "pick the right chart". Brand-neutral and framework-neutral — visual identity comes from the project's brand source, and page-level visual styles come from the design-styles catalogue. Defer implementation mechanics to the framework and Tailwind skills.
---

# Enterprise / admin product UX

Product interfaces are judged by task completion, not visual impression.
This skill routes to normative references for designing them; read the
relevant reference in full before designing — never from memory.

## Workflow

1. Classify the task, then read the matching reference(s) fully:
   - Screen structure, components, density, tables, forms, states →
     `references/ui-design-system.md`
   - Task flows, navigation, search/filter, bulk actions, permissions,
     notifications, error/empty/loading behavior →
     `references/ux-workflows.md`
   - Charts, dashboards, metrics, choosing and rendering visualizations →
     `references/data-visualization.md`
   Most real tasks span two of these; read both rather than guessing.
2. Apply the project's brand values on top (brand source: MCP server,
   `brand.json`, or tokens — ask if absent, never invent). If the product
   surface also has a named visual style, its definition in the
   design-styles catalogue applies to the visual layer while these
   references govern structure and behavior.
3. Respect the references' normative language (must/should/may) and their
   accessibility requirements — keyboard paths, focus, ARIA on complex
   widgets are part of done.
4. Defer code mechanics to the framework/Tailwind skills.

## Reference files

| File | Contents |
|---|---|
| `references/ui-design-system.md` | Enterprise UI system: layout/density, navigation chrome, tables, forms, feedback (incl. toasts), states, component rules |
| `references/ux-workflows.md` | Workflow patterns: task flows, search & filtering, bulk actions, permissions, notifications policy, error/empty/loading behavior |
| `references/data-visualization.md` | Data visualization: chart selection, dashboards, metrics presentation, visualization accessibility |

## Boundaries

Not for marketing/editorial websites — that is design-styles territory.
Not a styling skill (Tailwind skill) and not a component-code skill
(framework skills). This skill owns product-UX structure and behavior.
