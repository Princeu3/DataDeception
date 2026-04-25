# Related-Work Audit — Top 20 Papers and What They Teach Us

**Date**: 2026-04-25
**Method**: Parallel arXiv searches (via blazickjp/arxiv-mcp-server) + Exa supplements across 8 search dimensions. Selected papers ranked by citation count where known, recency for newer work, and direct methodological proximity to DataDeception.

---

## The 20 papers, by tier of relevance

### Tier 1 — Direct methodological predecessors (must-cite)

| # | Paper | Year | Cites | Why we must engage with it |
|---|---|---|---|---|
| 1 | **Mathur, Acar, Friedman et al. — "Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites"** [arXiv:1907.07032] | 2019 | 258+ on Semantic Scholar; 454+ on Google Scholar | Closest analog to ours: empirical taxonomy + cross-product audit + policy framing. They studied 11K websites for UI dark patterns; we study 13 EVs for spec-claim deception. Same methodology shape. |
| 2 | **Mathur, Kshirsagar, Mayer — "What Makes a Dark Pattern... Dark? Design Attributes, Normative Considerations, and Measurement Methods"** | 2021 | 454+ | Definitional framework for what counts as a "dark pattern". We need an analogous framing for what counts as "claim/reality divergence". |
| 3 | **Gray, Kou, Battles et al. — "The Dark (Patterns) Side of UX Design"** | 2018 | 657+ | Most-cited paper in the deceptive-design literature. Defined the original 5 high-level pattern families (nagging, obstruction, sneaking, interface interference, forced action). Direct precedent for our 5-family tactic taxonomy. |
| 4 | **Luguri & Strahilevitz — "Shining a Light on Dark Patterns"** | 2020 | 260+ | Empirical + legal framing; runs randomized experiments on dark patterns in commerce. Connects our work to the legal tradition (FTC §5, UDAP statutes). |
| 5 | **Gebru, Morgenstern, Vecchione, Wallach et al. — "Datasheets for Datasets"** [arXiv:1803.09010, CACM 2021] | 2018/2021 | 5,000+ on Google Scholar; 496+ on ACM | Foundational dataset-documentation framework. Our methodology paper should adopt Gebru's lifecycle structure (Motivation, Composition, Collection, Preprocessing, Uses, Distribution, Maintenance). We are essentially writing "a datasheet for a deception dataset". |

### Tier 2 — Adjacent methodology / accountability / dataset framing (should-cite)

| # | Paper | Year | Why relevant |
|---|---|---|---|
| 6 | **Mitchell, Wu, Zaldivar et al. — "Model Cards for Model Reporting"** [arXiv:1810.03993] | 2018 | Companion to Gebru. Formalizes per-artifact reporting. Justifies our per-product JSON schema. |
| 7 | **Pushkarna, Zaldivar, Kjartansson — "Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI"** | 2022 | Refines Gebru's framework with an emphasis on stakeholder needs. Relevant for our consumer-facing surface vs. researcher-facing dataset distinction. |
| 8 | **Raji, Smart, White, Mitchell et al. — "Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing"** [arXiv:2001.00973] | 2020 | Audit framework. Our evidence-grade rubric is an internal-audit instrument. |
| 9 | **Costanza-Chock, Raji, Buolamwini — "Who Audits the Auditors?"** [arXiv:2310.02521] | 2023 | Field scan of the algorithmic-audit ecosystem. Our work is an audit; this paper situates it. |
| 10 | **Birhane, Steed, Ojewale et al. — "Towards AI Accountability Infrastructure: Gaps and Opportunities in AI Audit Tooling"** [arXiv:2402.17861] | 2024 | Recent audit-tooling survey. Our schema + validators are tooling contributions. |

### Tier 3 — Recent deceptive-pattern detection and AI-era extensions

| # | Paper | Year | Why relevant |
|---|---|---|---|
| 11 | **"50 Shades of Deceptive Patterns: A Unified Taxonomy, Multimodal Detection, and Security Implications"** [arXiv:2501.13351] | 2025 | Most recent unified taxonomy work; merges multiple prior taxonomies. We should align our family-naming with this where possible. |
| 12 | **"Emergent Dark Patterns in AI-Generated User Interfaces"** [arXiv:2602.18445] | 2026 | Very recent. Documents how AI generation produces dark patterns automatically. Suggests our methodology will be needed in AI-generated marketing copy too. |
| 13 | **"Deception by Design: A Temporal Dark Patterns Audit of McDonald's Self-Ordering Kiosks"** [arXiv:2603.03218] | 2026 | Recent applied audit of a single product over time. Methodologically similar to what our Phase 2 longitudinal work would look like. |
| 14 | **"Dark Patterns in the Interaction with Cookie Banners"** [arXiv:2103.14956] | 2021 | Single-domain (cookie-banners) audit. Demonstrates that targeted vertical audits can be high-impact. |

### Tier 4 — Fact-checking / claim-verification methodology (we already cite Pennycook & Rand)

| # | Paper | Year | Why relevant |
|---|---|---|---|
| 15 | **Pennycook & Rand — "Online misinformation warning labels work despite distrust of fact-checkers"** [Nature Human Behaviour] | 2024 | Already cited. Establishes that warning labels reduce belief and sharing. |
| 16 | **"HoVer: A Dataset for Many-Hop Fact Extraction And Claim Verification"** [arXiv:2011.03088] | 2020 | Methodologically close: structured claim-verification dataset. |
| 17 | **"SciClaimHunt: A Large Dataset for Evidence-based Scientific Claim Verification"** [arXiv:2502.10003] | 2025 | Recent. Evidence-grading approach analogous to our A/B/C/D rubric. |
| 18 | **CheckThat! Lab series (CLEF 2020–2026)** [arXiv:2007.07997, 2503.14828, 2602.09516] | 2020–2026 | Establishes a shared-task framework for claim verification. Justifies our schema as a CheckThat-compatible artifact. |

### Tier 5 — Adjacent regulatory / policy framing

| # | Paper | Year | Why relevant |
|---|---|---|---|
| 19 | **"Online Behavioral Advertising: A Literature Review and Research Agenda"** [arXiv:2511.01895] | 2025 | Recent literature review of advertising-related research agenda. Helps situate our consumer-protection framing. |
| 20 | **"The Perfect Match? A Closer Look at the Relationship between EU Consumer Law and..."** [arXiv:2510.13466] | 2025 | EU consumer law framing — relevant since EU consumer-protection statutes are stricter than US for some claims (UCPD). |

---

## What the closest prior work teaches us about structure

I extracted the section headings from the three most-relevant papers (Mathur 2019, Gebru 2018, "50 Shades" 2025).

### Mathur 2019 — section flow
```
1 Introduction
2 Related Work
   2.1 Online Shopping and Influencing User Behavior
   2.2 Dark Patterns in User Interface Design
   2.3 Comparison to Prior Work    ← we don't have this
3 A Taxonomy of Dark Pattern Characteristics
4 Method
   4.1 Creating a Corpus of Shopping Websites
   4.2 Data Collection with a Website Crawl
   4.3 Data Analysis with Clustering
   4.4 Detecting Deceptive Dark Patterns
5 Findings
   5.1 Categories of Dark Patterns
   5.2 [Case Study]                 ← strong move; we should add Tesla Cybertruck or FSD as our case study
6 Discussion
   6.1 Dark Patterns and Implications For Consumers
   6.2 Implications for Consumer Protection Policy and Retailers   ← we don't have this
   6.3 Dark Patterns and Future Studies At Scale
```

### Gebru 2018 — section flow (lifecycle-driven)
```
1 Introduction
   1.1 Objectives
2 Development Process
3 Questions and Workflow
   3.1 Motivation
   3.2 Composition
   3.3 Collection Process
   3.4 Preprocessing/cleaning/labeling
   3.5 Uses
   3.6 Distribution
   3.7 Maintenance
4 Impact and Challenges
```

The Gebru lifecycle (Motivation → Composition → Collection → Preprocessing → Uses → Distribution → Maintenance) is **the implicit standard for dataset papers in cs.LG / cs.CY**. Reviewers expect to see something resembling it.

---

## What works in these papers (writing-craft synthesis)

### 1. The "we are not the first, but we are the first to..." move
Mathur §2.3 ("Comparison to Prior Work") explicitly differentiates from each predecessor in 1-2 sentences. They open with a table (or paragraph) that says: "Prior work X did A. Prior work Y did B. We do C, which neither did." This is ruthlessly efficient. **Our paper does not do this — we should add it.**

### 2. Concrete case study inside Findings
Mathur §5.2 picks ONE pattern (third-party social-proof providers) and goes deep. This is more memorable than the aggregate findings. **Our paper has Tesla Cybertruck and Tesla FSD as candidates — we should formalize one as a §5.X case study.**

### 3. Policy implications as a separate subsection
Mathur §6.2 dedicates a subsection to "Implications for Consumer Protection Policy and Retailers". This is what makes the work matter outside academia. **Our Limitations section is fine, but we lack a dedicated Implications subsection.**

### 4. Lifecycle framing borrowed from Gebru
Gebru's §3 (Questions and Workflow) reframes the "method" section as a lifecycle of stages. **Our Methodology section could be reorganized along Gebru's lifecycle to align with reviewer expectations.**

### 5. Open development process and reproducibility
Both Mathur and Gebru explicitly describe their development process (§2 in both cases) and tools released. **Our Reproducibility statement covers this, but we could spend a paragraph on it earlier in the paper (in §3).**

### 6. Numerical anchoring in the abstract
Mathur abstract has "11K websites, ~53K product pages, 1,818 dark pattern instances, 15 types, 7 categories". **Our abstract has "13 products × 28 records × 13 tactics" — solid, but we could add the cross-manufacturer count "across 8 manufacturers, mean gap −15%".**

### 7. Open-source artifact links in the abstract
Both Gebru and Mathur explicitly mention they release code/data in the abstract. **Our abstract does say "released under MIT (code) and CC-BY-4.0 (data)" — good.**

---

## Specific concrete recommendations for our v5 paper

Based on the audit, here are 8 concrete edits I'd make:

| # | Where | What | Estimated time |
|---|---|---|---|
| 1 | §2 Related Work | Add subsection §2.4 "Comparison to Prior Work" with 5–6 sentences differentiating from Mathur 2019, Gebru 2018, Mathur 2021, Pennycook & Rand. | 30 min |
| 2 | §1 Intro | Add 1 sentence in the "three contributions" para citing Gebru/Mathur as foundations we build on. | 5 min |
| 3 | §2 Related Work | Add 6 new citations across all 5 tiers: Gray 2018, Mathur 2021, Luguri 2020, Gebru 2018, Mitchell 2018, "50 Shades" 2025. | 30 min |
| 4 | §3 Methodology | Reorganize to align with Gebru's lifecycle: Motivation → Source Taxonomy (Composition) → Evidence Rubric (Collection criteria) → Gap Formalism (Preprocessing) → Uses → Distribution → Maintenance. | 45 min |
| 5 | §5 Findings | Promote Tesla Cybertruck OR Tesla FSD to a §5.6 "Case Study" subsection with deeper narrative. | 20 min |
| 6 | §5 Findings | Add §5.7 "Implications for Consumer Protection Policy". | 30 min |
| 7 | Abstract | Add "across 8 manufacturers" to the numerical anchoring. | 2 min |
| 8 | references.bib | Add ~10 new bib entries for the new citations. | 30 min |

**Total time**: ~3 hours. This would bring our paper from ~22 citations → ~32 citations and substantially improve its positioning relative to the closest prior work.

---

## What we should NOT change

After this audit, I think we should **keep** these aspects of our paper as-is because they differentiate us from the prior work:

- **Per-record JSON schema** + validation tooling — Mathur 2019 and Gebru 2018 don't have this. It's a methodological contribution we should keep prominent.
- **Tactic taxonomy as a 2D card grid figure** — none of the prior taxonomy papers visualize their taxonomy this clearly. It's a small visual contribution.
- **Severity scale** for non-numeric gaps — novel; Mathur uses categorical patterns but doesn't apply a severity-of-harm gradient.
- **Counter-examples** explicitly included — Mathur 2019 does not include "honest" websites for confirmation-bias mitigation. We do (Mercedes EQS, Mach-E).
- **Tier-1 NHTSA recall integration** — single-vertical specific but a strong signal of methodology that can pull from regulatory open data.

---

## Open question for the next session

Should we drill deeper into any specific paper? My priorities, in order:

1. **Mathur 2019 §3 "Taxonomy of Dark Pattern Characteristics"** — read the actual taxonomy details and compare to ours. May surface gaps in our 5-family structure.
2. **Gebru §3.1 "Motivation" questions** — apply each to our dataset and add a `MOTIVATION.md` if any aren't already covered.
3. **"50 Shades" 2025 multimodal detection method** — maybe useful for Phase 2 if we add automated detection.

Let me know which (if any) to drill into next.
