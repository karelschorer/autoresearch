# ClaimPilot — Business Model Canvas

## Problem Statement
41-89% of EU supplement products carry non-compliant health claims. Getting claims wrong is not a tail risk — it is the default state. Consequences: €15-50K+ per enforcement action (relabeling, legal, inventory write-off), fines up to €1.03M (NVWA), packaging delays of 4-8 weeks, marketplace delisting (Amazon/Bol.com). The manual process of cross-referencing claims against the EU Register, EFSA opinions, and conditions of use is repetitive expert labor that scales linearly with SKU count. Timing catalysts: CJEU Novel Nutriology ruling (April 2025) killed the botanical "on-hold" loophole affecting thousands of supplement products; NVWA enforcement broadening to thematic sweeps (collagen 83% non-compliant, influencers 56%); Amazon/Bol.com now requiring third-party compliance verification.

## Target Customer (ICP)
**Beachhead:** Dutch supplement brands with 50-300 SKUs, 1-3 regulatory affairs staff, under active NVWA enforcement pressure. Estimated 30-70 brands at this scale in NL, reachable through founder network, NVWA enforcement-driven outreach, and trade events.
**Expand-to:** Mid-size FMCG companies across EU (Germany, France, UK) with 50-500 SKUs. Supplement brands first, then functional foods, then broader FMCG.

## Proposed Solution & Wedge
AI-assisted regulatory compliance platform using Claude Opus to pre-screen marketing claims against the EU Register, EFSA opinions, and conditions of use. The AI generates a draft verdict with regulatory traceability; a human regulatory expert reviews and validates before delivery. This "AI pre-screen + expert validation" model reduces review time by 60-80% while maintaining the human accountability that regulatory professionals require.

**Post-flag workflow:** When a claim is flagged as non-compliant, ClaimPilot suggests compliant alternative claim wordings from the authorized EU Register that match the product's ingredients and dosage. This closes the job-to-be-done: users don't just learn "this claim is wrong" — they get "here's what you can say instead." This thin "next step" layer avoids the need to become a full PLM platform while keeping users in the tool.

Wedge: pre-screening nutrition and health claims for supplement/functional food packaging.

## Pricing Model
Tiered pricing aligned to SKU count and service level:
- **Trial:** 14-day free trial with expert guidance. Converts through demonstrated accuracy. No perpetual free tier — compliance buyers need trust, not freemium.
- **Starter (€199/mo):** Up to 50 SKUs. AI pre-screening with regulatory traceability. Self-serve dashboard. No human review included. At €2,388/yr, competes with one-time consultant review (€2-4K) while providing ongoing monitoring.
- **Professional (€799/mo):** Up to 200 SKUs. AI pre-screening + expert spot-check (10% sample review of flagged claims). Monthly compliance summary report.
- **Enterprise (€2,000-5,000/mo):** 200-500+ SKUs. Full AI + expert validation on all flagged claims. Dedicated regulatory advisor. Custom SLA. Quarterly compliance audit.

The tiered model ensures: (a) low-tier is pure SaaS with 80%+ gross margins, (b) mid-tier limits human cost to spot-checks, (c) enterprise-tier prices human review at sustainable rates. Starter at €199/mo competes directly with one-time consultant reviews while providing ongoing regulatory monitoring. Value proposition anchored on time savings (primary) + fine avoidance (secondary).

## Go-to-Market Channel
*Note: ECGT (EU 2024/825) covers sustainability claims, not health claims (EC 1924/2006). GTM revised to reflect this.*
1. **NVWA enforcement-driven content marketing:** "Is your supplement label NVWA-compliant?" free audit tool targeting brands in categories where NVWA has recently fined competitors (collagen, weight-loss, botanicals). Urgency from ongoing enforcement, not a deadline.
2. **Founder network (primary channel):** Stijn's ex-Unilever/FMCG connections for warm introductions to first 5-10 design partners. This is the fastest path to first revenue.
3. **Direct outreach to non-compliant brands:** NVWA publishes enforcement actions. Brands found non-compliant in sweeps are self-qualified leads with acute pain.
4. **Product-led trial:** Time-limited free trial with expert guidance (not a perpetual free tier — compliance SaaS requires trust, not freemium). Convert through demonstrated accuracy.
5. **Trade event presence:** Vitafoods, NPN events as awareness channels (not co-marketing partnerships — NPN doesn't endorse vendors).

## Defensibility & Moat
*Note: Technology (NLP over public corpus) is NOT the moat — it's standard engineering. The moat builds from speed-to-revenue in a winner-take-most vertical market.*
- **Speed-to-first-revenue advantage:** Vertical SaaS leaders capture 40-60% market share (Windsor Drake Q4 2025). First credible entrant with paying customers compounds switching costs, data, and word-of-mouth in a small industry. Bootstrap speed avoids 6-12 month fundraising delay.
- **Compliance switching costs (system of record):** Audit trail continuity, accumulated configuration, workflow embedding, regulatory continuity risk. Customers won't switch mid-audit-cycle. Compliance SaaS churn 1.4-1.9% monthly.
- **Proprietary claim adjudication dataset:** Every claim reviewed generates structured data (claim text → regulation match → verdict → expert override). Data flywheel kicks in at ~50-200 customers. Cannot be replicated without equivalent customer volume.
- **Network effects via free tier:** Free-tier-for-data strategy means early adoption generates claim verification data that improves the product for paid customers.
- **Founder combination:** Stijn's FMCG network provides warm introductions for first 5-10 design partners. Karel's working PoC accelerates time-to-first-revenue. These are speed advantages, not permanent moats — the permanent moat builds from customer relationships and data.

## Key Assumptions
1. Claim verification is a significant, painful time sink for the target persona
2. The pain is acute enough at €299-5,000/month (tiered) to justify a subscription at each company size
3. Hybrid system (deterministic matching against authorized claims + semantic embeddings for paraphrases + LLM for condition-of-use logic and edge cases) + human expert review can achieve >95% final accuracy with traceability. Corpus includes ~270 Art.13.1 authorized + ~2,078 botanical on-hold + specialty claims. Deterministic layer catches exact matches; embeddings handle creative paraphrases; LLM evaluates conditions of use (dose, population, food matrix)
4. Mid-market is underserved by existing enterprise tools and consultancies
5. The team can build trust with risk-averse regulatory professionals
6. Regulatory expansion (Green Claims Directive) will increase demand
7. Each customer engagement generates proprietary data that strengthens the moat over time
