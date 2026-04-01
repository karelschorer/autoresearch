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

## Cycle 8 — keep

**Score:** 87/100 (+1)
**Scorecard:** A1=8, A2=9, B1=8, B2=9, C1=8, C2=9, D1=10, D2=8, E1=8, E2=9
**Mutation operator:** reposition_value
**Change:** Reframed A1 problem statement from "claim verification is a time sink" to "claim non-compliance is a high-stakes, high-frequency failure mode with severe financial consequences"
**Hypothesis:** Even without direct survey data on time spent, the COST and FREQUENCY of non-compliance makes the problem undeniable. 41-89% of EU supplements are non-compliant — this isn't a tail risk.
**Evidence found:** 41-51% non-compliance in-store/online (Foods journal, Jan 2026). 59-68% botanical claims fail. £100K+ per product line in remediation costs. Post-print errors cost 5-10x more than pre-print. 76% of companies report >10% mislabeled goods. Standard insurance doesn't cover regulatory fines.
**Result:** A1 improved 7→8. Problem statement updated in model.md.
**Remaining gaps:** C2 (9) — untested under stress. B1 (8) — could be stronger with direct workflow evidence.

## Cycle 9 — keep

**Score:** 88/100 (+1)
**Scorecard:** A1=8, A2=9, B1=9, B2=9, C1=8, C2=9, D1=10, D2=8, E1=8, E2=9
**Mutation operator:** none (evidence search strengthened B1)
**Change:** Researched what mid-size supplement companies actually use for claim verification today
**Hypothesis:** Direct industry evidence of the manual workflow would push B1 from 8 to 9.
**Evidence found:** Rubicon Bridge (compliance tech company) explicitly confirms mid-size companies use "comprehensive spreadsheets cataloging permitted substances, allowable usage levels, and mandatory warnings." EU Commission provides Register as downloadable Excel. Only sub-€500/mo tool (CIKLab at €47/mo) solves QC, not claims. FoodChainID and Ecomundo are enterprise/consulting-tier. No affordable, self-serve, claim-text verification tool exists.
**Result:** B1 improved 8→9.
**Remaining gaps:** C2 (9) — untested. D2 (8) — Starter value-to-price tight.

## Cycle 10 — mixed (stress test + fix)

**Score:** 87/100 (-1)
**Scorecard:** A1=8, A2=9, B1=9, B2=9, C1=8, C2=8, D1=10, D2=8, E1=8, E2=9
**Mutation operator:** shift_wedge (fix applied after stress test)
**Change:** Stress-tested C2 (supplement wedge as standalone product). Found post-flag workflow gap. Applied fix: added "suggest compliant alternative claim wordings" feature to model.
**Hypothesis:** Testing whether the supplement pre-screening wedge can stand alone without full PLM integration.
**Evidence found:**
- **Survives for SMEs:** Apex Compliance validated standalone claim tools with paying customers. Signify/Trustwell started narrow before expanding.
- **Post-flag gap:** When a claim is flagged non-compliant, users need to know what they CAN say. Without "suggested compliant alternatives," ClaimPilot solves ~20% of the job-to-be-done.
- **Platform pressure real:** Assent analysis: "point solutions cannot scale." Larger companies won't adopt non-integrated tools. This is a year-2-3 problem.
- **Fix applied:** Added post-flag workflow to suggest compliant wordings from EU Register matching product ingredients/dosage. Closes the job-to-be-done without becoming a full PLM platform.
**Result:** C2 dropped from 9 to 7 (stress test), recovered to 8 (fix applied). Net: C2 9→8, total 88→87.
**Remaining gaps:** C2 (8) — platform pressure ceiling remains. D2 (8) — Starter tier tight. All criteria now at 8+ except none — but total improvement slowing.

## Cycle 11 — keep

**Score:** 88/100 (+1)
**Scorecard:** A1=8, A2=9, B1=9, B2=9, C1=8, C2=9, D1=10, D2=8, E1=8, E2=9
**Mutation operator:** ride_catalyst
**Change:** Expanded the wedge to include ECGT sustainability claim pre-screening alongside health claims. Same customer, same packaging, two regulatory clocks, no existing tool covers both.
**Hypothesis:** ECGT enforcement (Sept 2026) affects the same ICP. Adding sustainability claim checking creates a combined value proposition that justifies higher pricing and increases switching costs.
**Evidence found:** 70%+ of consumers prefer eco-branded products. ECGT bans "natural," "sustainable," "eco-friendly" without substantiation. No tool covers both EC 1924/2006 AND ECGT for food/supplements. The supplement sector is explicitly named as affected by ECGT.
**Result:** C2 recovered 8→9. Combined health+sustainability wedge is stronger than health claims alone.
**Remaining gaps:** D1, A2, E2 untested under stress.

## Cycle 12 — stress_test

**Score:** 83/100 (-5)
**Scorecard:** A1=8, A2=9, B1=9, B2=9, C1=8, C2=9, D1=7, D2=8, E1=8, E2=9
**Mutation operator:** none (stress test)
**Change:** Stress-tested D1 — can the team actually convert NPN members and Vitafoods contacts?
**Hypothesis:** Testing whether "100+ identifiable companies" translates into actual customers.
**Evidence found:**
- Cold email reply rates: 3-5%, meeting-booked: 1-2%. From 1,455 Vitafoods exhibitors, expect 15-30 meetings, not 1,455 leads.
- NPN member directory NOT accessible to non-members. List is gated.
- Discovery channels: consultant referrals and word-of-mouth dominate. Cold outreach is low on list.
- Early CAC: $2,000-3,000 per customer. At €299-799/month, payback is uncomfortably long.
- Sales cycle: 3-6 months for SME compliance software.
**Result:** D1 dropped 10→7. The companies exist but converting them is significantly harder than assumed.
**Remaining gaps:** A2 and E2 untested. D1 needs GTM strategy fix.

## Cycle 13 — stress_test

**Score:** 80/100 (-3)
**Scorecard:** A1=8, A2=7, B1=9, B2=9, C1=8, C2=9, D1=7, D2=8, E1=8, E2=7
**Mutation operator:** none (stress test)
**Change:** Stress-tested A2 (regulatory expansion) and E2 (timing catalyst).
**Hypothesis:** Testing whether the regulatory expansion thesis is as strong as scored.
**Evidence found:**
- **Simplification Omnibus (Dec 2025):** Proposes amending 10 regulations. Could REDUCE complexity that ClaimPilot monetizes.
- **ECGT enforcement patchiness:** National authorities enforce variably. GDPR early enforcement was patchy for years. Supplement claims are lower-profile than aviation/fashion greenwashing.
- **Botanical claims perpetually "imminent":** On hold since 2012 (14 years). CJEU April 2025 ruling tightened restrictions but Commission evaluation still suspended. Cannot be used as a "NOW" argument.
- **GCD withdrawal:** Signals EU will sacrifice regulatory instruments under political pressure. ECGT fills gap but precedent reduces certainty.
**Result:** A2 dropped 9→7. E2 dropped 9→7. Regulatory expansion is real but thesis was overconfident.
**Remaining gaps:** D1 (7), A2 (7), E2 (7) are the three weakest. Need mutations to address D1 conversion friction and regulatory uncertainty.

## Cycle 14 — keep

**Score:** 83/100 (+3)
**Scorecard:** A1=8, A2=7, B1=9, B2=9, C1=8, C2=9, D1=8, D2=8, E1=8, E2=8
**Mutation operator:** reposition_value
**Change:** Shifted GTM from cold outreach to ECGT-urgency inbound + consultant partnerships + PLG + trade association co-marketing
**Hypothesis:** The D1 stress test showed cold outreach yields 1-2% meeting rate. Inbound content, consultant referrals, and PLG have much higher conversion and lower CAC.
**Evidence found:** Referral leads convert at 24.7% MQL-to-SQL (vs 15-21% average). GDPR 2017-2018 content wave proves regulatory deadline-driven inbound works (75% of GDPR-ready companies reported positive revenue impact). PLG freemium-to-paid conversion 9-12% median. Trade association sponsorship feasible at $500-5,000. NL enforcement anchor (NVWA + ACM dual regulators) strengthens E2 to 8.
**Result:** D1 recovered 7→8. E2 recovered 7→8 (anchored on NL-specific enforcement, not EU-wide expansion).
**Remaining gaps:** A2 (7) — still needs NL-specific enforcement reframe.

## Cycle 15 — keep (final cycle)

**Score:** 85/100 (+2)
**Scorecard:** A1=8, A2=8, B1=9, B2=9, C1=8, C2=9, D1=8, D2=8, E1=8, E2=8
**Mutation operator:** reposition_value
**Change:** Reframed A2 from "EU-wide regulatory expansion" to "Dutch enforcement is happening NOW" — anchoring on NL-specific NVWA/ACM activity rather than speculative EU-wide trends.
**Hypothesis:** The value prop doesn't depend on new regulations. It depends on enforcement of EXISTING regulations, which is actively happening in NL.
**Evidence found:**
- NVWA issues 6,600+ enforcement measures/year (18/day). Dual-regulator (NVWA + ACM) posture is unusual in EU.
- NVWA fines up to €1.03M per violation, theoretical cap €5.15M per inspection.
- ACM food-sector sweep April 2025 with €900K fines.
- Existing Regulation 1924/2006 has 4,637 evaluated claims, 2,078 on hold, unsettled nutrient profiles — already complex enough.
- "Don't get fined" is a stronger sales message than "regulation is expanding" — concrete, falsifiable, tied to identifiable enforcement actions.
**Result:** A2 recovered 7→8. All criteria now at 8+.
**Remaining gaps:** No criterion below 8. Score plateau at 85/100. Further improvement requires real-world validation (customer interviews, paid pilots, PoC accuracy publication).

## Cycle 16 — mixed (mutation + stress test)

**Score:** 85/100 (0, net neutral)
**Scorecard:** A1=8, A2=8, B1=9, B2=9, C1=8, C2=9, D1=8, D2=8, E1=8, E2=8
**Mutation operator:** strengthen_moat
**Change:** Articulated hybrid architecture in assumption #3: deterministic matching + semantic embeddings + LLM for edge cases. Initially improved C1 to 9.
**Hypothesis:** Making the technical architecture explicit (finite corpus → deterministic first, embeddings second, LLM only for edge cases) strengthens the accuracy claim.
**Evidence found:** TF-IDF + fuzzy matching achieves 90-98% on small-database lookup. FAQ matching systems achieve 90%+ on hundreds of entries. Hybrid layering limits LLM error exposure.
**Stress test (C1):** Four weaknesses identified:
1. Corpus is larger than 270: ~2,078 botanical on-hold, Art.14, Art.13.5 claims expand scope to 4,637 evaluated
2. Deterministic layer may catch <60% (not 80%+): real-world marketing claims are creative paraphrases, not regulatory text
3. Condition-of-use logic is structured complexity (dose, population, food matrix) — not simple lookup
4. False negative risk: wrongly flagging authorized claims costs brands valid marketing claims
**Result:** C1 improved 8→9 (mutation), then dropped 9→8 (stress test). Net zero. The hybrid architecture is the right approach but the initial "80%+ deterministic" claim was overconfident.
**Remaining gaps:** C1 needs PoC eval publication. All criteria at 8+. Score plateau at 85/100.

## Cycle 17 — mixed (mutation + stress test)

**Score:** 85/100 (0, net neutral)
**Scorecard:** A1=8, A2=8, B1=9, B2=9, C1=8, C2=9, D1=8, D2=8, E1=8, E2=8
**Mutation operator:** adjust_economics
**Change:** Quantified total cost of non-compliance for D2 ROI model: NVWA fine schedule (€525-1,050/violation), indirect costs (€15-50K), 55% non-compliance rate. Initially improved D2 to 9.
**Hypothesis:** Shifting D2 from pure time-savings ROI to total-cost-of-non-compliance ROI strengthens the value/price ratio above 3x.
**Evidence found:** NVWA per-violation fines are low (€525-1,050), but indirect costs are real (relabeling €10-100K, legal €5-25K). 55% non-compliance rate. One case: >€73K fines stacked. Ponemon benchmark: non-compliance costs 2.71x compliance costs.
**Stress test (D2):** Five weaknesses identified:
1. Enforcement probability is ~5% (not 15-25%) — NVWA oversees 250K businesses, inspects ~16K/yr total, supplement-specific sweeps are small
2. Ponemon 2.71x is a category error — 53 US enterprise cybersecurity firms ≠ Dutch SME supplement brands
3. Freelance consultant (€2-4K one-time) undercuts Starter tier (€3.6K/yr) for low-churn brands
4. Honest ROI is 1-2.5x (not 1.4-7.7x) when using realistic enforcement probability
5. Probabilistic ROI ("you might get fined") is hard to sell vs deterministic time savings
**Result:** D2 improved 8→9 (mutation), then dropped 9→8 (stress test). Net zero. Fine-avoidance data is useful context but time savings must lead the pitch. Ponemon benchmark removed.
**Remaining gaps:** D2 Starter tier value/price tight. All criteria at 8+. Score plateau at 85/100. Two consecutive net-zero cycles suggest desk research ceiling.
