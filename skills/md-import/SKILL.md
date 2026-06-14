---
name: md-import
description: One-step ingest of a finished Master Duel deck code as your new current deck. Paste a `ydke://` (e.g. exported from the deck-transfer browser extension) or give a `.ydk` path; this decodes it, verifies legality, cross-checks the MD banlist, shows the diff vs your current deck, writes it into the journal as `deck-current`, logs the change, and offers to commit to the repo. Triggers on `/md-import`, a pasted `ydke://` string, and phrases like "this is my current deck now", "import my deck", "I exported my deck from Master Duel", "ingest this ydke", "capture my in-game deck". The simple front door for capturing an in-game deck change.
version: 1.0.0
---

# md-import

The **one command** to capture a finished deck (built in-game, exported via the deck-transfer
browser extension as a `ydke://`) into the journal as your current deck. You paste one line;
this does decode -> verify -> banlist cross-check -> diff -> version -> log -> (offer) commit.
It composes the `md-ydk` codec — it does not re-implement it.

`SK = /home/archuser/Documents/YGO/tools` · `JD = /home/archuser/Documents/YGO/journal`
`CODEC = "$SK/ydk_codec.py"`

## When this runs
The user pastes a `ydke://…`, points at a `.ydk`, or says "this is my current deck."
Default assumption: it's their **live in-game deck**, captured via the deck-transfer
extension's Export button (see the repo README for how the code gets out of Master Duel).

## Steps (do these in order)
1. **Decode + verify.**
   `python3 "$CODEC" decode '<input>'` then `python3 "$CODEC" verify '<input>'`.
   Show the sectioned card list. Surface every verify flag: illegal section sizes,
   any card over 3 copies, non-MD cards, unresolved ids. If a name comes back
   `UNRESOLVED`, hand just that name to the **`ygo-card-resolver`** agent — never guess a
   passcode.
2. **Banlist cross-check.** Read `$JD/PATCH-BANLIST.md`. Flag any card that exceeds its
   current Master Duel limit — the codec/API does NOT know banlist counts (e.g.
   **Maxx "C" is Limited 1**). If anything is over its limit, STOP and tell the user before
   writing anything.
3. **Diff vs current.** `python3 "$CODEC" decode "$JD/deck-current.ydk"` and compare to the
   new code at the **card-NAME** level (alt-art passcodes canonicalize — the name multiset is
   the invariant, not raw bytes). Report added / removed / count-changed cards. If identical,
   say so and stop (nothing to write).
4. **Write the new current deck.** The `.ydk` is a derived convenience file; regenerate both
   deterministically:
   - Write `$JD/deck-current.ydke.txt` = the imported `ydke://`.
   - Build the matching `.ydk`: take the passcodes from step 1's decode, write them as a
     bare-passcode list under `#main`/`#extra`/`#side` to a temp `.txt`, then
     `python3 "$CODEC" build <temp>.txt --out "$JD/deck-current.ydk"`. That writes the `.ydk`
     and re-emits a canonical `ydke://`; if it differs from the pasted one only by alt-art
     canonicalization, prefer the canonical one in `deck-current.ydke.txt` and note it.
5. **Log.** Append a dated entry to `$JD/TWEAK-LOG.md`: the date, the source
   ("imported from in-game via deck-transfer extension" unless the user says otherwise), and
   the step-3 diff. Append-only — never rewrite prior entries.
6. **Commit (offer).** Offer to commit + push to the public repo. Run git **as archuser**
   (root contaminates `.git/objects`), no Co-Authored-By trailer:
   `sudo -u archuser sh -c 'cd /home/archuser/Documents/YGO && git add -A && git commit -m "deck: import <short-desc>" && git push'`

## Hard rules
1. **Never invent a passcode.** The codec resolves from cache/API or reports `UNRESOLVED`;
   route unresolved names to `ygo-card-resolver`. A wrong passcode silently builds the wrong
   deck.
2. **Banlist limits aren't in the API.** Always do step 2 against `$JD/PATCH-BANLIST.md`
   before declaring a deck legal.
3. **Ownership.** This skill OWNS the "ingest a finished external deck code -> `deck-current.*`"
   write. `/md-deck tune` owns *proposed ratio changes* (it reads the meta/banlist journals
   and suggests); `/md-ydk` is the low-level codec. Different jobs — don't duplicate or
   re-research here. `md-import` does not pull meta or run matchup analysis.
4. **Fish shell** for any copy-paste command handed to the user (`; end` not `; done`,
   `set -gx` not `export`).

## Files this skill touches
| Path | When |
|---|---|
| `$CODEC` | decode / verify / build the input (don't edit per-import) |
| `$SK/card-id-cache.json` | read every command; written if a new card resolves |
| `$JD/PATCH-BANLIST.md` | read for the limit cross-check (step 2) |
| `$JD/deck-current.ydk` + `deck-current.ydke.txt` | written — the new current deck (step 4) |
| `$JD/TWEAK-LOG.md` | appended — the change record (step 5) |

## Agents used
- **`ygo-card-resolver`** — only for a name the codec returns `UNRESOLVED`/ambiguous. Hard
  mode, primary-source (ygoprodeck), seeds the cache so the next import is offline.
