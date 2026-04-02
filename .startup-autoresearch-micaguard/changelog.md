# MiCAGuard — Autoresearch Changelog

## Cycle 0 — Baseline (from ideation)
**Score: 72/100**
**Scorecard:** A1:8 A2:8 B1:6 B2:6 C1:8 C2:7 D1:5 D2:7 E1:9 E2:8

Baseline model from startup ideation phase. Key strengths: team fit (E1:9), timing (E2:8), problem validation (A1:8, A2:8). Key weaknesses: TAM (D1:5), competitive landscape (B1:6, B2:6). Priority: validate TAM first — if <100 MiCA-licensed entities, the idea may be fatal.

## Cycle 1 — D1 TAM validation + narrow_icp
**Score: 74/100** (+2)
**Scorecard:** A1:8 A2:8 B1:6 B2:6 C1:8 C2:7 **D1:7↑** D2:7 E1:9 E2:8
**Mutation:** narrow_icp — updated ICP with hard data on MiCA-licensed entity count
**Research:** ESMA register shows 102 authorized CASPs as of Dec 2025, growing rapidly. Expected 150-180 by mid-2026 (July 1 grandfathering deadline). Pre-MiCA market was ~3,100 VASPs; ~75% will be eliminated. The >=100 threshold is cleared. Sweet spot ICP (10-100 employees, mid-market) estimated at 60-100 of the 150-180 total.
**Key finding:** The market is larger than feared but smaller than a typical SaaS TAM. MiCA is causing a massive consolidation — from 3,100 VASPs to ~180 licensed CASPs. This means fewer but more serious targets. The beachhead (NL, ~40 firms) is viable; EU-wide (150-180) provides growth runway.
**D1 moved from 5→7:** TAM exists and clears threshold, but still a niche market. Not an 8 because the ICP filter (mid-market, 10-100 employees) may reduce the addressable count to 60-100.

## Cycle 2 — B1 competitor mapping + shift_wedge
**Score: 72/100** (-2)
**Scorecard:** A1:8 A2:8 **B1:5↓** B2:6 C1:8 **C2:6↓** D1:7 D2:7 E1:9 E2:8
**Mutation:** shift_wedge — marketing compliance wedge → disclosure generation wedge
**Research:** Mapped the full crypto compliance RegTech landscape. Found 3-layer stack: identity/KYC (Sumsub, Muinmos), transaction monitoring (Chainalysis, Elliptic, TRM Labs), travel rule (Notabene). CRITICAL FINDING: **Sedric AI** (500+ financial institutions, RegTech100 2026, HSBC-backed) already does MiCA marketing compliance scanning — scans websites, ads, social media in 40+ languages with LLM-powered detection. This directly occupies MiCAGuard's proposed marketing compliance wedge.
**Wedge shift:** Moved from marketing compliance (occupied by Sedric) to disclosure generation (crypto-asset white papers per Article 6 MiCA). No tool automates this; currently done by law firms at EUR 10-30K per white paper. This is the remaining gap.
**B1 dropped 6→5:** The competitive landscape is more developed than assumed. Every compliance layer has established, well-funded players. The marketing wedge is occupied.
**C2 dropped 7→6:** New disclosure generation wedge is unvalidated. Need to confirm white paper generation is a recurring, SaaS-worthy task (not a one-time deliverable).

## Cycle 3 — Wedge validation + second shift_wedge
**Score: 71/100** (-1)
**Scorecard:** A1:8 A2:8 B1:5 B2:6 C1:8 **C2:5↓** D1:7 D2:7 E1:9 E2:8
**Mutation:** shift_wedge — disclosure generation → ongoing compliance operations platform
**Research:** MiCA white papers are mandatory but ONE-TIME deliverables per token. Updates only for "material changes." Templates already exist (CCRI). Law firms offer drafting at EUR 5-15K. This is a project, not SaaS. CCRI, MiCA Crypto Alliance, LEXR, CERHA HEMPEL, Inteliumlaw all offer this service.
**Wedge shift:** Moved from white paper generation (one-time) to ongoing compliance operations: periodic NCA reporting, regulatory change tracking, disclosure updates, complaints handling/record-keeping. These are RECURRING tasks that justify monthly subscription.
**C2 dropped 6→5:** Second wedge shift in two cycles — not a good sign. The "ongoing MiCA operations" wedge is plausible but completely unvalidated. Need to research: what exactly are the recurring MiCA obligations? How much time do they take? Is this a real workflow pain?
**Emerging concern:** We're now on the third wedge attempt. Marketing (occupied by Sedric), disclosures (one-time), ongoing operations (unvalidated). The product needs a clear, defensible entry point.

## Cycle 4 — Recurring obligations validated + reposition_value
**Score: 73/100** (+2)
**Scorecard:** A1:8 A2:8 B1:5 B2:6 C1:8 **C2:7↑** D1:7 D2:7 E1:9 E2:8
**Mutation:** reposition_value — repositioned from "compliance tool" to "MiCA operations platform"
**Research:** MiCA imposes multiple RECURRING obligations on CASPs: continuous record-keeping (Art.68, RTS 2025/1140), complaints handling (Art.71, RTS 2025/294), quarterly NCA reporting, annual compliance audits, governance change reporting, and business continuity (DORA). Level 2 measures still being published — complexity growing.
**C2 recovered 5→7:** The recurring obligations create genuine SaaS-worthy workflows. A "MiCA compliance dashboard" that automates reporting deadlines, manages complaint records, tracks regulatory changes, and prepares NCA submissions has recurring value. Mid-market CASPs (1-3 compliance staff) can't manage this with spreadsheets alone as obligations compound.
**Remaining gap:** The operations wedge is broad. Need to narrow to ONE launch feature (NCA reporting or complaints handling) before building the full platform. Still unvalidated with real users.

## Cycle 5 — D2 unit economics validation + adjust_economics
**Score: 74/100** (+1)
**Scorecard:** A1:8 A2:8 B1:5 B2:6 C1:8 C2:7 D1:7 **D2:8↑** E1:9 E2:8
**Mutation:** adjust_economics — strengthened pricing justification with compliance cost data
**Research:** 35% of blockchain startups estimate >$500K/yr MiCA compliance costs. 73% investing in compliance tech (willingness-to-pay signal). EUR 540M+ in fines issued. Per-violation penalties EUR 50K-5M. Mid-market CASP spending EUR 50-200K on compliance; MiCAGuard at EUR 12K/yr = 2.4-24% of budget. Even 10% time savings = 2-4x ROI.
**D2 moved 7→8:** Economics are defensible. The pricing tiers (EUR 299/999/3-5K) align well with the compliance budget spectrum. 73% investing in compliance tech validates willingness-to-pay. Fine avoidance provides secondary ROI. Not a 9 because mid-market CASPs at the low end may find EUR 999/mo steep relative to their total compliance budget.
