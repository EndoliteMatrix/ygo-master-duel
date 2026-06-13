---
name: md-patch
description: Watch Master Duel's operational state — the latest client patch, the current Forbidden/Limited (banlist) deltas, the active Ranked season, running events, and new packs. Two modes — no-args prints the last known state and staleness; `check` re-pulls via the md-banlist-watcher agent and flags any banlist change that touches Dark Magician / Spellcaster cards or the top-meta decks. Triggers on `/md-patch`, `/md-patch check`, and phrases like "did anything get banned", "what's the latest master duel update", "is there a new banlist", "what event is running". HARD MODE — Konami official preferred, secondary trackers labelled, every date sourced or "no data".
version: 1.0.0
---

# md-patch

Maintain the Master Duel operational-state file at `$JD/PATCH-BANLIST.md` (`$JD = /home/archuser/Documents/YGO/journal/`). This skill OWNS the banlist/patch pull. The banlist is the single most consequential thing to keep fresh — a ban/limit can delete a card from the deck or gut a meta deck.

## Hard rules

1. **Primary-source-or-no-data.** Prefer Konami's official MD channels; when they 403 (common), fall back to masterduelmeta / YGOrganization / Wargamer and **label them secondary**. Cross-confirm a banlist delta across ≥2 secondaries. Never fabricate a status, a date, or a patch note — mark unreachable per-card statuses `no data`.
2. **MD banlist only** — separate from TCG/OCG. MD-legal-but-TCG-banned cards (Maxx "C", etc.) are normal; report MD's actual status/count.
3. **Reconcile content-patch vs banlist** — they're often announced on different dates and applied on another; state both, don't conflate.
4. **Always flag DM/Spellcaster relevance and top-meta relevance** of every delta — that's why `/md-deck` cares. "Nothing Spellcaster/DM was hit" is a report-it finding.
5. **Stamp `Last verified: YYYY-MM-DD`** and the source-access note (what was blocked) at the top.

## Modes

### Mode 1: no args (`/md-patch`)
Read-only. `cat "$JD/PATCH-BANLIST.md"` and present the latest patch, the current banlist deltas, the season + events, and new packs. Show `Last verified` + staleness. If a newer banlist date is rumored/known to have passed, prompt: "Banlist may have updated — run `/md-patch check`?"

### Mode 2: `check` (`/md-patch check`)
1. Note the stored `Last verified` date (pass to the agent).
2. **Launch the `md-banlist-watcher` agent.** It returns: latest patch (version + date), the current banlist deltas (each card old→new + effective date + source, `no data` where unreachable), DM/Spellcaster + top-meta relevance, the ranked season, running events, and new packs.
3. Diff against the stored file. Summarize what changed.
4. **Replace `$JD/PATCH-BANLIST.md`** in place (keep the source-access note + caveats).
5. **If a delta hits a Dark Magician / Spellcaster card** (forbidden/limited/unlimited) **or a top-meta deck**, flag it loudly and:
   - if it touches a card in `deck-current.ydk`, tell the user the deck may now be illegal or improvable → suggest `/md-deck tune`.
   - if it reshapes the meta, suggest `/md-meta refresh` then `/md-deck tune`.
6. Don't edit the deck or the meta snapshot here — just flag and hand off.

## Files this skill touches
| Path | When |
|---|---|
| `$JD/PATCH-BANLIST.md` | mode 1 reads; mode 2 replaces in place |
| `$JD/deck-current.ydk` | mode 2 reads (to check if a banned/limited card is in the deck) |

## Agents used
- **`md-banlist-watcher`** — primary-source watch of patch / banlist / season / events. Hard mode; re-verifies every time (the banlist changes — never trust cached memory).

## Permissions
- Reading: anywhere under `$JD/`.
- Writing: only `$JD/PATCH-BANLIST.md`.
- Running: read-only research via the agent. No deck edits — that's `/md-deck`.
