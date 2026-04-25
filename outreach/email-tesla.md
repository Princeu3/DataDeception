# Email — Tesla (8 records)

⚠ **Tesla dissolved its U.S. press team in 2020.** No public press email is reliably routed. Recommended path on launch day:

1. **Web contact form**: https://www.tesla.com/contact → Vehicle Safety. Paste the body below.
2. **X mention**: Quote-tweet your launch Tweet 1 mentioning `@TeslaSafety` with "Notification of records filed via safety contact form" and the GitHub URL.
3. **NHTSA copy** (FSD record only): forward via https://www.nhtsa.gov/contact-nhtsa Office of Defects Investigation, referencing NHTSA's existing 2.88M-vehicle FSD investigation.

Best-guess email if you want to also try direct: `vehiclesafetycontact@tesla.com` (historically present in NHTSA filings; live status unverified).

---

## Subject line

```
Notification: DataDeception v0.1 dataset includes 8 records concerning Tesla vehicles
```

## Body

> Dear Tesla Communications team,
>
> I am an independent researcher writing to notify you that **DataDeception v0.1**, a structured, citation-first dataset documenting where U.S. consumer-EV manufacturer claims diverge from independently-measured reality, was released today and includes **8 records concerning Tesla vehicles**. The dataset and accompanying preprint are public:
>
> - GitHub repository: https://github.com/Princeu3/DataDeception
> - arXiv preprint: [arXiv-URL]
>
> Each record carries a verbatim claim quote with archived URL, an independent-measurement citation (Tier-1 regulatory or Tier-2 independent test), an evidence grade (A–D), and an assigned tactic from a 13-tactic taxonomy. The methodology is detailed in §3 of the preprint.
>
> **Records concerning Tesla vehicles:**
>
> 1. `tesla-cybertruck-2025-awd__range__highway_70mph` — EPA combined-cycle 318 mi vs. MotorTrend instrumented test at 70 mph 224 mi (−30% gap). Source: MotorTrend, 2024 Tesla Cybertruck Dual Motor Real-World Range Test. Largest documented gap in v0.1.
>
> 2. `tesla-cybertruck-2025-awd__announcement_promise__500_mi_unfulfilled` — November 2019 announcement promised 500-mi range trim. Range Extender accessory (\$16,000) cancelled May 2025 with full refunds; never delivered. Source: InsideEVs, May 2025.
>
> 3. `tesla-model-y-2025-long-range-awd__range__highway_70mph` — EPA combined-cycle vs. independent 70 mph measurement gap.
>
> 4. `tesla-model-y-2025-long-range-awd__charging__peak_dc_sustained_duration` — peak DC charge rate marketing vs. sustained-duration independent measurement (EVKX charging-curve data).
>
> 5. `tesla-model-y-2025-long-range-awd__performance__zero_to_60_rollout` — 0–60 mph marketing figure does not subtract the conventional 1-foot rollout that EPA-instrumented testing applies. Source: Car and Driver instrumented testing.
>
> 6. `tesla-model-y-2025-long-range-awd__pricing__starting_at_destination` — "starting at" price excludes mandatory destination/delivery fee.
>
> 7. `tesla-model-y-2025-long-range-awd__software_features__fsd_naming` — "Full Self-Driving" categorical naming overclaim. California Administrative Law Judge ruling December 2025: name is "unambiguously false and counterfactual." NHTSA October 2025 investigation: 2.88M vehicles, 14 crashes, 23 injuries. Severity grade: critical.
>
> 8. `tesla-model-3-2025-long-range-awd__range__highway_70mph` — EPA combined-cycle vs. independent 70 mph measurement gap.
>
> Per the methodology stated in §3.7 of the paper, **responses received within 30 days of this notification are integrated as additional sources alongside each affected record, not as redactions**. The audit trail is preserved in the public Git history. If your team identifies a factual inaccuracy in any record's claim quote, citation, or gap quantification, please reply with:
>
> 1. The record identifier (filename in the format shown above);
> 2. The specific factual element being contested;
> 3. Supporting evidence (citation, archived URL, or measurement reference) we should add as a Tier-1 or Tier-4 source.
>
> The dataset is released under MIT (code) and CC-BY-4.0 (data).
>
> Thank you for your time.
>
> Sincerely,
>
> Prince Upadhyay
> Independent Researcher
> princeupadhyay1401@gmail.com
> https://github.com/Princeu3/DataDeception

---

## Notes

- If submitting via web form (recommended), the form has a 4000-char limit on most categories — the body above is ~2200 chars, well within limit.
- The X mention should be one of your launch-day tweets, not a separate post — keeps the timeline coherent.
- Do NOT post the form-submission confirmation number publicly. Log it in `outreach/sent-log.md` only.
