# User Portal UI/UX 2026

> Rules for authenticated self-service portals where individuals view and manage their own account, records, documents, preferences, requests, and support.

## 1. Purpose

A user portal should let a person understand their relationship with a service and complete common self-service tasks without needing expert knowledge.

Typical content:

- profile;
- status;
- applications;
- appointments;
- documents;
- messages;
- preferences;
- consent;
- payments;
- support.

## 2. Primary principle

Organize around the user's tasks and life cycle, not the organization's departments.

Good navigation:

```text
Overview
My requests
Documents
Messages
Payments
Profile
Help
```

Weak navigation:

```text
Operations
Administration
Records Management
```

## 3. Portal homepage

The homepage should answer:

- What needs attention?
- What changed?
- What is the status?
- What can I do now?
- Where can I get help?

Prioritize actionable items over generic dashboard metrics.

## 4. Status

Show:

```text
current state
last update
next expected step
responsible party
estimated timing when reliable
required user action
```

Avoid internal workflow codes.

## 5. Requests and applications

Provide a clear list, filters where volume requires it, detail pages, history, attachments, and next steps.

Preserve drafts and explain submission consequences.

## 6. Documents

Show title, type, date, source, status, version, file size, and accessible preview or summary.

Do not present raw filenames as the main label.

## 7. Messages and notifications

Separate service messages, support conversations, security alerts, and marketing communication.

Let users control nonessential notification channels.

## 8. Profile and identity

Separate editable contact details from verified identity attributes. Explain why locked fields cannot be changed and how to request correction.

## 9. Consent and privacy

Provide clear consent history, current choices, data access, export, and withdrawal where applicable.

## 10. Payments

Show amount, currency, due date, status, invoice, payment method, refund, and support.

Do not hide fees or renewal conditions.

## 11. Support

Offer contextual help, searchable guidance, contact methods, expected response, and accessibility support.

Do not force chatbot use as the only route.

## 12. Empty states

A new user may legitimately have no requests or documents. Explain what the section is for and whether an action is expected.

## 13. Navigation

Use a small, stable set of destinations. On compact screens use a navigation bar for a few high-frequency areas or a clear drawer/stack for broader structures. Material distinguishes navigation bars for smaller devices and drawers for larger or broader app structures.

## 14. Security

Include session/device history, password or passkey management, MFA, recovery, sign-out-all, and suspicious-activity reporting where relevant.

## 15. Accessibility and plain language

Assume mixed digital confidence. Use direct labels, visible focus, persistent form labels, clear errors, zoom/reflow, and understandable status.

## 16. Anti-patterns

Avoid admin terminology, metric-heavy dashboards, hidden support, raw document IDs, unexplained status, and requiring users to call for routine self-service actions.

## 17. Agent rules

An AI agent must design around personal tasks, translate internal status into user language, preserve privacy boundaries, and provide a non-AI support route.

## 18. Checklist

- [ ] Task-based navigation
- [ ] Attention/status overview
- [ ] Request history
- [ ] Draft preservation
- [ ] Document metadata
- [ ] Notification control
- [ ] Identity/correction
- [ ] Consent/privacy
- [ ] Payment clarity
- [ ] Human support
- [ ] Security
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

