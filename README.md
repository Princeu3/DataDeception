# DataDeception

A structured, citation-first dataset comparing what electric-vehicle manufacturers advertise against what independent measurement reveals. Designed as the foundation for a research paper on systematic claim/reality divergence in the US EV market, with a consumer-facing surface as a secondary output.

**Status (v0.1, 2026-04-25)**: 13 products · 28 deception records · 13 tactic patterns · all schema-validated. NHTSA recall data integrated as Tier-1 evidence. See [`CONSUMER_REPORT.md`](CONSUMER_REPORT.md) for the buyer-facing summary.

---

## What this is

Most claim-vs-reality projects in the EV space focus on individual products in isolation (one YouTube video, one consumer review). DataDeception is a structured database that:

- Treats each product as a tuple of `(manufacturer, model, model_year, trim)` with stable identifiers
- Documents *every* relevant deception axis with manufacturer claim, independent measurement, and citations on both sides
- Tags each record with a **tactic** — a repeatable pattern shared across products and manufacturers — so the data supports cross-cutting analysis
- Carries an **evidence grade** (A–D) per record, with a documented rubric in [`METHODOLOGY.md`](METHODOLOGY.md)
- Includes deliberate **counter-examples** (Mercedes EQS beats EPA, Ford Mach-E matches EPA) to mitigate confirmation bias
- Validates against JSON Schema 2020-12 with referential-integrity and ID-convention checks

The dataset and methodology are designed to support a research paper. The consumer-facing report is auto-generated from the same JSON.

## Structure

```
DataDeception/
├── README.md                    # this file
├── PLAN.md                      # what we're building, scope, schema rationale
├── METHODOLOGY.md               # how data is collected, source taxonomy, evidence rubric
├── RESEARCH_QUESTIONS.md        # RQs and hypotheses for paper
├── LIMITATIONS.md               # honest threats-to-validity inventory
├── CONSUMER_REPORT.md           # auto-generated buyer-facing summary
├── LICENSE                      # MIT (code) + CC-BY-4.0 (data)
├── validate.py                  # schema + integrity validator
├── generate_report.py           # regenerates CONSUMER_REPORT.md from data/
├── schema/                      # JSON Schema 2020-12
│   ├── product.schema.json
│   ├── deception.schema.json
│   ├── tactic.schema.json
│   └── source.schema.json
└── data/
    ├── products/                # one JSON per (manufacturer, model, year, trim)
    ├── deceptions/              # one JSON per (product, axis, sub_axis) record
    └── tactics/                 # repeatable deception patterns
```

## Reproducibility

```bash
python3 -m venv .venv
.venv/bin/pip install jsonschema referencing
.venv/bin/python validate.py        # schema + integrity check
.venv/bin/python generate_report.py # regenerate CONSUMER_REPORT.md
```

Validation must pass before any release. Tier-1 sources (EPA fueleconomy.gov, NHTSA recalls.gov) can be re-fetched via the API endpoints documented in METHODOLOGY.md §2.

## Source taxonomy (TL;DR — full version in METHODOLOGY.md)

- **Tier 1** — regulatory / open government (EPA, NHTSA, court rulings, FTC orders)
- **Tier 2** — independent measurement (Consumer Reports, MotorTrend, Edmunds, InsideEVs, Recharged, Out of Spec, Bjørn Nyland)
- **Tier 3** — community / forum (vehicle owner forums, Reddit threads with N≥10 corroborating reports)
- **Tier 4** — manufacturer / brand (treated as the *claim*, not the truth)

## Headline findings (preliminary, from current dataset)

1. **EPA combined-cycle range systematically overstates real-world highway range** across the US EV market. Mean gap on documented products: roughly −15%, with dispersion that includes both negative and positive cases (Mercedes EQS, Ford Mach-E both match or beat EPA in independent tests).
2. **Towing collapses range 50–70%** on EV trucks. Capacity and EPA range are advertised together; only one applies at a time.
3. **Peak DC charging numbers are sustained for ~6 minutes**, not the duration of a road-trip charge.
4. **First-year recall density varies enormously**: Rivian R1S 9, Hyundai Ioniq 5 8, Lucid Air 5 vs. multiple competitors at 0.
5. **"Full Self-Driving" was ruled "unambiguously false and counterfactual"** by a California administrative law judge in December 2025; NHTSA links it to 14 crashes.
6. **The Cybertruck is the largest documented announcement-to-delivery gap** (500 mi promised → 320 delivered; Range Extender accessory cancelled May 2025).

These are preliminary results from a non-randomized sample of 13 products. See [LIMITATIONS.md](LIMITATIONS.md) before drawing population-level conclusions.

## How to cite

If this dataset informs your work, please cite it:

```bibtex
@misc{datadeception2026,
  author       = {Prince Upadhyay},
  title        = {DataDeception: A Structured Dataset of Manufacturer-Claim
                  vs. Independent-Measurement Divergence in US Electric Vehicles},
  year         = {2026},
  howpublished = {\url{https://github.com/Princeu3/DataDeception}},
  note         = {Version 0.1, 13 products / 28 records, CC BY 4.0}
}
```

For consumer-facing references, link to [`CONSUMER_REPORT.md`](CONSUMER_REPORT.md) directly.

## Contributing / corrections

Manufacturers, journalists, or researchers who find errors should open a GitHub issue with:
- The deception record `id` in question
- The specific claim or value to correct
- A citable source for the correction

Per LIMITATIONS.md §6, any manufacturer mentioned in the dataset is invited to submit a structured response that will be added as an additional source on the relevant records.

## License

- **Code** (`validate.py`, `generate_report.py`, `schema/*.json`) — MIT
- **Data and research writing** — CC BY 4.0 with attribution
- **Verbatim third-party quotes** embedded in records — fair-use for research/commentary; underlying copyright remains with original authors

See [LICENSE](LICENSE) for full text.

## Disclaimer

DataDeception is a research project. Records use the term *divergence* or *gap* by default; *deceptive* is used only where a regulator or court has so ruled. No content here constitutes legal advice. Manufacturer trademarks are referenced solely to identify products under analysis.
