# ClaimPilot — Mutation Changelog

*Scoring: each criterion rated 1-10 per cycle. Total = sum of all 10 criteria (max 100).*

## Cycle 0 — baseline

**Score:** 68/100
**Scorecard:** A1=7, A2=8, B1=7, B2=8, C1=4, C2=9, D1=10, D2=8, E1=3, E2=9
**Mutation operator:** none
**Change:** Initial model as provided by founder
**Hypothesis:** N/A — establishing baseline
**Evidence found:** Strong problem validation (A1, A2), clear market gap (B1, B2), credible wedge in supplements (C2), large reachable market (D1), solid unit economics (D2), compelling timing (E2). Weak spots: C1 (LLM accuracy unproven, trust barrier) and E1 (no customers, no proprietary data, nascent moat).
**Remaining gaps:** C1 needs architecture/framing change. E1 needs competitive positioning and moat articulation.

## Cycle 1 — keep

**Score:** 73/100 (+5)
**Scorecard:** A1=7, A2=9, B1=7, B2=8, C1=7, C2=9, D1=10, D2=8, E1=3, E2=9
**Mutation operator:** reposition_value
**Change:** Repositioned solution from "AI delivers verdict" to "AI pre-screens + human expert validates"
**Hypothesis:** C1 weakness was partly framing. By making human-in-the-loop the core value prop, accuracy bar shifts to "AI+human >95%" which is achievable.
**Evidence found:** Veeva PromoMats uses same model for 1,500+ pharma companies (50-75% cycle time reduction). FDA adopted AI-assisted review in 2025. White & Case survey confirms trust requires human oversight.
**Result:** C1 improved 4→7. A2 strengthened to 9 with additional ECGT/NVWA evidence.
**Remaining gaps:** E1 still very weak (3). D2 untested under stress.

## Cycle 2 — keep

**Score:** 78/100 (+5)
**Scorecard:** A1=7, A2=9, B1=8, B2=9, C1=7, C2=9, D1=10, D2=8, E1=6, E2=9
**Mutation operator:** strengthen_moat
**Change:** Added data moat strategy: proprietary claim adjudication dataset (flywheel), system-of-record stickiness, free-tier-for-data, articulated founder time advantage
**Hypothesis:** E1 weak because model didn't articulate why the team's position (working PoC + FMCG network + unoccupied niche) is defensible.
**Evidence found:** ComplyAdvantage, Vanta, Drata built data moats from zero. Compliance SaaS churn 1.4-1.9% monthly. No funded competitor in exact niche. FoodChain ID and Trustwell/AskReg are adjacent but not direct competitors.
**Result:** E1 improved 3→6. B1/B2 strengthened by detailed competitive research.
**Remaining gaps:** E1 still moderate (6) — moat is pathway not asset. D2 untested under stress.

## Cycle 3 — stress_test (no mutation)

**Score:** 73/100 (-5)
**Scorecard:** A1=7, A2=9, B1=8, B2=9, C1=7, C2=9, D1=10, D2=5, E1=6, E2=9
**Mutation operator:** none (stress test cycle)
**Change:** No model change — adversarial stress test on D2 (pricing) and E1 (competitive threats)
**Hypothesis:** Testing whether the 10/10 binary score was masking weaknesses when scored on a granular scale.
**Evidence found:**
- **D2 PROBLEM FOUND:** At 200 SKUs × 6-7 claims = 1,200-1,400 claims, even with AI handling 80%, human review of remaining 20% (240-280 claims × 5 min = 20-23 hours) costs €1,660-1,900/cycle at freelance rates. €300-500/month subscription doesn't cover it. Managed service model has structural margin problem at current pricing.
- **E1 CONFIRMED:** Niche genuinely unoccupied. No funded startup targets EU food claim pre-screening specifically. FoodChain ID and Trustwell/AskReg are adjacent but not direct. Real risk is feature-add by existing player, not new entrant.
**Result:** D2 dropped 8→5. E1 held at 6.
**Remaining gaps:** D2 pricing model needs restructuring (primary). E1 moat needs conversion from pathway to asset (secondary). C1 needs PoC accuracy data (tertiary).
