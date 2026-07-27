# AI-Assisted Interaction Patterns 2026

> Rules for AI suggestions, generation, extraction, summarization, natural-language control, and agentic actions in product interfaces.

## 1. Purpose

AI should help users understand, draft, find, classify, or act without concealing uncertainty, source, cost, permission, or consequence.

## 2. AI interaction types

Distinguish:

```text
search
summarization
extraction
classification
recommendation
generation
prediction
automation
agentic action
```

Each type needs different review and risk controls.

## 3. Entry point

Use contextual AI entry points where the task exists. A global assistant may supplement but should not replace normal navigation and controls.

## 4. Prompting

Provide examples, scope, available data, and expected output. Do not require users to learn hidden prompt syntax for routine tasks.

## 5. Output anatomy

Show:

- generated status;
- sources;
- uncertainty;
- affected scope;
- edit;
- accept/reject;
- retry;
- feedback;
- cost/usage when relevant.

## 6. Sources and grounding

Cite the records, documents, or data used. Let users inspect them.

Do not invent a source display when the system is not actually grounded.

## 7. Human review

Require review for high-impact, regulated, financial, legal, health, employment, security, or external actions.

Review should show changed fields and consequences, not only generated prose.

## 8. Agentic actions

Before execution, show:

```text
goal
planned steps
systems affected
permissions
data sent
external side effects
cost
reversibility
confirmation
```

During execution, show progress and stop controls. After execution, show results, failures, and audit.

## 9. Reversibility

Provide undo, draft, preview, version history, or recovery where possible.

Do not describe an action as reversible when external consequences already occurred.

## 10. Uncertainty

Use plain language and relevant confidence information. Avoid false numerical precision.

## 11. Failure

Handle unavailable model, timeout, unsafe request, missing permission, weak source, partial result, and conflicting data.

Provide a conventional workflow alternative.

## 12. Privacy and data

Explain which data is used, retained, shared, and available to administrators. Respect workspace boundaries and least privilege.

## 13. Personalization

Allow users to understand and reset personalization. Do not silently alter canonical facts or pricing.

## 14. Feedback

Collect useful feedback without presenting it as guaranteed model training. Explain what feedback does.

## 15. Accessibility

Generated content must be navigable, announced appropriately, and available without motion. Streaming output should not overwhelm screen readers.

## 16. Content safety

Do not allow generated output to bypass product policy, permissions, validation, or domain review.

## 17. Anti-patterns

Avoid magic sparkle buttons everywhere, AI-only workflows, hidden sources, auto-execution, fake confidence, anthropomorphic certainty, generated decisions attributed to users, and chat replacing structured controls.

## 18. Agent rules

An AI agent designing AI UI must classify risk, expose sources and permissions, define review, stop, undo, audit, conventional fallback, and partial-failure behavior.

## 19. Checklist

- [ ] Interaction type
- [ ] Contextual entry
- [ ] Scope/examples
- [ ] Sources
- [ ] Uncertainty
- [ ] Human review
- [ ] Permissions
- [ ] Plan/progress/stop
- [ ] Undo/recovery
- [ ] Privacy/cost
- [ ] Accessibility
- [ ] Conventional fallback


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

