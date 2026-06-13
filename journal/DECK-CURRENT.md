# DECK-CURRENT — Dark Magician (Disruption build)

`Last updated: 2026-06-13` · managed by the `/md-deck` skill · pilot: Mr. Rocketship

Import code (`deck-current.ydke.txt`, regenerated from `deck-current.ydk`):
```
ydke://rvTMAq70zAKu9MwC+CsmAKj50gFHvNEFR7zRBUe80QVhGGwAYRhsAGEYbAD1KrsA9Sq7APUquwAIj9ACCI/QAgiP0AJ4Q18BeENfAXhDXwEM+sMFDPrDBQQdjAMK0OYCCtDmAm47GwDEA1QBryPeAK8j3gCvI94ANQeDAjUHgwIiSJkAIkiZACJImQAqlWUB1xqfAaCUBAI+pHEBXWneAg==!umKKA7piigNS6REF1pD+AtaQ/gLhBd8F4QXfBTnKYAR6nXwCzzd+BH6JQwNIiLMA8bgeBScJwAX/JrsC!!
```

## The honest ceiling (read this first)

Dark Magician is a **rogue / untiered** deck in Master Duel as of `2026-06-13` (it does not appear in masterduelmeta's Tier 1/2/3 — see [[META-SNAPSHOT]]). The realistic ceiling for a true DM build is a **Platinum / Diamond ladder climber that posts the occasional Master-rank top**, *not* Tier 1. The tiered "Spellcaster" decks (Kewl Tune, Elfnote) are different engines, not Dark Magician.

So "yield results over time" here means four concrete, achievable things — **not** turning DM into a top deck:
1. **Better piloting** — knowing the 1-card lines and the Eye/Gaze toolbox (below).
2. **Matchup prep** — the [[MATCHUPS]] briefs for the decks that beat you.
3. **Ratio tuning** — `/md-deck tune` trims clunkers and adjusts the disruption count as the meta moves.
4. **Catching banlist shifts** — `/md-patch check` flags any hit to your cards or the meta ([[PATCH-BANLIST]]).

This is honestly stated once, here, so the system never quietly over-promises. Source: masterduelmeta tier list, observed 2026-06-13.

## Why it used to feel ~50/50 (the diagnosis we fixed)

- **Bricks crowded the hand.** The old list ran a Chaos package with no enabler (Master of Chaos / Chaos cards needing Chaos Form, which wasn't in the deck) and a 44-card pile. Dead cards = no opening.
- **Almost no proactive disruption.** Modern decks "do something off any hand" because they run a redundant engine *plus* hand traps that act on the opponent's turn. The old build had ~3 Ash + 2 Imperm and nothing else — so on the draw you sat there while they comboed.
- **Fix:** cut to a tight 40, removed the dead Chaos line, and added a real hand-trap / disruption suite (3 Ash, 3 Imperm, Maxx "C", Nibiru, 2 Mulcharmy Fuwalos, Bystial Magnamhut, Called by the Grave, Super Poly). Now you interact on their turn instead of praying.

## The deck (40 main / 15 extra)

### Engine / starters (this is what gives you a "do-something" hand)
| # | Card | What it starts |
|---|---|---|
| 3 | **Dark Magician** | The anchor every fusion + Eternal Soul + Circle keys off. |
| 3 | **Magician's Rod** | NS → search a DM Spell/Trap (grab **Eternal Soul** or **Dark Magical Circle**). GY: tribute a face-up Spellcaster to add Rod back — recurs. |
| 3 | **Magicians' Souls** | Send up to 2 Spells/Traps OR 1 DM/DMG from deck to GY + **draw 2**; or special a Lv6+ Spellcaster from hand. Fills GY + digs. |
| 3 | **Illusion of Chaos** | Reveal in hand → add Dark Magician (or a card that mentions it) + place 1 from hand on top of deck. Quick effect: bounce itself, SS a DM from GY, **negate an opponent monster effect** — a built-in hand trap. |
| 3 | **Dark Magical Circle** | On any DM summon: reveal top 3, add a DM-or-related. On activation: reveal top 3, and if a DM is there, **banish 1 card the opponent controls** — your clean removal/out. |
| 3 | **Soul Servant** | Stack the top of your deck with a DM-related card (fixes your next draw). GY: banish it → **draw = different DM/DMG/Palladium names on field + GY**. |
| 2 | **Preparation of Rites** | Search **Illusion of Chaos** (Lv≤7 Ritual) from deck + recover a Ritual Spell from GY. Effectively copies 4-6 of your searcher. |
| 1 | **Secrets of Dark Magic** | Quick-Play: Fusion **or** Ritual summon including DM/DMG from hand/field. Flexible fusion enabler at instant speed. |

### The Eye / Gaze of Timaeus toolbox (the piloting key)
**1x The Eye of Timaeus** (Normal) + **1x The Gaze of Timaeus** (Quick-Play, works from **field OR GY**, but the fusion banishes itself next End Phase — temporary). Each, off a **single Dark Magician**, can fusion-summon any DM-listing fusion using just that one body (single-material substitution). Pick the answer per matchup:

| Make this | When / why (verbatim-verified) |
|---|---|
| **Timaeus the United** | *"after Special Summoned, unaffected by other cards' effects until the end of your next turn."* Walks through **HERO's Dark Law** and **Enneacraft's flip-negates.** Best vs floodgate/negate decks. Quick effect: destroy 1 S/T. |
| **Dark Cavalry** | Quick Effect: *"a card/effect is activated that targets a card on the field: discard 1; negate the activation and destroy it."* Generic targeting-negate body. |
| **Dark Paladin** | Quick Effect: *"a Spell is activated: discard 1; negate and destroy it."* Spell-negate — great vs Sky Striker / Branded / spell-heavy combo. +500 per Dragon. |
| **DM the Dragon Knight** | *"opponent cannot target your Spells/Traps with effects, also they can't be destroyed by opponent's effects."* Shields **Eternal Soul / Dark Magical Circle.** |
| **Amulet Dragon** | On SS: banish any number of Spells from any GY, +100 ATK each. Removal + ATK. |
| **Dark Magician of Destruction** | On SS: add a DM or a card that mentions it. A second searcher-body. (Can also self-SS by banishing a Lv6+ DARK Spellcaster on a turn a Spell resolved.) |
| **Master of Chaos** | On Fusion Summon: SS a LIGHT/DARK from GY. Tribute 1 LIGHT + 1 DARK: **banish ALL opponent monsters** (board wipe). |

> Note: **Dark Paladin** lists "Dark Magician + Buster Blader," but Eye/Gaze substitute the whole material, so you make it off one DM with **no Buster Blader in the deck** — that is intended.

### Disruption suite (this is the half that fixed the 50/50)
| # | Card | Role |
|---|---|---|
| 3 | **Ash Blossom & Joyous Spring** | Negate a search / SS-from-deck / mill / draw. Universal "stop your one card." |
| 3 | **Infinite Impermanence** | Negate a face-up monster effect (+ column-lock Spells if you control no cards). **Careful vs face-down decks** — see [[MATCHUPS]] Enneacraft. |
| 1 | **Maxx "C"** | **Limited to 1 in Master Duel** (do not run 3 — that's now illegal). Draw per opponent Special Summon; taxes combo decks. |
| 1 | **Nibiru, the Primal Being** | Punish 5+ summons (wipes their over-extended board). Weak vs low-summon decks (HERO, Enneacraft). |
| 2 | **Mulcharmy Fuwalos** | Going-**second** only ("control no cards"): draw each time they SS from deck/Extra. **Dead on the play** — that's why it's 2, not 3. |
| 1 | **Bystial Magnamhut** | From hand: banish a LIGHT/DARK from a GY → SS this, search a Bystial / disrupt their GY. Also a DARK Dragon body for the Timaeus/Paladin Dragon clauses. |
| 1 | **Called by the Grave** | Answer their **Maxx "C"** on your turn, and their GY effects. |
| 1 | **Super Polymerization** | *"Neither player can activate cards or effects in response."* Uninterruptible — steal an opponent monster as fusion material. See target math in [[MATCHUPS]]. |

### Backbone traps
| # | Card | Role |
|---|---|---|
| 2 | **Eternal Soul** | DM in your zone is **unaffected by opponent's effects**; once/turn SS a DM from hand/GY, or add Dark Magic Attack/Thousand Knives. **Downside:** if it leaves the field, *destroy all your monsters* — don't let it get bounced into a full board. |

### Other main-deck bodies
- **1x Apprentice Illusion Magician** (DARK, 2000) — discard 1 to SS from hand, on summon add a Dark Magician. A DARK Spellcaster body for Super Poly (Mudragon) and a 2000 beater.
- **1x Dark Magician Girl the Magician's Apprentice** — SS by discarding 1; becomes "Dark Magician Girl." **Honest note: its printed search (Shining Sarcophagus) is DEAD here** — no Sarcophagus in the deck. It's a discard-enabler / DMG body only. Flagged as a soft spot; `/md-deck tune` may cut it.

### Extra deck (15)
2x Dark Magician of Destruction · 2x The Dark Magicians · 2x Dark Paladin · 1x Dark Cavalry · 1x DM the Dragon Knight · 1x Amulet Dragon · 1x Master of Chaos · 1x Timaeus the United · 1x Mudragon of the Swamp · 1x Garura · 1x Ebon Illusion Magician · 1x Selene, Queen of the Master Magicians.

- **Mudragon** = Super Poly target for "same Attribute, **different** Types" (e.g. your DARK Spellcaster + their DARK Warrior HERO).
- **Garura** = Super Poly target for "same Type **and** Attribute, different names" (e.g. two FIRE Dragons vs Tenpai).
- **Ebon Illusion Magician** (Rank 7) + **Selene** (Link-2) = extender/recursion bodies off two Level-7 Spellcasters / a wide board.

## 1-card openers (what a good hand actually does)

Any **one** of these is a real opening: Magician's Rod, Magicians' Souls, Illusion of Chaos, Dark Magical Circle, Soul Servant, or Preparation of Rites (→ Illusion of Chaos). Starter density is high (≈18-19 cards see a starter), which is the whole point of the rebuild.

- **Rod line:** NS Rod → search **Eternal Soul** → (later) Eternal Soul SS Dark Magician → Dark Magical Circle banish / Eye into a negate body.
- **Souls line:** Souls send DM to GY + draw 2 → Eternal Soul (from Rod or drawn) revives DM → Circle.
- **Circle line:** activate Circle, reveal top 3; summon any DM (Eternal Soul / Apprentice) to trigger Circle's **banish**.
- **Goal of turn 1 on the play:** a Dark Magician on board under **Eternal Soul** (unaffected) + **Dark Magical Circle** up + a held disruption (Ash / Imperm). That's a real, defensible board for a rogue deck.

## Mulligan / keep guide

- **On the draw:** keep any hand with **a starter + a disruption** (Ash / Imperm). Ash protects your engine; a starter builds the board.
- **On the play:** you want a starter that ends on **Eternal Soul + Circle**; Mulcharmy Fuwalos is a **dead card on the play** — don't count it as your interaction.
- **Going second into a known combo deck:** Mulcharmy Fuwalos + Ash + Imperm is a great "break their turn" hand. Nibiru shines only vs decks that summon 5+.
- **Reject** hands that are all bodies + no starter and no disruption.

## Known soft spots (candidates for `tune`)
- **DMG the Magician's Apprentice** — dead search (no Shining Sarcophagus).
- **2x Mulcharmy Fuwalos** — pure going-second; some metas want it at 1, or swapped for a 2nd Called by the Grave / 3rd disruption depending on what's tiered ([[META-SNAPSHOT]]).
- **Super Poly at 1** vs a Fusion-heavy meta could go to 2; vs a low-fusion meta it's a luxury.

## Craft reference
Full owned-cards + rarity list is in `collection-reference.csv` (N/R/SR/UR per card = craft cost). **Caveat:** that CSV lists Maxx "C" x3 — now illegal (Limited 1 in MD). The live, legal list is this file + `deck-current.ydk`.

---
Linked: [[META-SNAPSHOT]] · [[MATCHUPS]] · [[PATCH-BANLIST]] · [[TWEAK-LOG]]
