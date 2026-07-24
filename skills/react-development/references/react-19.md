# React 19 — API surface & migration reference

Verified July 2026 against react.dev (release posts and the versions page).
React 19.0: December 2024 · 19.1: March 2025 · 19.2: October 2025 (current
minor). Re-verify the installed version per project.

## React 19.0 — the big shift

### Actions (mutations & forms)

```tsx
// <form action> takes an async function; React manages pending state.
function Rename({ save }: { save: (name: string) => Promise<string | null> }) {
  const [error, submitAction, isPending] = useActionState(
    async (_prev: string | null, formData: FormData) => {
      return await save(formData.get("name") as string); // return error or null
    },
    null,
  );
  return (
    <form action={submitAction}>
      <input name="name" />
      <button disabled={isPending}>Save</button>
      {error && <p role="alert">{error}</p>}
    </form>
  );
}
```

- `useActionState(fn, initial)` → `[state, action, isPending]`.
- `useFormStatus()` reads the enclosing form's pending state (design-system
  buttons without prop drilling).
- `useOptimistic(value)` shows the expected result while the action runs and
  reverts on failure.

### `use()`

Reads a promise or context *during render*; unlike hooks it may be called
conditionally. Suspends on promises — pair with `<Suspense>` and an error
boundary. Client-side: don't create the promise in render; accept one created
upstream or by a caching layer.

### `ref` as a prop

```tsx
function TextInput({ ref, ...props }: { ref?: React.Ref<HTMLInputElement> }) {
  return <input ref={ref} {...props} />;
}
```

No `forwardRef`. Ref callbacks may return a cleanup function.

### Also in 19.0

- Document metadata (`<title>`, `<meta>`, `<link>`) rendered in components is
  hoisted to `<head>`.
- Stylesheet/async-script de-duplication and `preload`/`preinit` APIs.
- Better hydration-error diffs; Context can be rendered directly as
  `<MyContext value={...}>` instead of `<MyContext.Provider>`.

### Removed in 19.0

| Removed | Replacement |
|---|---|
| `propTypes` | TypeScript |
| `defaultProps` on function components | default parameters |
| Legacy context (`contextTypes`/`getChildContext`) | `createContext` |
| String refs | ref callbacks / `useRef` |
| `ReactDOM.render` / `hydrate` (pre-18 roots) | `createRoot` / `hydrateRoot` |

## React 19.1 (March 2025)

Quality release: owner-stack debug info in dev, Suspense fixes. No API
removals.

## React 19.2 (October 2025)

- **`<Activity mode="visible" | "hidden">`** — hide UI while preserving its
  state (and deprioritizing its updates) instead of unmounting.
- **`useEffectEvent`** — extract event-ish logic from effects so the effect
  doesn't re-run when only that logic's dependencies change; the replacement
  for stale-closure/`useRef` workarounds.
- `useId` prefix changed to `_r_` (valid for `view-transition-name`).
- `eslint-plugin-react-hooks` latest: flat config default, opt-in
  compiler-powered rules.
- Web Streams support for Node SSR.

## React Compiler

- Shipped stable; enabled per project via `babel-plugin-react-compiler`
  (Vite: through the react plugin's babel options) plus the compiler eslint
  rules.
- With it enabled: **stop writing** `useMemo`/`useCallback`/`React.memo` for
  performance; the compiler memoizes automatically and existing manual memo
  is mostly dead weight (remove opportunistically, not in a big bang).
- The compiler assumes the Rules of React — components/hooks must be pure,
  props/state immutable. Rule violations silently disable optimization for
  that component; the eslint rules surface them.
- Without the compiler: memoize only measured hot paths.

## Scaffold (Vite)

```bash
npm create vite@latest myapp -- --template react-ts
```

create-react-app is deprecated (February 2025) — never scaffold with it.
For SSR/routing needs beyond an SPA, that is meta-framework territory and out
of this skill's scope.

## State architecture — decision rules

1. **Local `useState`/`useReducer`** — default; most state never leaves the
   component.
2. **Lift** to the lowest common ancestor only when siblings truly share it.
3. **Context** — low-frequency, wide-reach values (theme, locale, session).
   Never per-keystroke data.
4. **External store** (e.g. a small atom/store lib) — genuinely global,
   high-frequency *client* state; rare in practice.
5. **Server state** — TanStack Query or the framework loader. Cache key =
   request identity; components read the cache, they don't own copies.

URL state (filters, pagination, tabs) belongs in the URL, not in `useState`.

## Migration checklist (from 17/18 habits)

1. Upgrade to the **current 19.2 patch** — versions 19.0.0–19.2.2 carry a
   critical React-Server-Components vulnerability patched December 2025
   (client-only apps are not affected by the RCE but should update anyway).
2. Replace `forwardRef` with `ref` props; delete `defaultProps`/`propTypes`.
3. Convert form-submission `useState` bookkeeping to
   `useActionState`/`useFormStatus`.
4. Move `useEffect` data fetching into the server-state layer.
5. Delete effects that only derive state; compute during render.
6. Enable the compiler + eslint rules; remove manual memoization as files are
   touched.
7. Run the codemods where available (`npx codemod@latest react/19/...`) and
   the updated `eslint-plugin-react-hooks`.
