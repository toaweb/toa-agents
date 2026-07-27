# Permissions, Roles & Audit Patterns 2026

> Rules for access control presentation, role management, approvals, audit history, and high-impact actions.

## 1. Purpose

Users need to understand what they can do, why something is unavailable, who controls access, and what happened to important records.

## 2. Permission model

Document:

```text
role
resource
action
scope
condition
inheritance
exception
owner
```

The UI reflects authoritative backend permission; it does not enforce security by itself.

## 3. Hidden versus disabled

Hide actions that are irrelevant or would reveal sensitive information. Disable actions when users benefit from seeing that the capability exists and why it is unavailable.

## 4. Explanation

Where safe, explain required role, object state, approval, or next step.

Avoid leaking the existence of restricted records.

## 5. Role management

Show role purpose and capability summary. Avoid only internal permission codes.

For custom roles, support comparison, search, dependencies, and clear scope.

## 6. Invitations

Show recipient, role, workspace, expiry, status, resend, revoke, and security implications.

## 7. Approvals

Approval views should show identity, submitter, changes, evidence, risk, comments, and allowed actions.

Do not force approvers to reconstruct context across several pages.

## 8. High-impact actions

Require clear consequence, object identity, authority, and sometimes reason. Use step-up authentication when risk justifies it.

## 9. Audit history

Record:

- actor;
- time;
- action;
- object;
- old/new values;
- source;
- reason;
- automated versus human;
- correlation/reference.

Make history filterable and understandable.

## 10. Version history

Allow comparison and restoration where appropriate. Explain downstream consequences.

## 11. AI and automation

Audit AI recommendations and agentic actions separately from human approval. Show model/tool identity, sources, user confirmation, and execution result where relevant.

## 12. Accessibility

Permission messages, role matrices, and audit tables must work with keyboard and screen readers. Do not encode permission only through lock icons.

## 13. Anti-patterns

Avoid vague “Access denied,” client-side-only permissions, giant unreadable matrices, hidden approval changes, mutable audit records, and AI actions attributed to the user.

## 14. Agent rules

An AI agent must not invent permissions. It must show backend authority, explain safe restrictions, define audit events, and preserve human versus automated attribution.

## 15. Checklist

- [ ] Model and scope
- [ ] Hide/disable policy
- [ ] Safe explanation
- [ ] Roles/custom roles
- [ ] Invitations
- [ ] Approval context
- [ ] High-impact review
- [ ] Audit fields
- [ ] Version restoration
- [ ] AI attribution


## Research basis

Primary references:

- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/patterns/
- GOV.UK Design System patterns: https://design-system.service.gov.uk/patterns/
- U.S. Web Design System components: https://designsystem.digital.gov/components/overview/
- IBM Carbon patterns: https://carbondesignsystem.com/patterns/overview/
- Material Design 3 components: https://m3.material.io/components
- Atlassian Design System: https://atlassian.design/
- Shopify Polaris: https://polaris.shopify.com/

