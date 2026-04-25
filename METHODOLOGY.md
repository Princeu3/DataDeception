# DataDeception — Methodology

**Status**: v0.1 (Phase 0 complete, 3 products documented)
**Last revised**: 2026-04-25

This document defines how DataDeception collects, structures, and grades evidence of divergence between manufacturer claims and independently-measured reality. It is intended as the methodology section of an eventual research paper.

---

## 1. Operational definitions

We use the following terms with precise meanings:

- **Claim**: A quantitative or qualitative assertion made by a manufacturer in any of: marketing copy, configurator pages, spec sheets, regulatory filings (e.g., EPA), press releases, or labeled hardware. The *manufacturer claim* is what the buyer encounters.
- **Reality**: An independently-measured value or characterization of the same property. *Independence* requires the source to (a) not be paid by the manufacturer for that test, and (b) document its methodology.
- **Gap**: The difference between claim and reality. Numeric gaps have absolute and percentage forms. Non-numeric gaps are characterized categorically (definitional, naming, status).
- **Tactic**: A repeatable pattern by which a claim diverges from reality across multiple products. Tactics are the unit of theoretical interest — individual gaps are observations of tactics.
- **Deception record**: A single (product, axis, sub_axis) tuple binding one or more tactics to a claim/reality pair with citations.

We do *not* use the term *fraud* unless a regulatory or judicial finding has used it. We use *divergence* and *gap* by default, and *deceptive* only where a regulator (FTC, state DMV, NHTSA, EU consumer authority) or court has so ruled.

---

## 2. Source taxonomy

Every claim and reality measurement carries one or more sources, each tagged with a tier:

### Tier 1 — Regulatory / open-government
Highest evidence weight. Sources include EPA fueleconomy.gov, NHTSA recalls.gov, NHTSA Part 583 disclosures, DOE AFDC, FTC press releases and consent orders, state attorney general filings, court rulings, EU/UNECE regulatory filings.

These sources are authoritative because they are produced under legal obligation, methodology is published, and they are typically open data.

### Tier 2 — Independent measurement
High evidence weight. Sources include Consumer Reports, Edmunds, MotorTrend, Car and Driver, InsideEVs, Out of Spec Reviews, TFL Truck, Bjørn Nyland, Recurrent Auto, A Better Routeplanner database, Plugshare aggregate stats, Notebookcheck (laptops), RTings (TVs), Audio Science Review (audio).

Tier-2 sources publish methodology, purchase test units anonymously where possible, and explicitly disclose any manufacturer relationships. A source that accepts review units but discloses doing so is still Tier 2; a source that does not disclose is downgraded to Tier 3.

### Tier 3 — Community / forum
Medium evidence weight. Sources include vehicle owner forums (Tesla Motors Club, F-150 Lightning Forum, Rivian Forums, Mach-E Forum), subreddit threads with high engagement, community-submitted data sites (evrangetools.com, Recharged community).

Tier-3 sources are cited only when N ≥ 10 corroborating reports exist or when a single high-engagement thread is referenced for sentiment / lived-experience signal (clearly labeled as such).

### Tier 4 — Manufacturer / brand
Treated as the *claim*, not the *truth*. Manufacturer spec pages, marketing copy, press releases, configurator headlines, sales talking points. A Tier-4 source establishes what the manufacturer is asserting; it cannot establish whether the assertion is correct.

---

## 3. Evidence grading rubric

Each deception record carries an `evidence_grade` ∈ {A, B, C, D}.

### Grade A — Strong evidence
Both of the following must hold:
- The **claim** is sourced from a Tier-1 (regulatory) document or a Tier-4 (manufacturer) document with a verbatim quote.
- The **reality** is established by either (a) a Tier-1 government measurement, (b) two or more independent Tier-2 measurements that converge within their stated uncertainty, or (c) a single Tier-2 measurement *plus* a Tier-3 community signal with N ≥ 10 corroborating reports.

A-grade records carry the implicit claim that any informed reader can reproduce the finding from the cited sources alone.

### Grade B — Moderate evidence
At least one of the following:
- Reality is from a single Tier-2 source with documented methodology, no corroboration yet.
- Reality is editorial framing of a manufacturer-disclosed number (e.g., "150 kW peak is unusually low for a 131 kWh battery") rather than a direct measurement gap.
- Tier-3 community signal with N ≥ 5 corroborating reports but no Tier-2 confirmation.

B-grade is the default for findings that are likely-true but where corroboration is pending.

### Grade C — Weak evidence
- Single Tier-3 source with smaller N (3–5 reports), or older reports (>3 years from current model year).
- Tier-2 source with disclosed methodological limitations (e.g., test conducted on pre-production unit, or in unrepresentative conditions).

C-grade records are flagged but not asserted with confidence in consumer-facing surfaces.

### Grade D — Anecdotal / preliminary
- Tier-4 source only (manufacturer's own disclosure of a gap, with no independent corroboration).
- Single anecdotal post.
- Theoretical / inferential ("based on physics, X must be true") without measurement.

D-grade records are tracked internally but not surfaced to consumers.

### Re-grading discipline
Every record's grade is re-evaluated when (a) new corroborating evidence is added, (b) an existing source is updated, or (c) the model year of the product changes. The `last_verified` field tracks the last grade re-evaluation.

---

## 4. Gap quantification

### Numeric gaps
For metrics like range, charging speed, 0–60 time, price:
- `gap.kind = "numeric"`
- `gap.absolute = reality - claim` (with unit)
- `gap.pct = (reality - claim) / claim × 100`
- Negative percentages indicate reality is below claim.

### Categorical gaps
For naming/classification mismatches (e.g., "Full Self-Driving" vs. SAE Level 2):
- `gap.kind = "categorical"`
- No `absolute` or `pct`; `severity` field is required.

### Definitional gaps
For cases where the claimed property and the measured property are different things despite shared naming (e.g., "motion rate" vs. refresh rate):
- `gap.kind = "definitional"`
- No `absolute` or `pct`; `severity` field is required.

### Severity scale (for categorical and definitional gaps)
- **critical**: Active regulatory finding, safety-of-life impact, or judicial ruling against the claim.
- **high**: Substantial consumer-decision distortion, or a safety pattern with documented incidents but no ruling yet.
- **moderate**: Material misrepresentation but no safety angle and small dollar/utility impact.
- **low**: Technical inaccuracy or industry-convention quirk; informed buyers can correct for it.
- **informational**: Documented for record but unlikely to alter purchase decision.

---

## 5. Tactic taxonomy

Tactics are the theoretical units of this research. Individual records cite ≥1 tactic; tactics may be cited by many records across products and manufacturers. The current taxonomy (v0.1) contains 10 tactics in 5 families:

### Family A — Regulated metric misapplied
Manufacturer cites a regulated number correctly but in a context where it does not apply.
- `epa_vs_highway_70mph`: EPA combined cycle treated as if it represents highway range.

### Family B — Instantaneous peak as average
A peak number is advertised as if it is a sustained or average rate.
- `peak_dc_charge_sustained_briefly`: Peak charging rate sustained <10 min.
- `peak_charge_rate_unrealistic`: Peak rate not reproducibly observed in tests.

### Family C — Specs in isolation
Two specs are advertised as if they apply simultaneously when they don't.
- `towing_range_collapse_undisclosed`: Tow capacity + EPA range advertised together; towing collapses range 40–60%.

### Family D — Methodology / disclosure gaps
- `zero_to_60_marketing_vs_instrumented`: Rollout convention not disclosed.
- `starting_at_excludes_mandatory_fees`: Headline price excludes destination/delivery.
- `level_2_home_charging_time`: EPA-mandated number disclosed but de-emphasized in marketing.
- `silent_discontinuation`: Production halted without prominent disclosure.

### Family E — Linguistic / definitional overclaim
- `feature_naming_implies_capability`: Feature name implies higher capability than provided (e.g., "Full Self-Driving").
- `touchscreen_obscures_basic_controls`: Marketed design choice has documented safety regression.

The taxonomy is open: new tactics may be added when ≥2 independent products exhibit a pattern not covered by existing tactics. Single-product patterns are noted in the relevant record's `narrative` but not promoted to the tactic dictionary until corroborated.

---

## 6. Sampling strategy (current)

### Phase 0 (this version, 3 products)
Selection criterion: products with the strongest available independent measurement *and* the highest cultural salience. Tesla Model Y (best-selling EV globally), Ford F-150 Lightning (Consumer Reports' largest-gap finding), Rivian R1S Dual Max (CR's tied-largest-gap, headline 410-mi flagship). Bias acknowledged: this oversamples products *we already knew had gaps*. Phase 1 will sample products without prior expectation of deception.

### Phase 1 (next, 12 more products)
Add: Tesla Model 3, Tesla Cybertruck, Hyundai Ioniq 5/6, Kia EV6, Lucid Air, Mercedes EQS, Chevy Silverado EV, GMC Hummer EV, Ford Mustang Mach-E, VW ID.4, Polestar 2.

### Phase 2 (longitudinal)
Same products, multi-year tracking (model year as a covariate). Goal: detect whether tactics are tightening or loosening over time, controlled for product evolution.

---

## 7. Coverage discipline

Within each (product, model_year, trim), we currently target the following 12 sub-axes when data exists:

1. `range / highway_70mph` (vs. EPA combined)
2. `range / cold_weather_loss`
3. `range / towing_loss` (trucks/SUVs only)
4. `charging / peak_dc_sustained_duration`
5. `charging / peak_dc_observed_vs_advertised`
6. `charging / level2_240v_full_charge`
7. `performance / zero_to_60_rollout`
8. `software_features / autonomy_naming` (where relevant)
9. `pricing / starting_at_destination`
10. `pricing / tax_credit_eligibility`
11. `production_status / discontinuation`
12. `ui_ergonomics / touchscreen_distraction`

Records may be omitted if data is unavailable or not applicable. *Omission is not assertion of absence*.

---

## 8. Reproducibility commitments

- All claim sources include a verbatim quote so a reader can verify against the original even if URLs rot.
- Tier-4 (manufacturer) sources receive a `snapshot_url` to web.archive.org. *Phase 1 deliverable; Phase 0 records pending.*
- All JSON conforms to JSON Schema 2020-12; the `validate.py` script in the repo root validates the entire dataset.
- This document and the schema files are versioned alongside data; methodology changes are recorded in CHANGELOG.md (Phase 1).

---

## 9. Threats to validity

See `LIMITATIONS.md` for the full list. Briefly:

- Selection bias in product set (Phase 0).
- Source bias: Consumer Reports tests are excellent but represent N=1 unit; their result may not generalize.
- Temporal bias: independent tests are typically conducted at one point in time and may not reflect later software updates that can shift performance materially.
- Self-confirmation bias: we hypothesize gaps exist before measuring; care taken to also document records where claim ≈ reality.
- Manufacturer copy mutates: a quote captured today may not match the page tomorrow. Snapshot URLs mitigate but do not eliminate.
