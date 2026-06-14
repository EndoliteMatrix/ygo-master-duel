# DECK-CURRENT — Dark Magician (Sarcophagus / Disruption build)

`Last updated: 2026-06-13` · managed by the `/md-deck` + `/md-import` skills · pilot: Mr. Rocketship

Import code (`deck-current.ydke.txt`) — captured from the live in-game deck via `/md-import`:
```
ydke://r/TMAq/0zAKv9MwCR7zRBUe80QVHvNEFKpVlAWEYbABhGGwAYRhsALAj3gCwI94AsCPeADUHgwI1B4MCNQeDAqj50gGglAQC+CsmAJE6BQBYmW0C6tzbAvUquwD1KrsA9Sq7AAz6wwUM+sMFbjsbAAiP0AIIj9ACCI/QAgaHwQRdad4CPqRxAXhDXwF4Q18BeENfAQQdjAPEA1QBXqPAAV6jwAEiSJkAIkiZACJImQAK0OYCCtDmAg==!folDA0iIswDiBd8F4gXfBc83fgR6nXwCOcpgBNaQ/gLWkP4CUukRBbpiigO6YooD8bgeBY9ZCAUnCcAF!!
```

> **Note (2026-06-13):** This file now reflects your **actual in-game deck (46 main / 15 extra)**,
> imported via `/md-import`, replacing the earlier 40-card "Disruption v2" baseline. The diff and
> rationale are in [[TWEAK-LOG]]. It is **46, not a tight 40** — see "Honest read" below.

## The honest ceiling (read this first)

Dark Magician is a **rogue / untiered** deck in Master Duel as of `2026-06-13` (it does not appear in masterduelmeta's Tier 1/2/3 — see [[META-SNAPSHOT]]). The realistic ceiling for a true DM build is a **Platinum / Diamond ladder climber that posts the occasional Master-rank top**, *not* Tier 1. The tiered "Spellcaster" decks (Kewl Tune, Elfnote) are different engines, not Dark Magician.

"Yield results over time" here means four achievable things — **not** turning DM into a top deck:
1. **Better piloting** — the 1-card lines and the Eye/Gaze toolbox (below).
2. **Matchup prep** — the [[MATCHUPS]] briefs for the decks that beat you (HERO, Enneacraft).
3. **Ratio tuning** — `/md-deck tune` trims clunkers as the meta moves.
4. **Catching banlist shifts** — `/md-patch check` flags any hit to your cards or the meta ([[PATCH-BANLIST]]).

Source: masterduelmeta tier list, observed 2026-06-13.

## Honest read of this 46-card build (the upside and the dead weight)

**The good — a Shining Sarcophagus sub-engine.** You added a real package that fixes a prior soft spot:
- **Shining Sarcophagus** (Continuous Spell) *"add 1 card that mentions 'Shining Sarcophagus' from your Deck to your hand"* — searches **DMG the Magician's Apprentice** (her printed search is no longer dead) **and Dark Magician the Magician of Black Magic.** It also disrupts: *"If your opponent Special Summons a monster(s) from the GY… discard 1 Spell, then target 1… send it to the GY"* (anti-Bystial / anti-revival).
- **Dark Magician the Magician of Black Magic** (Lv7 DARK Spellcaster) — *"This card's name becomes 'Dark Magician' while on the field."* Free SS from hand *"If 'Shining Sarcophagus' is on the field,"* and when destroyed by effect with a Lv5+ monster out it *"Special Summon this card, then… Set 1 Spell/Trap from your Deck that mentions 'Dark Magician'"* (recovers Eternal Soul / Circle). A resilient extra DM-body — more density for Eternal Soul, Circle, and Eye/Gaze fusion.

**The dead weight — the two "Chaos" monsters (cut candidates, verbatim-verified):**
- **Dark Magician of Chaos** (40737112, Lv8) is a **brick** here: no Special Summon clause (needs a tribute to Normal Summon), its name **never becomes "Dark Magician,"** and *"If this face-up card would leave the field, banish it instead"* — so it can't even feed the GY for Eternal Soul. It enables nothing in this deck.
- **Magician of Chaos** (47963370, Lv7 Ritual) reads *"You can Ritual Summon this card with 'Chaos Form'"* — and **there is no Chaos Form in the deck**, so you can't hard-cast it. Its only use here is as **discard fuel**: get it to the GY (e.g. Apprentice Illusion Magician's discard cost), where *"This card's name becomes 'Dark Magician'… in the GY,"* then **Eternal Soul revives it** as a 2300 body with a once/turn Quick-Effect *"target 1 card on the field; destroy it."* Narrow and conditional. Either add Chaos Form to make it a real Ritual, or treat it as one-of Eternal-Soul fuel, or cut.

**Consistency.** 46 main vs a tight 40 = ~6 extra non-starters, slightly lower odds of opening a starter. Fine for ladder; the first thing `/md-deck tune` would trim toward 40 is the Chaos pair + a Bottomless.

## The deck (46 main / 15 extra)

### Engine / starters (what gives you a "do-something" hand)
| # | Card | What it starts |
|---|---|---|
| 3 | **Dark Magician** | The anchor every fusion + Eternal Soul + Circle keys off. |
| 3 | **Magician's Rod** | NS → search a DM Spell/Trap (grab **Eternal Soul** or **Dark Magical Circle**). GY: tribute a face-up Spellcaster to add Rod back. |
| 3 | **Magicians' Souls** | Send up to 2 S/T OR 1 DM/DMG from deck to GY + **draw 2**; or special a Lv6+ Spellcaster from hand. Fills GY + digs. |
| 3 | **Illusion of Chaos** | Reveal in hand → add Dark Magician (or a card mentioning it) + place 1 from hand on top of deck. Quick effect: bounce itself, SS a DM from GY, **negate an opponent monster effect** — a built-in hand trap. |
| 3 | **Dark Magical Circle** | On any DM summon: reveal top 3, add a DM-or-related. On activation: reveal top 3, and if a DM is there, **banish 1 card the opponent controls** — clean removal/out. |
| 3 | **Soul Servant** | Stack the top of your deck with a DM-related card. GY: banish it → **draw = different DM/DMG/Palladium names on field + GY**. |
| 2 | **Preparation of Rites** | Search **Illusion of Chaos** (Lv≤7 Ritual) + recover a Ritual Spell from GY. Effectively copies your searcher. |
| 1 | **Secrets of Dark Magic** | Quick-Play: Fusion **or** Ritual summon including DM/DMG from hand/field. Flexible instant-speed enabler. |

### Shining Sarcophagus sub-engine (the new package)
| # | Card | Role |
|---|---|---|
| 1 | **Shining Sarcophagus** | Continuous Spell; *"cannot be destroyed by monster effects."* Searches a "mentions Shining Sarcophagus" card (DMG the Magician's Apprentice / DM the Magician of Black Magic) + sends-to-GY any monster the opponent SS's from their GY. |
| 1 | **DM the Magician of Black Magic** | Name = "Dark Magician" on field; free SS off Sarcophagus; self-recurs + Sets a DM S/T from deck when destroyed by effect. A resilient DM-body. |
| 1 | **DMG the Magician's Apprentice** | SS by discarding 1; becomes "Dark Magician Girl." Her printed **Shining Sarcophagus search is now live** (resolves the old dead-card flag). Also a discard-enabler / Super Poly DARK Spellcaster body. |

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
| 3 | **Mulcharmy Fuwalos** | Going-**second** only ("control no cards"): draw each time they SS from deck/Extra. **Dead on the play** — now at 3 (was 2); strong vs the SS-heavy field, but raises your brick-on-play rate. |
| 1 | **Maxx "C"** | **Limited to 1 in Master Duel.** Draw per opponent Special Summon; taxes combo. |
| 1 | **Bystial Magnamhut** | From hand: banish a LIGHT/DARK from a GY → SS this, search a Bystial / disrupt their GY. Also a DARK Dragon body for the Timaeus/Paladin Dragon clauses. |
| 1 | **Called by the Grave** | Answer their **Maxx "C"** on your turn, and their GY effects. |
| 1 | **Super Polymerization** | *"Neither player can activate cards or effects in response."* Uninterruptible — steal an opponent monster as fusion material (Mudragon / Garura). Target math in [[MATCHUPS]]. |
| 2 | **Bottomless Trap Hole** | *"When your opponent Summons a monster(s) with 1500+ ATK: destroy… and banish it."* Honest caveat: **reactive and narrow** — only fires on a 1500+ ATK *summon*, does nothing to effects or sub-1500 combo pieces. **Slow into HERO and Enneacraft** (your two worst matchups). Top trim candidate. |

> **Note: Nibiru was cut** in this build (was 1 in the baseline) — it only shone vs 5+ summon boards.

### Backbone traps
| # | Card | Role |
|---|---|---|
| 2 | **Eternal Soul** | DM in your zone is **unaffected by opponent's effects**; once/turn SS a DM from hand/GY, or add Dark Magic Attack/Thousand Knives. **Downside:** if it leaves the field, *destroy all your monsters* — don't let it get bounced into a full board. Note: it can revive **Magician of Chaos** out of the GY (name = DM there). |

### Other main-deck bodies
- **1x Apprentice Illusion Magician** (DARK, 2000) — discard 1 to SS, on summon add a Dark Magician. A DARK Spellcaster for Super Poly (Mudragon), a 2000 beater, and the **discard outlet** that turns Magician of Chaos into Eternal-Soul fuel.
- **1x Dark Magician of Chaos** — see "dead weight" above. Brick; cut candidate.
- **1x Magician of Chaos** — see "dead weight" above. Discard-and-revive fuel only (no Chaos Form).

### Extra deck (15)
2x Dark Magician of Destruction · 2x The Dark Magicians · 2x Dark Paladin · 1x Dark Cavalry · 1x DM the Dragon Knight · 1x Amulet Dragon · 1x Master of Chaos · 1x Timaeus the United · 1x Mudragon of the Swamp · 1x Garura · 1x Ebon Illusion Magician · **1x Quintet Magician** *(replaced Selene)*.

- **Mudragon** = Super Poly target for "same Attribute, **different** Types" (your DARK Spellcaster + their DARK Warrior HERO).
- **Garura** = Super Poly target for "same Type **and** Attribute, different names."
- **Quintet Magician** (Lv12 Fusion, *"5 Spellcaster monsters"*) — *"If… Fusion Summoned using 5 Spellcaster monsters with different names: destroy all cards your opponent controls,"* and it *"cannot be destroyed by card effects."* A hard board-wipe finisher, but **demanding (5 different-named Spellcasters)** — a grind-game payoff, not a turn-1 play.
- **Ebon Illusion Magician** (Rank 7) = extender/recursion off two Level-7 Spellcasters.

## 1-card openers
Any **one** of these is a real opening: Magician's Rod, Magicians' Souls, Illusion of Chaos, Dark Magical Circle, Soul Servant, or Preparation of Rites (→ Illusion of Chaos). Starter count is ≈18-19 — but spread over 46 cards, so density is slightly lower than the 40-card version.

- **Rod line:** NS Rod → search **Eternal Soul** → Eternal Soul SS Dark Magician → Circle banish / Eye into a negate body.
- **Souls line:** Souls send DM to GY + draw 2 → Eternal Soul revives DM → Circle.
- **Circle line:** activate Circle, reveal top 3; summon any DM to trigger Circle's **banish**.
- **Sarcophagus line:** resolve Shining Sarcophagus → search DM the Magician of Black Magic → (Sarcophagus on field) free-SS it as a "Dark Magician" → Circle trigger / Eye fusion.
- **Goal of turn 1 on the play:** a Dark Magician on board under **Eternal Soul** (unaffected) + **Dark Magical Circle** up + a held disruption (Ash / Imperm).

## Mulligan / keep guide
- **On the draw:** keep any hand with **a starter + a disruption** (Ash / Imperm).
- **On the play:** want a starter that ends on **Eternal Soul + Circle**. **Mulcharmy Fuwalos is dead on the play** — and at 3 copies you'll brick on it more often, so don't keep a hand leaning on it as your interaction.
- **Going second into a known combo deck:** Fuwalos + Ash + Imperm is a great "break their turn" hand.
- **Reject** hands that are all bodies + no starter and no disruption (and watch for clogging on the Chaos pair).

## Known soft spots (candidates for `tune`)
- **Dark Magician of Chaos (40737112)** — brick, enables nothing. Strongest cut.
- **Magician of Chaos (47963370)** — no Chaos Form in deck; only Eternal-Soul fuel. Add Chaos Form or cut.
- **Bottomless Trap Hole x2** — reactive/narrow, slow into HERO & Enneacraft. Trim toward 40.
- **3x Mulcharmy Fuwalos** — pure going-second; some metas want it at 2.
- Trimming the above is the obvious **46 → 40** path if you want the tighter, more consistent build back.

## Craft reference
Full owned-cards + rarity list is in `collection-reference.csv` (N/R/SR/UR = craft cost). **Caveat:** that CSV lists Maxx "C" x3 — illegal (Limited 1). The live, legal list is this file + `deck-current.ydk`.

---
Linked: [[META-SNAPSHOT]] · [[MATCHUPS]] · [[PATCH-BANLIST]] · [[TWEAK-LOG]]
