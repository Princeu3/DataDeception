# Launch-day checklist — DataDeception v0.1

Concurrent-with-publication notification protocol (per §3.7 of the paper). All four launch actions happen on a single morning.

---

## Pre-launch (T-1 day)

- [ ] **Verify manufacturer email addresses** in `outreach/EMAIL_TEMPLATE.md`. The addresses listed there are best-guesses based on corporate-PR conventions; some may have changed. Verify each before sending.
- [ ] **Choose launch day.** Tuesday or Wednesday morning ET. Avoid Mondays (inbox flood from weekend), Fridays (low engagement), and US federal holidays.
- [ ] **Final paper read-through.** Open `paper/main.pdf` and read end to end one more time. Once arXiv is submitted, the v1 cannot be deleted (only superseded).
- [ ] **Test arXiv submission flow** if first-time submitter. arXiv requires endorsement for new authors in some categories; cs.CY and cs.HC are open without endorsement.
- [ ] **Pre-fill arXiv form fields** (offline draft):
  - Title: from `\title{}` in `paper/main.tex`
  - Abstract: from `\begin{abstract}` block, plain text (strip LaTeX commands)
  - Authors: Prince Upadhyay
  - Categories: cs.CY (Computers and Society) primary; cs.HC (Human-Computer Interaction) secondary
  - License: CC-BY-4.0 (matches the data license; the LaTeX source license can be MIT but arXiv only allows specific licenses)
  - Comments field: "13 pages, 7 figures. Data and code: https://github.com/Princeu3/DataDeception"
- [ ] **Final tweet copy review.** Tweet 1 is the share asset for everyone else; check character counts, finalize attached image (suggest the gap-dotplot or the Findings-at-a-glance screenshot).

---

## Launch morning (T+0)

Single coordinated drop. Order matters because each step's output feeds the next.

### Step 1 — Make GitHub repo public (T+0:00)

```
gh repo edit Princeu3/DataDeception --visibility public --accept-visibility-change-consequences
```

Verify: open https://github.com/Princeu3/DataDeception in a private/incognito window. Should load without auth.

### Step 2 — Submit to arXiv (T+0:05)

Upload the LaTeX source bundle (not the PDF — arXiv compiles its own). The bundle should include:
- `paper/main.tex`, `paper/references.bib`, `paper/arxiv.sty`
- `paper/figures/*.tex` (all generated TikZ/pgfplots inputs)
- `paper/figures/methodology-flow.tex`, `paper/figures/tactic-taxonomy.tex`

Do **not** include build artifacts (`.aux`, `.bbl`, `.log`, `.pdf`).

Submit, verify on the announce screen, wait for the email with the assigned arXiv ID (typically 5–30 minutes during US business hours).

### Step 3 — Send manufacturer notification emails (T+0:30)

Use `outreach/EMAIL_TEMPLATE.md`. Send individually, not BCC'd. Recommended order:

1. Tesla (8 records — most extensive, send first while attention is fresh)
2. Ford (5 records)
3. Rivian (5 records)
4. Hyundai (3 records)
5. Lucid (3 records)
6. GMC / GM (2 records)
7. Mercedes-Benz (1 record — counter-example, lowest stakes)
8. Volkswagen (1 record)

Skip Polestar (0 records).

Append a row to `outreach/sent-log.md` for each send: `<datetime>, <company>, <to_address>, <records_count>`. This file is the ground truth for the 30-day response window.

### Step 4 — Post Twitter/X thread (T+1:00)

Use `social/LAUNCH_POSTS.md` Twitter section. Post Tweet 1, then schedule Tweets 2–8 at 90-second intervals via the compose UI. Attach the gap-dotplot figure to Tweet 2 and the tactic-taxonomy figure to Tweet 7.

The Tweet 1 URL becomes the share asset for LinkedIn and Reddit.

### Step 5 — Post LinkedIn (T+1:30)

Use `social/LAUNCH_POSTS.md` LinkedIn section. Single post, no thread. Replace `[arXiv-URL]` with the actual arXiv URL.

### Step 6 — Post Reddit r/electricvehicles (T+2:00)

Use `social/LAUNCH_POSTS.md` Reddit section. Stay on the post for 60–90 minutes after submission to engage with comments — Reddit ranking penalizes posts whose authors disappear.

### Step 7 — Cross-post Reddit r/cars (T+3:30)

Only after the r/electricvehicles post has 5+ comments. Cross-post manually (do not use the Reddit cross-post button — it triggers spam filters more aggressively than a fresh post with the same content).

---

## Post-launch monitoring (T+0 through T+30 days)

- **Daily:** check email for manufacturer responses. Log to `outreach/responses-log.md` with received timestamps.
- **Every 3 days:** check GitHub issues. Triage to: (a) factual correction → integrate as new source; (b) methodology question → respond inline; (c) feature request → log for Phase 2.
- **T+24 hr:** post quote-tweet of Tweet 1 with one additional finding (e.g., the recall density bar chart). Lets the thread re-enter timelines.
- **T+7 days:** if any manufacturer response is substantive, draft an integration commit but do not ship until 30-day window closes (avoids partial-response bias).
- **T+30 days:** close the response window. Ship v0.2 with all integrated responses as a single `git tag` event, paired with a tweet/LinkedIn/Reddit recap of what was integrated and what wasn't.

---

## Abort conditions

Stop the launch and reassess if any of these occur before Step 4:

- arXiv submission errors with a moderation hold (could indicate a content concern; resolve before social drop).
- A factual error is discovered in the paper (rebuild PDF, push, then re-do arXiv submission with corrected source — better to delay than ship wrong).
- A manufacturer responds within the first hour of email send with a substantive correction (rare but possible; integrate the correction into v0.1 before social distribution).

---

## What to NOT do

- Do not delete or rewrite git history. The audit trail is part of the methodology contribution.
- Do not respond to social-media controversy by editing the paper. Use a reply or a v0.2 commit instead.
- Do not engage with bad-faith comments on Twitter; flag, mute, move on. Reddit and LinkedIn comments are generally higher signal — engage there.
- Do not post to brand-specific subreddits (r/teslamotors, r/teslainvestorsclub). They will remove critical research regardless of methodology and the removal becomes its own news cycle.
