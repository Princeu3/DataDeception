# Email — General Motors (for GMC, 2 records)

**To:** `media@gm.com` (best guess catch-all)
**Backup:** GM Pressroom at https://media.gm.com/ — the site has a Media Contacts directory with named GM Communications staff (look up "Hummer EV" or "EV portfolio" specialist).
**Phone backup:** GMC Customer Assistance / Media line: 1-800-462-8782 (consumer line; may route a media inquiry).

⚠ GM's media routing is heavily centralized through GM Communications, not GMC-brand-specific. Address to GM, mention GMC in the subject.

---

## Subject line

```
Notification: DataDeception v0.1 dataset includes 2 records concerning the GMC Hummer EV
```

## Body

> Dear GM Communications team,
>
> I am an independent researcher writing to notify you that **DataDeception v0.1**, a structured, citation-first dataset documenting where U.S. consumer-EV manufacturer claims diverge from independently-measured reality, was released today and includes **2 records concerning the GMC Hummer EV Pickup (2025, 2X)**. The dataset and accompanying preprint are public:
>
> - GitHub repository: https://github.com/Princeu3/DataDeception
> - arXiv preprint: [arXiv-URL]
>
> Each record carries a verbatim claim quote with archived URL, an independent-measurement citation, an evidence grade (A–D), and an assigned tactic from a 13-tactic taxonomy. The methodology is detailed in §3 of the preprint.
>
> **Records concerning GMC Hummer EV Pickup (2025, 2X):**
>
> 1. `gmc-hummer-ev-pickup-2025-2x__range__highway_70mph` — EPA combined-cycle vs. independent 70 mph measurement gap. The Hummer EV's high curb weight makes the cycle-vs-cruising delta particularly pronounced.
>
> 2. `gmc-hummer-ev-pickup-2025-2x__range__heavy_duty_exemption` — the Hummer EV exceeds the 8500 lb GVWR threshold, which exempts it from the EPA combined-cycle range labeling regime that applies to lighter EVs. Marketing-surface range claims for the Hummer EV therefore do not have the same regulatory grounding as range claims for vehicles like the Bolt EUV. The record framing is informational, not a deceptive-intent finding — but the evidentiary asymmetry between Hummer EV range claims and Bolt EUV range claims is real and material to consumers cross-shopping at the GM dealer level.
>
> Per the methodology in §3.7, **responses received within 30 days of this notification are integrated as additional sources alongside each affected record, not as redactions**. If your team identifies a factual inaccuracy in either record's claim quote, citation, or gap quantification, please reply with:
>
> 1. The record identifier;
> 2. The specific factual element being contested;
> 3. Supporting evidence we should add.
>
> The heavy-duty-exemption record is the one most likely to benefit from a GM response: the regulatory framing is correct as documented, but GM-side context on internal range-test methodology for the Hummer EV (which would not be EPA-mandated, but may exist) would materially strengthen the record's Tier-4 source set.
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

- GM's communications layer is centralized; a single email to `media@gm.com` typically routes to the appropriate brand specialist within 24 business hours.
- Do not also send to GMC-brand customer service — it'll create dueling tickets and delay routing.
- The heavy-duty exemption is a regulatory-architecture finding, not a deceptive-marketing finding. If GM responds with "the EPA exemption is by design," that's a correct response and we add it as a source — it's the right framing for the record.
