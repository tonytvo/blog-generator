# Outline format (talks-outline) — the depth bar

Every outline is a standalone `.md` the reader keeps and shares. **Depth comes from
granularity, not word count.** A talk that enumerates many things becomes many `###`
subsections, never a table that swallows them. If a draft feels thin, split tables and
paragraphs back into numbered subsections and per-line bullets — do not just add words.

## Language
The whole file is in the language spoken in the talk (from `meta.json` `language`, verified
against the transcript body; trust the body on conflict). Headers, table headers, tag
legend, critical observations — all one language. Keep technical terms as spoken (DCF, ROE,
TOD, pull request…). Only an explicit user override changes this; then note "translated from
<language>" in the header.

## Exhaustive-outline rules (apply to every talk)
- Preserve **every** anecdote, name (people/companies/tools), number, statistic, direct
  quote, and concrete example. Do not compress, generalize, or summarize away specifics.
- **Deep decimal hierarchy:** `##` top sections (1, 2, 3…), `###` subsections (1.1, 1.2…),
  `####` where it helps. One `###` per distinct sub-topic, example, or step. A long talk has
  **25+** `###`, not 3.
- **One idea per bullet line.** Never pack several facts into one paragraph or table cell.
- **Enumerations** (patterns, steps, rules, trends, companies) -> each item its own numbered
  `###` with its own bullets (rationale, metaphor, quote, example). A summary table at the
  end is a nice *addition* but must never *replace* the per-item subsections.
- **Worked examples decomposed** step by step — each micro-step its own `###`
  (e.g. "7.1 Extract + placeholder name", "7.2 Rename").
- **Q&A finely broken:** one `###` per question (Q1, Q2…; multi-part -> Q5, Q5a). Name the
  asker when known.
- Attribute quotes and claims to whoever said them. Quotes stay under 15 words.
- Open with a **framing blockquote**: speaker, venue, format, the talk's own structure.
- End with a **"People & References Cited"** index.
- **Enrich pass** before writing: reread the transcript and add any anecdote, name, number,
  or example the outline missed.
- **Shape matches the talk:** a 90-min workshop -> very long outline; a narrative keynote or
  interview compresses to prose and is shorter at the *same* fidelity — expected, not a
  defect. Panels/podcasts -> outline as a topic-threaded conversation (still blockquote +
  References index). If a scheduled guest was absent or it became a roundtable, say so —
  never fabricate.

## Analytical layer (this skill adds on top of the playbook)
Tag factual rows: `[V]` verifiable · `[D]` speaker's estimate/opinion · `[P]` pending
verification · `[E]` error or self-contradiction (state the correction). Speech-to-text
garbles numbers and proper nouns — flag likely mis-transcriptions as `[E]`.
Before the References index, add:
- **Critical observations** — analysis *not* in the talk: factual errors, contradictions,
  missing counter-arguments, sponsor/product incentives, sample-size or survivorship issues,
  claims stated as rules that rest on one anecdote.
- **Pending verification** — table of `[P]` claims with suggested primary sources.

## Skeleton
```markdown
---
title: "<Talk Title>"
date: "<YYYY-MM-DD>"
description: "<rich one-line description of what the outline covers>"
type: "reference"
tags: ["<domain>"]        # e.g. software / investing / self-help; add "ai" when apt
---

# <Talk Title>

> <Framing blockquote: speaker(s), venue/date, format (keynote/workshop/panel/podcast),
> and the talk's own structure. One paragraph.>

**Language:** <spoken language> · caption source: <manual | auto>
<add "translated captions only — treat wording with caution" or
 "outline translated from <language> at user request" when either applies>

## 1. <first section>
### 1.1 <sub-topic / example / step>
- one idea per bullet, tagged where factual  [V]/[D]/[P]/[E]
### 1.2 ...

## N. Q&A
### Q1 — <asker if known>: <question>
- <answer points>

## Critical observations (not in the talk)
| # | Issue | Why it matters to the reader |

## Pending verification
| Claim / figure | Suggested primary source |

## People & References Cited
- <person / company / tool / book / paper mentioned>

*Video: https://www.youtube.com/watch?v=<ID> — transcript fetched automatically; outline generated from the transcript.*
```
(For a long transcript captured across passes, append "(partial for a long transcript)" to
the footer.)

## Domain blocks (fold into the numbered sections where relevant)

### Software engineering
Problem & context · architecture/approach (with trade-offs) · tools & versions (versions ->
`[P]`) · reproducible workflow/steps · code/config shown (short snippets only) · perf /
productivity claims (tagged, note if benchmarked) · where it holds vs breaks (monorepo vs
micro-repo, solo vs team). Decompose every demo step by step.

### Value investing / finance / real estate
Macro/cycle context (dated timeline) · business or asset (how it makes money, moat) · every
figure in a tagged row with units/currency · valuation method + inputs (DCF/multiples/NAV) ·
policy/regulation with dates (usually `[P]`) · base/bull/bear outlook as stated + what was
omitted · incentives (is the channel selling a course/fund/product?). Test the speaker's
thesis against their own evidence in Critical observations.

### Self-help / productivity / mindset
Core model in one framework · evidence type per claim (study / anecdote / authority, tagged)
· practices (how to do it, time cost, expected effect) · failure modes the speaker admits and
ones they don't · who it's for / not for. Separate testable claims (a 2-week experiment) from
motivational framing; flag pop-psych stated as settled science.

## Style
Every row carries information; no filler. A 3-hour talk gets more sections, not longer rows.
No more than one short (<15-word) verbatim quote per section. Never invent timestamps,
figures, or names not in the transcript.
