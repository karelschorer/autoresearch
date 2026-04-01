# ClaimPilot — Business Model Canvas

## Problem Statement
41-89% of EU supplement products carry non-compliant health claims. Getting claims wrong is not a tail risk — it is the default state. Consequences are severe: £100K+ per product line in remediation costs, fines up to €150K (NVWA) or 4% of EU turnover (ECGT), packaging delays of 4-8 weeks, and brand damage. The manual process of cross-referencing claims against the EU Register, EFSA opinions, and conditions of use is repetitive expert labor that scales linearly with SKU count — and the regulatory burden is actively expanding (ECGT Sept 2026, PPWR Aug 2026, botanical claim resolution pending).

## Target Customer (ICP)
**Beachhead:** Dutch supplement brands with 50-300 SKUs, 1-3 regulatory affairs staff, actively preparing for ECGT enforcement (September 27, 2026). Estimated 80-150 brands in this segment, reachable through NPN membership and Stijn's FMCG network.
**Expand-to:** Mid-size FMCG companies across EU (Germany, France, UK) with 50-500 SKUs. Supplement brands first, then functional foods, then broader FMCG.

## Proposed Solution & Wedge
AI-assisted regulatory compliance platform using Claude Opus to pre-screen marketing claims against the EU Register, EFSA opinions, and conditions of use. The AI generates a draft verdict with regulatory traceability; a human regulatory expert reviews and validates before delivery. This "AI pre-screen + expert validation" model reduces review time by 60-80% while maintaining the human accountability that regulatory professionals require.

**Post-flag workflow:** When a claim is flagged as non-compliant, ClaimPilot suggests compliant alternative claim wordings from the authorized EU Register that match the product's ingredients and dosage. This closes the job-to-be-done: users don't just learn "this claim is wrong" — they get "here's what you can say instead." This thin "next step" layer avoids the need to become a full PLM platform while keeping users in the tool.

Wedge: pre-screening nutrition and health claims for supplement/functional food packaging.

## Pricing Model
Tiered pricing aligned to SKU count and service level:
- **Free tier:** Up to 10 claims/month, AI pre-screening only, no expert review. Data acquisition strategy — every free claim improves the model.
- **Starter (€299/mo):** Up to 50 SKUs. AI pre-screening with regulatory traceability. Self-serve dashboard. No human review included.
- **Professional (€799/mo):** Up to 200 SKUs. AI pre-screening + expert spot-check (10% sample review of flagged claims). Monthly compliance summary report.
- **Enterprise (€2,000-5,000/mo):** 200-500+ SKUs. Full AI + expert validation on all flagged claims. Dedicated regulatory advisor. Custom SLA. Quarterly compliance audit.

The tiered model ensures: (a) low-tier is pure SaaS with 80%+ gross margins, (b) mid-tier limits human cost to spot-checks, (c) enterprise-tier prices human review at sustainable rates. The free tier feeds the data flywheel.

## Go-to-Market Channel
1. **ECGT deadline-driven inbound:** Free "ECGT Compliance Checker" tool that tells brands if their current claims are at risk. Drives self-qualified inbound leads. (GDPR content marketing wave is the proven analogue.)
2. **Regulatory consultant partnerships:** White-label or referral partnerships with 3-5 Dutch consultancies (EU Food Comply, The Regulatory Company, Ecomundo). Referral leads convert at 24.7% MQL-to-SQL.
3. **Trade association co-marketing:** Sponsor NPN/FSE webinars on ECGT readiness for access to membership list without cold outreach.
4. **Product-led growth:** Free tier (10 claims/month) serves as PLG engine. Median freemium-to-paid conversion: 9-12%.
5. **Founder network:** Stijn's ex-Unilever/FMCG connections for warm introductions to first 5-10 design partners.

## Defensibility & Moat
- **Proprietary claim adjudication dataset:** Every claim reviewed through ClaimPilot generates structured data (claim text → regulation match → verdict → expert override). This accumulates into a proprietary eval/training dataset that improves accuracy and cannot be replicated without equivalent customer volume.
- **Customer-specific regulatory history:** The managed service model creates per-customer claim archives with audit trails. Switching costs increase over time as the platform becomes the system of record for regulatory decisions.
- **Domain-specific eval harness:** The PoC eval harness, validated against real regulatory cases, is a competitive advantage that generic AI tools cannot match without equivalent regulatory domain investment.
- **Network effects via free tier:** Free-tier-for-data strategy means early adoption generates claim verification data that improves the product for paid customers.
- **Founder combination:** Stijn's FMCG network (ex-Unilever/Magnum) provides warm introductions that a generic AI startup would need 12-18 months to build. Karel's technical PoC is already functional. Bootstrap execution speed avoids the 6-12 month fundraising delay that funded competitors face.

## Key Assumptions
1. Claim verification is a significant, painful time sink for the target persona
2. The pain is acute enough at €299-5,000/month (tiered) to justify a subscription at each company size
3. Hybrid system (deterministic matching against authorized claims + semantic embeddings for paraphrases + LLM for condition-of-use logic and edge cases) + human expert review can achieve >95% final accuracy with traceability. Corpus includes ~270 Art.13.1 authorized + ~2,078 botanical on-hold + specialty claims. Deterministic layer catches exact matches; embeddings handle creative paraphrases; LLM evaluates conditions of use (dose, population, food matrix)
4. Mid-market is underserved by existing enterprise tools and consultancies
5. The team can build trust with risk-averse regulatory professionals
6. Regulatory expansion (Green Claims Directive) will increase demand
7. Each customer engagement generates proprietary data that strengthens the moat over time
