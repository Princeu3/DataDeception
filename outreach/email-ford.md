# Email — Ford (5 records)

**To:** `media@ford.com` (confirmed in Ford Media Center)
**CC:** `usmedia@ford.com` (alternate North America media inbox)

---

## Subject line

```
Notification: DataDeception v0.1 dataset includes 5 records concerning Ford vehicles
```

## Body

> Dear Ford Media Relations team,
>
> I am an independent researcher writing to notify you that **DataDeception v0.1**, a structured, citation-first dataset documenting where U.S. consumer-EV manufacturer claims diverge from independently-measured reality, was released today and includes **5 records concerning Ford vehicles**. The dataset and accompanying preprint are public:
>
> - GitHub repository: https://github.com/Princeu3/DataDeception
> - arXiv preprint: [arXiv-URL]
>
> Each record carries a verbatim claim quote with archived URL, an independent-measurement citation, an evidence grade (A–D), and an assigned tactic from a 13-tactic taxonomy. The methodology is detailed in §3 of the preprint.
>
> **Records concerning Ford vehicles:**
>
> 1. `ford-f-150-lightning-2024-extended-range__range__highway_70mph` — EPA combined-cycle 320 mi vs. Consumer Reports measurement at 70 mph 270 mi. Source: Consumer Reports 2024 Road Test Report.
>
> 2. `ford-f-150-lightning-2024-extended-range__range__towing_50pct_loss` — towing-mode range collapse (~50% reduction); record carries a stranding-risk severity classification per §3.4 because towing-range disclosure does not appear adjacent to range marketing.  Sources: Recharged towing review, MotorTrend / Automobile towing test (Tingwall).
>
> 3. `ford-f-150-lightning-2024-extended-range__charging__peak_dc_low_for_battery` — peak DC charge rate appears below the industry expectation for the battery size; documented via independent fast-charging tests.
>
> 4. `ford-f-150-lightning-2024-extended-range__production_status__2025_discontinued` — silent-discontinuation tactic (2024 model year was the last; consumer-facing surfaces did not flag end-of-life).
>
> 5. `ford-mustang-mach-e-2025-awd-extended__range__highway_70mph` — **counter-example**: independent measurement matches EPA combined cycle. Included by design; no contested gap.
>
> Per the methodology in §3.7 of the paper, **responses received within 30 days of this notification are integrated as additional sources alongside each affected record, not as redactions**. The audit trail is preserved in the public Git history. If your team identifies a factual inaccuracy in any record's claim quote, citation, or gap quantification, please reply with:
>
> 1. The record identifier;
> 2. The specific factual element being contested;
> 3. Supporting evidence we should add.
>
> Note that the Mach-E counter-example is a positive finding — if Ford has additional measurements that would shift any record (in either direction), those are equally welcome.
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

- Ford has been historically responsive to fact-check requests routed through `media@ford.com`. Realistic to expect a same-week reply.
- Lead with the Mach-E counter-example in any follow-up — it shows the dataset isn't anti-Ford and primes a constructive engagement.
- If a Ford rep asks for a specific point of contact at GitHub, point them to the Issues tab of the repo.
