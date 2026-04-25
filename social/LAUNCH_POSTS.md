# Launch-day social copy — DataDeception v0.1

Three platforms. Post in this order: **Twitter/X thread → LinkedIn → Reddit**. Twitter first because the thread URL becomes the canonical share asset that LinkedIn and Reddit can link to.

Replace `[arXiv-URL]` with the actual arXiv link once assigned. The GitHub URL is `https://github.com/Princeu3/DataDeception`.

---

## Twitter/X — 8-tweet thread

**Tweet 1 (hook).**

> Tesla advertised 318 miles of range for the Cybertruck. Independent measurement at 70 mph: 224 miles. A 30% shortfall.
>
> Today we're releasing **DataDeception**, a citation-first dataset of where US EV manufacturer claims diverge from independent measurement. 28 records, 8 manufacturers. 🧵

**Tweet 2 (the pattern).**

> The Cybertruck isn't an outlier. The same gap pattern (`epa_vs_highway_70mph`) recurs across 8 manufacturers in our v0.1 sample: Tesla, Ford, Rivian, Hyundai, Lucid, Mercedes, GMC, VW.
>
> Mean gap: −15%. Worst: −30%. Best: +3%.
>
> [attach: gap-dotplot figure]

**Tweet 3 (the cause).**

> This isn't a coincidence of marketing choices. EPA's combined city/highway test cycle is the only mandatory range figure manufacturers must publish. Customers care about sustained 70 mph cruising. The two diverge systematically.
>
> The cross-cutting pattern is regulatory test-cycle mismatch.

**Tweet 4 (counter-examples — credibility move).**

> The dataset deliberately includes counter-examples to address confirmation bias. Mercedes EQS measured **422 mi vs. 350 mi EPA** (+72 mi over). Ford Mach-E matches EPA in independent testing.
>
> Cross-manufacturer doesn't mean cross-villainy. The measurement gap is structural.

**Tweet 5 (case study).**

> Case study: Tesla Cybertruck range promise (2019–2025).
>
> 2019: 500 mi promised
> 2023: shipped at 318 mi EPA
> 2024: MotorTrend instrumented 224 mi @ 70 mph
> May 2025: Range Extender accessory cancelled, full refunds, zero delivered
>
> 6 years of receipts.

**Tweet 6 (FSD).**

> Categorical deception, not just numeric: Tesla's "Full Self-Driving" was ruled "unambiguously false and counterfactual" by a California ALJ in December 2025. NHTSA's October 2025 investigation: 2.88M vehicles, 14 crashes, 23 injuries.
>
> Severity grade: critical.

**Tweet 7 (methodology + open data).**

> Every record carries a verbatim claim quote with archived URL, a tier-classified independent measurement, an evidence grade (A–D), and a tactic from a 13-tactic taxonomy across 5 families.
>
> Schema-validated. Reproducible. MIT (code) + CC-BY-4.0 (data).
>
> [attach: tactic-taxonomy figure]

**Tweet 8 (link + ask).**

> 📄 Paper: [arXiv-URL]
> 💾 Dataset + code: https://github.com/Princeu3/DataDeception
> 🔧 Methodology: §3 of the paper
>
> If you've been mis-sold an EV spec, file a record. If you're a regulator, the data is yours. If you're a manufacturer, our notification email is in your inbox.

---

## LinkedIn — single post

> **Today: releasing DataDeception, a citation-first dataset of US EV manufacturer-claim vs. independent-measurement divergence.**
>
> The bottleneck in commercial-claims accountability isn't methodology — FTC §5 and decades of comparative-advertising case law already define what counts as deceptive. It's data availability. Independent measurements exist (Consumer Reports, MotorTrend, Edmunds), but they're paywalled, fragmented, and unstructured.
>
> v0.1: 13 products × 28 records × 13 tactics across 8 manufacturers. Schema-validated against JSON Schema 2020-12. Tier-1 NHTSA recall data integrated.
>
> Some highlights:
>
> ▸ Mean highway-range gap: −15%. The Cybertruck Dual Motor advertises 318 mi; MotorTrend's instrumented test at 70 mph: 224 mi (−30%).
>
> ▸ The dominant tactic (`epa_vs_highway_70mph`) recurs across 8 manufacturers — evidence that the gap is structural, not a marketing choice.
>
> ▸ Counter-examples are included by design: Mercedes EQS exceeds EPA by 72 mi, Ford Mach-E matches. The dataset is designed to falsify itself, not to confirm a thesis.
>
> ▸ Three policy implications follow directly from the corpus: a supplemental 70 mph EPA rating; per-se UDAP treatment of feature-naming overclaims at SAE-level mismatch; and mandatory disclosure of independent measurements adjacent to manufacturer claims.
>
> The methodology is organized along Gebru et al.'s datasheet lifecycle (Motivation → Composition → Collection → Preprocessing → Uses → Distribution → Maintenance) and builds on the empirical-taxonomy approach of Mathur et al.'s "Dark Patterns at Scale."
>
> Manufacturers represented in v0.1 receive a concurrent notification today; responses returned within 30 days are integrated as additional sources alongside each affected record, not as redactions.
>
> Paper: [arXiv-URL]
> Dataset + code: https://github.com/Princeu3/DataDeception
>
> Released under MIT (code) and CC-BY-4.0 (data). Phase 2 work prioritizes randomized expansion to 25+ products and longitudinal re-verification.
>
> #ConsumerProtection #ElectricVehicles #OpenData #FTC #ResearchData

---

## Reddit — primary post (r/electricvehicles)

**Title:** `[Research] DataDeception v0.1 — a citation-first dataset of where US EV manufacturer claims diverge from independent measurement (28 records, 8 manufacturers, all evidence A–D graded)`

**Body:**

> I'm an independent researcher and I've spent the last few weeks building a structured dataset of where US EV manufacturer claims diverge from independent measurement. v0.1 is out today and I want to share it with this community because frankly you all are the closest thing the field has to a Tier-3 reality check.
>
> **The basics:**
> - 13 products, 28 deception records, 13 tactics across 5 families
> - 8 manufacturers represented (Tesla, Ford, Rivian, Hyundai, Lucid, Mercedes, GMC, VW)
> - Every record has paired claim/reality citations and an evidence grade A–D
> - Counter-examples included by design (Mercedes EQS, Ford Mach-E)
> - Tier-1 NHTSA recall data integrated
> - Schema-validated, reproducible, MIT + CC-BY-4.0
>
> **What surprised me:**
>
> The biggest finding isn't any single product gap — it's that the same pattern (EPA combined cycle vs. real 70 mph cruising) recurs across **8 different manufacturers** including counter-examples in both directions. That's not a coincidence of marketing choices. It's regulatory test-cycle mismatch: EPA's combined city/highway weighting doesn't reflect how range gets used. Every manufacturer is reporting the higher number because that's the only mandatory figure.
>
> **The Cybertruck case:** advertised 318 mi → MotorTrend 70 mph test: 224 mi. The Range Extender accessory promised at the 2019 announcement to bridge the 500-mi gap was officially cancelled May 2025 with full refunds, never delivered to a single customer.
>
> **The Mercedes EQS case:** advertised 350 mi EPA → Edmunds measured 422 mi (+72 mi). Counter-examples are real and they're in the dataset.
>
> **The methodology** (full version in §3 of the paper) is organized along Gebru et al.'s datasheet lifecycle and builds on Mathur et al.'s "Dark Patterns at Scale." Every claim and every reality measurement is cited with verbatim quotes and web.archive.org snapshots. Records are stored as JSON files validated against a published schema.
>
> **What I'm asking for:**
> 1. **Tell me where I'm wrong.** If a record's claim quote, reality value, or severity is off, file a GitHub issue. Responses get integrated as additional sources, not as redactions.
> 2. **Tell me what's missing.** Phase 2 will expand to 25+ products. If you've documented a gap on a vehicle not yet in v0.1, the schema can absorb it.
> 3. **Tell me about counter-examples.** I want more, not fewer.
>
> Manufacturers represented receive a concurrent notification email today; responses within 30 days are integrated.
>
> Paper: [arXiv-URL]
> GitHub: https://github.com/Princeu3/DataDeception
>
> Happy to answer methodology questions in the comments.

### Reddit secondary — r/cars cross-post

Same body, title slightly more accessible: `Open dataset documenting where US EV manufacturer range/spec claims diverge from independent measurement — 28 records across 8 manufacturers, with paired citations and counter-examples`

### Reddit — what NOT to cross-post

- **r/teslamotors** — historically removes critical Tesla research; will be flagged regardless of methodology.
- **r/teslainvestorsclub** — same reason.
- **r/electricvehicles is the primary community.** r/cars is fine. Skip the brand-specific subs.

---

## Cadence

- **T+0 (launch tweet):** post Tweet 1, schedule Tweets 2–8 at 90-second intervals (faster than reading speed but slow enough to avoid the algorithmic clump filter).
- **T+30 min:** post LinkedIn.
- **T+60 min:** post Reddit r/electricvehicles. Wait for first 5 comments before cross-posting to r/cars (Reddit's cross-post detection is suspicious of simultaneous drops).
- **T+24 hr:** quote-tweet the original Tweet 1 with one additional finding the thread didn't cover (e.g., the recall density bar chart). This lets the thread re-enter timelines.

---

## Tone notes

- **Don't use clickbait language** ("you won't believe", "shocking", "exposed"). The data is strong enough; tabloid framing weakens it.
- **Don't lead with brand attacks**. Lead with the finding, name the brand only once the receipt is established.
- **Do credit prior work** when methodology comes up — Mathur 2019, Gebru 2018, Pennycook & Rand. Lifts the work into the academic frame without sacrificing accessibility.
- **Do welcome corrections explicitly**. "Tell me where I'm wrong" is the Reddit equivalent of the manufacturer notification email — it sets the falsifiability frame and pre-empts hostile responses.
