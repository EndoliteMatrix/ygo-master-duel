# YGO — Master Duel command center (Dark Magician)

A small, self-contained system for piloting and maintaining a **Dark Magician** deck in
Yu-Gi-Oh! Master Duel over time: a versioned journal (deck + meta + matchups + banlist),
a deck-file codec, and the Claude Code skills/agents that drive them.

> **Honest framing, up front:** Dark Magician is a **rogue / untiered** deck in the current
> Master Duel meta. The realistic ceiling is a **Platinum / Diamond ladder climber** that
> occasionally tops — *not* Tier 1. This system's job is better piloting, matchup prep,
> ratio tuning, and catching banlist shifts. It does **not** pretend to turn DM into a top
> deck. Every fact in the journal is primary-sourced (masterduelmeta / ygoprodeck / Konami)
> and dated, or marked `no data`.

## Layout

```
YGO/
├── README.md                  ← this file
├── journal/                   ← the living data (skills read/write here)
│   ├── DECK-CURRENT.md         deck list, game plan, mulligan, Eye/Gaze toolbox, honest ceiling
│   ├── META-SNAPSHOT.md        current tier list + "what each deck does off one card"
│   ├── MATCHUPS.md             per-archetype matchup briefs (HERO, Enneacraft, …)
│   ├── PATCH-BANLIST.md        latest patch, MD Forbidden/Limited deltas, season, events
│   ├── TWEAK-LOG.md            append-only history of every deck change + why
│   ├── deck-current.ydk        the deck (passcodes)
│   ├── deck-current.ydke.txt   the ydke:// import code (paste into Master Duel)
│   └── collection-reference.csv owned cards + rarity (= craft cost)
├── tools/                     ← the deck-file codec (canonical home)
│   ├── ydk_codec.py            name↔passcode, .ydk↔ydke, MD-legality
│   └── card-id-cache.json      passcode cache, seeded FROM the ygoprodeck API
├── skills/                    ← reference copies of the installed Claude Code skills
│   └── md-deck|md-meta|md-patch|md-ydk|md-import / SKILL.md
└── agents/                    ← reference copies of the installed agents
    └── md-meta-researcher | md-matchup-analyst | md-banlist-watcher | ygo-card-resolver .md
```

**Source vs installed.** The live skills/agents must live under `~/.claude/skills` and
`~/.claude/agents` for Claude Code to load them; they hold absolute paths into this repo
(`/home/archuser/Documents/YGO/...`). The copies in `skills/` and `agents/` here are the
versioned source of record. To re-install (or move to another machine), copy them back into
`~/.claude/` and adjust the absolute `JD` / `SK` paths if the repo lives elsewhere.

## The tools

### Skills (type the slash command)
- **`/md-deck`** — show the deck + game plan; `matchup <archetype>` briefs a matchup;
  `tune` proposes a small, gated ratio change from the meta+banlist+your recent losses;
  `export` regenerates the import code.
- **`/md-meta`** — show the tier list; `refresh` re-pulls it.
- **`/md-patch`** — show the patch/banlist/season; `check` re-pulls it and flags anything
  that touches your cards or the top decks.
- **`/md-ydk`** — the deck-file codec (below).
- **`/md-import`** — the one-step front door for capturing a finished deck: paste a `ydke://`
  (exported from the [deck-transfer browser extension](https://github.com/DawnbrandBots/deck-transfer-for-master-duel))
  and it decodes, verifies, cross-checks the banlist, diffs against your current deck, writes
  it in as `deck-current`, logs the change, and offers to commit. Master Duel has no public
  API — this is how an in-game deck change gets captured without re-typing it.

### Agents (hard-mode researchers the skills call)
`md-meta-researcher`, `md-matchup-analyst`, `md-banlist-watcher`, `ygo-card-resolver` —
all primary-source-or-no-data, dated. Dedicated agents (not generic) so every refresh is
consistent and the skills stay lean.

## The deck-file codec (`tools/ydk_codec.py`)

Cache-first (instant, offline, repeatable); falls back to the ygoprodeck API for unknown
cards, then caches them. The cache is seeded **from the API**, so every passcode is
primary-sourced by construction. Master Duel banlist *limits* (e.g. Maxx "C" Limited 1) are
NOT in the API — cross-check `journal/PATCH-BANLIST.md`.

```fish
set CODEC /home/archuser/Documents/YGO/tools/ydk_codec.py

python3 $CODEC decode journal/deck-current.ydk          # name every card in a deck
python3 $CODEC id "Triple Tactics Talent"               # one name -> passcode
python3 $CODEC name 46986414                            # one passcode -> name
python3 $CODEC build mylist.txt --out deck.ydk          # named list -> .ydk + prints ydke://
python3 $CODEC verify deck.ydk                          # sizes / <=3 / MD-legality
python3 $CODEC seed-from-ydk a.ydk b.ydk                # pre-load cards into the cache
```

`build` input (`mylist.txt`) — sections + quantities; bare passcodes and `# comments` work:
```
#main
3 Dark Magician
3x Magician's Rod
Maxx "C"
#extra
2 Dark Paladin
```
`build` canonicalizes alt-art passcodes to the standard one (cosmetic; Master Duel imports
them identically). Card-name identity is the invariant, not the raw bytes.

## Maintenance workflow

1. `/md-patch check` — has the banlist/patch changed? It flags hits to your cards or the meta.
2. `/md-meta refresh` — re-pull the tier list if it's stale.
3. `/md-deck matchup <deck>` — build a brief for anything beating you.
4. `/md-deck tune` — small, gated ratio change; logs to `TWEAK-LOG.md`.
5. `/md-ydk build` — regenerate the importable file after a change.

Everything is dated; treat anything older than the latest banlist as stale and re-check.
