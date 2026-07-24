---
name: react-development
description: Build and review React 19 SPAs and components — function components with TypeScript, hooks, React 19/19.2 APIs (Actions, useActionState, useOptimistic, use(), ref as prop, Activity, useEffectEvent), Vite scaffolding, state architecture (local vs context vs external store vs server state), and React Compiler implications for memoization. Also use to modernize legacy patterns (class components, forwardRef, defaultProps/propTypes, CRA, useEffect data fetching, manual memo everywhere). Not for Vue/Nuxt or Astro page work — inside Astro islands this skill owns component internals while the Astro skill owns integration — and not a styling skill; defer tokens and Tailwind mechanics to the Tailwind skill. Meta-framework routing and React Server Components infrastructure are out of scope.
---

# React 19 development

Senior React specialist. React 19 is the baseline (19.0 December 2024; 19.2
current minor since October 2025) and the **React Compiler is shipped and
stable** — which inverts years of memoization advice. Training-data React
skews toward 17/18 habits; treat older examples with suspicion and verify the
project's react version and compiler status before writing code.

## Core principles

**Function components + TypeScript, only.** No class components — new React
19 features don't target them. Type props explicitly; `propTypes` and
`defaultProps` on functions are removed in 19 (use default parameters).

**The compiler changes the memo calculus.** With the React Compiler enabled,
manual `useMemo` / `useCallback` / `React.memo` for performance is mostly
obsolete noise. **Check whether the project has the compiler enabled before
adding or stripping memoization** — with it on, write plain code and let the
compiler optimize; without it, memoize only measured hot paths.

**Server state is not client state.** Data that lives on a server (fetched,
cached, revalidated) belongs in a server-state library (e.g. TanStack Query)
or the meta-framework's loader — never hand-rolled `useEffect` + `useState`
fetching. Client state (UI, form drafts) stays local.

**State as low as possible; derive, don't sync.** Lift state only to the
lowest common ancestor. Anything computable from existing state/props is
computed during render — never mirrored into state via an effect.

**Effects are for external systems.** Subscriptions, DOM APIs, non-React
widgets. If an effect only transforms data or chains state updates, the
design is wrong. For event logic inside effects, 19.2's `useEffectEvent`
replaces the stale-closure workarounds.

**Actions for mutations.** Form submissions and mutations use 19's Actions:
`<form action={fn}>`, `useActionState` for pending/error state,
`useOptimistic` for optimistic UI — not `useState` spinner bookkeeping.

**Accessibility is part of done.** Semantic elements, real labels, keyboard
paths, and stable generated ids via `useId`.

## Anti-patterns — never produce these

- Class components, string refs, legacy context.
- `forwardRef` in React 19 — `ref` is a normal prop now.
- `defaultProps` / `propTypes` on function components (removed in 19).
- Scaffolding with create-react-app (deprecated) — use Vite.
- `useEffect` for data fetching or for deriving state from props/state.
- Effect chains where one state update triggers the next.
- `index` as key on reorderable/dynamic lists.
- Context for high-frequency state (per-keystroke, animation) — it re-renders
  every consumer.
- Blanket manual memoization in a compiler-enabled project.
- Pinning react 19.0.0–19.2.2 — a critical RSC vulnerability was patched in
  December 2025; use the current patch release even in client-only apps.

## Workflow

1. Confirm the react version, TypeScript config, and whether the React
   Compiler is enabled (look for `babel-plugin-react-compiler` / compiler
   rules in the eslint config) before writing code.
2. **Before using any React-19-specific API**, read
   `references/react-19.md` — the 19.0/19.1/19.2 API surface, removals,
   compiler notes and the migration checklist.
   - **Before writing Actions, `use()`, `<Activity>` or `useEffectEvent`
     code, fetch https://react.dev/reference/react and verify the current
     signature — do not write 19.x APIs from memory**; several are new
     enough that recollection drifts.
   - **When the project's react version is unclear or newer than this file,
     fetch https://react.dev/versions and the release post it links before
     assuming the API surface.**
3. State placement before code: local → lifted → context (low-frequency) →
   store/server-state library. Justify each promotion.
4. Defer styling to the Tailwind skill; this skill owns component structure,
   state and data flow.
5. Verify: typecheck, `eslint-plugin-react-hooks` (flat config, compiler
   rules where enabled), and a production build before calling it done.

## Reference files

| File | Contents |
|---|---|
| `references/react-19.md` | React 19.0/19.1/19.2 API surface (Actions, use(), ref-as-prop, Activity, useEffectEvent), removals, React Compiler notes, Vite scaffold, state-architecture decision rules, migration checklist, security note |

## Source note

Written July 2026, verified against react.dev (19.2 release post, versions
page) — React 19.2 current, React Compiler stable, CRA deprecated. Re-verify
the installed react version and compiler status per project.
