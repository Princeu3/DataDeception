# Launch-day social copy — DataDeception v0.1

Three platforms. Post in this order: **Twitter/X thread → LinkedIn → Reddit**. Twitter first because the thread URL becomes the canonical share asset that LinkedIn and Reddit can link to.

**Zenodo DOIs** (concept, always-latest):
- Paper: `https://doi.org/10.5281/zenodo.19777605` (PDF opens directly in Zenodo viewer)
- Dataset + code: `https://doi.org/10.5281/zenodo.19777404`

**GitHub:** `https://github.com/Princeu3/DataDeception`. arXiv URL will be added as a separate line once endorsement is secured.

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

> 📄 Paper: https://doi.org/10.5281/zenodo.19777605
> 💾 Dataset & code: https://doi.org/10.5281/zenodo.19777404
> 🔧 Methodology: §3 of the paper
>
> If you've been mis-sold an EV spec, file a record. If you're a regulator, the data is yours. If you're a manufacturer, your notification email is in your inbox.

---

## LinkedIn — single post (humanized, in your voice — POSTED 2026-04-26)

> Tesla advertised 318 miles of Cybertruck range. Independent measurement at 70 mph: 224.
>
> That's a 30% shortfall. It's also the least interesting number in this story.
>
> The interesting number is 8. Eight different manufacturers — Tesla, Ford, Rivian, Hyundai, Lucid, Mercedes, GMC, VW — all show the same gap pattern. Mean −15%. Worst −30%. Best +3% (Mercedes EQS — the one that beats EPA, by 72 miles).
>
> Eight manufacturers don't coordinate. So either they're all reading the same playbook, or there isn't a playbook at all. There isn't a playbook.
>
> EPA's combined city/highway cycle is the only mandatory range figure on the Monroney sticker. It doesn't match how anyone actually drives. Every manufacturer publishes the higher EPA number because that's the legally-required one. The "deception" you keep seeing in EV reviews isn't dishonesty. It's a regulatory test cycle that hasn't been seriously updated in 30 years.
>
> That's the actual story, and it took me a few weeks to see it.
>
> I built a structured dataset to make this kind of pattern legible:
>
> DataDeception v0.1 — 13 products, 28 records, 13 tactics, 8 manufacturers. Every record has paired claim/reality citations, an A–D evidence grade, and an archived URL on the manufacturer's marketing surface. Counter-examples by design (Mercedes EQS, Ford Mach-E). NHTSA recall data integrated. Schema-validated. MIT + CC-BY-4.0.
>
> Built on Gebru et al.'s "Datasheets for Datasets" (arXiv:1803.09010) and Mathur et al.'s "Dark Patterns at Scale" (arXiv:1907.07032). Citation-first means every claim has its receipt.
>
> Things that surprised me writing it:
>
> → The Cybertruck Range Extender — Tesla's $16,000 auxiliary-battery accessory announced in 2019 to bridge the 500-mile range promise — was officially cancelled May 2025. Six years. Zero delivered.
>
> → "Full Self-Driving" was ruled "unambiguously false and counterfactual" by a California ALJ in December 2025. NHTSA's investigation now covers 2.88M vehicles, 14 crashes, 23 injuries. The name is still on the configurator with a parenthetical.
>
> → Rivian R1S 2025: 9 NHTSA recalls. Hyundai Ioniq 5 2025: 8 (two separate high-voltage traction-battery campaigns). Brand quality language doesn't track this.
>
> The dataset is built to falsify itself. If a record is wrong, file a GitHub issue. I'll integrate the correction as an additional source, not a redaction.
>
> 📄 Paper: https://doi.org/10.5281/zenodo.19777605
> 💾 Dataset + code: https://doi.org/10.5281/zenodo.19777404
>
> 1 of the 13 vehicles audited beats its EPA range. That's the load-bearing finding — without counter-examples, this would be confirmation-bias dressed up as research.
>
> #ElectricVehicles #ConsumerProtection #OpenScience #FTC

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
> Paper (PDF, direct): https://doi.org/10.5281/zenodo.19777605
> Dataset + code (DOI): https://doi.org/10.5281/zenodo.19777404
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
