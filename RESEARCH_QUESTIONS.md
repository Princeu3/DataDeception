# Research Questions

**Status**: v0.1 (Phase 0 — initial framing)

This document states the research questions DataDeception is designed to answer, the hypotheses associated with each, and what would constitute evidence for and against each hypothesis. It is the foundation for any eventual paper or external publication.

---

## RQ1 — Do EV manufacturer claims systematically diverge from independently measured reality?

**H1.0 (null)**: Manufacturer claims are within ±5% of independent measurements on a population-weighted basis. Differences are random noise from test-condition variation.

**H1.1 (working)**: Manufacturer claims systematically overstate reality on at least three axes (range, charging speed, performance) by ≥10% on average across the top-15 US-market EVs.

**Evidence we will accept for H1.1**: ≥10 deception records with grade A across ≥6 distinct manufacturers showing claim/reality gaps in the same direction (manufacturer-favorable).

**Evidence we will accept for H1.0**: Distribution of gaps centered at zero with standard deviation ≤5% across the same coverage.

**Phase 0 status**: 13 records, 3 manufacturers. All 3 highway-range gaps trend in the same direction (claim > reality) with magnitudes 13–23%. Insufficient to reject H1.0 at population scale, but consistent with H1.1.

---

## RQ2 — Are there reproducible patterns (tactics) shared across manufacturers?

**H2.0 (null)**: Each manufacturer's deceptions are idiosyncratic. There are no patterns that recur across ≥3 manufacturers.

**H2.1 (working)**: At least 5 distinct tactics recur across ≥3 manufacturers each, suggesting industry-wide convention rather than manufacturer-specific behavior.

**Evidence we will accept for H2.1**: A tactic taxonomy where ≥5 tactics each have records linking to products from ≥3 distinct manufacturers, with grade ≥B.

**Phase 0 status**: `epa_vs_highway_70mph` already has records on Tesla, Ford, and Rivian (3 manufacturers); other tactics have only 1–2 manufacturers covered. Phase 1 will provide the test.

---

## RQ3 — Is divergence growing or shrinking over time?

**H3.0 (null)**: Year-over-year gaps for the same product (model year as covariate) are random.

**H3.1a (tightening)**: As regulatory scrutiny grows (FTC, NHTSA, CA DMV, EU directives), gaps narrow over time.

**H3.1b (loosening)**: As manufacturer competition intensifies and AI-driven copy generation accelerates, gaps widen over time.

**Evidence**: Longitudinal study (Phase 2) of same products across ≥3 model years. Cannot be addressed in Phase 0/1.

---

## RQ4 — Which tactics are most consumer-harmful?

This is partly normative and partly empirical. We approach it by combining:
- **Decision distortion**: how much does the tactic alter purchase choice? (Estimated via the absolute size of the gap × product-decision criticality of the metric.)
- **Safety implication**: does the tactic correlate with documented incidents (e.g., FSD crashes in NHTSA database)?
- **Regulatory severity**: have authorities ruled against the tactic?

**H4.1 (working ranking, hypothesized)**: From most to least harmful — feature_naming_implies_capability (safety), towing_range_collapse_undisclosed (stranding risk), epa_vs_highway_70mph (decision distortion at scale), peak_dc_charge_sustained_briefly (frustration), starting_at_excludes_mandatory_fees (price clarity).

**Evidence**: Cross-correlation of tactics with NHTSA complaints, regulatory actions (FTC §5 cases, state DMV findings), and consumer survey data (deferred to Phase 3).

---

## RQ5 — Where does enforcement (regulatory or market) succeed or fail?

**Working hypothesis**: Regulatory action follows a long lag relative to first deception observation. Tactics that remain unaddressed for ≥5 years after first independent documentation either (a) are too dispersed to attribute, or (b) lack a coherent enforcement venue.

**Evidence**: Cross-reference each tactic's `first_documented` (in this dataset, anchored to Phase 0 timestamps) against the date of the first known regulatory or judicial action. Compute the lag.

**Phase 0 anchor case**: Tesla "Full Self-Driving" — ~9 years from product launch (2016) to CA DMV deceptive-marketing ruling (Dec 2025). Long lag confirmed in this case; need ≥5 cases to claim a pattern.

---

## Threats to inference

- **Confirmation bias**: We started this project because we expected to find divergence. Mitigation: log and publish records where claim ≈ reality (gap within ±5%) so the dataset is balanced.
- **Sampling bias**: Phase 0 oversamples products with known gaps. Phase 1 will randomize within the top-15 US sales list.
- **Source independence**: Some Tier-2 sources have business relationships with manufacturers (review units, event invitations). Each source receives an `independence_assertion` field in Phase 1.
- **Metric arbitrage**: The set of deception axes we choose may itself be biased toward axes where we expect to find gaps. Mitigation: include all 12 priority axes per product, even when data shows no gap.

---

## Output trajectory

- **Phase 0** (this): exploratory dataset (3 products × 13 records), schema and methodology, public-facing technical writeup.
- **Phase 1** (next 4–8 weeks): 15-product expansion, RQ1 + RQ2 first-pass testing, methodology paper draft.
- **Phase 2** (3–6 months): longitudinal extension, RQ3 testing.
- **Phase 3** (6–12 months): consumer-survey instrument, RQ4 calibration, peer-review submission target.

The consumer-facing website (originally proposed in PLAN.md) is a *secondary* output that is expected to drive (a) data corrections from informed users and (b) press attention that recruits collaborators. It is not the primary research artifact.
