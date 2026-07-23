# Tailwind — mobile-first & accessibility reference

Stable responsive and accessibility rules (not version-specific). Apply on every
surface.

## Mobile-first breakpoints

- **Unprefixed utilities = mobile**, and apply at all sizes.
- `sm:` `md:` `lg:` `xl:` expand **upward** from the mobile base.
- Never start from a desktop layout and walk it back down with `md:`.

```html
<!-- CORRECT: mobile base, expands up -->
<div class="flex flex-col md:flex-row">

<!-- WRONG: desktop-first thinking -->
<div class="flex flex-row md:flex-col">
```

## Touch & input rules

- **Touch targets:** at least 44×44px — `min-h-[44px] min-w-[44px]` (or padding
  that reaches it) on anything tappable.
- **Form inputs:** always `text-base` (16px) minimum — smaller sizes trigger
  iOS's auto-zoom on focus.
- **Global:** `touch-action: manipulation` to remove the 300ms tap delay and
  avoid accidental double-tap zoom on interactive elements.

## Container queries

Use container queries (`@container`) for components that must adapt to **their
container's** width rather than the viewport — the correct tool for reusable
components that appear in sidebars, grids, and full-width slots alike.

```html
<div class="@container">
  <div class="flex flex-col @md:flex-row">…</div>
</div>
```

Container queries are first-class in Tailwind v4 (no plugin needed).

## Testing order

1. Test the mobile viewport first — it is the base layer.
2. Then verify each breakpoint upward.
3. Confirm touch targets and input sizing on a real small viewport, not just a
   desktop window narrowed down.
