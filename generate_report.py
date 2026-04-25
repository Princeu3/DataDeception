#!/usr/bin/env python3
"""Generate consumer-facing summary report from the dataset.

Reads data/products/*.json and data/deceptions/*.json, produces CONSUMER_REPORT.md.

Run: .venv/bin/python generate_report.py
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
DATA = REPO / "data"
OUT = REPO / "CONSUMER_REPORT.md"

SEVERITY_ORDER = {"critical": 0, "high": 1, "moderate": 2, "low": 3, "informational": 4}
SEVERITY_BADGE = {
    "critical": "🔴 CRITICAL",
    "high": "🟠 HIGH",
    "moderate": "🟡 MODERATE",
    "low": "🟢 LOW",
    "informational": "ℹ️  INFO",
}
GRADE_BADGE = {"A": "★★★", "B": "★★", "C": "★", "D": "—"}


def load_json(p: Path) -> dict:
    with open(p) as fh:
        return json.load(fh)


def load_all():
    products = {p.stem: load_json(p) for p in (DATA / "products").glob("*.json")}
    decs = [load_json(p) for p in (DATA / "deceptions").glob("*.json")]
    tactics = {t.stem: load_json(t) for t in (DATA / "tactics").glob("*.json")}
    by_product = defaultdict(list)
    for d in decs:
        by_product[d["product_id"]].append(d)
    return products, by_product, tactics, decs


def fmt_money(n) -> str:
    return f"${n:,}" if n else "—"


def severity_badge(s: str) -> str:
    return SEVERITY_BADGE.get(s, s or "—")


def write_product_section(p: dict, decs: list[dict]) -> str:
    lines = []
    label = f"{p['manufacturer']} {p['model']} {p['model_year']} {p['trim']}"
    lines.append(f"## {label}")
    lines.append("")

    # At-a-glance facts
    epa = p.get("epa", {})
    base = p.get("msrp_usd_base")
    delivered = p.get("msrp_usd_delivered_min")
    nhtsa = p.get("nhtsa", {})
    rcount = nhtsa.get("recall_count", "?")

    lines.append(f"**EPA combined range:** {epa.get('range_combined_mi','?')} mi · "
                 f"**Starting MSRP:** {fmt_money(base)} (delivered ≈ {fmt_money(delivered)}) · "
                 f"**NHTSA recalls (this model year):** {rcount}")
    if rcount and isinstance(rcount, int) and rcount >= 5:
        lines.append("")
        lines.append(f"> ⚠️  **{rcount} NHTSA recalls** — among the highest in this dataset. "
                     f"Components: {', '.join(nhtsa.get('components_affected', [])[:5])}. "
                     f"[Full list]({nhtsa.get('recall_url','')})")
    lines.append("")

    if not decs:
        lines.append("_No deception records yet for this product._")
        lines.append("")
        return "\n".join(lines)

    # Sort by severity then evidence grade
    decs_sorted = sorted(
        decs,
        key=lambda d: (
            SEVERITY_ORDER.get(d.get("gap", {}).get("severity"), 9),
            -ord(d.get("evidence_grade", "Z")[0])
        )
    )

    lines.append("### What's advertised vs. what's real")
    lines.append("")
    lines.append("| Severity | Axis | One-liner | Evidence |")
    lines.append("|---|---|---|---|")
    for d in decs_sorted:
        sev = d.get("gap", {}).get("severity", "—")
        axis = d["axis"].replace("_", " ")
        one = d.get("narrative_one_liner") or d.get("narrative", "")[:160]
        # markdown-table-safe
        one = one.replace("|", "\\|").replace("\n", " ")
        grade = d.get("evidence_grade", "?")
        lines.append(f"| {severity_badge(sev)} | {axis} | {one} | {GRADE_BADGE.get(grade,'?')} {grade} |")
    lines.append("")

    # Per-record detail
    lines.append("<details>")
    lines.append("<summary>Full record detail (click to expand)</summary>")
    lines.append("")
    for d in decs_sorted:
        sev = d.get("gap", {}).get("severity", "—")
        sub = d["sub_axis"].replace("_", " ")
        lines.append(f"#### {d['axis']} / {sub} — {severity_badge(sev)}")
        lines.append("")
        lines.append(f"_{d.get('narrative','')}_")
        lines.append("")
        gap = d.get("gap", {})
        if gap.get("kind") == "numeric" and gap.get("pct") is not None:
            lines.append(f"- **Gap**: {gap.get('absolute')} {gap.get('absolute_unit')} ({gap.get('pct')}%)")
        # Top sources
        for side, label_ in (("claim", "Manufacturer claim"), ("reality", "Independent measurement")):
            srcs = d.get(side, {}).get("sources", [])
            if srcs:
                src = srcs[0]
                snap = f" · [archive]({src['snapshot_url']})" if src.get("snapshot_url") else ""
                lines.append(f"- **{label_}**: [{src.get('name','source')}]({src.get('url','')}) "
                             f"(Tier {src.get('tier','?')}){snap}")
        lines.append("")
    lines.append("</details>")
    lines.append("")
    return "\n".join(lines)


def write_overview(products: dict, by_product: dict, decs: list[dict]) -> str:
    lines = []
    lines.append("# DataDeception — Consumer Report")
    lines.append("")
    lines.append("**Last generated:** 2026-04-25 · **Auto-generated from `data/`** — do not hand-edit. "
                 "Run `python generate_report.py` to refresh.")
    lines.append("")
    lines.append("This report distills the DataDeception dataset for buyers researching electric "
                 "vehicles. For each product, we compare what the manufacturer advertises against "
                 "what independent testing measured. Every claim cites its source so you can verify.")
    lines.append("")
    lines.append("**How to read severity**:")
    lines.append("- 🔴 **Critical** — regulatory finding, safety-of-life impact, or judicial ruling")
    lines.append("- 🟠 **High** — substantial purchase-decision distortion or documented safety pattern")
    lines.append("- 🟡 **Moderate** — material misrepresentation; informed buyers can correct for it")
    lines.append("- 🟢 **Low** — technical or convention quirk")
    lines.append("- ℹ️  **Info** — counter-example or honest baseline")
    lines.append("")
    lines.append("**Evidence grade** (per [METHODOLOGY.md](METHODOLOGY.md)):")
    lines.append("- **★★★ A** — Tier-1 (regulatory/government) source or ≥2 independent Tier-2 measurements")
    lines.append("- **★★ B** — single Tier-2 source or editorial framing of a manufacturer disclosure")
    lines.append("")

    # Summary table — one row per product, key takeaways
    lines.append("## Quick comparison")
    lines.append("")
    lines.append("| Product | EPA range | Real (70mph) | Highway gap | Recalls | Most-critical issue |")
    lines.append("|---|---:|---:|---:|---:|---|")

    rows = []
    for pid, p in products.items():
        ds = by_product.get(pid, [])
        # Find highway range deception if present
        hw_d = next((d for d in ds if d["axis"] == "range" and "highway" in d["sub_axis"]), None)
        hw_real = "—"
        hw_gap = "—"
        if hw_d:
            r = hw_d.get("reality", {}).get("value")
            hw_real = f"{r} mi" if isinstance(r, (int, float)) else (str(r) if r else "—")
            pct = hw_d.get("gap", {}).get("pct")
            if pct is not None:
                hw_gap = f"{pct:+.1f}%"
        epa_combined = p.get("epa", {}).get("range_combined_mi", "—")
        recalls = p.get("nhtsa", {}).get("recall_count", "?")
        # Most-critical = highest-severity deception narrative_one_liner
        critical = "—"
        if ds:
            top = sorted(ds, key=lambda d: SEVERITY_ORDER.get(d.get("gap", {}).get("severity"), 9))[0]
            sev = top.get("gap", {}).get("severity", "")
            critical = f"{severity_badge(sev)}: {top.get('narrative_one_liner','')[:90]}…"
        label = f"{p['manufacturer']} {p['model']} {p['model_year']}"
        rows.append((label, epa_combined, hw_real, hw_gap, recalls, critical))

    # Sort by recall count desc then by name
    rows.sort(key=lambda r: (-(r[4] if isinstance(r[4], int) else 0), r[0]))
    for r in rows:
        lines.append(f"| {r[0]} | {r[1]} mi | {r[2]} | {r[3]} | {r[4]} | {r[5]} |")
    lines.append("")

    lines.append("## Key takeaways for buyers")
    lines.append("")
    lines.append("1. **EPA range is a city-weighted average, not a highway estimate.** Most products "
                 "in this dataset deliver 80–88% of EPA at steady 70 mph. Plan road trips on the lower "
                 "number. Worst offenders: Tesla Cybertruck (-30%), Lucid Air on 19in wheels (-21%), "
                 "Hyundai Ioniq 6 (-19%). Counter-examples that beat or match EPA: Mercedes EQS, "
                 "Ford Mach-E.")
    lines.append("")
    lines.append("2. **Towing collapses range 50–70%.** Both electric trucks documented here "
                 "(F-150 Lightning, GMC Hummer EV) lose half their range when towing a typical "
                 "6,000–7,000 lb trailer. Tow capacity and EPA range are advertised together as if "
                 "independent; they are not.")
    lines.append("")
    lines.append("3. **Peak DC charging numbers are sustained for minutes, not the whole charge.** "
                 "Tesla's 250 kW peak holds ~6 minutes; Rivian's 220 kW peak hasn't been observed close "
                 "to that in CR testing. The advertised number does not reflect the average rate during "
                 "a 10–80% road-trip charge.")
    lines.append("")
    lines.append("4. **First-year recall density varies enormously.** Rivian R1S (9 recalls), "
                 "Hyundai Ioniq 5 (8 — including TWO traction battery campaigns), Lucid Air (5) lead. "
                 "Ford Mach-E, F-150 Lightning, Mercedes EQS, GMC Hummer EV, Polestar 2 currently show "
                 "0 NHTSA recalls for the documented model year.")
    lines.append("")
    lines.append("5. **'Full Self-Driving' was ruled unambiguously false** by a CA judge (Dec 2025). "
                 "NHTSA is investigating 2.88M Tesla vehicles connecting FSD to 14 crashes and "
                 "23 injuries. Tesla complied with the name change but is suing the DMV.")
    lines.append("")
    lines.append("6. **'Starting at' MSRP excludes destination fees.** Universal in US auto industry. "
                 "Add $1,000–$2,500 to any headline price.")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def main():
    products, by_product, tactics, decs = load_all()
    out = [write_overview(products, by_product, decs)]
    out.append("# Per-product details")
    out.append("")
    # Order by severity of worst deception
    pids_sorted = sorted(
        products.keys(),
        key=lambda pid: (
            min(
                (SEVERITY_ORDER.get(d.get("gap", {}).get("severity"), 9) for d in by_product.get(pid, [])),
                default=9,
            ),
            products[pid]["manufacturer"],
            products[pid]["model"],
        )
    )
    for pid in pids_sorted:
        out.append(write_product_section(products[pid], by_product.get(pid, [])))

    # Footer
    out.append("---")
    out.append("")
    out.append("## Methodology and limitations")
    out.append("")
    out.append("- Sources are tiered: Tier 1 (EPA, NHTSA, court rulings) > Tier 2 (Consumer Reports, "
               "Edmunds, MotorTrend, etc.) > Tier 3 (owner forums, with N≥10 to cite) > Tier 4 "
               "(manufacturer claims — treated as the *claim*, not the truth).")
    out.append("- Read [LIMITATIONS.md](LIMITATIONS.md) before drawing population-level conclusions: "
               "selection bias, single-unit testing, software-update effects, and absence of "
               "manufacturer response are all real.")
    out.append("- This report is auto-generated. The underlying records are at "
               "`data/products/`, `data/deceptions/`, `data/tactics/`. Run `validate.py` to verify "
               "schema and referential integrity.")
    out.append("")
    out.append(f"_Total: {len(products)} products · {len(decs)} deception records · "
               f"{len(tactics)} tactic patterns documented._")

    OUT.write_text("\n".join(out))
    print(f"✓ Wrote {OUT.relative_to(REPO)} ({sum(1 for _ in OUT.read_text().splitlines())} lines)")


if __name__ == "__main__":
    main()
