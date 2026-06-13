---
name: md-meta
description: Track the current Master Duel meta — the tier list, the top decks and what each does off one card, and the field's hand-trap / disruption package. Two modes — no-args prints the last snapshot and how stale it is; `refresh` re-pulls the meta via the md-meta-researcher agent, diffs it against the stored snapshot, and flags any matchup brief that the shift affects. Triggers on `/md-meta`, `/md-meta refresh`, and phrases like "what's the master duel meta", "what's tier 1 right now", "refresh the meta", "what decks am I facing". HARD MODE — every tier/list carries a primary source (masterduelmeta) and a date; power score and play-rate reported separately; honest that Dark Magician is rogue.
version: 1.0.0
---

# md-meta

Maintain the Master Duel meta snapshot at `$JD/META-SNAPSHOT.md` (`$JD = /home/archuser/Documents/YGO/journal/`). This skill OWNS the meta pull — `/md-deck tune` reads its output rather than re-researching, so the meta lives in exactly one place.

## Hard rules

1. **Primary-source-or-no-data.** Tiers, decklists, and ratios come from masterduelmeta.com (primary for MD) / ygoprodeck / Konami, each with a date. No estimated tiers, no invented win-rates. The agent returns `no data` rather than guess; preserve that honesty in the snapshot.
2. **Master Duel ≠ TCG/OCG.** Only the MD pool/banlist. Confirm MD-specific facts (Maxx "C" legal + Limited count) rather than importing TCG assumptions.
3. **Power ≠ popularity.** When a deck's tier and its play-rate diverge (e.g. Enneacraft: T3 power, #2 played), record both numbers — don't flatten.
4. **Reconcile, don't average.** If two sources disagree on the #1 deck, trust masterduelmeta (the established MD primary) and **flag the discrepancy** in the snapshot; don't silently pick or blend.
5. **Always stamp `Last verified: YYYY-MM-DD`** and the format era + banlist date at the top of the snapshot.

## Modes

### Mode 1: no args (`/md-meta`)
Read-only. `cat "$JD/META-SNAPSHOT.md"` and present the tier list + the disruption package + DM's standing, formatted. Show the `Last verified` date and the staleness. If >14 days stale (or older than the latest banlist date in `$JD/PATCH-BANLIST.md`), prompt: "Snapshot is N days old — run `/md-meta refresh`?"

### Mode 2: `refresh` (`/md-meta refresh`)
1. Note the current snapshot's `Last verified` date (pass it to the agent so it can report what changed since).
2. **Launch the `md-meta-researcher` agent.** It returns: format era + banlist date, the tier list (deck → tier/power → play-rate → "off one card" → source), the disruption package, and DM's standing — all sourced + dated.
3. Diff against the stored snapshot. Summarize to the user: what's new in the tier list, what dropped, what's unchanged.
4. **Replace `$JD/META-SNAPSHOT.md`** in place with the fresh snapshot (keep the reconciliation note + sources + caveats sections).
5. **Cross-check matchups:** for each archetype with a brief in `$JD/MATCHUPS.md`, if its tier/role changed materially or a new deck entered the top tiers without a brief, tell the user — and offer `/md-deck matchup <new deck>` to generate the missing brief. Don't auto-generate; just flag.
6. If the meta shift suggests a deck change (e.g. a fusion-heavy deck rose → Super Poly wants to be 2), suggest the user run `/md-deck tune` — don't tune here (that's /md-deck's job).

## Files this skill touches
| Path | When |
|---|---|
| `$JD/META-SNAPSHOT.md` | mode 1 reads; mode 2 replaces in place |
| `$JD/MATCHUPS.md` | mode 2 reads (to flag stale/missing briefs — never writes) |
| `$JD/PATCH-BANLIST.md` | mode 1/2 reads (banlist date for staleness) |

## Agents used
- **`md-meta-researcher`** — primary-source pull of the MD tier list + disruption package. Hard mode; re-fetches every time (the meta moves monthly — never trust cached memory).

## Permissions
- Reading: anywhere under `$JD/`.
- Writing: only `$JD/META-SNAPSHOT.md`.
- Running: read-only research via the agent (WebFetch/WebSearch/ygoprodeck API). No deck edits — that's `/md-deck`.
