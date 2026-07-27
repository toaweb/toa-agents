# Product UI Design Tokens 2026

> Canonical, brand-neutral rules for defining, naming, governing, and consuming UI design tokens across web, desktop, mobile, and product surfaces.

## 1. Purpose

Design tokens turn design decisions into reusable, machine-readable values. They connect design tools, documentation, components, application code, themes, tests, and generated assets without hardcoding visual decisions in individual components.

A token system should answer:

- Which values are canonical?
- What does each token mean?
- Which tokens can a product override?
- Which values change by theme, density, platform, or state?
- Which tokens are deprecated?
- How are breaking changes communicated?

## 2. Token layers

Use three layers.

### Primitive tokens

Raw values without component meaning:

```text
color.blue.600
space.4
font.size.300
radius.200
duration.fast
```

### Semantic tokens

Values named by purpose:

```text
color.text.default
color.surface.canvas
color.border.subtle
color.action.primary
space.component.gap
```

### Component tokens

Values scoped to a component when shared semantic roles are insufficient:

```text
button.primary.background.default
data-grid.header.border
dialog.max-width
```

Prefer semantic tokens. Add component tokens only when the component has a real, repeatable need.

## 3. Naming rules

Names should describe purpose, not current appearance.

Good:

```text
color.text.muted
color.status.warning.background
space.form.section-gap
```

Weak:

```text
gray-500
yellow-box
big-gap
```

Primitive tokens may use visual names. Semantic and component tokens should not.

Use one naming convention across repositories. Generated code may transform canonical names into CSS custom properties, Swift constants, Kotlin resources, or TypeScript objects.

## 4. Required domains

Define at minimum:

- color;
- typography;
- spacing;
- size;
- adaptive class or breakpoint;
- radius;
- border width;
- elevation;
- opacity;
- icon size;
- control height;
- motion duration;
- motion easing;
- layering/z-index;
- focus;
- density;
- data-visualization color.

## 5. Color tokens

Do not expose only a brand palette. Define functional roles:

```text
text
icon
surface
border
action
focus
selection
status
disabled
overlay
data visualization
```

Every meaningful state needs values for supported surfaces and themes.

## 6. Typography tokens

A typography token should include more than font size:

```json
{
  "fontFamily": "ui",
  "fontSize": "1rem",
  "fontWeight": 400,
  "lineHeight": 1.5,
  "letterSpacing": "0"
}
```

Define roles such as body, label, heading, code, data, and display. Do not create a unique token for every text instance.

## 7. Spacing tokens

Use a small mathematical or curated scale, commonly based on 4px with 8px as a major rhythm.

Distinguish:

- inset;
- inline;
- stack;
- component gap;
- section gap;
- touch separation;
- compact/default/comfortable density.

Avoid undefined names such as `small`, `medium`, and `large`.

## 8. Responsive and platform tokens

Prefer semantic adaptive classes:

```text
compact
medium
expanded
large
```

Tokens may resolve differently by platform while retaining purpose. Touch targets, typography, and control height may differ between pointer and touch contexts.

## 9. Theme architecture

Themes may change color, elevation, selected-state treatment, chart palette, and material appearance.

Themes must not change component meaning, task order, or permission logic.

Support system preference where useful and provide a user override when persistence matters.

## 10. State tokens

Cover:

```text
default
hover
focus
active
selected
disabled
loading
error
warning
success
read-only
```

Do not generate all states through arbitrary opacity. Verify contrast and meaning independently.

## 11. Canonical source

Choose one version-controlled canonical format, normally JSON or a compatible design-token schema. Design-tool libraries and code packages should be generated or synchronized from it.

Never maintain independent hand-edited definitions in Figma, CSS, iOS, and Android without drift detection.

## 12. Versioning and deprecation

Classify changes:

- patch: metadata or nonvisual correction;
- minor: additive token;
- major: removal, rename, or changed meaning.

Deprecate before removal. Publish replacement, migration guidance, owner, and target removal version.

## 13. Validation

Automate checks for:

- duplicate names;
- invalid references;
- circular aliases;
- missing theme values;
- contrast;
- invalid units;
- unreferenced deprecated tokens;
- generated-output drift.

## 14. Anti-patterns

Avoid hardcoded values, component names in primitives, hundreds of near-duplicate spacing values, theme-specific component logic, undocumented roles, and tokens treated only as a visual palette.

## 15. Agent rules

An AI agent must inspect existing tokens before adding values, prefer semantic roles, preserve complete state coverage, document new concepts, and flag duplicate or contradictory tokens.

## 16. Checklist

- [ ] Canonical source
- [ ] Primitive/semantic/component layers
- [ ] Naming convention
- [ ] Themes and density
- [ ] Complete state coverage
- [ ] Contrast validation
- [ ] Platform generation
- [ ] Versioning/deprecation
- [ ] Drift detection
- [ ] Ownership


## Research basis

Primary references:

- W3C, Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- GOV.UK Design System: https://design-system.service.gov.uk/
- U.S. Web Design System: https://designsystem.digital.gov/
- IBM Carbon Design System: https://carbondesignsystem.com/
- Material Design 3: https://m3.material.io/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines
- Atlassian Design System: https://atlassian.design/
- GitHub Primer: https://primer.style/
- Adobe Spectrum: https://spectrum.adobe.com/
- Shopify Polaris: https://polaris.shopify.com/

Validate all rules with the actual audience, platform, language, product risk, and regulatory context.

