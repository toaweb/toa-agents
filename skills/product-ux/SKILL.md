---
name: product-ux
description: Product UI/UX for authenticated application interfaces — admin panels, dashboards, SaaS apps, user and customer portals, operational control panels, mobile products, data tables, complex forms, workflows and AI-assisted features. Covers the foundations they rest on (design tokens, component states, surfaces and affordance, dark mode, UI copy, illustration, accessibility) and constrained visual treatments for product surfaces (flat/elevated, glassmorphism, neumorphism, skeuomorphic controls). Use for anything behind a login: "build an admin dashboard", "design this settings page", "how should this table/filter/bulk action work", "what should this error say", "should this panel be glass". Separate from the design-styles catalogue, which covers public websites and marketing pages. Brand-neutral and framework-neutral — brand values come from the project; defer implementation mechanics to the framework and Tailwind skills.
---

# Product UX

Interfaces used *after authentication* — products, not marketing pages.
They are judged by task completion, not visual impression. This skill
routes to normative references; read the relevant one in full before
designing, never from memory.

## Scope boundary

This is its own category, deliberately separate from the design-styles
catalogue and from any website design system:

| | Product UX (this skill) | design-styles |
|---|---|---|
| Surface | behind a login | public site, marketing, editorial |
| Judged by | task completion, safety, state clarity | expression, identity, impression |
| Visual layer | constrained *treatments* (below) | named *styles* (brutalist, editorial, …) |

Glassmorphism, neumorphism, skeuomorphism and flat/elevated live **here**
as product treatments with hard safety constraints — they are not entries
in the design-styles catalogue and must not be applied from it.

## Precedence

When guidance conflicts, resolve in this order:

```text
safety, law, and platform requirements
→ accessibility
→ product task and information architecture
→ foundations
→ shared UX patterns
→ application-type rules
→ visual treatment
→ decorative detail
```

A visual treatment must never override task clarity, component semantics,
state visibility, accessibility, or operational safety.

## Workflow

1. **Classify the surface**, then read its application-type reference in
   full — `saas-product-ui.md`, `user-portal-ui.md`,
   `customer-portal-ui.md`, `analytics-dashboard-ui.md` or
   `operational-control-panel-ui.md`. If none fits, the surface is a
   generic admin/internal tool: use the core references below.

2. **Read the core references the task touches** —
   `ui-design-system.md` (structure, components, density, tables, forms),
   `ux-workflows.md` (task flows, search/filter, bulk actions,
   permissions, notifications, error/empty/loading),
   `data-visualization.md` (charts, dashboards, metrics).
   Most real tasks span two; read both rather than guessing.

3. **Read the foundations the task touches** — tokens, component states,
   surfaces and affordance, dark mode, UI copy, illustration,
   accessibility. See the table below.

4. **Add cross-cutting rules** where they apply: `mobile-product-ui.md`
   for mobile or native surfaces, `ai-assisted-interactions.md` for any
   generated, suggested or agentic behavior.

5. **Only then choose a visual treatment**, and only after the functional
   model and every state are defined. Read the treatment's constraints in
   full — each one lists contexts it must not be used in.

6. **Apply the project's brand values on top** (brand source: MCP server,
   `brand.json`, or tokens — ask if absent, never invent).

7. Respect the references' normative language (must/should/may). Keyboard
   paths, focus, and ARIA on complex widgets are part of done.

8. When changing a shared design system rather than one screen —
   `design-system-governance.md`.

9. Defer code mechanics to the framework/Tailwind skills.

## Reference files

### Core product UX

| File | Contents |
|---|---|
| `references/ui-design-system.md` | Product UI system: layout/density, navigation chrome, tables, forms, feedback (incl. toasts), states, component rules |
| `references/ux-workflows.md` | Workflow patterns: task flows, search & filtering, bulk actions, permissions, notifications policy, error/empty/loading behavior |
| `references/data-visualization.md` | Data visualization: chart selection, dashboards, metrics presentation, visualization accessibility |

### Application types

| File | Contents |
|---|---|
| `references/saas-product-ui.md` | Authenticated SaaS app: shell, workspace/org switching, onboarding, settings architecture, billing, integrations, trials & limits, admin vs end-user UI |
| `references/user-portal-ui.md` | Self-service portal for individuals: task-based navigation, status in plain language, requests, documents, consent/privacy, payments, human support routes |
| `references/customer-portal-ui.md` | B2B/B2C customer portal: account & site scope, orders, deliveries, invoices, contracts, service cases, assets, customer-side roles |
| `references/analytics-dashboard-ui.md` | Dashboards by type (operational/analytical/strategic/embedded): the dashboard question, KPI anatomy, filters, drill-down, real-time and stale data, saved views |
| `references/operational-control-panel-ui.md` | High-consequence control: environment & live/simulation context, severity model, alarm anatomy, command lifecycle, authorization, audit, offline/degraded behavior |

### Cross-cutting surfaces

| File | Contents |
|---|---|
| `references/mobile-product-ui.md` | Mobile & native: platform conventions, one-handed use, touch targets, safe areas, offline, notifications, biometrics, permissions |
| `references/ai-assisted-interactions.md` | AI in product UI: interaction types, entry points, output anatomy, grounding & sources, human review, agentic actions, reversibility, uncertainty |

### Foundations

| File | Contents |
|---|---|
| `references/design-tokens.md` | Token layers (primitive → semantic → component), naming, required domains, theme architecture, canonical source, versioning & deprecation |
| `references/component-anatomy-states.md` | Component API and anatomy, state model, disabled vs read-only, loading, empty, error, composition, variants, maturity, quality gates |
| `references/affordance-depth-and-surfaces.md` | What reads as interactive: surface hierarchy, affordance cues, flat vs bordered vs elevated, elevation semantics, tonal surfaces, drag, forced colors |
| `references/dark-mode-theme-system.md` | Light/dark as a theme system: semantic roles per appearance, system/light/dark user control, contrast per state, theme-specific assets, charts, code, focus |
| `references/content-design.md` | UI copy: labels, headings, instructions, error and empty-state text, confirmations, terminology, units, localization, AI-generated content |
| `references/product-illustration-system.md` | Illustration inside products: roles, productive vs expressive, scale tiers, representation of people, technical accuracy, alt-text decisions, rights |
| `references/accessibility-foundations.md` | Keyboard access, focus management, accessible names, dynamic updates, contrast, reflow, motion safety, testing strategy |

### Visual treatments

Read only after the functional model and states are defined. Each file
states the contexts its treatment must **not** be used in.

| File | Contents |
|---|---|
| `references/flat-and-elevated-ui.md` | The default combination: flat base, bordered forms, elevation reserved for real overlap; card types, navigation selection, dark-mode substitution |
| `references/glassmorphism-translucent-ui.md` | Translucent materials: transient surfaces only, contrast against uncontrolled backgrounds, opaque fallback, reduced-transparency, performance, no glass over dense data |
| `references/neumorphism-soft-ui-constraints.md` | Experimental and limited — mostly a guard: ruled out for forms, primary actions, auth, tables and regulated workflows; testing gate before any use |
| `references/skeuomorphic-spatial-controls.md` | Physical metaphors and instruments: dials, switches, sliders, direct manipulation, precision entry, safety and simulation-vs-live distinction |

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
