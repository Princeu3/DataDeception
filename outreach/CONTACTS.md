# Manufacturer contact verification — DataDeception v0.1 launch

Status of address discovery for each company in v0.1. All addresses below should be **re-verified the morning of launch** — corporate PR routing changes frequently.

| Company | Primary contact | Confidence | Fallback |
|---|---|---|---|
| Tesla | (no public press email — see notes) | n/a | Contact form + X/@TeslaSafety |
| Ford | `media@ford.com` | confirmed (Ford media center) | https://media.ford.com/ contact form |
| Rivian | `press@rivian.com` | guess (format: [first_initial][last]) | https://rivian.com/newsroom |
| Hyundai | (no public email — form only) | n/a | https://www.hyundainews.com/contact |
| Lucid | `andrewhussey@lucidmotors.com` | guess (format: FirstLast@; person confirmed) | `davidbuchko@lucidmotors.com` (Product PR Mgr) |
| Mercedes-Benz USA | `mediarelations@mbusa.com` | guess (catch-all convention) | https://media.mbusa.com/contact |
| GM (for GMC) | `media@gm.com` | guess (catch-all) | https://media.gm.com/ contact directory |
| Volkswagen USA | `media.relations@vwoa.com` | guess (format: first.last@vw.com) | https://media.vw.com/en-us/contact |

## Tesla — special handling

Tesla dissolved their U.S. press team in October 2020 and has not maintained a public press contact since. Standard recourse:

1. **Web contact form** at https://www.tesla.com/contact, Vehicle Safety category. This routes to internal triage.
2. **X (Twitter) post** mentioning @TeslaSafety with the GitHub URL. Tesla communicates almost exclusively through X; a public mention is sometimes more visible than an email.
3. **NHTSA copy.** For records related to FSD (`tesla-model-y-2025-long-range-awd__software_features__fsd_naming`) the relevant regulator is already involved — copy the NHTSA Office of Defects Investigation (ODI) at the address on https://www.nhtsa.gov/contact-nhtsa for completeness.

Document this asymmetry in the launch tweet thread itself ("Tesla doesn't maintain a public press contact; this notification was filed via the safety contact form. Update if a response comes via X.") — it's part of the methodology story.

## Verification protocol for launch morning

For each address marked "guess" above, do one of the following before sending:

1. **Send a short test email 24 hours before launch** ("Hi — verifying this address is the right one for U.S. consumer-product communications. Replying with even a one-word confirmation would help.") and wait for a bounce or auto-reply. A bounce in 4 hours is faster than discovering it on launch day.

2. **Search the company's most recent press release on Google News** in the last 30 days. Press releases usually list a "For media inquiries:" line at the bottom with the current correct contact.

3. **LinkedIn check.** For named contacts (Lucid Andrew Hussey, VW Michael Lowder), confirm they're still in the role on LinkedIn before sending. Job changes are common in auto-industry PR.

## What to log

After each send, append to `outreach/sent-log.md` (created on launch day, not committed in advance):

```
<ISO datetime> | <company> | <to_address> | <delivery_method: email|form|tweet> | <records_count> | <reply_expected_by: launch_date + 30d>
```

This file is the ground truth for the 30-day response window in §3.7 of the paper.
