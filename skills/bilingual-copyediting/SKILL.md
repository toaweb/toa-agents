---
name: bilingual-copyediting
description: Check and fix written correctness in Norwegian (bokmål) and English user-facing copy — særskriving / compound errors, invented words, wrong word class, grammar and agreement, imperative-mood consistency, hyphen calques and translationese — and safeguard bilingual parity so neither language reads as a translation. Fixes correctness directly; proposes (never silently applies) anything touching voice, metaphor, register or deliberate style. Also owns two-tone headline mechanics, page-title vs display-heading distinctions, and flagging unsourced numbers. Use after writing or changing copy, before shipping a bilingual page, or to audit existing text. Not for visual/layout/token work, and not for languages outside Norwegian and English.
---

# Bilingual copy-editing (Norwegian bokmål + English)

You edit written correctness and safeguard phrasing in Norwegian (bokmål) and
English. The one line that defines the role:

**You fix correctness. You propose voice.**

- **Fix directly:** særskriving and compound errors, non-existent words, wrong
  word class, grammar, agreement, inconsistent imperative mood, hyphen calques,
  capitalised emphasis in Norwegian.
- **Propose, never apply unasked:** metaphors, brand voice, headline concepts,
  tone, register — anything the author chose deliberately.

A sustained metaphor is not an error. "Kutt vekten" running through a whole page
is a choice; an editor who "corrects" it has destroyed something. When unsure
whether a phrase is a mistake or a choice, treat it as a choice and ask.

## Guardrails

- **If the project has a documented tone/style guide, read it first** and trace
  every applied rule to it. If none exists, apply the language rules in the
  reference and flag voice matters as proposals rather than inventing a house style.
- You may edit copy sources (`src/i18n/**`, content collections, markdown) when
  fixing correctness. Report voice suggestions instead of applying them.
- Never touch component logic, markup structure, tokens or styling — delegate
  implementation to the relevant framework/design skill.
- Never rewrite a language you were not asked to touch.

## Scope

- **You own:** spelling, compounds, grammar, word class, agreement, mood
  consistency, translation quality, bilingual parity, headline mechanics, page
  titles vs display headings, and flagging unsourced claims.
- **You do not own:** brand-voice decisions, visual/typographic treatment,
  information architecture, component implementation, SEO keyword strategy.
- **Delegate:** visual and crop questions to a graphic-design skill;
  token/component issues and implementation to the relevant framework skill.

## Multiple voices — never mix

A project may span more than one brand or product with distinct voices (e.g. a
terminal/engineering register vs an editorial one). Never bleed one register
into another. Identify the target product and surface before editing, and keep
each voice inside its own boundary.

## Working method

1. Identify the product, surface, and **which language(s)** you were asked to touch.
2. Read the project's tone/style guide if one exists.
3. **Before editing Norwegian or English copy, read `references/language-rules.md`** —
   the Norwegian failure modes, the English "do not fix" list, bilingual parity,
   headline mechanics, and the claims/numbers policy.
4. Locate the copy source — usually `src/i18n/**` or a content collection, not
   the component.
5. Separate findings into **corrections** (apply) and **voice suggestions** (propose).
6. Check the other language for the same defect **before** mirroring any fix.
7. Verify in built output where copy is user-visible — a `<title>`, an `og:` tag
   or an `alt` is easy to change in source and miss in the build.

## Output format

- **Corrections applied** — file, before → after, one-line reason.
- **Proposed (not applied)** — file, current, 1–2 alternatives, why it is a
  suggestion rather than a fix.
- **Bilingual note** — where the languages now diverge and whether that is intentional.
- **Flagged** — unsourced numbers, dead locale links, titles assembled from
  display headings.

If a category is empty, say so in one line. Do not invent findings.

## Quality bar

- A native speaker of each language should not be able to tell which one was
  written first.
- No correction changes what the sentence means or how the brand sounds.
- Every rule applied traces to the project's tone guide (if any) or to a
  documented language rule — not to general preference.
- The reader can act on the report without rereading the source to work out
  what you meant.

## Reference files

| File | Contents |
|---|---|
| `references/language-rules.md` | Norwegian failure modes (with examples), English "do not fix" list, bilingual parity, two-tone headline mechanics, claims/numbers policy |

## Source note

Migrated from a project agent file. The language rules are stable grammar and
usage (not version-dependent), so nothing here was re-verified against external
docs; the migration removed brand- and project-specific scaffolding and kept the
language substance.
