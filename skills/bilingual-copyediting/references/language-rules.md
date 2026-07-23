# Language rules — Norwegian (bokmål) + English

Concrete correctness rules for bilingual copy-editing. Examples are generic, not
tied to any particular product.

## Norwegian — recurring failure modes

Check every one of these:

1. **Særskriving / compounds.** Norwegian compounds are written as **one word**.
   `Migrerings-protokollen` → `Migreringsprotokollen`. Use a hyphen only for
   abbreviations (`SEO-redirects`), proper nouns (`WordPress-plugin`), numerals
   (`3-lags`), or when a solid compound is genuinely unreadable.
2. **Hyphen calques from English.** `statisk-først`, `innhold-først` are calques
   of `static-first` / `content-first`. Norwegian does not hyphenate these.
3. **Invented words.** `sidebygger` is not Norwegian. Use the term the audience
   actually says — often the established English loan.
4. **Wrong word class.** `Arkitekter` is a plural noun, not a verb. This shows up
   when translating English words that are both verb and noun (`Architect`,
   `Engineer`, `Design`).
5. **Imperative consistency.** Every step in an action list must be in the same
   mood — don't switch between imperative and infinitive/noun forms mid-list.
6. **Capitalised emphasis.** `Studioet ER styrken` is an English device.
   Norwegian conveys emphasis through word order or punctuation, not capitals.
7. **Number agreement in a series.** `Ingen database. Ingen plugins. Ingen
   kompromiss.` → `kompromisser`. Match number across a parallel series.

## English — what must NOT be "fixed"

The most damaging failure mode is mirroring a Norwegian fix back into English:

- `content-first`, `static-first`, `page-builder layer` — hyphenated compound
  modifiers are **correct English**. The Norwegian hyphenated versions were
  calques of this; that is why the *Norwegian* ones were the errors, not these.
- `Architect` / `Engineer` as verbs are **real English verbs**.
- `No compromise` (singular) is idiomatic English.

**Rule:** carry a Norwegian fix into English **only** if the same error exists in
English. A correct English construction is not made wrong by its bad Norwegian calque.

## Bilingual parity

- Both languages must read as original text. Neither is "the translation".
- **Localise intent, not words.** An idiomatic Norwegian line that says something
  slightly different from the English is correct; a literal rendering that reads
  stiffly is not.
- **Divergence is a legitimate outcome.** State it explicitly in the report so the
  owner can decide whether the other language should follow.
- Page titles are written deliberately per language — never assembled from a split
  display heading.
- Source-language-only content (e.g. an English-only release feed) does not need
  translating. Flag the route as single-locale and check the language switcher
  does not link to a page that does not exist.

## Headline mechanics — two-tone headings

A common device: a heading split into two lines (`h1a` + `h1b`), the second line
in an accent colour.

**Both halves must carry meaning alone.** The eye reads large headings line by
line, and the accent line takes extra stress.

- Fails: `Få et` / `tilbud.` (first line is meaningless alone)
- Works: `Fortell om` / `prosjektet.`

Never split a sentence so that one line is a stranded function word.

## Claims and numbers

Flag, do not silently keep:

- Numbers with no measurement and no cited source.
- Comparisons against named competitors without a reference.
- Measured figures presented without their source — e.g. a raw `1284 pages`
  claim, or a benchmark figure quoted without saying what was measured, on what,
  and when.

The editor flags these; the owner decides whether to source, soften, or cut them.
