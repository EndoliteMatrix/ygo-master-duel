# TWEAK-LOG — Dark Magician deck change history

Append-only, newest first. Each entry: date · what changed · why · result (filled in after testing). The `/md-deck tune` mode appends here; never rewrite history.

---

## 2026-06-13 — system created + Disruption v2 baseline
**Change:** Stood up the Master Duel command-center (3 skills + 3 agents + this journal). Set the baseline deck = **Dark Magician — Disruption v2** (40 main / 15 extra), the build finalized 2026-06-09.
**Why:** The prior build felt ~50/50: a dead Chaos package (Master of Chaos with no enabler) + a 44-card pile + almost no proactive disruption (only 3 Ash + 2 Imperm). Rebuild cut to a tight 40, removed the dead Chaos line, and added a real disruption suite (3 Ash, 3 Imperm, Maxx "C" x1, Nibiru, 2 Mulcharmy Fuwalos, Bystial Magnamhut, Called by the Grave, Super Poly). Master of Chaos KEPT — now legitimately summonable via Eye/Gaze of Timaeus single-material substitution (verified card text 2026-06-13).
**Verified this session (ygoprodeck card text):** the Eye/Gaze toolbox off one Dark Magician = Timaeus the United (unaffected), Dark Cavalry (target-negate), Dark Paladin (spell-negate), DM the Dragon Knight (S/T protection), Amulet Dragon, Dark Magician of Destruction (searcher), Master of Chaos (board-wipe). Maxx "C" is **Limited 1 in MD** (collection CSV's x3 is now illegal).
**Open soft-spots flagged for a future `tune`:** DMG the Magician's Apprentice (dead Shining Sarcophagus search); 2x Mulcharmy Fuwalos (pure going-second); Super Poly at 1.
**Result:** baseline — pending live results. User reports HERO and Enneacraft as the worst matchups → see [[MATCHUPS]].

### How to use this log going forward
When you play a batch of games, tell `/md-deck tune` (a) what beat you and how, and (b) any card that felt dead. It will read [[META-SNAPSHOT]] + [[PATCH-BANLIST]], propose a small ratio change (gated on your confirmation), update [[DECK-CURRENT]] + `deck-current.ydk`, and append the next entry here. Small changes, one variable at a time — so you can tell what actually helped.
