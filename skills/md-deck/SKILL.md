---
name: md-deck
description: Inspect, pilot, and tune the user's Master Duel Dark Magician / Paladin deck. Three modes — no-args prints the current decklist, game plan, mulligan guide, and honest tier ceiling; `matchup <archetype>` shows or generates (via the md-matchup-analyst agent) a per-deck matchup brief; `tune` proposes a small, gated ratio change from the current meta + banlist + the user's recent losses, then updates the deck files and the tweak log. Triggers on `/md-deck`, `/md-deck matchup X`, `/md-deck tune`, and phrases like "show my dark magician deck", "how do I beat <deck> with dark magician", "what should I change in my deck", "my deck keeps bricking / losing to X". HARD MODE — primary-source-or-no-data, every card ruling cited, honest about DM being a rogue deck.
version: 1.0.0
---

# md-deck

Pilot and maintain the user's **Dark Magician ("Disruption" build)** in Master Duel. The journal lives at `$JD = /home/archuser/Documents/YGO/journal/`. This skill OWNS the deck files and the tweak log; it READS the meta/patch journals (owned by `/md-meta` and `/md-patch`) — **it does not do its own web research for tuning.** That separation is deliberate: it keeps the three skills from drifting.

## Hard rules

1. **Honest ceiling, always.** Dark Magician is rogue/untiered in MD; the realistic ceiling is a Platinum/Diamond climber, not Tier 1 (see `$JD/DECK-CURRENT.md` "honest ceiling"). Never imply a tweak makes it a top deck. The user prefers definitives stated plainly over hype.
2. **Card rulings are primary-sourced.** Any combo/interaction claim added to the journal is verified verbatim via the ygoprodeck API (`https://db.ygoprodeck.com/api/v7/cardinfo.php?name=<CARD>` → `.data[0].desc`). Rulings reasoned from text are labelled `(inference)`.
3. **Deck legality.** Max 3 of a card, respect the MD banlist in `$JD/PATCH-BANLIST.md` (e.g. **Maxx "C" is Limited 1 in MD** — never propose 3). Keep main 40-60 (target 40), extra ≤15, side ≤15.
4. **Tune in small steps, one variable at a time**, so the user can tell what helped. Gate every change on explicit confirmation before writing files.
5. **Keep the import code in sync.** After any deck change, regenerate `deck-current.ydke.txt` from `deck-current.ydk` (the converter is in the skill's "export" steps) — the user imports the ydke, so a stale code is a silent footgun.

## Modes

### Mode 1: no args (`/md-deck`)
Read-only. `cat "$JD/DECK-CURRENT.md"` and present it formatted: the honest ceiling first, then the deck table, the 1-card openers, the Eye/Gaze toolbox, and the mulligan guide. End with the import code. Terse — the user is checking, not reading a novel. If `DECK-CURRENT.md` is missing, say so and offer to rebuild from `deck-current.ydk`.

### Mode 2: `matchup <archetype>` (`/md-deck matchup Enneacraft`)
1. Check `$JD/MATCHUPS.md` for a current, dated brief on that archetype. If one exists and is newer than the last banlist date in `$JD/PATCH-BANLIST.md`, present it.
2. Otherwise (no brief, or stale) **launch the `md-matchup-analyst` agent** with the archetype name (or the user's description of an unknown deck). It returns a sourced brief (how the deck plays off one card, key threats verbatim, what lands/whiffs vs DM, how DM breaks the board, win condition).
3. Write/replace that archetype's section in `$JD/MATCHUPS.md` (dated, sourced), then present it. Don't invent a matchup from memory — the agent fetches it.

### Mode 3: `tune` (`/md-deck tune`)
Propose a small, evidence-based ratio change. **No web research here — read the journals.**
1. Read `$JD/DECK-CURRENT.md`, `$JD/META-SNAPSHOT.md`, `$JD/PATCH-BANLIST.md`. If either of the latter two is >14 days stale, tell the user to run `/md-meta refresh` and/or `/md-patch check` first (their freshness gates a good tune).
2. Ask the user (if not already given): what beat you and how, and what felt dead? Combine with the meta's top decks + the "soft spots" list in DECK-CURRENT.md.
3. Propose **1-3 swaps max**, each with: the card out, the card in, the matchup/why, and the craft cost (from `collection-reference.csv` rarity). Show the resulting counts. State legality against the current banlist.
4. **Gate:** "Apply this change? (yes / no / adjust)." Never write without a yes.
5. On yes: edit `deck-current.ydk`, regenerate `deck-current.ydke.txt` (Mode 4 converter), update the relevant tables + import code in `DECK-CURRENT.md`, and **append a new dated entry to `$JD/TWEAK-LOG.md`** (newest first; never rewrite prior entries).

### Mode 4: `export` (`/md-deck export`)
Regenerate and print the ydke import code from `deck-current.ydk`:
```fish
cd "/home/archuser/Documents/YGO/journal"
python3 -c 'import base64,struct,sys
def parse(p):
 secs={"main":[],"extra":[],"side":[]};cur=None
 for ln in open(p):
  s=ln.strip()
  if s.lower().startswith("#main"):cur=secs["main"];continue
  if s.lower().startswith("#extra"):cur=secs["extra"];continue
  if s.startswith("!side"):cur=secs["side"];continue
  if s.startswith("#") or not s:continue
  if cur is not None and s.isdigit():cur.append(int(s))
 return secs
def enc(x):return base64.b64encode(b"".join(struct.pack("<I",i) for i in x)).decode()
d=parse("deck-current.ydk")
print("ydke://%s!%s!%s!"%(enc(d["main"]),enc(d["extra"]),enc(d["side"])))'
```
Write the result to `deck-current.ydke.txt` and show it.

## Files this skill touches
| Path | When |
|---|---|
| `$JD/DECK-CURRENT.md` | mode 1 reads; mode 3 updates tables + import code |
| `$JD/deck-current.ydk` | mode 3 edits |
| `$JD/deck-current.ydke.txt` | mode 3 & 4 regenerate |
| `$JD/MATCHUPS.md` | mode 2 writes/replaces an archetype section |
| `$JD/TWEAK-LOG.md` | mode 3 appends (newest first; append-only) |
| `$JD/META-SNAPSHOT.md`, `$JD/PATCH-BANLIST.md` | mode 3 reads (never writes — those are owned by /md-meta and /md-patch) |
| `$JD/collection-reference.csv` | mode 3 reads for craft cost |

## Agents used
- **`md-matchup-analyst`** — generates a sourced matchup brief vs a given archetype (mode 2). Hard mode; re-verifies card text every time.

## Permissions
- Reading: anywhere under `$JD/`.
- Writing: only under `$JD/` (deck files, MATCHUPS.md sections, TWEAK-LOG.md). Never META-SNAPSHOT.md or PATCH-BANLIST.md.
- Running: `curl` to the ygoprodeck API (card text), `python3` for the ydke converter. No game automation — this is a planning tool; the user duels manually.
