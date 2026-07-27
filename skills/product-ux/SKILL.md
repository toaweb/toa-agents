---
name: product-ux
description: Product UI/UX patterns for application interfaces — admin panels, dashboards, internal tools, SaaS product surfaces, mobile and native apps, data tables, complex forms, multi-step workflows, notifications, AI-assisted features, and data visualization. Also covers the foundations they rest on: design tokens, component anatomy and states, UI content design, accessibility, and design-system governance. Use when designing or reviewing product UX (not marketing sites): "build an admin dashboard", "design this settings page", "how should this table/filter/bulk action work", "what should this error say", "pick the right chart". Brand-neutral and framework-neutral — visual identity comes from the project's brand source, page-level visual styles from the design-styles catalogue. Defer implementation mechanics to the framework and Tailwind skills.
---

# Product UX

Product interfaces are judged by task completion, not visual impression.
This skill routes to normative references for designing them; read the
relevant reference in full before designing — never from memory.

## Precedence

When guidance conflicts, resolve in this order:

```text
accessibility and platform requirements
→ foundations (tokens, states, content, a11y)
→ product-UX structure and behavior
→ product-category rules (admin / SaaS / mobile)
→ visual design style
→ decorative detail
```

A named visual style governs appearance only. It never overrides
accessibility, platform behavior, task safety, or component semantics.

## Workflow

1. Classify the task, then read the matching reference(s) fully:
   - Screen structure, components, density, tables, forms, states →
     `references/ui-design-system.md`
   - Task flows, navigation, search/filter, bulk actions, permissions,
     notifications, error/empty/loading behavior →
     `references/ux-workflows.md`
   - Charts, dashboards, metrics, choosing and rendering visualizations →
     `references/data-visualization.md`
   - Authenticated SaaS app — shell, workspace/org model, onboarding,
     settings, billing, integrations, trials/limits →
     `references/saas-product-ui.md`
   - Mobile or native surfaces — platform conventions, touch, safe areas,
     offline, permissions, biometrics → `references/mobile-product-ui.md`
   - AI suggestions, generation, agentic actions, review and reversibility →
     `references/ai-assisted-interactions.md`

   Most real tasks span two of these; read both rather than guessing.

2. Read the foundations the task touches:
   - Token definition, naming, layering, theming, deprecation →
     `references/design-tokens.md`
   - A single component's API, anatomy, variants, state model →
     `references/component-anatomy-states.md`
   - Labels, errors, empty states, confirmations, terminology →
     `references/content-design.md`
   - Keyboard, focus, contrast, reflow, assistive-tech behavior →
     `references/accessibility-foundations.md`

3. Apply the project's brand values on top (brand source: MCP server,
   `brand.json`, or tokens — ask if absent, never invent). If the product
   surface also has a named visual style, its definition in the
   design-styles catalogue applies to the visual layer while these
   references govern structure and behavior.

4. Respect the references' normative language (must/should/may) and their
   accessibility requirements — keyboard paths, focus, ARIA on complex
   widgets are part of done.

5. When establishing or changing a shared design system rather than one
   screen — ownership, contribution, releases, deprecation, design-code
   parity → `references/design-system-governance.md`.

6. Defer code mechanics to the framework/Tailwind skills.

## Reference files

### Product UX core

| File | Contents |
|---|---|
| `references/ui-design-system.md` | Enterprise UI system: layout/density, navigation chrome, tables, forms, feedback (incl. toasts), states, component rules |
| `references/ux-workflows.md` | Workflow patterns: task flows, search & filtering, bulk actions, permissions, notifications policy, error/empty/loading behavior |
| `references/data-visualization.md` | Data visualization: chart selection, dashboards, metrics presentation, visualization accessibility |

### Product categories

| File | Contents |
|---|---|
| `references/saas-product-ui.md` | Authenticated SaaS app: shell, workspace/org switching, onboarding, settings architecture, billing, integrations, trials & limits, admin vs end-user UI |
| `references/mobile-product-ui.md` | Mobile & native: platform conventions, one-handed use, touch targets, safe areas, offline, notifications, biometrics, permissions |
| `references/ai-assisted-interactions.md` | AI in product UI: interaction types, entry points, output anatomy, grounding & sources, human review, agentic actions, reversibility, uncertainty |

### Foundations

| File | Contents |
|---|---|
| `references/design-tokens.md` | Token layers (primitive → semantic → component), naming, required domains, theme architecture, canonical source, versioning & deprecation |
| `references/component-anatomy-states.md` | Component API and anatomy, state model, disabled vs read-only, loading, empty, error, composition, variants, maturity, quality gates |
| `references/content-design.md` | UI copy: labels, headings, instructions, error and empty-state text, confirmations, terminology, units, localization, AI-generated content |
| `references/accessibility-foundations.md` | Keyboard access, focus management, accessible names, dynamic updates, contrast, reflow, motion safety, testing strategy |

### System-level

| File | Contents |
|---|---|
| `references/design-system-governance.md` | Ownership, contribution model, maturity levels, releases, deprecation, design-code parity, decision records, adoption metrics |

## Boundaries

Not for marketing/editorial websites — that is design-styles territory.
Not a styling skill (Tailwind skill) and not a component-code skill
(framework skills). `content-design.md` covers product UX writing —
language correctness and bilingual parity belong to the copy-editing
skill. This skill owns product-UX structure and behavior.
