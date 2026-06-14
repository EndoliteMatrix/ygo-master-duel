# DECK-CURRENT — "Eternal Sarcophagus" (Dark Magician control / disruption)

**Deck name:** Eternal Sarcophagus — use this in-game so the journal, deck file, and client all match.
`Last updated: 2026-06-13` · managed by the `/md-deck` + `/md-import` skills · pilot: Mr. Rocketship

Import code (`deck-current.ydke.txt`):
```
ydke://r/TMAq/0zAKv9MwCR7zRBUe80QVHvNEFKpVlAWEYbABhGGwAYRhsALAj3gCwI94AsCPeADUHgwI1B4MCqPnSAaCUBAL4KyYAkToFAPUquwD1KrsA9Sq7AAz6wwUM+sMFbjsbAAiP0AIIj9ACCI/QAgaHwQRdad4CPqRxAXhDXwF4Q18BBB2MA8QDVAEiSJkAIkiZACJImQAK0OYCCtDmAg==!folDA0iIswDiBd8F4gXfBc83fgR6nXwCOcpgBNaQ/gLWkP4CUukRBbpiigO6YooD8bgeBY9ZCAUnCcAF!!
```

> **Status (2026-06-13):** Trimmed from the 46-card in-game import to a tight **40 main / 15 extra**
> via `/md-deck tune`. Six cuts, five forced by card logic. Full diff + reasoning in [[TWEAK-LOG]].

## The honest ceiling (read this first)

Dark Magician is a **rogue / untiered** deck in Master Duel as of `2026-06-13` (it does not appear in masterduelmeta's Tier 1/2/3 — see [[META-SNAPSHOT]]). The realistic ceiling for a true DM build is a **Platinum / Diamond ladder climber that posts the occasional Master-rank top**, *not* Tier 1. The tiered "Spellcaster" decks (Kewl Tune, Elfnote) are different engines, not Dark Magician.

"Yield results over time" here means four achievable things — **not** turning DM into a top deck:
1. **Better piloting** — the 1-card lines and the Eye/Gaze toolbox (below).
2. **Matchup prep** — the [[MATCHUPS]] briefs for the decks that beat you (HERO, Enneacraft).
3. **Ratio tuning** — `/md-deck tune` trims clunkers as the meta moves.
4. **Catching banlist shifts** — `/md-patch check` flags any hit to your cards or the meta ([[PATCH-BANLIST]]).

Source: masterduelmeta tier list, observed 2026-06-13.

## What this 40 is (after the trim)

This keeps the **Shining Sarcophagus sub-engine** that the in-game build added — the genuinely good part — and removes the dead weight that was diluting the 46:

**Kept — the Sarcophagus sub-engine.**
- **Shining Sarcophagus** (Continuous Spell) *"add 1 card that mentions 'Shining Sarcophagus' from your Deck to your hand"* — searches **DMG the Magician's Apprentice** (her printed search is no longer dead) **and Dark Magician the Magician of Black Magic.** Also disrupts: *"If your opponent Special Summons a monster(s) from the GY… discard 1 Spell, then target 1… send it to the GY"* (anti-Bystial / anti-revival).
- **Dark Magician the Magician of Black Magic** (Lv7 DARK Spellcaster) — *"name becomes 'Dark Magician' while on the field."* Free SS from hand *"If 'Shining Sarcophagus' is on the field,"* self-recurs + Sets a DM S/T from deck when destroyed by effect. A resilient extra DM-body for Eternal Soul, Circle, and Eye/Gaze fusion.

**Cut (see [[TWEAK-LOG]] for the verbatim text behind each):** Dark Magician of Chaos (brick — no self-SS, never renames to DM, banishes itself instead of feeding the GY); Magician of Chaos (no Chaos Form in deck → un-castable, fuel-only); Bottomless Trap Hole ×2 (reactive/narrow, slow vs HERO & Enneacraft); Mulcharmy Fuwalos 3→2; Soul Servant 3→2. Nibiru was already cut in the import.

**Consistency.** Back to a tight 40 — starter density is up vs the 46, and you brick on going-second-only cards less often.

## The deck (40 main / 15 extra)

### Engine / starters (what gives you a "do-something" hand)
| # | Card | What it starts |
|---|---|---|
| 3 | **Dark Magician** | The anchor every fusion + Eternal Soul + Circle keys off. |
| 3 | **Magician's Rod** | NS → search a DM Spell/Trap (grab **Eternal Soul** or **Dark Magical Circle**). GY: tribute a face-up Spellcaster to add Rod back. |
| 3 | **Magicians' Souls** | Send up to 2 S/T OR 1 DM/DMG from deck to GY + **draw 2**; or special a Lv6+ Spellcaster from hand. Fills GY + digs. |
| 3 | **Illusion of Chaos** | Reveal in hand → add Dark Magician (or a card mentioning it) + place 1 from hand on top of deck. Quick effect: bounce itself, SS a DM from GY, **negate an opponent monster effect** — a built-in hand trap. |
| 3 | **Dark Magical Circle** | On any DM summon: reveal top 3, add a DM-or-related. On activation: reveal top 3, and if a DM is there, **banish 1 card the opponent controls** — clean removal/out. |
| 2 | **Soul Servant** | Stack the top of your deck with a DM-related card. GY: banish it → **draw = different DM/DMG/Palladium names on field + GY**. (Trimmed 3→2.) |
| 2 | **Preparation of Rites** | Search **Illusion of Chaos** (Lv≤7 Ritual) + recover a Ritual Spell from GY. Effectively copies your searcher. |
| 1 | **Secrets of Dark Magic** | Quick-Play: Fusion **or** Ritual summon including DM/DMG from hand/field. Flexible instant-speed enabler. |

### Shining Sarcophagus sub-engine
| # | Card | Role |
|---|---|---|
| 1 | **Shining Sarcophagus** | Continuous Spell; *"cannot be destroyed by monster effects."* Searches a "mentions Shining Sarcophagus" card + sends-to-GY any monster the opponent SS's from their GY. |
| 1 | **DM the Magician of Black Magic** | Name = "Dark Magician" on field; free SS off Sarcophagus; self-recurs + Sets a DM S/T from deck when destroyed by effect. |
| 1 | **DMG the Magician's Apprentice** | SS by discarding 1; becomes "Dark Magician Girl." Her **Shining Sarcophagus search is now live.** Also a discard-enabler / Super Poly DARK Spellcaster body. |

### The Eye / Gaze of Timaeus toolbox (the piloting key)
**1x The Eye of Timaeus** (Normal) + **1x The Gaze of Timaeus** (Quick-Play, works from **field OR GY**, fusion banishes itself next End Phase — temporary). Each, off a **single Dark Magician**, can fusion-summon any DM-listing fusion using just that one body (single-material substitution). Pick the answer per matchup:

| Make this | When / why (verbatim-verified) |
|---|---|
| **Timaeus the United** | *"after Special Summoned, unaffected by other cards' effects until the end of your next turn."* Walks through **HERO's Dark Law** and **Enneacraft's flip-negates.** Best vs floodgate/negate. Quick effect: destroy 1 S/T. |
| **Dark Cavalry** | *"a card/effect is activated that targets a card on the field: discard 1; negate the activation and destroy it."* Generic targeting-negate body. |
| **Dark Paladin** | *"a Spell is activated: discard 1; negate and destroy it."* Spell-negate — great vs Sky Striker / Branded / spell-heavy combo. (Made off one DM with **no Buster Blader in deck** — intended.) |
| **DM the Dragon Knight** | Opponent *"cannot target your Spells/Traps with effects, also they can't be destroyed by opponent's effects."* Shields **Eternal Soul / Dark Magical Circle.** |
| **Amulet Dragon** | On SS: banish any number of Spells from any GY, +100 ATK each. Removal + ATK. |
| **Dark Magician of Destruction** | On SS: add a DM or a card that mentions it. A second searcher-body. |
| **Master of Chaos** | On Fusion Summon: SS a LIGHT/DARK from GY. Tribute 1 LIGHT + 1 DARK: **banish ALL opponent monsters** (board wipe). |

### Disruption suite
| # | Card | Role |
|---|---|---|
| 3 | **Ash Blossom & Joyous Spring** | Negate a search / SS-from-deck / mill / draw. Universal "stop your one card." |
| 3 | **Infinite Impermanence** | Negate a face-up monster effect (+ column-lock if you control no cards). **Careful vs face-down decks** — see [[MATCHUPS]] Enneacraft. |
| 2 | **Mulcharmy Fuwalos** | Going-**second** only ("control no cards"): draw each time they SS from deck/Extra. **Dead on the play** — at 2 (trimmed from 3). |
| 1 | **Maxx "C"** | **Limited to 1 in Master Duel.** Draw per opponent Special Summon; taxes combo. |
| 1 | **Bystial Magnamhut** | From hand: banish a LIGHT/DARK from a GY → SS this, search a Bystial / disrupt their GY. Also a DARK Dragon body for the Timaeus/Paladin Dragon clauses. |
| 1 | **Called by the Grave** | Answer their **Maxx "C"** on your turn, and their GY effects. |
| 1 | **Super Polymerization** | *"Neither player can activate cards or effects in response."* Uninterruptible — steal an opponent monster as fusion material (Mudragon / Garura). Target math in [[MATCHUPS]]. |

### Backbone traps
| # | Card | Role |
|---|---|---|
| 2 | **Eternal Soul** | DM in your zone is **unaffected by opponent's effects**; once/turn SS a DM from hand/GY, or add Dark Magic Attack/Thousand Knives. **Downside:** if it leaves the field, *destroy all your monsters* — don't let it get bounced into a full board. |

### Other main-deck bodies
- **1x Apprentice Illusion Magician** (DARK, 2000) — discard 1 to SS, on summon add a Dark Magician. A DARK Spellcaster for Super Poly (Mudragon), a 2000 beater, and a discard outlet.

### Extra deck (15)
2x Dark Magician of Destruction · 2x The Dark Magicians · 2x Dark Paladin · 1x Dark Cavalry · 1x DM the Dragon Knight · 1x Amulet Dragon · 1x Master of Chaos · 1x Timaeus the United · 1x Mudragon of the Swamp · 1x Garura · 1x Ebon Illusion Magician · 1x Quintet Magician.

- **Mudragon** = Super Poly target for "same Attribute, **different** Types" (your DARK Spellcaster + their DARK Warrior HERO).
- **Garura** = Super Poly target for "same Type **and** Attribute, different names."
- **Quintet Magician** (Lv12 Fusion, *"5 Spellcaster monsters"*) — *"destroy all cards your opponent controls"* if fused with 5 different-named Spellcasters, and *"cannot be destroyed by card effects."* A grind-game board-wipe finisher, demanding (5 materials) — not a turn-1 play.
- **Ebon Illusion Magician** (Rank 7) = extender/recursion off two Level-7 Spellcasters.

## 1-card openers
Any **one** of these is a real opening: Magician's Rod, Magicians' Souls, Illusion of Chaos, Dark Magical Circle, Soul Servant, or Preparation of Rites (→ Illusion of Chaos). With the trim, starter density is back up (~16-18 starters over 40).

- **Rod line:** NS Rod → search **Eternal Soul** → Eternal Soul SS Dark Magician → Circle banish / Eye into a negate body.
- **Souls line:** Souls send DM to GY + draw 2 → Eternal Soul revives DM → Circle.
- **Circle line:** activate Circle, reveal top 3; summon any DM to trigger Circle's **banish**.
- **Sarcophagus line:** resolve Shining Sarcophagus → search DM the Magician of Black Magic → (Sarcophagus on field) free-SS it as a "Dark Magician" → Circle trigger / Eye fusion.
- **Goal of turn 1 on the play:** a Dark Magician on board under **Eternal Soul** (unaffected) + **Dark Magical Circle** up + a held disruption (Ash / Imperm).

## Mulligan / keep guide
- **On the draw:** keep any hand with **a starter + a disruption** (Ash / Imperm).
- **On the play:** want a starter that ends on **Eternal Soul + Circle**. **Mulcharmy Fuwalos is dead on the play** — don't keep a hand leaning on it as your interaction.
- **Going second into a known combo deck:** Fuwalos + Ash + Imperm is a great "break their turn" hand.
- **Reject** hands that are all bodies + no starter and no disruption.

## Known soft spots (candidates for the next `tune`)
- **Super Polymerization at 1** — vs a Fusion-heavy meta could go to 2; vs a low-fusion meta it's a luxury.
- **Quintet Magician** — high payoff, hard to assemble (5 Spellcasters); earns its slot only in grind games.
- **Bystial Magnamhut at 1** — strong vs DARK/LIGHT GY decks (incl. some HERO lines); the meta could justify a 2nd.
- If HERO / Enneacraft keep beating you, the lever is more *unaffected/uninterruptible* outs (Timaeus lines, a 2nd Super Poly), not more reactive traps — log the losses and `/md-deck tune` will weigh it.

## Craft reference
Full owned-cards + rarity list is in `collection-reference.csv` (N/R/SR/UR = craft cost). **Caveat:** that CSV lists Maxx "C" x3 — illegal (Limited 1). The live, legal list is this file + `deck-current.ydk`.

---
Linked: [[META-SNAPSHOT]] · [[MATCHUPS]] · [[PATCH-BANLIST]] · [[TWEAK-LOG]]
