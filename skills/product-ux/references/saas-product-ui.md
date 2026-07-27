# SaaS Product UI Design System 2026

> Rules for the authenticated SaaS application, not the public marketing website.

## 1. Purpose

A SaaS product UI must help individuals and teams reach value, understand system state, collaborate, configure the product, and manage account-level responsibilities.

## 2. Application shell

Define stable areas:

```text
product navigation
workspace or organization switcher
global search
notifications
help
user/account
main workspace
contextual panel
```

Do not mix account administration with daily work without clear separation.

## 3. Workspace model

Make current organization, workspace, project, or environment visible.

Switching context should explain impact on data, permissions, billing, and integrations.

## 4. Onboarding

Onboarding should lead to first value through real work.

Use:

- setup checklist;
- sample data;
- import;
- guided task;
- role-specific starting point;
- progress;
- skip and resume.

Avoid long forced tours and empty dashboards that only say “Create your first item.”

## 5. Team and collaboration

Support:

- invitations;
- roles;
- presence;
- comments;
- mentions;
- assignments;
- activity history;
- conflict handling;
- notification preferences.

Clearly distinguish personal, team, and organization settings.

## 6. Settings architecture

Separate:

```text
personal preferences
workspace settings
organization administration
security
integrations
billing
developer settings
```

Use deep links and search for large settings areas.

## 7. Billing

Show plan, billing period, usage, seats, add-ons, invoices, payment method, renewal, cancellation, and impact of changes.

Do not hide variable usage or make cancellation intentionally difficult.

## 8. Integrations

Show status, owner, permissions, direction, last sync, failure, reconnect, logs, and removal consequences.

API keys and secrets need clear creation, display-once, rotation, scope, expiry, and revocation patterns.

## 9. Notifications

Separate in-product, email, push, and system alerts. Let users control categories without losing critical security notifications.

## 10. Search and command palette

Global search may include objects, people, documents, settings, and commands.

Command palettes supplement navigation. They should not contain surprising irreversible actions.

## 11. Empty states

Use realistic paths:

- import;
- sample;
- invite;
- connect;
- create;
- learn.

Differentiate no data from no results and permission restrictions.

## 12. Feature discovery

Use contextual prompts, release notes, and optional tours. Do not cover the application in badges and coach marks.

## 13. Trials and limits

Show remaining time, usage, plan limits, and what happens after expiration. Preserve user work where possible.

## 14. Upgrade prompts

Place prompts at relevant limits. Explain value and cost. Avoid interrupting unrelated work.

## 15. Security

Provide session management, MFA, SSO, recovery, device history, role review, and audit where appropriate.

## 16. Admin versus end-user UI

Administrative features may use greater density and explicit risk controls. Do not expose admin complexity to ordinary users.

## 17. AI features

Explain AI input, output, source, uncertainty, human review, cost, and action scope. Provide undo and audit for consequential actions.

## 18. Mobile

Identify which workflows genuinely need mobile support. Preserve status, approvals, search, notifications, and quick actions without reproducing every desktop feature.

## 19. Accessibility

Apply native semantics, full keyboard support, focus management, accessible data grids, readable charts, captions, reduced motion, and zoom/reflow.

## 20. Anti-patterns

Avoid generic dashboards, hidden workspace context, settings scattered across the product, unclear usage billing, forced onboarding, AI chat on every page, and notifications with no control.

## 21. Agent rules

An AI agent must define account/workspace boundaries, roles, onboarding value, settings ownership, billing effects, integration states, and complete error/recovery behavior.

## 22. Checklist

- [ ] Shell and workspace context
- [ ] First-value onboarding
- [ ] Team/roles
- [ ] Settings architecture
- [ ] Billing/usage
- [ ] Integrations/secrets
- [ ] Notifications
- [ ] Search/commands
- [ ] Trial/upgrade
- [ ] Security/audit
- [ ] AI control
- [ ] Mobile/accessibility


## Research basis

Primary references:

- W3C, WCAG 2.2: https://www.w3.org/TR/WCAG22/
- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
- Material Design 3: https://m3.material.io/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines
- IBM Carbon Design System: https://carbondesignsystem.com/
- Atlassian Design System: https://atlassian.design/
- GitHub Primer: https://primer.style/
- Shopify Polaris: https://polaris.shopify.com/
- GOV.UK Design System: https://design-system.service.gov.uk/
- U.S. Web Design System: https://designsystem.digital.gov/

