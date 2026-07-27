# Feedback, Loading, Empty & Error States 2026

> Rules for system status, notifications, progress, failure, partial data, offline behavior, and recovery.

## 1. Purpose

The interface must continuously communicate what happened, what is happening, what is affected, and what the user can do.

## 2. Feedback levels

Use:

```text
field
component
section
page
global system
persistent notification history
```

Place feedback at the smallest scope that accurately represents the issue.

## 3. Loading

Use skeletons for known structure, spinners for short localized work, progress bars for measurable tasks, and background-job status for long operations.

Preserve existing data during refresh when safe.

## 4. Success

Use inline confirmation for local actions and toasts for brief noncritical confirmation. Persist success when the user needs a reference or next step.

## 5. Errors

State:

- what failed;
- affected scope;
- what remains safe;
- recovery;
- support reference when needed.

Do not expose raw stack traces to normal users.

## 6. Partial success

List succeeded and failed items. Allow retry of failed items without repeating successful work.

## 7. Empty states

Differentiate:

- first use;
- no results;
- completed work;
- setup required;
- permission restricted;
- load failed.

## 8. Offline and stale data

Show connection state, last update, queued work, and synchronization status.

Do not present stale data as current.

## 9. Notifications

Classify by urgency and persistence. Include source, time, object, reason, and action.

Avoid sending the same low-value event as toast, email, push, and persistent notification.

## 10. Banners and dialogs

Use banners for persistent scoped issues. Use dialogs for decisions requiring immediate attention.

Do not use modal dialogs for routine informational messages.

## 11. Session and timeout

Warn before timeout, preserve work, and offer extension where security permits.

## 12. Accessibility

Announce meaningful changes without overwhelming. Manage focus for blocking errors and dialogs. Do not rely on color.

## 13. Anti-patterns

Avoid permanent spinners, success toasts for actions that actually failed later, generic “Something went wrong,” decorative empty states without action, and stale data without a timestamp.

## 14. Agent rules

An AI agent must define every asynchronous and failure state, including partial success, offline, retry, cancellation, and accessible announcements.

## 15. Checklist

- [ ] Scope
- [ ] Loading type
- [ ] Success persistence
- [ ] Error recovery
- [ ] Partial success
- [ ] Empty-state causes
- [ ] Offline/stale
- [ ] Notification policy
- [ ] Timeout
- [ ] Accessibility


## Research basis

Primary references:

- W3C, ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/patterns/
- GOV.UK Design System patterns: https://design-system.service.gov.uk/patterns/
- U.S. Web Design System components: https://designsystem.digital.gov/components/overview/
- IBM Carbon patterns: https://carbondesignsystem.com/patterns/overview/
- Material Design 3 components: https://m3.material.io/components
- Atlassian Design System: https://atlassian.design/
- Shopify Polaris: https://polaris.shopify.com/

