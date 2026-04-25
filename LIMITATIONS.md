# Limitations

**Status**: v0.1 — must be re-read before any external claim is made from this dataset.

A research dataset is only as good as its honest accounting of what it can and cannot tell you. This document lists known limitations of DataDeception (Phase 0). New limitations should be added here as they are discovered, and addressed limitations should be marked rather than removed (history matters).

---

## 1. Selection bias (Phase 0)

The three products in Phase 0 (Tesla Model Y 2025 LR AWD, Ford F-150 Lightning 2024 ER, Rivian R1S 2025 Dual Max) were chosen partly because Consumer Reports already documented large claim/reality gaps for two of them. **This dataset, in its current state, cannot be used to claim that EV manufacturers in general systematically deceive.** It can only be used to claim that *these specific products*, on *these specific axes*, exhibit the documented gaps.

Phase 1 will randomize selection across the top-15 US sales list to address this.

---

## 2. Single-unit testing (Tier-2 sources)

Consumer Reports, Edmunds, MotorTrend, and similar testers typically purchase one unit per product and run their tests on that single unit. A single bad (or good) unit can shift the result. Manufacturers also know which units these publishers buy and where they send them; while CR purchases anonymously, this is not a guarantee.

Mitigation: Where possible, we record measurements from ≥2 independent Tier-2 testers. We also record Tier-3 owner-forum corroboration (with N declared) when available.

Live concern: Even with N=2 Tier-2 sources, this is not a randomized large-sample estimate. Population claims (RQ1) require Phase 1+ data.

---

## 3. Software updates change reality

EVs receive frequent OTA updates that can materially change battery management, charging behavior, performance modes, and feature naming. A measurement made today may not reflect the same vehicle six months from now. Tesla in particular has done both upward (more range, better acceleration) and downward (post-purchase range nerfs) revisions via OTA.

Mitigation: Every record has a `last_verified` field. Records older than 12 months should be re-verified before being cited.

Live concern: Phase 0 records are anchored to 2026-04-25. By 2027 several may be stale. Need a verification cadence (Phase 1 deliverable).

---

## 4. Cherry-picking risk in our own writing

We chose `verbatim_quote` snippets from longer source articles. The full article context may include caveats, alternative framings, or methodological disclosures we did not capture. A skeptical reviewer is right to verify against the linked source.

Mitigation: We deliberately keep `verbatim_quote` short and link to the full source. We explicitly recommend reviewers read the source.

Live concern: Until Phase 1 delivers `snapshot_url` for all sources, link rot can hide context. Manufacturer pages especially mutate.

---

## 5. Tactic taxonomy is provisional

The 10 tactics in `data/tactics/` are based on patterns observable in 3 products plus prior reading (the Mrwhosetheboss/MKBHD video, FTC enforcement history, and academic literature on deceptive advertising). We have not validated that this taxonomy is exhaustive or non-overlapping. There may be tactics we are missing that Phase 1 will surface.

Mitigation: Tactics are open to revision. Adding a new tactic requires ≥2 independent products exhibiting the pattern.

Live concern: In Phase 0 we have not yet tested whether two independent annotators converge on the same tactic assignments for the same record. Inter-rater reliability is a Phase 2 deliverable.

---

## 6. Manufacturer perspective is absent

We have not contacted Tesla, Ford, Rivian, or any other manufacturer for response or correction. Their position on the gaps documented here may include factors we have not considered (e.g., test-cycle disclosure obligations, fine-print qualifiers, software-version specifics). A manufacturer reply could legitimately raise grade A records to B or vice versa.

Mitigation: Pre-publication of any external research output, the relevant manufacturer will be contacted with the records that mention them and given ≥30 days to respond. Their response, if any, will be added as an additional source on the affected records.

Live concern: This dataset, in Phase 0 form, is a one-sided account.

---

## 7. Consumer-Reports tested unit ≠ trim documented

CR's R1S test was on a Dual Max trim purchased for $94,550. Our `data/products/rivian-r1s-2025-dual-max.json` record uses CR's price and battery values directly. However, EPA fueleconomy.gov vehicle ID 48433 ("R1S Dual Max (20in)") may differ from CR's tested trim in wheel size or other config. Cross-trim contamination is a known risk.

Mitigation: Phase 1 will require an exact EPA vehicle-ID match between any cited Tier-2 source and our product record. Where mismatches exist, we will document them or split into separate records.

Live concern: One Phase 0 record is affected. Marked.

---

## 8. Bias in source selection

Sources used heavily in Phase 0:
- Consumer Reports (2 records cite directly): independent, credible, but US-only and one-unit.
- EVKX, Recharged: lower-profile but appear independent. Their methodology is described on their own sites, which is what we have to go on.
- Tesla Motors Club forum: high-engagement but Tesla-only owners (N>10 confirmed for the cited charging-curve thread).

We have not used: Out of Spec Reviews (YouTube), Bjørn Nyland (YouTube), TFL Truck (YouTube). These are well-regarded sources we should add in Phase 1 via yt-dlp transcript extraction.

Live concern: Phase 0 over-relies on US-text-publication sources. Adds language and modality bias.

---

## 9. Verbatim quotes from publications behind paywalls

Consumer Reports content is partly subscription-gated. Quotes captured here are from accessible portions or AI-search-result snippets. A skeptical reader without a CR subscription cannot fully verify our quotes against the source.

Mitigation: We attempt to use the publicly indexed portions. Phase 1: where a CR full article is paywalled, we will note this on the record and reduce evidence grade by one tier if no other corroboration exists.

Live concern: Two F-150 Lightning records and three R1S records depend on CR access.

---

## 10. Gap percentages assume the claim's denominator

Where we compute `gap.pct = (reality - claim) / claim × 100`, we are using the manufacturer's claim as the denominator. This is a deliberate choice (it aligns with how a buyer would think about the gap), but readers should know that the same data yields a different percentage under reverse framing.

Live concern: Sign and magnitude conventions must be consistent. They are. But a reader skimming the dataset should understand them.

---

## 11. We are not lawyers

Some records reference legal terms (FTC §5, deceptive advertising, FTC Section 12, Lanham Act, California Vehicle Code §11713, EPA test cycle 40 CFR 600). These are cited for context. We have not had any of this dataset reviewed by counsel. Before using DataDeception in any legal proceeding or formal regulatory submission, the user must consult qualified legal counsel.

Live concern: Critical for any consumer-facing site language. Plan to obtain a legal review before launch.

---

## 12. The set of axes is incomplete

We chose 12 priority sub-axes. Others not yet covered: battery degradation curves (year 5, year 10), warranty exclusion fine print, real cost of ownership over 5/10 years, software subscription drift over time, repairability scores, parts availability, dealer-network quality. Each could be a meaningful deception axis we are currently silent on.

Live concern: Absence of evidence is not evidence of absence. We should be explicit about scope when communicating findings.
