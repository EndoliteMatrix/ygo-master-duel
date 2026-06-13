---
name: md-ydk
description: Generate, decode, and verify Yu-Gi-Oh .ydk / ydke:// deck files for Master Duel from a card-NAME list — fast and repeatably — using a local passcode codec backed by a cache seeded from the ygoprodeck API. Modes — `build` turns a named decklist into a .ydk + ydke import code; `decode` names every card in a .ydk/ydke; `verify` checks sizes / max-copies / MD-legality; `lookup` resolves one name↔passcode; `seed` adds cards to the cache. Triggers on `/md-ydk`, and phrases like "build a ydk", "make a deck file", "generate the ydke", "what's the passcode for X", "decode this ydke", "turn this list into an importable deck". HARD MODE — passcodes come from the ygoprodeck API or the seeded cache, never guessed; ambiguous names go to the ygo-card-resolver agent.
version: 1.0.0
---

# md-ydk

Deterministic Yu-Gi-Oh deck-file codec so deck changes become **fast and repeatable** instead of one-off passcode lookups. The engine is `ydk_codec.py` (in the repo tools/ dir); it is cache-first (instant, offline) and falls back to the ygoprodeck API for unknown cards, caching them. The cache (`card-id-cache.json`) is seeded FROM the API, so every passcode is primary-sourced by construction.

`SK = /home/archuser/Documents/YGO/tools` · `JD = /home/archuser/Documents/YGO/journal`

## Hard rules

1. **Never invent a passcode.** Every id comes from the cache or a live ygoprodeck fetch. If a name won't resolve, report it `UNRESOLVED` — don't fabricate. (The script already enforces this: a build with any unresolved name writes nothing and exits non-zero.)
2. **Master Duel pool.** The codec records MD availability (`misc=yes` → formats includes "Master Duel"). Warn on any card not flagged MD-legal.
3. **Banlist limits are NOT in the API.** The script enforces ≤3 and legal deck sizes, but per-card MD limits (e.g. **Maxx "C" Limited 1**) live in `$JD/PATCH-BANLIST.md` — always cross-check a built deck against it before declaring it legal.
4. **Alt-art is cosmetic.** The codec canonicalizes a name to one standard passcode on `build` (so output is repeatable); alt-art ids still decode correctly. Card-name identity is the invariant, not the raw bytes.
5. **Fish shell** for any copy-paste command you hand the user (`; end` not `; done`).

## Modes

All invocations: `python3 "$SK/ydk_codec.py" <cmd> ...`. Add `--no-net` to force cache-only (offline / fully repeatable).

### `build` — named list → .ydk + ydke (the main use)
1. Get the decklist as names. Either the user pastes it, or you write it to a `.txt` from what they tell you. Format: `#main` / `#extra` / `#side` section headers, one card per line as `3 Card Name`, `3x Card Name`, `Card Name` (=1), or a bare passcode. Inline `# comments` are ignored.
2. Run `python3 "$SK/ydk_codec.py" build <list.txt> --out <path.ydk>`. It prints the `ydke://` code and writes the `.ydk`.
3. **If any name comes back `UNRESOLVED` or `ambiguous`**, hand just those names to the **`ygo-card-resolver` agent** (it disambiguates printings/typos and confirms MD-legality), add the returned passcodes to the list (or let the agent seed them), and re-run.
4. **Cross-check legality** against `$JD/PATCH-BANLIST.md` (limited cards) and report. Present the user the `ydke://` to paste into Master Duel + the saved `.ydk` path.
5. If this is the user's live deck, offer to also update `$JD/deck-current.ydk` + `deck-current.ydke.txt` (that write belongs to `/md-deck` — hand off or do it with confirmation).

### `decode` — .ydk / ydke → named list
`python3 "$SK/ydk_codec.py" decode <deck.ydk | 'ydke://...'>` → sectioned list with `Nx Name [passcode]`. Use this to read any deck the user drops or pastes.

### `verify` — legality check
`python3 "$SK/ydk_codec.py" verify <deck.ydk | 'ydke://...'>` → flags illegal sizes, >3 copies, non-MD cards, unresolved ids. Then cross-check the MD banlist in `$JD/PATCH-BANLIST.md` for limited cards (the API can't).

### `lookup` — one card either direction
`python3 "$SK/ydk_codec.py" id "Card Name"` or `... name <passcode>`. Loose matching works (`maxx c` → 23434538).

### `seed` — grow the cache
`python3 "$SK/ydk_codec.py" seed-from-ydk <a.ydk> [b.ydk ...]` or `... seed <id,id,...>` to fetch from the API and cache. Run this to pre-load a new archetype's cards so future builds are offline.

## Files this skill touches
| Path | When |
|---|---|
| `$SK/ydk_codec.py` | the engine (don't edit per-build) |
| `$SK/card-id-cache.json` | read every command; written on any new resolution / seed |
| `<path>.ydk` (caller-specified, e.g. `$JD/` or `~/Downloads/`) | `build` writes |
| `$JD/PATCH-BANLIST.md` | read for the MD banlist cross-check |

## Agents used
- **`ygo-card-resolver`** — resolves an ambiguous / fuzzy / unknown card name to the correct Master Duel passcode, confirms MD-legality and any banlist limit. Hard mode; primary-source (ygoprodeck), never guesses. Call it only for names the script couldn't resolve cleanly.

## Permissions
- Reading: `$SK/`, `$JD/`, and any `.ydk` the user points at (e.g. `~/Downloads/`).
- Writing: `$SK/card-id-cache.json` and caller-specified `.ydk` output paths. Updating `$JD/deck-current.*` is `/md-deck`'s job — hand off or confirm.
- Running: `python3 "$SK/ydk_codec.py" ...` and the `curl` it shells out for API fetches.
