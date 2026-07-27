# Product Data Visualization

> Brand-neutral reference for dashboards, KPI systems, data tables, charts, diagrams, status visualization, reporting, monitoring, and accessible analytics in enterprise applications.

---

## 1. Purpose

Product data visualization should help users understand current state, identify exceptions, compare values, detect change, diagnose causes, verify evidence, make decisions, and take action.

A dashboard is not a collection of charts. It is a structured decision interface.

---

## 2. Dashboard categories

### Operational dashboard

Used to monitor current work, surface exceptions, manage queues, and respond quickly. Emphasizes current data, alerts, tasks, status, and compact records.

### Analytical dashboard

Used to explore, compare, filter, drill down, and identify causes or patterns. Emphasizes richer controls, longer time ranges, and multiple dimensions.

### Strategic dashboard

Used to track goals, review trends, and support periodic decisions. Emphasizes fewer metrics, targets, ownership, and narrative context.

### Embedded dashboard

Provides narrow, object-specific insight inside an operational workflow.

### Narrative report

Explains what happened and why using ordered text, annotations, charts, and a clear conclusion.

Do not mix all dashboard categories without hierarchy.

---

## 3. Design process

1. Identify the audience.
2. Identify the decision.
3. Identify the questions.
4. Identify the available actions.
5. Verify the data.
6. Define update frequency.
7. Define comparison or target.
8. Choose the representation.
9. Design drill-down.
10. Add accessible equivalents.
11. Test with real data and edge cases.

Do not begin with chart selection.

---

## 4. Information hierarchy

```text
Action required
Critical state
Primary indicators
Trend and comparison
Diagnostic detail
Raw records
Methodology and source
```

The most prominent element should be the most decision-relevant, not merely the largest number.

---

## 5. KPI design

A KPI needs:

- label;
- value;
- unit;
- period;
- scope;
- comparison;
- target where relevant;
- update time;
- source or definition;
- status only when rule-based.

Bad:

```text
98%
```

Better:

```text
On-time delivery
98.2%
Last 30 days
Target ≥ 97%
Updated 14:05
```

### Comparisons

Use previous period, same period last year, target, forecast, baseline, peer group, or SLA.

Do not show a green upward arrow when an increase is undesirable, such as incidents or delays.

### KPI cards

Use for a small set of primary indicators. Avoid ten equally prominent cards, ambiguous color logic, percentages without denominators, decorative sparklines, and animated count-up by default.

---

## 6. Representation selection

| User question | Recommended representation |
|---|---|
| Exact value | Table or KPI |
| Category comparison | Bar chart |
| Change over time | Line chart |
| Part-to-whole | Stacked bar; pie only for few simple parts |
| Relationship | Scatter plot |
| Spatial distribution | Map only when location matters |
| Distribution | Histogram or box plot |
| Sequence | Timeline or process diagram |
| Current state | Status summary or operational table |
| Cause | Drill-down, decomposition, annotated comparison |
| Required action | Prioritized queue or exception table |

Use a table when precise values matter more than visual pattern.

---

## 7. Chart rules

### Bar charts

- Use for category comparison.
- Start quantitative axes at zero unless a justified exception is clearly marked.
- Sort meaningfully.
- Use horizontal bars for long labels.
- Avoid 3D.
- Label values directly where useful.

### Line charts

- Use for ordered time.
- Show gaps honestly.
- Distinguish actual, forecast, and target.
- Limit series.
- Include time-zone and aggregation context.
- Avoid smoothing that implies false values.

### Area charts

Use when filled magnitude has meaning. Avoid opaque overlap that hides values.

### Pie and donut

Use only for a small, clear part-to-whole relationship. Prefer bars for many or similar categories.

### Scatter plots

Use for relationship and outliers. Include units, sample size, and accessible descriptions.

### Histograms and box plots

Use when distribution and variation matter. Do not replace them with a single average.

### Gauges

Avoid speedometer gauges for ordinary KPIs. Prefer bullet charts, progress bars, target bands, and labeled values.

### Complex flow and network charts

Use only when relationships are the subject. Provide a simplified explanation and accessible equivalent.

---

## 8. Axes and scales

- Include units.
- Use consistent precision.
- Avoid misleading truncation.
- Mark logarithmic scales.
- Keep tick intervals understandable.
- Avoid dual axes unless necessary and clearly explained.
- Distinguish missing data from zero.
- Show uncertainty where material.
- Explain normalization.

---

## 9. Color

### Semantic color

Use stable meanings for error, warning, success, information, neutral, and inactive. Do not rely on red and green alone.

### Categorical color

Use distinguishable hues for unordered categories. Limit category count and keep mapping consistent across views.

### Sequential color

Use light-to-dark for low-to-high values.

### Diverging color

Use around a meaningful midpoint such as zero, target, or acceptable range.

### Highlight color

Reserve one strong color for selected or important data. Do not color every element equally.

---

## 10. Labels and annotation

Include:

- clear title;
- question or conclusion subtitle;
- axis labels;
- units;
- direct labels;
- update time;
- source;
- annotation for significant events;
- definition access.

Prefer direct labels over distant legends. Annotations should explain why a change matters, not merely repeat the value.

---

## 11. Tables as visualization

Tables are best for exact values, many dimensions, operational records, scanning, sorting, filtering, bulk actions, and audit data.

### Anatomy

```text
Title and context
Search/filter toolbar
Column headers
Rows
Status and actions
Selection state
Result count
Pagination
```

### Numeric formatting

- Right-align values.
- Use tabular numerals.
- Include units.
- Use consistent precision.
- Use locale-aware separators.
- Distinguish negative values.
- Show time zone where relevant.
- Do not over-round critical data.

### Enhancements

Possible features include sticky headers, pinned identifier column, column visibility, resizing, grouping, totals, expandable rows, conditional formatting, inline trends, and export. Add only what supports tasks.

### Conditional formatting

Use for overdue items, threshold breaches, missing required data, selected records, or recent change. Avoid rainbow heatmaps and low-contrast text.

---

## 12. Status visualization

Status requires a stable label and may include icon, color, and update time.

Example:

```text
✓ Complete
! Requires review
× Blocked
○ Draft
↻ Processing
```

Distinguish workflow state, data quality, system health, permission, risk, and completion. Do not compress every meaning into one badge system.

---

## 13. Alerts and thresholds

An alert should identify:

- what happened;
- severity;
- affected scope;
- time;
- threshold or rule;
- recommended action;
- owner;
- acknowledgement state.

Do not leave resolved issues as permanent red banners. Thresholds must be documented and permission-controlled.

---

## 14. Drill-down

Recommended path:

```text
KPI
→ filtered chart
→ relevant records
→ object detail
→ action
```

Preserve filter context, time range, selected category, and return position. A KPI should not open an unrelated generic report.

---

## 15. Filters and comparison

Dashboard filters may include date range, location, business unit, customer, product, status, owner, or category.

Rules:

- Show global versus local scope.
- Display current filters.
- Preserve them through drill-down.
- Provide comparison mode where useful.
- Indicate unavailable combinations.
- Never silently reset filters.

---

## 16. Time

Time-based data needs exact period, aggregation, time zone, update cadence, latency, actual versus estimate, and comparison period.

Distinguish event time, processing time, last updated, reporting period, and forecast horizon.

---

## 17. Real-time data

Show connection status, last update, paused state, stale state, delayed data, and retry behavior.

Do not animate every incoming event. Batch updates when constant change would prevent reading.

---

## 18. Missing, partial, and stale data

Represent separately:

```text
Zero
No data
Not applicable
Unknown
Delayed
Partial
Estimated
Failed
Hidden by permission
```

Do not convert missing data to zero. Explain how partial data affects conclusions.

---

## 19. Forecasts and uncertainty

Show the historical/forecast boundary, uncertainty interval, method or definition, update date, and material assumptions.

Do not present model output as confirmed fact.

---

## 20. Maps

Use only when spatial relationships matter.

- Reduce irrelevant basemap detail.
- Label important locations.
- Avoid hover-only information.
- Provide list or table equivalent.
- Disclose clustering and aggregation.
- Avoid decorative world maps.

---

## 21. Process and system diagrams

Use for lifecycle, architecture, workflow, dependency, responsibility, routes, sequence, and data flow.

Rules:

- One primary message.
- Consistent node shapes and connector meanings.
- Predictable direction.
- Minimal line crossing.
- Clear labels.
- Simplified responsive version.
- Text alternative.

---

## 22. Dashboard layout

Recommended order:

```text
Page context
Critical alert or action queue
Primary metrics
Primary trend or comparison
Diagnostic view
Supporting details
Record table
Definitions and source
```

Rules:

- Give more space to more important information.
- Avoid identical card sizes for unequal content.
- Align related modules.
- Keep critical state visible without excessive scrolling.
- Let modules expand into detail views.
- Avoid decorative whitespace that displaces useful data.

---

## 23. Interaction

Useful interactions include focus or hover detail, selection, filter, range selection, drill-down, compare, annotate, export, open records, and save view.

All hover interactions need keyboard or touch equivalents. Do not use interaction to hide basic meaning.

---

## 24. Tooltips

Tooltips may show precise value, date, category, comparison, and definition.

They must be keyboard-accessible, stable enough to read, concise, consistently formatted, and never the sole location of critical information.

---

## 25. Accessibility

Important visualizations require:

- descriptive title;
- concise plain-language summary;
- keyboard access if interactive;
- screen-reader labels;
- non-color distinctions;
- sufficient contrast;
- visible focus;
- table or structured-text equivalent;
- downloadable machine-readable data where appropriate;
- update time and source;
- reduced-motion support.

For public or high-stakes dashboards, provide a status/trend summary, matching accessible table or CSV, and explicit source and update time.

---

## 26. Responsive design

Desktop may show multiple charts, dense tables, master-detail, and comparisons.

Compact layouts should:

- prioritize one question at a time;
- stack modules;
- simplify charts;
- provide table access;
- reduce category count;
- move filters to a drawer;
- preserve critical alerts and actions.

Do not shrink an unreadable desktop chart.

---

## 27. Export and reporting

Exports should preserve title, filters, period, source, update time, units, definitions, and owner where relevant.

Use:

- CSV for raw data;
- XLSX for working tables;
- PDF for fixed reports;
- image for presentation;
- shareable link for interactive state.

Do not export unlabeled charts.

---

## 28. Data provenance

Users should be able to discover source, owner, refresh frequency, definition, transformations, exclusions, quality notes, last updated, and contact for questions.

Do not hide metric definitions in inaccessible documentation.

---

## 29. AI-generated insights

AI may summarize trends, identify anomalies, propose explanations, suggest follow-up questions, or draft narrative reports.

Separate:

```text
Observed data
Calculated result
Generated interpretation
Recommended action
```

Provide evidence links and verification paths. Generated prose must not replace access to charts and records.

---

## 30. Performance

Data-heavy views should:

- load priority content first;
- use structural skeletons;
- paginate or virtualize responsibly;
- cache stable definitions;
- debounce expensive filters;
- communicate query progress;
- cancel superseded requests;
- handle partial responses;
- preserve prior data during safe refresh.

---

## 31. Anti-patterns

Avoid:

- dashboards with no decision or action;
- KPI cards without context;
- every metric shown as a chart;
- 3D charts;
- gauges for ordinary values;
- red/green-only status;
- hidden units or periods;
- misleading axes;
- rainbow palettes;
- hover-only data;
- auto-refresh that interrupts reading;
- missing data shown as zero;
- maps where geography is irrelevant;
- AI summaries without evidence;
- exports without filter context;
- charts with invented production data.

---

## 32. AI-agent instructions

An AI agent must:

1. identify the user question;
2. identify the decision;
3. verify data availability;
4. choose the simplest representation;
5. include units and time;
6. define comparison;
7. define missing-data behavior;
8. define drill-down;
9. define accessibility equivalent;
10. define responsive transformation;
11. document source and definition;
12. avoid invented data;
13. distinguish observation from interpretation;
14. define loading and stale states;
15. test extreme and empty values.

---

## 33. Production checklist

### Purpose

- [ ] Audience defined
- [ ] Dashboard type defined
- [ ] Decision defined
- [ ] Action path defined
- [ ] Update cadence defined

### Metrics

- [ ] Label
- [ ] Value
- [ ] Unit
- [ ] Period
- [ ] Scope
- [ ] Comparison
- [ ] Target
- [ ] Definition
- [ ] Source
- [ ] Updated time

### Charts and tables

- [ ] Correct representation
- [ ] Honest axes
- [ ] Direct labels
- [ ] Accessible colors
- [ ] Missing data handled
- [ ] Uncertainty shown
- [ ] Mobile version
- [ ] Table or text alternative

### Interaction and states

- [ ] Filters visible
- [ ] Global/local scope clear
- [ ] Drill-down preserves context
- [ ] Keyboard and touch access
- [ ] Loading
- [ ] Empty
- [ ] Partial
- [ ] Stale
- [ ] Error
- [ ] Permission denied

### Accessibility

- [ ] Plain-language summary
- [ ] Structured table or CSV
- [ ] Screen-reader labels
- [ ] Non-color distinctions
- [ ] Visible focus
- [ ] Reduced motion

---

## 34. Research basis

- Carbon dashboard guidance: https://v10.carbondesignsystem.com/data-visualization/dashboards/
- Carbon data table: https://carbondesignsystem.com/components/data-table/usage/
- Carbon empty states: https://carbondesignsystem.com/patterns/empty-states-pattern/
- Atlassian dynamic table: https://atlassian.design/components/dynamic-table
- Dashboard Design Patterns research: https://arxiv.org/abs/2205.00757
- Accessibility Gaps in U.S. Government Dashboards: https://arxiv.org/abs/2511.06688
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
- IBM data overview: https://www.ibm.com/think/topics/data
- Fuselab dashboard trends 2026: https://fuselabcreative.com/top-dashboard-design-trends-2025/

---

## 35. Final rule

A product visualization succeeds when the user can understand what happened, verify why it matters, reach the underlying records, and take the correct next action.
