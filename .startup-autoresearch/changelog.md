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

## Cycle 4 — keep

**Score:** 82/100 (+9)
**Scorecard:** A1=7, A2=9, B1=8, B2=9, C1=7, C2=9, D1=10, D2=8, E1=6, E2=9
**Mutation operator:** adjust_economics
**Change:** Replaced flat €300-500/month with tiered pricing: Free (10 claims/mo, data acquisition), Starter €299/mo (50 SKUs, AI only), Professional €799/mo (200 SKUs, AI + 10% spot-check), Enterprise €2,000-5,000/mo (200-500+ SKUs, full expert validation)
**Hypothesis:** The flat pricing broke because it bundled human expert review at a price that couldn't cover the cost. Tiering separates AI-only (high margin) from managed service (appropriately priced).
**Evidence found:** Professional tier math: 28 spot-check claims × 10 min = 5 hrs × €50/hr = €250 cost on €799 revenue = 69% gross margin. Comparable tools (VComply $1K/mo, Regology $1.25K/user/mo) validate price range. Freemium conversion in compliance SaaS is 5-8%. Enterprise pricing of €2-5K/mo is in-market for managed compliance.
**Result:** D2 recovered 5→8. Total improved 73→82.
**Remaining gaps:** E1 (6/10) — moat is pathway not asset. C1 (7/10) — needs PoC accuracy data. A1 (7/10) — needs direct survey evidence on time spent.

## Cycle 5 — keep

**Score:** 85/100 (+3)
**Scorecard:** A1=7, A2=9, B1=8, B2=9, C1=7, C2=9, D1=10, D2=8, E1=8, E2=9
**Mutation operator:** narrow_icp
**Change:** Narrowed beachhead from "mid-size EU FMCG 50-500 SKUs" to "Dutch supplement brands with 50-300 SKUs preparing for ECGT enforcement September 27, 2026"
**Hypothesis:** The team's advantages (Stijn's Dutch FMCG network, NVWA domain knowledge, working PoC) are strongest in NL. The ECGT deadline creates urgency that favors fast-moving bootstrapped teams over funded competitors. A narrow beachhead is easier to defend.
**Evidence found:** NL supplement market €600-800M, 60% of Dutch adults consume supplements, estimated 80-150 brands at 50-300 SKUs. ECGT enforcement Sept 2026 is a hard deadline. Dutch enforcement culture already active (KLM greenwashing ruling, NVWA crackdowns). SGS DigiComply lacks Dutch-specific supplement depth. Country-first compliance SaaS is a validated playbook.
**Result:** E1 improved 6→8. All other criteria unchanged.
**Remaining gaps:** A1 (7) — desk research ceiling, needs interviews. C1 (7) — needs PoC accuracy data. D2 (8) — Starter tier value-to-price ratio is tight.

## Cycle 6 — discard

**Score:** 85/100 (no change)
**Scorecard:** A1=7, A2=9, B1=8, B2=9, C1=7, C2=9, D1=10, D2=8, E1=8, E2=9
**Mutation operator:** none (evidence search, no model change)
**Change:** Searched for direct quantitative data on time spent on claim verification by regulatory affairs professionals
**Hypothesis:** Finding a direct survey or time-motion study measuring % of role on claim verification would push A1 from 7 to 8-9.
**Evidence found:** FoLSol reports 2 days per label manually (70% reduction with software). Job postings show claims as 1 of 4-6 core duties (~15-25%). RAPS Workforce Report likely has data but is paywalled. FDA spends 8.1 FTEs on health claim review. No direct industry survey found measuring hours/week on claim verification.
**Result:** A1 unchanged at 7. Desk research has hit its ceiling for this criterion — it requires primary research (customer interviews) to improve.
**Remaining gaps:** Same as Cycle 5.

## Cycle 7 — keep

**Score:** 86/100 (+1)
**Scorecard:** A1=7, A2=9, B1=8, B2=9, C1=8, C2=9, D1=10, D2=8, E1=8, E2=9
**Mutation operator:** none (evidence search strengthened C1)
**Change:** Researched specific accuracy benchmarks for AI/LLM on regulatory text classification tasks comparable to EU health claim verification
**Hypothesis:** Finding published accuracy figures for structured regulatory rule-matching (closer to ClaimPilot's task than general legal reasoning) would improve C1 score.
**Evidence found:** 92.8% precision / 94.1% recall on structured regulatory compliance text classification (WJAETS 2025). GoVisually claims 90% on food label compliance. RAG over finite corpus (270 EU claims) is best-case scenario for retrieval precision. IEEE 2024 paper demonstrated automated nutritional claim verification. EVERSANA pharma MLR: 86% error reduction after engineering investment.
**Result:** C1 improved 7→8. The task (claim text → finite authorized list → condition check) is structurally one of the easiest LLM/RAG tasks in regulatory space.
**Remaining gaps:** A1 (7) — needs primary research. D2 (8) — Starter tier value-to-price tight. C1 (8) — needs PoC eval harness published results for 9+.
