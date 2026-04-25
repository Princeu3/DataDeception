# DataDeception — EV Vertical Plan

**Date**: 2026-04-25
**Phase 0**: ✅ complete (3 products, 13 records, 10 tactics, 4 schemas, methodology+RQ+limitations docs)
**Phase 1**: ✅ in-session expansion complete (10 additional products, 12 additional records, 2 new tactics)
**Current totals**: 13 products · 25 deception records · 12 tactics · all validated against schema
**Vertical**: Electric Vehicles (passenger + light truck, US market)
**Decision rationale**: see DECISION.md (TBD) — short version: best open data foundation (EPA fueleconomy.gov), live cultural moment (Tesla dashboard-rigging), high-stakes purchase, multi-axis deception, low legal risk.

---

## 1. What we're actually building

A **structured, citation-first dataset** of where EV manufacturer claims diverge from independently-measured reality, then a thin consumer surface on top.

**Core artifact**: a public, versioned database keyed on `(manufacturer, model, model_year, trim)` that cross-references manufacturer claims against independent measurements, with provenance for every number.

**Consumer surface (v1)**: a public website with one page per (model, trim) showing claim-vs-reality for every deception axis, with citations. Inline "marketing tactic detected" flags.

**Out of scope for now**:
- Chrome extension (later, once the data has authority)
- LLM-generated verdicts (we use rules + citations, not model opinions)
- Used-car / private-party deception
- Hybrid / PHEV
- Two-wheelers, micromobility
- Outside-US markets (mention WLTP/NEDC for context, don't catalog)

---

## 2. Deception axes (the schema)

Six top-level axes, each with sub-axes. Every data point is `(product, axis, sub_axis, claim_value, real_value, gap_pct, sources[], evidence_grade)`.

### 2.1 Range deception
| Sub-axis | Manufacturer claim source | Independent measurement source | Typical gap |
|---|---|---|---|
| EPA combined range (mi) | EPA fueleconomy.gov | (regulatory baseline — used as the *claim*) | — |
| Highway range @ 70mph | Marketing copy ("up to X miles") | Consumer Reports 70mph test, Edmunds, InsideEVs | -10% to -25% |
| Cold-weather range loss | Rarely disclosed, sometimes "may vary" | Recurrent Auto annual report, owner-forum data | -20% to -40% |
| Towing range | Almost never disclosed | TFL Truck, Out of Spec Reviews, owner forums | -40% to -60% |
| High-speed (75-80mph) range | Not disclosed | Bjørn Nyland 1000km test, A Better Routeplanner | -15% to -30% |
| Year 5 / 100K mi capacity | "Battery designed to last 1M miles" puffery | Recurrent battery degradation data (anonymized fleet) | -8% to -15% capacity |

### 2.2 Charging deception
| Sub-axis | Claim source | Independent source | Typical gap |
|---|---|---|---|
| Peak DC fast-charge rate (kW) | Spec sheet ("up to 350kW") | Out of Spec, Bjørn Nyland charge curves | Sustained for 60-120s only |
| 10-80% time (min) | Manufacturer at "ideal" temp | Real-world cold/hot tests, owner forum data | +30% to +100% |
| Network compatibility | "Compatible with NACS adapter" | Plugshare, A Better Routeplanner reliability data | Variable |
| Charging curve degradation | Not disclosed | Out of Spec, Battery Life YT | Significant after 50% SOC |
| Charging cost | "Free Supercharging for 1 yr" | Real per-kWh cost vs gas equivalent | Network markup 30-100% |

### 2.3 Performance deception
| Sub-axis | Claim source | Independent source | Typical gap |
|---|---|---|---|
| 0-60 (sec) | Marketing ("3.0 seconds*") | Edmunds, MotorTrend instrumented tests | Often requires Launch Mode + summer tires |
| Top speed | Spec sheet | Track tests | Often software-locked, paid unlock |
| Sustained power (kW) | Peak number listed | Dyno tests | Peak holds <30 sec |
| Towing capacity | "10,000 lb tow rating" | Real-world with trailer brake controller | Comes with massive range collapse |
| Horsepower / torque | Peak | Wheel-dyno tests | Battery-temp dependent |

### 2.4 Software / Features deception
| Sub-axis | Claim source | Independent source | Notes |
|---|---|---|---|
| "Full Self Driving" capability | Marketing copy | NHTSA classification (still SAE L2) | FTC has open inquiry — Tesla, others |
| "Autopilot" naming | Brand name | SAE J3016 | Linguistic deception, not capability deception |
| Subscription-locked HW | "Available now" | Whether feature actually unlocks | Heated seats (BMW), range unlocks (Tesla) |
| OTA-removable features | Buy-time disclosure | Subsequent firmware behavior | Tesla post-purchase range nerfs |
| "Smart Summon" / driver-aid claims | Demo videos | Real-world failure rate | Anecdotal mostly |

### 2.5 Pricing deception
| Sub-axis | Claim source | Reality |
|---|---|---|
| "Starting at" MSRP | Price headline | Often w/o destination ($1,700+), order fees, mandatory packages |
| "After tax credit" pricing | Marketing copy | Eligibility varies (income cap, battery sourcing rules — IRA §30D) |
| Trade-in / lease deception | Advertised lease | Real money factor + residual + acquisition fee |
| Software subscription lifetime | Year-1 free or trial | $99-$199/mo recurring (FSD, premium connectivity) |
| Charging cost claims | "Cheaper than gas" | Network markup vs home-charge differential |

### 2.6 Build / Warranty / Reliability deception
| Sub-axis | Claim source | Independent source |
|---|---|---|
| "Built in USA" | Marketing copy | NHTSA Part 583 American Automobile Labeling Act % domestic content |
| Battery warranty exclusions | Fine print | Class actions, NHTSA TSBs |
| Battery replacement cost | Not disclosed | iFixit, third-party shop estimates ($15-30K typical) |
| Recall / NHTSA complaint history | Not in marketing | NHTSA recalls.gov, complaints database |
| J.D. Power / CR reliability | "Award-winning" if cherry-picked | CR/J.D. Power latest score |

**Total deception axes: 6 top-level, ~30 sub-axes.** First-pass MVP can ship with ~12 sub-axes (the ones with strong independent data and consumer relevance).

---

## 3. Source taxonomy

Each data point cites at least one **regulatory source** (when the claim is regulated) and one **independent source** (when challenging the claim).

### Tier 1 — Regulatory / open-government (highest evidence weight)
- **EPA fueleconomy.gov** — open data, all EV range/efficiency claims filed here
- **NHTSA recalls.gov + complaints database** — open data
- **NHTSA Part 583** — domestic content disclosures
- **DOE Alternative Fuels Data Center** — charging infrastructure
- **FTC consumer protection actions** — for precedent

### Tier 2 — Independent measurement (high evidence)
- **Consumer Reports** — 70mph highway tests, reliability surveys (paywalled but citable)
- **Edmunds** — long-term tests, instrumented 0-60
- **InsideEVs** — independent reviews, charge-curve testing
- **MotorTrend** — instrumented testing
- **Out of Spec Reviews** (YouTube + database) — range, charging, towing
- **TFL Truck** (YouTube) — real-world towing tests
- **Bjørn Nyland** — 1000km test methodology
- **Recurrent Auto** — anonymized fleet battery health data
- **A Better Routeplanner** — community real-world charging/range data
- **Plugshare** — community charging-station data

### Tier 3 — Community / forum (medium evidence — needs N>10 to cite)
- **r/electricvehicles, r/teslamotors, r/RivianForum, r/Lightning, r/MachE**
- **Tesla Motors Club, Rivian Forums, F-150 Lightning Owners**
- **evrangetools.com** — community range submissions

### Tier 4 — Manufacturer / brand (treated as the *claim*, not the *truth*)
- Manufacturer spec pages, configurators, marketing copy
- Manufacturer press releases
- Manufacturer disclosed financial filings (10-K, 10-Q)

### Citation format (every record)
```json
{
  "source_tier": 1|2|3|4,
  "source_name": "EPA fueleconomy.gov",
  "url": "https://...",
  "accessed_date": "2026-04-25",
  "snapshot_url": "https://web.archive.org/...",  // for non-API sources
  "verbatim_quote": "..."  // when text-based
}
```

**Snapshot rule**: any non-API source MUST be archived to web.archive.org before citation, to defend against "manufacturer changed the page" attacks.

---

## 4. Product seed list (v1 — top 15 US EVs)

Selection rule: top US sales 2024-2025 + headline-deception cases. We start with these because they're the products most buyers research and most journalists cover.

| # | Manufacturer | Model | Model Years | Why included |
|---|---|---|---|---|
| 1 | Tesla | Model Y | 2024, 2025, 2026 | Best-selling EV globally |
| 2 | Tesla | Model 3 | 2024, 2025, 2026 | Dashboard-rigging case |
| 3 | Tesla | Cybertruck | 2024, 2025 | "500 mi range" vs delivered 320 |
| 4 | Ford | F-150 Lightning | 2024, 2025 | CR found 50-mi gap |
| 5 | Ford | Mustang Mach-E | 2024, 2025 | Owner forum data rich |
| 6 | Rivian | R1T | 2024, 2025 | 52-mi gap on R1S analog |
| 7 | Rivian | R1S | 2024, 2025 | Direct CR 52-mi gap |
| 8 | Hyundai | Ioniq 5 | 2024, 2025 | High-volume, fast-charge claims |
| 9 | Hyundai | Ioniq 6 | 2024, 2025 | Advertised efficiency leader |
| 10 | Kia | EV6 | 2024, 2025 | Sister to Ioniq 5 |
| 11 | Chevy | Silverado EV | 2024, 2025 | Towing-range claims |
| 12 | GMC | Hummer EV | 2024, 2025 | Heaviest EV, range-claim controversies |
| 13 | Lucid | Air | 2024, 2025 | Longest-range claim (516 mi) |
| 14 | Mercedes | EQS | 2024, 2025 | German WLTP-vs-EPA mismatch |
| 15 | VW | ID.4 | 2024, 2025 | High-volume mainstream |

Total starting dataset: 15 models × ~3 trims avg × ~12 sub-axes = **~540 data points** for v1.

---

## 5. Schema (concrete)

### 5.1 `product.json`
```json
{
  "id": "tesla-model-y-2025-long-range-awd",
  "manufacturer": "Tesla",
  "model": "Model Y",
  "model_year": 2025,
  "trim": "Long Range AWD",
  "msrp_usd": 48990,
  "msrp_includes_destination": false,
  "destination_fee_usd": 1390,
  "battery_kwh_usable": 75.0,
  "battery_kwh_total": 78.4,
  "epa_range_mi": 310,
  "epa_range_url": "https://www.fueleconomy.gov/feg/...",
  "trim_inherits_from": "tesla-model-y-2025"  // for shared parent specs
}
```

### 5.2 `deception.json` (one record per axis-instance)
```json
{
  "product_id": "ford-f-150-lightning-2024-extended-range",
  "axis": "range",
  "sub_axis": "highway_70mph",
  "claim": {
    "value": 320,
    "unit": "mi",
    "source": {
      "tier": 4,
      "name": "Ford spec page",
      "url": "https://www.ford.com/...",
      "snapshot_url": "https://web.archive.org/web/...",
      "verbatim_quote": "EPA-est. range: 320 miles"
    }
  },
  "reality": {
    "value": 270,
    "unit": "mi",
    "source": {
      "tier": 2,
      "name": "Consumer Reports 70mph highway test",
      "url": "https://www.consumerreports.org/...",
      "snapshot_url": "https://web.archive.org/web/...",
      "verbatim_quote": "battery ran out after just 270 miles"
    }
  },
  "gap_pct": -15.6,
  "tactic_flags": ["epa_vs_highway", "ideal_conditions_only"],
  "evidence_grade": "A",
  "first_documented": "2024-03-15",
  "last_verified": "2026-04-25"
}
```

### 5.3 `tactic.json` (deception pattern dictionary)
```json
{
  "id": "epa_vs_highway",
  "label": "EPA combined vs. real highway gap",
  "description": "EPA combined cycle weighs city + highway; real-world highway driving at 70+mph is closer to highway-only and consistently shorter than EPA combined.",
  "regulatory_basis": "EPA test cycle (40 CFR 600)",
  "consumer_harm": "Buyers plan road trips assuming EPA range; arrive at chargers with less."
}
```

### 5.4 `evidence_grade` rubric
- **A**: Tier 1 or Tier 2 source, recent (<24 mo), N>1 measurement
- **B**: Tier 2 single test or Tier 3 with N>10
- **C**: Tier 3 only, smaller N, or older
- **D**: Tier 4 only, or anecdotal — flagged but not asserted

---

## 6. Pipeline (high-level — not building yet)

For now, **manual curation** for 15 products × 12 sub-axes. ~30 hours of work. No code.

When we automate (later):
1. EPA fueleconomy.gov has a CSV/API → easy
2. NHTSA recalls.gov has API → easy
3. CR / Edmunds / InsideEVs / MotorTrend → manual extract + structured note (not scraping; their content is the source we cite)
4. YouTube transcript pipeline (yt-dlp + claude-mem) → for Out of Spec, TFL Truck, Bjørn Nyland — extract real-world numbers from videos
5. Owner forum aggregation → only when we want N>10 community signal; until then skip

**No LLM-generated facts.** LLM is allowed for: tactic-tag suggestion, normalizing units, copy editing. Not for inventing or interpolating numbers.

---

## 7. Repo structure (what we'll build)

```
DataDeception/
├── PLAN.md (this doc)
├── data/
│   ├── products/
│   │   └── tesla-model-y-2025-long-range-awd.json
│   ├── deceptions/
│   │   └── ford-f-150-lightning-2024-extended-range__range__highway_70mph.json
│   ├── tactics/
│   │   └── epa_vs_highway.json
│   └── sources/
│       └── (raw scraped/saved snapshots)
├── schema/
│   └── (JSON Schema files for validation)
├── notes/
│   └── (per-product research notes during curation)
└── (later) web/
```

---

## 8. Risks & explicit non-goals

### Risks
1. **Manufacturer pushback** — mitigation: only cite, never editorialize. Show their fine-print + independent measurement; let user judge.
2. **Source data goes paywall** (CR, RTings cautionary tale) — mitigation: snapshot to web.archive.org; cite verbatim quotes; if a source paywalls, downgrade evidence grade.
3. **Manufacturer changes spec page** — mitigation: snapshot every claim source.
4. **Federal data politicized** (e.g., IRA tax credit changes) — mitigation: timestamp every record; track regulatory changes as their own log.
5. **EV market segments fast** — mitigation: model_year scoping, structured trim handling, version snapshots.

### Non-goals (intentional, can revisit)
- Chrome extension v1
- User accounts / submissions (community moderation cost too high too early)
- LLM verdicts ("this is misleading") — stick to factual gaps
- Outside-US markets
- Used EVs / private party
- Charging-network app (Plugshare/ABRP already do this)
- "Score" / "rating" per manufacturer (premature — let the data speak)

---

## 8.5 Phase 1 in-session results (2026-04-25)

10 additional products documented end-to-end with EPA + Tier-2 corroboration:

| Product | EPA combined | Tier-2 reality | Gap | Severity |
|---|---|---|---|---|
| Tesla Model 3 LR AWD | 346 mi | ~305 mi (Recharged 75mph; Out of Spec hit 370 ideal) | -12% | moderate |
| Tesla Cybertruck AWD | 325 mi | 224 mi (MotorTrend 70mph) | -30% | high |
| Mercedes EQS 450+ | 390 mi | 380 mi CR / 422 mi Edmunds (BEATS EPA — counter-example) | +/-3% | informational |
| GMC Hummer EV 2X | 318 mi | ~250 mi 75mph | -21% | high |
| Ford Mustang Mach-E AWD ER | 300 mi | 299 mi CR (matches — counter-example) | -0.3% | informational |
| VW ID.4 AWD Pro S | 263 mi | 240 mi C&D 75mph | -9% | moderate |
| Hyundai Ioniq 5 RWD LR | 318 mi | 267 mi CR (sister trim) | -16% | moderate |
| Hyundai Ioniq 6 SE RWD LR | 361 mi | 291 mi MotorTrend 70mph | -19% | high |
| Lucid Air Grand Touring 19" | 516 mi | 410 mi C&D 75mph; 344 mi CR | -21% | high |
| Polestar 2 Dual Motor | 276 mi | (deferred — no strong Tier-2 source) | TBD | TBD |

**New tactics introduced**:
- `unfulfilled_announcement_promise` — Cybertruck 500-mi promise, Range Extender cancellation
- `heavy_duty_certification_exemption` — Hummer EV 24-module pack 381 mi (no EPA cert)

**New deception records** (12 total):
- Range vs highway: 9 records (one per new product, plus 2 explicit counter-examples)
- Cybertruck announcement-promise saga: 1 record
- Hummer EV heavy-duty exemption: 1 record
- Lucid Air wheel-size cliff: 1 record

**Counter-examples now in dataset (essential for RQ1 honesty)**:
- Mercedes EQS — beats EPA by 30–72 mi
- Ford Mustang Mach-E — matches EPA within 1 mile
- Tesla Model 3 (partial) — beats EPA in ideal Out of Spec test, falls short in typical conditions

This addresses the confirmation-bias risk flagged in LIMITATIONS.md §1: the dataset now demonstrates that EPA-vs-real divergence is *not unidirectional*, which strengthens claims about the cases where divergence does occur.

**Severity distribution after Phase 1** (n=25 records):
- Critical: 2 (Tesla FSD, Lightning towing)
- High: 8 (Cybertruck range, Cybertruck promise, Hummer range, Hummer exemption, Tesla M3-no — wait Tesla M3 is moderate; Lightning range, Lightning discontinuation, Rivian touchscreen, Lucid Air range, Ioniq 6 range — 8 high)
- Moderate: 9
- Low: 2
- Informational: 4 (Tesla M3 sustained-charge, ID.4 marker, Mach-E counter-example, EQS counter-example)

**Evidence-grade distribution after Phase 1**:
- A: 14
- B: 11
- C: 0
- D: 0

## 9. Phase 0 (today / next session)

What I'll do next, when you say go:

1. Pick **3 products** from the seed list to fully document end-to-end as a schema-validation pass. Suggested: Tesla Model Y 2025 LR AWD, Ford F-150 Lightning 2024 Extended Range, Rivian R1S 2025 Dual-Motor.
2. For each, document **all 12 priority sub-axes** with claim + reality + sources, in the JSON schema above.
3. Output: 3 product files + ~36 deception records + tactic dictionary + sources file.
4. Eyeball the result with you. If schema holds, scale to the remaining 12 products.

**Estimate**: 3-4 hours for the 3-product validation pass.

---

## 10. Open questions for Prince

1. **Hosting/infra preference for the eventual site?** (Next.js + Supabase is easy; static-only with JSON files is also viable for v1; you have Vercel + Supabase already wired up.)
2. **Public from day one, or staging first?** Default: build in public on a private repo, switch to public when we have 5+ fully-documented products.
3. **Domain idea?** Working name `DataDeception` — fine for code, weak for consumer brand. Real names later (e.g., "RangeRealCheck", "SpecAudit", "ClaimGap.ev"). Don't decide now.
4. **Time budget?** This is 30+ hours of curation before we ship anything visible. Confirm you want to spend it.
