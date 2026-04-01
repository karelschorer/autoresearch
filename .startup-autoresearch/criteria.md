# Validation Criteria — ClaimPilot

## A. Problem Validation — Is the pain real and urgent?

### A1: Regulatory claim verification is a documented time sink
**Question:** Is there documented evidence that regulatory affairs professionals at mid-size FMCG/supplement companies spend significant time (>20% of their role) manually verifying product claims against EU regulations?
**Pass condition:** Multiple sources (job postings, industry surveys, regulatory consultancy reports, or professional community discussions) confirm that claim verification is a major, repetitive time commitment for regulatory affairs staff at companies with 50-500 SKUs.
**Fail condition:** Evidence suggests claim verification is a minor task, typically outsourced cheaply, or handled as a small part of a broader role with minimal friction.
**Research method:** Job posting analysis, industry reports, regulatory consultancy websites, LinkedIn/professional community signals.

### A2: The problem is growing due to regulatory expansion
**Question:** Is there concrete evidence that EU regulatory requirements for product claims (nutrition, health, sustainability) are expanding in scope and enforcement, making the verification burden worse over the next 2-3 years?
**Pass condition:** Identifiable regulatory developments (Green Claims Directive, Farm to Fork enforcement, NVWA/DGCCRF enforcement actions, new EFSA guidance) that will increase the number and complexity of claims requiring verification.
**Fail condition:** The regulatory landscape is stable or simplifying; no material new requirements on the horizon.
**Research method:** EU legislative tracker, regulatory news, enforcement action databases, industry association publications.

---

## B. Existing Alternatives — Is the current solution bad enough?

### B1: Existing alternatives are inadequate for mid-market
**Question:** Are the existing solutions for claim verification (Descartes, RIMS platforms, regulatory consultancies, manual processes) clearly inadequate for mid-size FMCG companies with 50-500 SKUs — either too expensive, too complex, too slow, or too manual?
**Pass condition:** Evidence that enterprise tools (Descartes, SAP EHS, Veeva) are priced/scoped for large enterprises (>1000 SKUs), that consultancies charge >€200/hour for ad-hoc reviews, and that mid-market companies default to manual spreadsheet/register cross-referencing.
**Fail condition:** Affordable, effective tools already exist for this segment, or consultancy costs are low enough that a SaaS tool offers minimal savings.
**Research method:** Competitor analysis, pricing research, G2/Capterra reviews, industry forum discussions.

### B2: There is a gap between current tools and what mid-market needs
**Question:** Is there a clearly identifiable gap between what existing regulatory information management systems offer and what a mid-size FMCG regulatory affairs team actually needs for day-to-day claim verification?
**Pass condition:** Evidence that existing tools focus on document management/registration tracking rather than real-time claim pre-screening with regulatory traceability; that the actual workflow pain (checking a specific claim against the EU Register + conditions of use) is not well-served.
**Fail condition:** Existing tools already offer claim-level verification with regulatory traceability at accessible price points.
**Research method:** Competitor feature analysis, product documentation review, user reviews.

---

## C. Solution-Market Fit — Can this specific solution win?

### C1: LLM + regulatory database can achieve sufficient accuracy
**Question:** Is there demonstrable evidence (from the PoC eval harness or comparable systems) that an LLM pipeline cross-referencing the EU Register and EFSA opinions can achieve >90% accuracy on claim verification, with reliable regulatory traceability?
**Pass condition:** The PoC eval harness shows >90% accuracy on real regulatory cases; or comparable LLM-based regulatory/compliance tools have demonstrated similar accuracy in peer-reviewed or industry-validated settings.
**Fail condition:** LLM accuracy on regulatory interpretation is demonstrably unreliable (<85%), or regulatory professionals would not trust AI-generated verdicts without full manual re-review (negating time savings).
**Research method:** Founder-provided PoC evidence, academic papers on LLM regulatory reasoning, comparable product case studies.

### C2: There is a credible narrow wedge that delivers value without full platform adoption
**Question:** Can ClaimPilot deliver clear value through a narrow first use case — specifically, pre-screening nutrition and health claims for supplement/functional food packaging — without requiring companies to adopt a full regulatory management platform?
**Pass condition:** The wedge (nutrition + health claim pre-screening for supplements) is a self-contained, high-frequency task that delivers standalone value; supplement companies have the highest claim density per product and the most acute regulatory exposure.
**Fail condition:** Claim verification cannot be meaningfully separated from the broader regulatory workflow; companies would need full platform integration to see value.
**Research method:** Regulatory workflow analysis, supplement industry claim patterns, founder domain knowledge.

---

## D. Market & Economics — Is the market real and reachable?

### D1: There are >=100 identifiable target companies reachable through <=2 channels
**Question:** Can you identify at least 100 mid-size FMCG/supplement companies in the Netherlands and broader EU that fit the ICP (50-500 SKUs, 1-3 regulatory staff, active health/nutrition claims) and are reachable through industry associations, trade events, or LinkedIn?
**Pass condition:** Identifiable industry associations (NPN, Food Supplements Europe), trade events (Vitafoods, SupplySide), LinkedIn groups, or company databases that contain >100 companies matching the ICP.
**Fail condition:** The segment is too small (<50 identifiable companies) or too fragmented to reach efficiently.
**Research method:** Industry association membership lists, trade event exhibitor directories, company database searches.

### D2: Unit economics work — value delivered is >=3x the proposed price
**Question:** Does the value ClaimPilot delivers (in time saved, risk avoided, packaging delay reduction) justify at least 3x the proposed price of €300-500/month at the target company size?
**Pass condition:** A regulatory affairs manager's time costs €50-80/hour; if the tool saves >15-20 hours/month in claim verification, the value (€750-1,600/month) exceeds 3x the subscription price. Additionally, avoided recall/fine risk has quantifiable value.
**Fail condition:** Time savings are <10 hours/month, or the risk-avoidance argument is too abstract to justify the price to a budget holder.
**Research method:** Salary data, regulatory workflow time estimates, recall/fine cost data, structured reasoning.

---

## E. Founder & Timing — Can this team win now?

### E1: The founding team has a defensible advantage over well-funded competitors
**Question:** Do the founders (Karel: technical/AI, Stijn: ex-Unilever FMCG, Martijn: M&A/finance) have a combination of domain expertise, industry relationships, and technical capability that creates a defensible advantage — particularly against a well-funded AI startup or a large regulatory data company entering this space?
**Pass condition:** The combination of Stijn's FMCG network + Karel's working PoC + bootstrap execution speed creates a credible moat through early customer relationships, domain-specific eval data, and industry trust that a generic AI company would struggle to replicate quickly.
**Fail condition:** The team has no proprietary data, no existing customer relationships, and no domain expertise that couldn't be replicated by a funded competitor within 6 months.
**Research method:** Team background analysis, competitive moat assessment, structured reasoning.

### E2: There is a timing catalyst that makes NOW the right moment
**Question:** Is there a specific, time-bound catalyst (regulatory change, technology shift, market event) that creates a window of opportunity for ClaimPilot in the next 12-24 months?
**Pass condition:** The Green Claims Directive (expected ~2026), expanding EFSA review scope, increasing enforcement actions, and the maturation of LLM technology create a convergent window where demand for claim verification is spiking while the technology to automate it has just become viable.
**Fail condition:** No urgency — the regulatory environment is stable, LLM technology has been available for years without triggering adoption, or the catalyst is >3 years away.
**Research method:** EU legislative timeline, enforcement trend data, LLM capability milestones.
