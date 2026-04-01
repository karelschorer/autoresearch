# ClaimPilot — Business Model Canvas

## Problem Statement
Regulatory affairs and quality teams at mid-size FMCG companies must manually verify whether product claims (nutrition, health, sustainability) on packaging and marketing materials comply with EU regulations — primarily EC 1924/2006. This manual cross-referencing of the EU Register, EFSA opinions, and conditions of use is repetitive expert labor that scales linearly with SKU count. Getting claims wrong leads to product recalls, fines, packaging delays, and brand damage.

## Target Customer (ICP)
Mid-size FMCG companies in the Netherlands and EU with 50-500 SKUs, 1-3 regulatory affairs staff. Primary wedge: supplement brands and functional food companies (highest claim density per product).

## Proposed Solution & Wedge
AI-assisted regulatory compliance platform using Claude Opus to pre-screen marketing claims against the EU Register, EFSA opinions, and conditions of use. The AI generates a draft verdict with regulatory traceability; a human regulatory expert reviews and validates before delivery. This "AI pre-screen + expert validation" model reduces review time by 60-80% while maintaining the human accountability that regulatory professionals require. Wedge: pre-screening nutrition and health claims for supplement/functional food packaging.

## Pricing Model
€300-500/month SaaS subscription. Positioned as managed regulatory intelligence service (includes internal expert shadow review), not pure self-serve SaaS. Free-tier-for-data acquisition strategy planned.

## Go-to-Market Channel
Founder network (Stijn's ex-Unilever/FMCG connections), industry associations (NPN, Food Supplements Europe), trade events (Vitafoods), LinkedIn outreach to regulatory affairs managers.

## Defensibility & Moat
- **Proprietary claim adjudication dataset:** Every claim reviewed through ClaimPilot generates structured data (claim text → regulation match → verdict → expert override). This accumulates into a proprietary eval/training dataset that improves accuracy and cannot be replicated without equivalent customer volume.
- **Customer-specific regulatory history:** The managed service model creates per-customer claim archives with audit trails. Switching costs increase over time as the platform becomes the system of record for regulatory decisions.
- **Domain-specific eval harness:** The PoC eval harness, validated against real regulatory cases, is a competitive advantage that generic AI tools cannot match without equivalent regulatory domain investment.
- **Network effects via free tier:** Free-tier-for-data strategy means early adoption generates claim verification data that improves the product for paid customers.
- **Founder combination:** Stijn's FMCG network (ex-Unilever/Magnum) provides warm introductions that a generic AI startup would need 12-18 months to build. Karel's technical PoC is already functional. Bootstrap execution speed avoids the 6-12 month fundraising delay that funded competitors face.

## Key Assumptions
1. Claim verification is a significant, painful time sink for the target persona
2. The pain is acute enough at €300-500/month to justify a subscription
3. LLM + regulatory database + human expert review can achieve >95% final accuracy with traceability (AI pre-screens at ~85-90%, expert catches remaining errors)
4. Mid-market is underserved by existing enterprise tools and consultancies
5. The team can build trust with risk-averse regulatory professionals
6. Regulatory expansion (Green Claims Directive) will increase demand
7. Each customer engagement generates proprietary data that strengthens the moat over time
