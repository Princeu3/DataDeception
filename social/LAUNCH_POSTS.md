# Launch-day social copy — DataDeception v0.1

Three platforms. Post in this order: **Twitter/X thread → LinkedIn → Reddit**. Twitter first because the thread URL becomes the canonical share asset that LinkedIn and Reddit can link to.

Zenodo DOI (concept, always-latest): `https://doi.org/10.5281/zenodo.19777404`. The GitHub URL is `https://github.com/Princeu3/DataDeception`. arXiv URL will be added as a separate line once endorsement is secured.

---

## Twitter/X — 8-tweet thread (in your voice)

**Tweet 1 (hook).**

> Tesla advertised 318 miles of Cybertruck range. MotorTrend at 70 mph: 224.
>
> A 30% shortfall — and it's not the most interesting part.
>
> Today: DataDeception, a citation-first dataset of where US EV manufacturer claims diverge from independent measurement. 28 records, 8 manufacturers. 🧵

**Tweet 2 (the pattern).**

> The Cybertruck is the largest gap. The Cybertruck is also not the point.
>
> The point: the same `epa_vs_highway_70mph` pattern recurs across 8 manufacturers — Tesla, Ford, Rivian, Hyundai, Lucid, Mercedes, GMC, VW.
>
> Mean gap: −15%. Worst: −30%. Best: +3%.
>
> [attach: gap-dotplot figure]

**Tweet 3 (the cause).**

> Why? Not coordination. Not marketing.
>
> The cause is regulatory: EPA's combined city/highway cycle is the only mandatory range figure on the Monroney sticker, and it doesn't match how anyone actually drives. Every manufacturer has the same incentive to publish the higher number.

**Tweet 4 (counter-examples).**

> The dataset deliberately includes counter-examples so you can falsify it.
>
> Mercedes EQS measured 422 mi vs. 350 mi EPA — beats by 72 mi.
> Ford Mach-E matches EPA in independent testing.
>
> Cross-manufacturer doesn't mean cross-villainy. The gap is structural.

**Tweet 5 (case study).**

> Cybertruck range promise, 2019–2025:
>
> 2019: "500+ miles" announced
> 2023: shipped at 318 mi EPA
> 2024: MotorTrend instrumented 224 mi @ 70 mph
> May 2025: Range Extender cancelled, full refunds, zero delivered
>
> Six years of receipts.

**Tweet 6 (FSD).**

> Categorical deception, not just numeric: "Full Self-Driving" was ruled "unambiguously false and counterfactual" by a CA Administrative Law Judge in December 2025.
>
> NHTSA's October 2025 investigation: 2.88M vehicles, 14 crashes, 23 injuries.
>
> Severity grade in our rubric: critical.

**Tweet 7 (methodology + open data).**

> Methodology builds on Gebru et al. "Datasheets for Datasets" (arXiv:1803.09010) and Mathur et al. "Dark Patterns at Scale" (arXiv:1907.07032).
>
> Every record: paired claim/reality citations, A–D evidence grade, archived URL, tactic from a 13-tactic taxonomy across 5 families. MIT + CC-BY-4.0.
>
> [attach: tactic-taxonomy figure]

**Tweet 8 (link + ask).**

> 📄 Paper: https://doi.org/10.5281/zenodo.19777404
> 💾 Code + data: github.com/Princeu3/DataDeception
> 🔧 Methodology: §3 of the paper
>
> If you've been mis-sold an EV spec, file a record. If you're a regulator, the data is yours. If you're a manufacturer, your notification email is in your inbox.

---

## LinkedIn — single post (in your voice)

> Tesla advertises 318 miles of range for the Cybertruck. MotorTrend's instrumented test at 70 mph: 224 miles.
>
> A 30% shortfall. It's also not what makes this case interesting.
>
> The interesting part is that the same gap pattern shows up across 8 different manufacturers. Tesla, Ford, Rivian, Hyundai, Lucid, Mercedes, GMC, Volkswagen. Mean gap: −15%. The Mercedes EQS goes the other way — beats EPA by 72 miles.
>
> So what's the actual finding? Marketing doesn't explain it. Coordination doesn't explain it. The cause is regulatory: EPA's combined city/highway test cycle is the only mandatory range figure on a Monroney sticker, and it doesn't match how anyone actually drives. Every manufacturer has the same incentive to publish the higher number; few publish the supplemental 70 mph figure independent measurement reveals.
>
> I spent the last few weeks building DataDeception v0.1 — a structured, citation-first dataset of where U.S. EV manufacturer claims diverge from independent measurement.
>
> → 13 products × 28 records × 13 tactics × 8 manufacturers
> → Every record carries paired claim/reality citations, an A–D evidence grade, and an archived URL on the manufacturer side
> → Counter-examples included by design (Mercedes EQS, Ford Mach-E)
> → Tier-1 NHTSA recall data integrated (Rivian R1S 2025: 9 recalls. Hyundai Ioniq 5 2025: 8, including two separate high-voltage traction-battery campaigns)
> → Schema-validated against JSON Schema 2020-12
> → MIT (code) + CC-BY-4.0 (data)
>
> The methodology builds on Gebru et al.'s "Datasheets for Datasets" (arXiv:1803.09010) and Mathur et al.'s "Dark Patterns at Scale" (arXiv:1907.07032). The contribution is a citation-first schema where every claim has its receipt and every gap is falsifiable.
>
> Three policy implications follow directly from the corpus:
>
> 1. A supplemental 70 mph constant-speed EPA rating on the Monroney label.
> 2. Per-se UDAP treatment for feature-naming overclaims at SAE-level mismatch — the Tesla "Full Self-Driving" name was ruled "unambiguously false and counterfactual" by a CA Administrative Law Judge in December 2025; NHTSA's investigation now covers 2.88M vehicles, 14 crashes, 23 injuries.
> 3. Mandatory disclosure of independent measurements adjacent to manufacturer claims.
>
> The dataset is built to falsify itself. If you've documented a gap that should be added, or if a record is wrong, file a GitHub issue. I'll integrate it.
>
> 📄 Paper: https://doi.org/10.5281/zenodo.19777404
> 💾 Dataset + code: github.com/Princeu3/DataDeception
>
> The biggest finding might be that 1 of 13 vehicles audited beats its EPA range. That's why this isn't an anti-EV piece — it's a measurement-infrastructure piece.
>
> #ElectricVehicles #ConsumerProtection #OpenData #FTC #ResearchData

---

## Reddit — primary post (r/electricvehicles, in your voice)

**Title:** `[Research] DataDeception v0.1 — citation-first dataset of where US EV manufacturer claims diverge from independent measurement (28 records, 8 manufacturers)`

**Body:**

> Tesla advertised 318 miles of Cybertruck range. MotorTrend at 70 mph: 224. A 30% shortfall — and it's not the most interesting part.
>
> Spent the last few weeks building a structured dataset of where US EV manufacturer claims diverge from independent measurement. v0.1 is out today, and this community already knows most of these gaps individually — the corpus just makes them legible at scale.
>
> **The numbers:**
>
> - 13 products, 28 deception records, 13 tactics across 5 families
> - 8 manufacturers (Tesla, Ford, Rivian, Hyundai, Lucid, Mercedes, GMC, VW)
> - Every record: paired claim/reality citations, A–D evidence grade, archived URL on the manufacturer side
> - Counter-examples included by design (Mercedes EQS, Ford Mach-E)
> - Tier-1 NHTSA recall data integrated (Rivian R1S 2025: 9 recalls. Hyundai Ioniq 5: 8, including two separate high-voltage traction-battery campaigns)
> - Schema-validated, reproducible, MIT + CC-BY-4.0
>
> **What I think is the actual finding:**
>
> The biggest finding isn't any single product gap. It's that the same pattern (EPA combined cycle vs. real 70 mph cruising) recurs across **8 different manufacturers including counter-examples in both directions**. That's not a coincidence of marketing choices. It's regulatory test-cycle mismatch: EPA's combined city/highway weighting doesn't reflect how range gets used. Every manufacturer is reporting the higher number because that's the only mandatory figure.
>
> The cross-cutting structure is evidence of test-cycle dominance, not coordinated deception. That distinction matters for the policy framing — the appropriate intervention is at the disclosure layer (require a supplemental 70 mph rating on the Monroney) rather than at the deceptive-intent layer (which faces a much higher evidentiary bar).
>
> **Cybertruck case:** advertised 318 mi → MotorTrend 70 mph test: 224 mi. The Range Extender accessory promised at the 2019 announcement to bridge the 500-mi gap was officially cancelled May 2025 with full refunds, never delivered to a single customer.
>
> **Mercedes EQS case:** advertised 350 mi EPA → Edmunds measured 422 mi (+72 mi over). Counter-examples are real and they're in the dataset.
>
> **Methodology:** full version in §3 of the paper. Built on Gebru et al.'s datasheet lifecycle and Mathur et al.'s "Dark Patterns at Scale." Every claim and every reality measurement is cited with verbatim quotes and web.archive.org snapshots. Records are JSON files validated against a published schema.
>
> **What I'm asking from this sub:**
>
> 1. Tell me where I'm wrong. If a record's claim quote, reality value, or severity is off, file a GitHub issue. Responses get integrated as additional sources, not as redactions.
> 2. Tell me what's missing. Phase 2 will expand to 25+ products. If you've documented a gap on a vehicle not yet in v0.1, the schema can absorb it.
> 3. Tell me about counter-examples. I want more, not fewer.
>
> Manufacturers represented receive a concurrent notification email today; responses within 30 days are integrated.
>
> Paper: https://doi.org/10.5281/zenodo.19777404
> GitHub: github.com/Princeu3/DataDeception
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
