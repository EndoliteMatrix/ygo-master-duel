# TWEAK-LOG — Dark Magician deck change history

Append-only, newest first. Each entry: date · what changed · why · result (filled in after testing). The `/md-deck tune` mode appends here; never rewrite history.

---

## 2026-06-13 — tune: trimmed 46 → 40 (cut dead weight)
**Change:** `/md-deck tune` cut 6 from main (46 → 40); extra untouched (15). Cuts: −1 Dark Magician of Chaos (40737112), −1 Magician of Chaos (47963370), −2 Bottomless Trap Hole (29401950), −1 Mulcharmy Fuwalos (3→2), −1 Soul Servant (3→2).
**Why (verbatim card text, ygoprodeck API 2026-06-13):**
- **DM of Chaos** — no Special Summon clause; name never becomes "Dark Magician"; *"If this face-up card would leave the field, banish it instead"* → can't even feed the GY. Enabled nothing.
- **Magician of Chaos** — *"You can Ritual Summon this card with 'Chaos Form'"*; no Chaos Form in deck → un-castable, only Eternal-Soul discard fuel. Cut over adding Chaos Form (this was a trim, not an expand).
- **Bottomless Trap Hole ×2** — *"When your opponent Summons a monster(s) with 1500 or more ATK"* — reactive, narrow, does nothing to effects / sub-1500 pieces; slow into HERO and Enneacraft (the two worst matchups).
- **Mulcharmy Fuwalos 3→2** — going-second-only / dead on the play; 2 keeps the tool, lowers play-brick.
- **Soul Servant 3→2** — the only judgment call; the 3rd copy is diminishing (one top-stack suffices; the GY-draw wants *different* names). Alternative considered: keep 3 Soul Servant, Fuwalos 3→1 — rejected because 2 Fuwalos has live targets in the SS-heavy meta.
**Kept:** the Shining Sarcophagus sub-engine (Sarcophagus + DM the Magician of Black Magic + DMG the Magician's Apprentice) — the genuine upgrade carried over from the import.
**Result:** tight 40 / 15 — pending live results. New `ydke://` in [[DECK-CURRENT]] + `deck-current.ydke.txt`.

## 2026-06-13 — imported live in-game deck (md-import pipeline established)
**Change:** Replaced the Disruption v2 baseline as `deck-current` with the user's **actual in-game deck**, captured via the new `/md-import` skill + the DawnbrandBots deck-transfer browser extension (ydke export → paste → decode/verify/diff/version). 46 main / 15 extra. Saved faithfully — the user's exact alt-art passcodes preserved, not canonicalized — since this is a snapshot of what they actually run.
**Diff vs baseline (Disruption v2, 40/15):**
- Main +7 / −1 → 46: Chaos package added (+1 Dark Magician the Magician of Black Magic, +1 Dark Magician of Chaos, +1 Magician of Chaos), +1 Shining Sarcophagus, +2 Bottomless Trap Hole, +1 Mulcharmy Fuwalos (2→3); −1 Nibiru, the Primal Being.
- Extra (15→15): +1 Quintet Magician, −1 Selene, Queen of the Master Magicians.
**Legality:** `verify` OK (legal sizes, ≤3 each, all in MD pool). Every ever-limited card (Maxx "C", Called by the Grave, Bystial Magnamhut, Super Polymerization) is run at exactly 1 → no per-card limit can be violated regardless of its value. No recent banlist change touches a DM/Spellcaster card ([[PATCH-BANLIST]]).
**Honest flags carried forward (for a future `tune`, NOT imposed):** 46 main lowers consistency vs a tight 40; Dark Magician of Chaos (40737112) is a brick here (no Special Summon enabler, GY name ≠ "Dark Magician"); Bottomless Trap Hole x2 is slow/weak into HERO and Enneacraft. On the plus side, Shining Sarcophagus + the Chaos package make DMG the Magician's Apprentice's search live, resolving a prior soft-spot.
**Result:** captured as current — pending live results.

## 2026-06-13 — system created + Disruption v2 baseline
**Change:** Stood up the Master Duel command-center (3 skills + 3 agents + this journal). Set the baseline deck = **Dark Magician — Disruption v2** (40 main / 15 extra), the build finalized 2026-06-09.
**Why:** The prior build felt ~50/50: a dead Chaos package (Master of Chaos with no enabler) + a 44-card pile + almost no proactive disruption (only 3 Ash + 2 Imperm). Rebuild cut to a tight 40, removed the dead Chaos line, and added a real disruption suite (3 Ash, 3 Imperm, Maxx "C" x1, Nibiru, 2 Mulcharmy Fuwalos, Bystial Magnamhut, Called by the Grave, Super Poly). Master of Chaos KEPT — now legitimately summonable via Eye/Gaze of Timaeus single-material substitution (verified card text 2026-06-13).
**Verified this session (ygoprodeck card text):** the Eye/Gaze toolbox off one Dark Magician = Timaeus the United (unaffected), Dark Cavalry (target-negate), Dark Paladin (spell-negate), DM the Dragon Knight (S/T protection), Amulet Dragon, Dark Magician of Destruction (searcher), Master of Chaos (board-wipe). Maxx "C" is **Limited 1 in MD** (collection CSV's x3 is now illegal).
**Open soft-spots flagged for a future `tune`:** DMG the Magician's Apprentice (dead Shining Sarcophagus search); 2x Mulcharmy Fuwalos (pure going-second); Super Poly at 1.
**Result:** baseline — pending live results. User reports HERO and Enneacraft as the worst matchups → see [[MATCHUPS]].

### How to use this log going forward
When you play a batch of games, tell `/md-deck tune` (a) what beat you and how, and (b) any card that felt dead. It will read [[META-SNAPSHOT]] + [[PATCH-BANLIST]], propose a small ratio change (gated on your confirmation), update [[DECK-CURRENT]] + `deck-current.ydk`, and append the next entry here. Small changes, one variable at a time — so you can tell what actually helped.
