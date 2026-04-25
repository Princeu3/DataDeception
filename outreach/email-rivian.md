# Email — Rivian (5 records)

**To:** `press@rivian.com` (best guess based on industry convention; verify before launch)
**Backup channels:**
- `media@rivian.com` (alternate guess)
- Newsroom contact form at https://rivian.com/newsroom
- LinkedIn: Tanya Miller, Senior Communications Manager (search-result confirmed)

⚠ Rivian email format per RocketReach is `[first_initial][last]@rivian.com`, so `tmiller@rivian.com` would be a direct route to Tanya Miller if no general PR email responds.

---

## Subject line

```
Notification: DataDeception v0.1 dataset includes 5 records concerning Rivian R1S
```

## Body

> Dear Rivian Communications team,
>
> I am an independent researcher writing to notify you that **DataDeception v0.1**, a structured, citation-first dataset documenting where U.S. consumer-EV manufacturer claims diverge from independently-measured reality, was released today and includes **5 records concerning the Rivian R1S 2025 (Dual Max)**. The dataset and accompanying preprint are public:
>
> - GitHub repository: https://github.com/Princeu3/DataDeception
> - arXiv preprint: [arXiv-URL]
>
> Each record carries a verbatim claim quote with archived URL, an independent-measurement citation, an evidence grade (A–D), and an assigned tactic from a 13-tactic taxonomy. The methodology is detailed in §3 of the preprint.
>
> **Records concerning Rivian R1S 2025 (Dual Max):**
>
> 1. `rivian-r1s-2025-dual-max__range__highway_70mph` — EPA 410 mi (Dual Max) vs. Consumer Reports measurement at 70 mph 358 mi. Source: Consumer Reports 2025 Road Test Report.
>
> 2. `rivian-r1s-2025-dual-max__build_warranty__nhtsa_recall_density` — 9 NHTSA recalls in MY 2025 — highest in the v0.1 corpus. Source: NHTSA recallsByVehicle API. The record's narrative discusses the asymmetry between brand-quality marketing language and first-year defect-discovery rate.
>
> 3. `rivian-r1s-2025-dual-max__charging__peak_dc_unrealistic` — peak DC charge rate marketing vs. sustained-duration measurement.
>
> 4. `rivian-r1s-2025-dual-max__charging__level2_15_hours` — Level-2 home charging time disclosure (~15 hours for full charge); typical owner expectation set by OEM marketing materials does not match this duration.
>
> 5. `rivian-r1s-2025-dual-max__ui_ergonomics__touchscreen_distraction` — touchscreen-only placement of basic vehicle controls; severity classification follows the IIHS / Consumer Reports critique of touchscreen-dependency in driving controls.
>
> Per the methodology in §3.7, **responses received within 30 days of this notification are integrated as additional sources alongside each affected record, not as redactions**. The audit trail is preserved in the public Git history. If your team identifies a factual inaccuracy, please reply with:
>
> 1. The record identifier;
> 2. The specific factual element being contested;
> 3. Supporting evidence we should add.
>
> The recall-density record is particularly worth a Rivian response: the underlying NHTSA data is public regulatory record, but Rivian-side context on root-cause classification and remediation status would materially improve the record. We'd integrate that as an additional Tier-1 source.
>
> Released under MIT (code) and CC-BY-4.0 (data).
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

- Rivian's PR is small and accessible compared to legacy OEMs. Direct LinkedIn DM to Tanya Miller is a reasonable backup if email bounces.
- The recall-density record is the most likely to draw a substantive reply — Rivian has been transparent about the recall pattern, and an integrated response strengthens the record without weakening the dataset.
