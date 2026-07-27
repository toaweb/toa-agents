# Analytics Dashboard UI/UX 2026

> Rules for authenticated operational, analytical, strategic, and embedded dashboards.

## 1. Purpose

A dashboard should help a defined audience answer a question, identify change, investigate causes, and take action.

It is not a collection of charts.

## 2. Dashboard types

### Operational

Current work, exceptions, queues, and alerts.

### Analytical

Exploration, filters, comparison, drill-down, and hypotheses.

### Strategic

Goals, trends, targets, ownership, and periodic review.

### Embedded

A small contextual view inside a workflow.

Define the type before choosing visualizations.

## 3. Dashboard question

Document:

```text
audience
primary question
decision
action
data source
update cadence
comparison
risk
```

A dashboard should have one dominant purpose.

## 4. Layout hierarchy

Recommended order:

```text
context and filters
critical alert/action
primary indicators
trend/comparison
diagnostic detail
records
source and definitions
```

Give more area to more important information.

## 5. KPI anatomy

Every KPI needs:

- name;
- value;
- unit;
- period;
- scope;
- comparison;
- target where relevant;
- update time;
- definition.

Avoid naked numbers.

## 6. Filters

Distinguish global and local filters. Preserve them during drill-down and make current context visible.

## 7. Drill-down

A useful path:

```text
KPI
→ chart segment
→ filtered records
→ object detail
→ action
```

Preserve return context.

## 8. Charts

Choose charts from the question. Use tables for exact values and operational records.

Avoid gauges, 3D charts, and color-heavy decoration.

## 9. Real-time data

Show:

- connection;
- last update;
- delay;
- stale state;
- paused state;
- retry.

Do not continuously animate all updates.

## 10. Missing and partial data

Distinguish zero, no data, unknown, not applicable, estimated, delayed, partial, and permission-restricted.

## 11. Saved dashboards

Support personal and shared views, filter state, ownership, revision, and default setting.

## 12. AI insights

Separate:

```text
observed data
calculation
generated interpretation
recommended action
```

Provide evidence and verification.

## 13. Responsive layout

Material guidance notes that layouts commonly move from one pane to two or three as space increases.

On mobile, prioritize one question, stack modules, simplify charts, and retain table access.

## 14. Accessibility

Provide plain-language summaries, keyboard interaction, direct labels, non-color cues, table equivalents, focus, and source.

## 15. Performance

Load critical indicators first, cancel superseded filter requests, preserve prior data during safe refresh, and avoid rendering many hidden charts.

## 16. Anti-patterns

Avoid dashboard-as-homepage by default, equal KPI cards, charts without units, hidden filters, auto-refresh that interrupts reading, and AI explanations without evidence.

## 17. Agent rules

An AI agent must define the audience question, action path, data states, comparison, drill-down, accessibility alternative, and update behavior.

## 18. Checklist

- [ ] Dashboard type
- [ ] Audience/question
- [ ] Decision/action
- [ ] KPI context
- [ ] Global/local filters
- [ ] Drill-down
- [ ] Missing/stale data
- [ ] Real-time behavior
- [ ] Saved views
- [ ] AI evidence
- [ ] Mobile
- [ ] Accessibility


## Research basis

Primary and current references:

- W3C, Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- Material Design 3, Breakpoints and adaptive panes: https://m3.material.io/foundations/layout/breakpoints
- Material Design 3, Navigation drawer: https://m3.material.io/components/navigation-drawer/guidelines
- Material Design 3, Navigation bar: https://m3.material.io/components/navigation-bar
- Microsoft Windows App NavigationView: https://learn.microsoft.com/en-us/windows/apps/develop/ui/controls/navigationview
- Microsoft Windows App Settings: https://learn.microsoft.com/en-us/windows/apps/design/app-settings/guidelines-for-app-settings
- IBM Carbon Design System: https://carbondesignsystem.com/
- IBM Carbon Empty States: https://carbondesignsystem.com/patterns/empty-states-pattern/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines

