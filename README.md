# DataDeception

A structured, citation-first dataset comparing what electric-vehicle manufacturers advertise against what independent measurement reveals. Designed as the foundation for a research paper on systematic claim/reality divergence in the US EV market, with a consumer-facing surface as a secondary output.

**Status (v0.1, 2026-04-25)**: 13 products · 28 deception records · 13 tactics across 5 families · 8 manufacturers · all schema-validated. NHTSA recall data integrated as Tier-1 evidence. Companion preprint: 13 pages, 23 citations, 7 figures (`paper/main.pdf`). See [`CONSUMER_REPORT.md`](CONSUMER_REPORT.md) for the buyer-facing summary; [`paper/main.pdf`](paper/main.pdf) for the methodology paper.

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
├── LAUNCH_CHECKLIST.md          # T+0 launch sequence, manifests publication protocol
├── LICENSE                      # MIT (code) + CC-BY-4.0 (data)
├── validate.py                  # schema + integrity validator
├── generate_report.py           # regenerates CONSUMER_REPORT.md from data/
├── schema/                      # JSON Schema 2020-12
│   ├── product.schema.json
│   ├── deception.schema.json
│   ├── tactic.schema.json
│   └── source.schema.json
├── data/
│   ├── products/                # one JSON per (manufacturer, model, year, trim)
│   ├── deceptions/              # one JSON per (product, axis, sub_axis) record
│   └── tactics/                 # repeatable deception patterns
├── paper/
│   ├── main.tex                 # 13-page preprint (kourgeorge arxiv-style)
│   ├── references.bib           # 23 citations (Gebru, Mathur, Gray, Luguri, etc.)
│   ├── figures/                 # 7 figures: 5 auto-generated from JSON, 2 hand-TikZ
│   ├── build.sh                 # local 3-pass pdflatex+bibtex build
│   └── main.pdf                 # built artifact (also in CI workflow output)
└── outreach/                    # per-manufacturer notification drafts
    ├── EMAIL_TEMPLATE.md        # master template + per-company appendix
    ├── CONTACTS.md              # address verification protocol
    └── email-{tesla,ford,...}.md # 8 ready-to-send drafts (1 per manufacturer in v0.1)
└── social/
    └── LAUNCH_POSTS.md          # Twitter thread + LinkedIn + Reddit copy
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

1. **The same `epa_vs_highway_70mph` gap recurs across 8 manufacturers** (Tesla, Ford, Rivian, Hyundai, Lucid, Mercedes, GMC, VW) including counter-examples in both directions. Mean gap: −15%; range −30% to +3%. The cross-cutting structure is evidence of regulatory test-cycle dominance, not coordinated marketing intent — the appropriate intervention is at the disclosure layer (a supplemental 70 mph rating on the Monroney label) rather than the deceptive-intent layer.
2. **The Cybertruck is the largest documented gap.** Advertised 318 mi → MotorTrend instrumented 224 mi at 70 mph (−30%). The Range Extender accessory promised at the 2019 announcement to bridge the 500 mi gap was officially cancelled May 2025 with full refunds, never delivered to a single customer. Six years of receipts.
3. **The Mercedes EQS is the largest counter-example.** 350 mi EPA → Edmunds-loop measured 422 mi (+72 mi over). Counter-examples are real and they're in the dataset by design — confirmation-bias mitigation.
4. **First-year recall density varies enormously**: Rivian R1S 2025 (9 recalls), Hyundai Ioniq 5 2025 (8, including two separate high-voltage traction-battery campaigns), Lucid Air 2025 (5) vs. multiple competitors at 0. Brand quality marketing language does not, in general, reflect this variance.
5. **Towing collapses range 50–70%** on EV trucks. Capacity and EPA range are advertised together; only one applies at a time. The F-150 Lightning towing record carries stranding-risk severity.
6. **"Full Self-Driving" was ruled "unambiguously false and counterfactual"** by a California Administrative Law Judge in December 2025; NHTSA's October 2025 investigation covers 2.88M vehicles, 14 crashes, 23 injuries. Severity grade: critical.

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

## Paper

The companion preprint is in [`paper/`](paper/) — a 13-page methodology-and-findings writeup. Section structure follows Gebru et al.'s datasheet lifecycle (Motivation, Composition, Collection, Preprocessing, Uses, Distribution, Maintenance) and builds on Mathur et al.'s "Dark Patterns at Scale" empirical-taxonomy approach. Includes a Cybertruck longitudinal case study (§5.6), three policy-implications proposals (§5.7), and a "Comparison to Prior Work" subsection (§2.4) differentiating from Mathur 2019, Gebru 2018, Mathur 2021, Pennycook & Rand, and Luguri & Strahilevitz.

LaTeX source compiles via the GitHub Actions workflow at [`.github/workflows/paper.yml`](.github/workflows/paper.yml) — every push that touches `paper/` or `data/` rebuilds. The PDF is available as a workflow artifact on the [Actions tab](../../actions).

To build locally:

```bash
# Option A — Docker (no host LaTeX install needed):
cd paper && docker run --rm -v "$PWD":/work -w /work texlive/texlive:latest \
  bash -c "pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex"

# Option B — host TeX Live / BasicTeX with pdflatex + bibtex on PATH:
cd paper && ./build.sh
```

The figure-generation pipeline (`paper/figures/generate.py`) reads the JSON dataset directly, so figures stay in sync with the data automatically. Hand-written diagrams (methodology flowchart, tactic taxonomy card grid) are in TikZ and live alongside the auto-generated ones.

## Manufacturer notification protocol

Per §3.7 of the paper, manufacturers represented in v0.1 receive a notification email concurrent with public release listing the specific records that pertain to their products. Responses received within a 30-day post-publication window are integrated as additional sources alongside each affected record, not as redactions; the audit trail is preserved in the public Git history.

Per-company drafts are in [`outreach/`](outreach/). The launch sequence (repo public → arXiv → notification emails → social distribution → 30-day monitoring) is documented in [`LAUNCH_CHECKLIST.md`](LAUNCH_CHECKLIST.md).

## License

- **Code** (`validate.py`, `generate_report.py`, `schema/*.json`) — MIT
- **Data and research writing** — CC BY 4.0 with attribution
- **Verbatim third-party quotes** embedded in records — fair-use for research/commentary; underlying copyright remains with original authors

See [LICENSE](LICENSE) for full text.

## Disclaimer

DataDeception is a research project. Records use the term *divergence* or *gap* by default; *deceptive* is used only where a regulator or court has so ruled. No content here constitutes legal advice. Manufacturer trademarks are referenced solely to identify products under analysis.
