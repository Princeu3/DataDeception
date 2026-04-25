# Manufacturer notification template — DataDeception v0.1

Use this template for the concurrent-with-publication notification protocol described in §3.7 of the paper. Send on launch day, after the GitHub repo is public and after the arXiv submission has an assigned ID.

**Send-from address:** `princeupadhyay1401@gmail.com`
**Subject line:** `Notification: DataDeception v0.1 dataset includes records for [Company Name]`
**Send-as:** plain text, no attachments. Include arXiv URL and GitHub URL as links.

---

## Email body (template)

> Dear [Company Name] Communications team,
>
> I am an independent researcher writing to notify you that **DataDeception v0.1**, a structured, citation-first dataset documenting where U.S. consumer-EV manufacturer claims diverge from independently-measured reality, was released today and includes **[N] record(s)** pertaining to [Company Name] vehicles. The dataset and accompanying preprint are public:
>
> - GitHub repository: https://github.com/Princeu3/DataDeception
> - arXiv preprint: [arXiv ID once assigned]
>
> The records pertaining to your products are listed below. Each record carries a verbatim claim quote with archived URL, an independent-measurement citation (Tier-2 or Tier-1), an evidence grade (A–D), and an assigned tactic from a 13-tactic taxonomy. The methodology is detailed in §3 of the preprint.
>
> **Records concerning [Company Name]:**
> [bulleted list — see appendix below for per-company specifics]
>
> Per the methodology stated in §3.7 of the paper, **responses received within 30 days of this notification are integrated as additional sources alongside each affected record, not as redactions**. The audit trail is preserved in the public Git history. If your team identifies a factual inaccuracy in any record's claim quote, citation, or gap quantification, please reply to this email with:
>
> 1. The record identifier (filename in the format shown above);
> 2. The specific factual element being contested (claim quote, reality value, severity assignment, or tactic mapping);
> 3. Supporting evidence (citation, archived URL, or measurement reference) we should add as a Tier-1 or Tier-4 source.
>
> Counter-examples (records where independent measurement matches or exceeds the manufacturer claim) are deliberately included in the dataset to mitigate confirmation bias; if your team has additional measurements that would shift any of your records in either direction, those are equally welcome.
>
> A consumer-facing surface auto-generated from the dataset is also published; updates flow from the underlying JSON, so a single integrated response propagates through all surfaces. The dataset, schema, validators, and figure-generation pipeline are released under MIT (code) and CC-BY-4.0 (data).
>
> I have copied the sender address as the response channel; for routing complex responses you may wish to escalate, the GitHub issue tracker is also monitored.
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

## Per-company appendix (customize the "Records concerning" section)

> ⚠ **Email addresses below are best guesses based on typical corporate-PR conventions. Verify each before sending.** Send to the most senior or specific PR/communications address that publicly responds to product-claim inquiries. Do not blast generic info@ addresses — those are filtered.

### Tesla (8 records)

- Suggested addresses: `press@tesla.com` (note: Tesla dissolved its U.S. press team in 2020; may bounce or auto-reply), `vehiclesafetycontact@tesla.com`. Backup: file via `service.tesla.com` contact form and reference the email.
- Records:
  - `tesla-cybertruck-2025-awd__range__highway_70mph` — EPA 318 mi vs. MotorTrend 70 mph 224 mi (−30%); largest gap in v0.1.
  - `tesla-cybertruck-2025-awd__announcement_promise__500_mi_unfulfilled` — 2019 announcement promised 500 mi trim; Range Extender accessory cancelled May 2025 with full refunds, never delivered.
  - `tesla-model-y-2025-long-range-awd__range__highway_70mph` — EPA combined vs. independent 70 mph gap.
  - `tesla-model-y-2025-long-range-awd__charging__peak_dc_sustained_duration` — peak DC charge rate vs. sustained-duration gap.
  - `tesla-model-y-2025-long-range-awd__performance__zero_to_60_rollout` — 0–60 marketing figure vs. instrumented (with rollout subtraction).
  - `tesla-model-y-2025-long-range-awd__pricing__starting_at_destination` — "starting at" price excluding mandatory destination/fees.
  - `tesla-model-y-2025-long-range-awd__software_features__fsd_naming` — "Full Self-Driving" categorical naming overclaim; California ALJ ruling December 2025; NHTSA investigation October 2025 covering 2.88M vehicles.
  - `tesla-model-3-2025-long-range-awd__range__highway_70mph` — EPA combined vs. independent 70 mph gap.

### Ford (5 records)

- Suggested addresses: `media@ford.com`, `usmedia@ford.com`. Ford Communications has been historically responsive to fact-check requests.
- Records:
  - `ford-f-150-lightning-2024-extended-range__range__highway_70mph` — EPA combined 320 mi vs. CR 70 mph 270 mi.
  - `ford-f-150-lightning-2024-extended-range__range__towing_50pct_loss` — towing-mode range collapse; stranding-risk severity.
  - `ford-f-150-lightning-2024-extended-range__charging__peak_dc_low_for_battery` — peak DC charge below industry expectation for battery size.
  - `ford-f-150-lightning-2024-extended-range__production_status__2025_discontinued` — silent discontinuation tactic.
  - `ford-mustang-mach-e-2025-awd-extended__range__highway_70mph` — counter-example: independent measurement matches EPA.

### Rivian (5 records)

- Suggested addresses: `media@rivian.com`, `press@rivian.com`. Rivian PR responds to public-record inquiries.
- Records:
  - `rivian-r1s-2025-dual-max__range__highway_70mph` — EPA 410 mi (Dual Max) vs. CR 70 mph 358 mi.
  - `rivian-r1s-2025-dual-max__build_warranty__nhtsa_recall_density` — 9 NHTSA recalls in MY 2025; highest in v0.1.
  - `rivian-r1s-2025-dual-max__charging__peak_dc_unrealistic` — peak DC rate marketing vs. sustained.
  - `rivian-r1s-2025-dual-max__charging__level2_15_hours` — Level-2 home charging time disclosure.
  - `rivian-r1s-2025-dual-max__ui_ergonomics__touchscreen_distraction` — touchscreen-only basic-controls placement.

### Hyundai (3 records)

- Suggested addresses: `media@hmausa.com`, `corp.comm@hyundai.com`.
- Records:
  - `hyundai-ioniq-5-2025-rwd-long-range__range__highway_70mph` — EPA combined vs. 70 mph gap.
  - `hyundai-ioniq-5-2025-rwd-long-range__build_warranty__nhtsa_recall_density` — 8 recalls including two separate high-voltage traction-battery campaigns.
  - `hyundai-ioniq-6-2025-rwd-long-range__range__highway_70mph` — EPA combined vs. 70 mph gap.

### Lucid (3 records)

- Suggested addresses: `press@lucidmotors.com`, `lucidmedia@lucidmotors.com`.
- Records:
  - `lucid-air-grand-touring-2025__range__highway_70mph` — EPA range vs. independent measurement.
  - `lucid-air-grand-touring-2025__range__wheel_size_cliff` — undisclosed range collapse with optional 21" wheels.
  - `lucid-air-grand-touring-2025__build_warranty__nhtsa_recall_density` — 5 recalls in MY 2025.

### Mercedes-Benz (1 record — counter-example)

- Suggested addresses: `media.mbusa@mbusa.com`, `mbusa.media@mbusa.com`.
- Records:
  - `mercedes-eqs-450-plus-2025__range__highway_70mph` — **counter-example**: Edmunds measured 422 mi vs. EPA 350 mi (+72 mi over). Included in dataset by design to mitigate confirmation bias. Notification is informational; no contested claim.

### GMC / General Motors (2 records)

- Suggested addresses: `media@gm.com`, `pr@gmc.com`.
- Records:
  - `gmc-hummer-ev-pickup-2025-2x__range__highway_70mph` — EPA combined vs. independent 70 mph gap.
  - `gmc-hummer-ev-pickup-2025-2x__range__heavy_duty_exemption` — heavy-duty class certification exemption (Hummer EV exceeds 8500 lb GVWR threshold and is therefore exempt from EPA combined-cycle range labeling that applies to lighter EVs).

### Volkswagen (1 record)

- Suggested addresses: `media.relations@vwoa.com`.
- Records:
  - `volkswagen-id4-2025-awd-pro-s__range__highway_70mph` — EPA combined vs. independent 70 mph gap.

### Polestar (0 records — no notification needed)

Polestar 2 is listed in the v0.1 product set as a 0-deception-record reference (no documented gaps that meet the evidence rubric); no notification is needed for v0.1.

---

## Sending mechanics

- Send each email **individually**, not BCC'd. Per-company personalization signals good faith and reduces auto-filter risk.
- Send between **9:00–11:00 ET on a Tuesday or Wednesday** (highest open rate window for corporate communications).
- **Do not** include the per-company appendix below the records list — that's metadata for you, not for them.
- After sending, log timestamps in `outreach/sent-log.md` (append-only) so you can compute the 30-day response window deterministically.
