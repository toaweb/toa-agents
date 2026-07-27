# Customer Portal UI/UX 2026

> Rules for authenticated B2B or B2C customer portals covering orders, deliveries, contracts, invoices, service cases, assets, contacts, and account collaboration.

## 1. Purpose

A customer portal should create a shared, reliable view of the commercial and service relationship.

Common domains:

- orders;
- shipments;
- subscriptions;
- invoices;
- contracts;
- service cases;
- installed products;
- documents;
- users and roles;
- account contacts.

## 2. Account context

Make current customer account, organization, site, or contract visible.

Users with access to several accounts need a safe switcher that explains scope and permissions.

## 3. Homepage

Prioritize:

- items needing action;
- open cases;
- upcoming deliveries;
- overdue invoices;
- contract changes;
- recent documents;
- service alerts.

Do not show decorative KPIs that offer no action.

## 4. Orders and deliveries

Show:

```text
reference
status
items
dates
locations
tracking
documents
contacts
exceptions
history
```

Distinguish estimate, planned, confirmed, dispatched, delivered, delayed, and cancelled.

## 5. Invoices and payments

Provide invoice status, due date, amount, currency, payment route, credit notes, disputes, and download.

Support bulk download and export for business customers.

## 6. Contracts and subscriptions

Show active term, renewal, included services, usage, amendments, notices, and responsible contacts.

Do not hide cancellation or renewal conditions.

## 7. Service cases

A case should include issue, priority, status, owner, messages, attachments, service-level target, timeline, and resolution.

Avoid presenting internal support categories without explanation.

## 8. Assets and installed products

Show model, serial/asset ID, location, warranty, service history, manuals, spare parts, and actions.

## 9. Documents

Use search, filtering, categories, revision, language, status, and accessible preview.

## 10. Customer organization

Support invitations, role scopes, locations, billing contacts, technical contacts, and deactivation.

Do not let customer admins assign privileges beyond their authorized scope.

## 11. Collaboration

Provide comments, assignments, mentions, shared history, and audit for high-value workflows.

## 12. Notifications

Allow preferences by account, site, object type, severity, and channel.

Critical security or service alerts may be mandatory but should be clearly distinguished.

## 13. Navigation

A persistent left navigation works well for many stable B2B areas. Microsoft NavigationView guidance recommends left navigation when several equally important top-level categories must remain prominent.

## 14. Mobile

Prioritize status, tracking, cases, documents, approvals, and contact. Complex account administration may remain desktop-oriented with a clear message.

## 15. Accessibility

Tables, filters, document lists, messages, and account switching require full keyboard and screen-reader support.

## 16. Anti-patterns

Avoid mixing several customer accounts without a visible scope, internal codes, unclear invoice totals, hidden contract terms, static PDFs as the only data source, and support with no timeline.

## 17. Agent rules

An AI agent must define account scope, commercial object relationships, status semantics, document governance, roles, and exception workflows.

## 18. Checklist

- [ ] Account/site context
- [ ] Action-oriented overview
- [ ] Orders/deliveries
- [ ] Invoice clarity
- [ ] Contracts/renewal
- [ ] Service cases
- [ ] Assets/manuals
- [ ] Documents
- [ ] Customer roles
- [ ] Notifications
- [ ] Mobile priorities
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

