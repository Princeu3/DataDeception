# DataDeception — Consumer Report

**Last generated:** 2026-04-25 · **Auto-generated from `data/`** — do not hand-edit. Run `python generate_report.py` to refresh.

This report distills the DataDeception dataset for buyers researching electric vehicles. For each product, we compare what the manufacturer advertises against what independent testing measured. Every claim cites its source so you can verify.

**How to read severity**:
- 🔴 **Critical** — regulatory finding, safety-of-life impact, or judicial ruling
- 🟠 **High** — substantial purchase-decision distortion or documented safety pattern
- 🟡 **Moderate** — material misrepresentation; informed buyers can correct for it
- 🟢 **Low** — technical or convention quirk
- ℹ️  **Info** — counter-example or honest baseline

**Evidence grade** (per [METHODOLOGY.md](METHODOLOGY.md)):
- **★★★ A** — Tier-1 (regulatory/government) source or ≥2 independent Tier-2 measurements
- **★★ B** — single Tier-2 source or editorial framing of a manufacturer disclosure

## Quick comparison

| Product | EPA range | Real (70mph) | Highway gap | Recalls | Most-critical issue |
|---|---:|---:|---:|---:|---|
| Rivian R1S 2025 | 410 mi | 358 mi | -12.7% | 9 | 🟠 HIGH: Rivian markets 'minimalist, uncluttered' interior; CR characterizes the same design as 'ex… |
| Hyundai Ioniq 5 2025 | 318 mi | 267 mi | -16.0% | 8 | 🟠 HIGH: Hyundai Ioniq 5 2025: 8 NHTSA recalls in first year — including TWO separate high-voltage … |
| Lucid Air 2025 | 516 mi | 410 mi | -20.5% | 5 | 🟠 HIGH: Lucid Air GT 516 mi EPA; CR 70 mph test 344 vs 396 EPA-at-time (-52 mi). C/D 75 mph: 410 m… |
| Hyundai Ioniq 6 2025 | 361 mi | 291 mi | -19.4% | 3 | 🟠 HIGH: Ioniq 6 SE RWD LR 361 mi EPA; MotorTrend 70 mph test 291 mi (-19%) — a 70-mile shortfall o… |
| Tesla Model 3 2025 | 346 mi | 305 mi | -11.8% | 3 | 🟡 MODERATE: Tesla Model 3 LR AWD 346 mi EPA; typical 75 mph testing 300–310 mi (~12% gap); Out of Spec… |
| Tesla Cybertruck 2025 | 325 mi | 224 mi | -29.6% | 2 | 🟠 HIGH: Cybertruck Dual Motor advertised 318 mi; MotorTrend 70 mph test measured 224 mi — 30% gap,… |
| Tesla Model Y 2025 | 311 mi | 240 mi | -22.8% | 2 | 🔴 CRITICAL: CA judge ruled FSD name 'unambiguously false and counterfactual' (Dec 2025); NHTSA links i… |
| Volkswagen ID.4 2025 | 263 mi | 240 mi | -8.7% | 1 | 🟡 MODERATE: VW ID.4 AWD Pro S advertised 263 mi EPA; Car and Driver 75 mph test 240 mi (~9% gap).… |
| Ford F-150 Lightning 2024 | 320 mi | 270 mi | -15.6% | 0 | 🔴 CRITICAL: Ford pairs '10,000 lb tow capacity' with '320 mi range'; real towing range with mid-size t… |
| Ford Mustang Mach-E 2025 | 300 mi | 299 mi | -0.3% | 0 | ℹ️  INFO: Counter-example: Mach-E AWD Extended matched its 300 mi EPA almost exactly in CR's 70 mph … |
| GMC Hummer EV Pickup 2025 | 318 mi | 250 mi | -21.4% | 0 | 🟠 HIGH: GM markets 381 mi for the 24-module Hummer EV pickup; this trim has no EPA window sticker … |
| Mercedes-Benz EQS 450 Plus 2025 | 390 mi | 380 mi | -2.6% | 0 | ℹ️  INFO: Counter-example: Mercedes EQS 450+ closely matches or beats EPA (CR 380 vs 350; Edmunds 42… |
| Polestar 2 2025 | 276 mi | — | — | 0 | — |

## Key takeaways for buyers

1. **EPA range is a city-weighted average, not a highway estimate.** Most products in this dataset deliver 80–88% of EPA at steady 70 mph. Plan road trips on the lower number. Worst offenders: Tesla Cybertruck (-30%), Lucid Air on 19in wheels (-21%), Hyundai Ioniq 6 (-19%). Counter-examples that beat or match EPA: Mercedes EQS, Ford Mach-E.

2. **Towing collapses range 50–70%.** Both electric trucks documented here (F-150 Lightning, GMC Hummer EV) lose half their range when towing a typical 6,000–7,000 lb trailer. Tow capacity and EPA range are advertised together as if independent; they are not.

3. **Peak DC charging numbers are sustained for minutes, not the whole charge.** Tesla's 250 kW peak holds ~6 minutes; Rivian's 220 kW peak hasn't been observed close to that in CR testing. The advertised number does not reflect the average rate during a 10–80% road-trip charge.

4. **First-year recall density varies enormously.** Rivian R1S (9 recalls), Hyundai Ioniq 5 (8 — including TWO traction battery campaigns), Lucid Air (5) lead. Ford Mach-E, F-150 Lightning, Mercedes EQS, GMC Hummer EV, Polestar 2 currently show 0 NHTSA recalls for the documented model year.

5. **'Full Self-Driving' was ruled unambiguously false** by a CA judge (Dec 2025). NHTSA is investigating 2.88M Tesla vehicles connecting FSD to 14 crashes and 23 injuries. Tesla complied with the name change but is suing the DMV.

6. **'Starting at' MSRP excludes destination fees.** Universal in US auto industry. Add $1,000–$2,500 to any headline price.

---

# Per-product details

## Ford F-150 Lightning 2024 4WD Extended Range

**EPA combined range:** 320 mi · **Starting MSRP:** $56,900 (delivered ≈ $58,895) · **NHTSA recalls (this model year):** 0

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🔴 CRITICAL | range | Ford pairs '10,000 lb tow capacity' with '320 mi range'; real towing range with mid-size trailer is ~100 mi (–69%). | ★★★ A |
| 🟠 HIGH | production status | Ford halted 2025 Lightning production; marketing page presents it as a current product. | ★★ B |
| 🟠 HIGH | range | Ford advertises 320 mi EPA; Consumer Reports' 70 mph highway test measured 270 mi — a 50-mile (16%) gap. | ★★★ A |
| 🟡 MODERATE | charging | Lightning's 150 kW peak is real but unusually low (1.15C) for a 131 kWh battery; competitors do 1.5–2.0C. | ★★ B |

<details>
<summary>Full record detail (click to expand)</summary>

#### range / towing 50pct loss — 🔴 CRITICAL

_Ford advertises 320 mi EPA range and 10,000 lb tow capacity as separate headline numbers. Independent testing shows that towing a typical 6,000–7,200 lb trailer at highway speeds drops range to roughly 90–150 miles — a 50–70% reduction. MotorTrend, Recharged, and owner forum tests converge on this. The truck does internally re-estimate range when a trailer profile is entered, but the marketing positions both numbers as if a buyer can plan towing trips around the EPA figure._

- **Gap**: -220 mi (-68.8%)
- **Manufacturer claim**: [Ford F-150 Lightning marketing materials (via Consumer Reports overview)](https://www.consumerreports.org/cars/ford/f-150-lightning/) (Tier 4)
- **Independent measurement**: [MotorTrend / Automobile — F-150 Lightning towing test (3 trailer weights)](https://www.automobilemag.com/reviews/ford-f150-lightning-electric-truck-towing-test) (Tier 2)

#### production_status / 2025 discontinued — 🟠 HIGH

_Ford has halted production of the 2025 F-150 Lightning. Consumer Reports' product page reflects this; Ford's own marketing site and configurator do not prominently disclose it to shoppers researching the truck. The next-generation Lightning is announced as a series-hybrid (range-extender) vehicle with an onboard generator — a fundamentally different powertrain that will not share parts, charging behavior, or warranty profile with the current battery-electric Lightning. Buyers comparing 'current' EV trucks should know they are evaluating end-of-line inventory._

- **Manufacturer claim**: [Ford — F-150 Lightning marketing site](https://www.ford.com/trucks/f150/f150-lightning/) (Tier 4)
- **Independent measurement**: [Consumer Reports — Ford F-150 Lightning overview (updated)](https://www.consumerreports.org/cars/ford/f-150-lightning/) (Tier 2)

#### range / highway 70mph — 🟠 HIGH

_Ford advertises the Extended Range Lightning at 320 mi EPA. Consumer Reports' instrumented 70 mph highway test measured 270 mi to depletion — a 50-mile, 15.6% gap. This is among the largest gaps CR has documented across 26 EVs they have tested, tied with the Rivian R1S Dual Max. EPA combined-cycle weighting toward city driving inflates the headline relative to real interstate use._

- **Gap**: -50 mi (-15.6%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 47818](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=47818) (Tier 1)
- **Independent measurement**: [Consumer Reports — Real-World Electric Car Range Comparison](https://www.consumerreports.org/cars/hybrids-evs/real-world-ev-range-tests-models-that-beat-epa-estimates-a1103288135/) (Tier 2)

#### charging / peak dc low for battery — 🟡 MODERATE

_Ford advertises 150 kW peak DC fast-charging on the Extended Range Lightning. While the number is accurate, it is unusually low relative to the 131 kWh battery pack — roughly half the C-rate of competitors like the Rivian R1T (220 kW on a similarly-sized pack). Consumer Reports flagged this as 'very slow considering the 131 kilowatt-hour battery pack.' Real-world impact: a 10–80% road-trip charge takes 45+ minutes vs. 20-ish for the Rivian._

- **Manufacturer claim**: [Consumer Reports — Ford F-150 Lightning overview](https://www.consumerreports.org/cars/ford/f-150-lightning/) (Tier 2)
- **Independent measurement**: [Consumer Reports — direct comparison commentary](https://www.consumerreports.org/cars/ford/f-150-lightning/2024/road-test-report/) (Tier 2)

</details>

## Tesla Model Y 2025 Long Range AWD

**EPA combined range:** 311 mi · **Starting MSRP:** $47,990 (delivered ≈ $49,380) · **NHTSA recalls (this model year):** 2

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🔴 CRITICAL | software features | CA judge ruled FSD name 'unambiguously false and counterfactual' (Dec 2025); NHTSA links it to 14 crashes. | ★★★ A |
| 🟠 HIGH | range | Tesla advertises 311 mi (EPA combined); independent tests show 225–255 mi at steady 70 mph (≈22% gap). | ★★★ A |
| 🟡 MODERATE | charging | Tesla's 250 kW peak Supercharging is sustained ~6 minutes (5–22% SOC); rate halves by 30% SOC. | ★★★ A |
| 🟢 LOW | pricing | 'Starting at $47,990' excludes the $1,390 destination fee — actual delivered MSRP is $49,380–$50,380. | ★★ B |
| 🟢 LOW | performance | Tesla's 0–60 figures use 1-ft rollout; instrumented tests without rollout are 0.2 sec slower (~5%). | ★★★ A |

<details>
<summary>Full record detail (click to expand)</summary>

#### software_features / fsd naming — 🔴 CRITICAL

_The name 'Full Self-Driving' was ruled 'unambiguously false and counterfactual' by a California administrative law judge in December 2025. Tesla's system is SAE Level 2 — driver-assistance requiring constant supervision. Tesla added '(Supervised)' to the name in January 2026 in response to the ruling, then sued the DMV in February 2026 to reverse the false-advertiser label. NHTSA's investigation links 14 crashes and 23 injuries to FSD operation._

- **Manufacturer claim**: [Tesla — FSD product / Autopilot support page](https://www.tesla.com/support/autopilot) (Tier 4) · [archive](http://web.archive.org/web/20250919114928/https://www.tesla.com/support/autopilot)
- **Independent measurement**: [California DMV administrative law judge ruling (December 2025), reported by TechCrunch](https://techcrunch.com/2025/12/16/tesla-engaged-in-deceptive-marketing-for-autopilot-and-full-self-driving-judge-rules/) (Tier 1)

#### range / highway 70mph — 🟠 HIGH

_Tesla advertises 311 mi EPA combined for the Model Y Long Range AWD. Independent 70-mph highway tests put real-world range at roughly 225–255 mi — a 20–25% gap. EPA combined averages city + highway driving with weighting that favors lower speeds where EVs are most efficient._

- **Gap**: -71 mi (-22.8%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 48770](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=48770) (Tier 1)
- **Independent measurement**: [Recharged — Tesla Model Y Real-World Highway Range Explained (2025)](https://recharged.com/articles/tesla-model-y-real-world-range-highway) (Tier 2)

#### charging / peak dc sustained duration — 🟡 MODERATE

_Tesla's 250 kW peak Supercharging is sustained for roughly 6 minutes between 5–22% state of charge, then tapers. By 30% SOC the rate has dropped to ~135 kW; by 50% it's ~80 kW. The headline number is real but is achieved only briefly under specific preconditioning conditions; it does not represent the average rate during a typical 10–80% road-trip charge._

- **Manufacturer claim**: [Car and Driver — 2026 Model Y Long Range AWD Test (mfr spec table reproduced)](https://www.caranddriver.com/reviews/a65562450/2026-tesla-model-y-long-range-awd-test/) (Tier 4)
- **Independent measurement**: [EVKX — Tesla Model Y Long Range systematic charging curve](https://evkx.net/models/tesla/model_y/model_y_long_range/chargingcurve/) (Tier 2)

#### pricing / starting at destination — 🟢 LOW

_The 'starting at' price quoted in marketing and configurator headlines excludes the mandatory $1,390 destination fee. The delivered MSRP a buyer encounters at order placement is $49,380 (2025) or $50,380 (2026 refresh). Edmunds also notes the Long Range AWD is not eligible for the federal Clean Vehicle Credit, which is sometimes referenced in advertised effective prices._

- **Gap**: 2390 USD (4.98%)
- **Manufacturer claim**: [Edmunds — 2025 Tesla Model Y configurator (republishes Tesla MSRP)](https://www.edmunds.com/tesla/model-y/2025/) (Tier 4)
- **Independent measurement**: [Cars.com — 2026 Tesla Model Y Gets Long Range AWD Variant, Starts at $50,380](https://www.cars.com/articles/2026-tesla-model-y-gets-long-range-awd-variant-starts-at-50380-506759/) (Tier 2)

#### performance / zero to 60 rollout — 🟢 LOW

_Tesla's published 0–60 time uses 1-foot rollout (timing starts after the vehicle has moved one foot, ~0.3 sec). Independent instrumented testing without rollout measures 3.9 sec (Car and Driver) and 3.8 sec (MotorTrend) for the refreshed 2026 model. The gap is small but systematic and complicates apples-to-apples comparison with manufacturers that don't use rollout._

- **Gap**: -0.2 sec (-4.9%)
- **Manufacturer claim**: [Autoguide — Tesla Model Y 0–60 Time documentation of rollout convention](https://autoguide.top/tesla-model-y-0-60-time-complete-acceleration-quarter-mile-breakdown-2020-2025/) (Tier 4)
- **Independent measurement**: [Car and Driver — 2026 Tesla Model Y Long Range AWD instrumented test](https://www.caranddriver.com/reviews/a65562450/2026-tesla-model-y-long-range-awd-test/) (Tier 2)

</details>

## GMC Hummer EV Pickup 2025 2X

**EPA combined range:** 318 mi · **Starting MSRP:** $96,550 (delivered ≈ $98,545) · **NHTSA recalls (this model year):** 0

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🟠 HIGH | range | GM markets 381 mi for the 24-module Hummer EV pickup; this trim has no EPA window sticker — exempt due to heavy-duty classification. | ★★ B |
| 🟠 HIGH | range | Hummer EV Pickup 2X advertised 318 mi EPA; independent 75 mph testing ~250 mi (~21% gap). 'Barn-door shape + 9,000 lb' explains it. | ★★ B |

<details>
<summary>Full record detail (click to expand)</summary>

#### range / heavy duty exemption — 🟠 HIGH

_GMC advertises 'up to 381 miles' for the long-range Hummer EV Pickup 3X (24-module battery pack). This vehicle is classified as heavy-duty (>8,500 lb GVWR) and is therefore exempt from EPA range certification. The 381-mi figure is GM's own estimate, not independently validated by the EPA test cycle. Real-world independent testing shows 260–320 mi at typical highway speeds. Buyers comparing this number against EPA-certified competitors (e.g., Rivian R1T 410 mi EPA, Silverado EV 450 mi EPA) are comparing apples to oranges — a manufacturer estimate against EPA-validated numbers._

- **Manufacturer claim**: [GMC — Hummer EV configurator (manufacturer estimate)](https://www.gmc.com/electric/hummer-ev) (Tier 4) · [archive](http://web.archive.org/web/20230420050203/https://www.gmc.com/electric/hummer-ev)
- **Independent measurement**: [Recharged — GMC Hummer EV Real-World Highway Range](https://recharged.com/articles/gmc-hummer-ev-real-world-range-highway) (Tier 2)

#### range / highway 70mph — 🟠 HIGH

_GMC advertises 318 mi EPA for the Hummer EV Pickup 2X with 170 kWh battery pack. Independent 75 mph testing returns roughly 250 mi — a 21% gap. The Hummer's brick-shaped aerodynamics and 9,000+ lb curb weight make highway-speed range loss particularly steep. Recharged synthesis puts typical 70 mph range at 230–280 mi for this trim._

- **Gap**: -68 mi (-21.4%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 48343](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=48343) (Tier 1)
- **Independent measurement**: [Recharged — 2024 GMC Hummer EV Review](https://recharged.com/articles/2024-gmc-hummer-ev-review) (Tier 2)

</details>

## Hyundai Ioniq 5 2025 RWD Long Range

**EPA combined range:** 318 mi · **Starting MSRP:** $42,500 (delivered ≈ $43,995) · **NHTSA recalls (this model year):** 8

> ⚠️  **8 NHTSA recalls** — among the highest in this dataset. Components: ELECTRICAL SYSTEM, EXTERIOR LIGHTING, SEAT BELTS, SERVICE BRAKES, HYDRAULIC, SUSPENSION. [Full list](https://www.nhtsa.gov/recalls?make=hyundai&model=ioniq%205&year=2025)

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🟠 HIGH | build warranty | Hyundai Ioniq 5 2025: 8 NHTSA recalls in first year — including TWO separate high-voltage battery recalls. | ★★★ A |
| 🟡 MODERATE | range | Ioniq 5 RWD Long Range 318 mi EPA; CR 70 mph test 267 mi (-16% gap on similar AWD trim). | ★★ B |

<details>
<summary>Full record detail (click to expand)</summary>

#### build_warranty / nhtsa recall density — 🟠 HIGH

_The Hyundai Ioniq 5 2025 is subject to 8 NHTSA recalls in its first model year, the second-highest count in this dataset after Rivian R1S. Two are high-voltage traction battery recalls, which are particularly significant because EV battery packs are extraordinarily expensive to remediate and represent the most safety-sensitive component of an EV. Other recalls include rear floor wiring, brake-control module (twice on Ioniq 5 N variant), headlight, rear suspension fasteners, and seat belt retractors. Hyundai markets the Ioniq 5 with 'award-winning' and 'reliable' language, which is contradicted by this defect-discovery density._

- **Manufacturer claim**: [Hyundai USA — Ioniq 5 marketing](https://www.hyundaiusa.com/us/en/vehicles/ioniq-5) (Tier 4)
- **Independent measurement**: [NHTSA recalls.gov — Hyundai Ioniq 5 2025](https://www.nhtsa.gov/recalls?make=hyundai&model=ioniq%205&year=2025) (Tier 1)

#### range / highway 70mph — 🟡 MODERATE

_Hyundai advertises 318 mi EPA for the 2025 Ioniq 5 RWD Long Range (84 kWh battery, up from 77.4 kWh in prior years). Consumer Reports' 70 mph highway test on the closely-related AWD trim with the older 77.4 kWh battery measured 267 mi against 266 mi EPA at the time — slightly beating EPA in that specific configuration. Recharged synthesis suggests typical 70 mph range for current RWD Long Range is about 250–270 mi (~16% gap from the new 318 figure). The Ioniq 5's boxy crossover shape makes aero drag a notable factor._

- **Gap**: -51 mi (-16.0%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 48713](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=48713) (Tier 1)
- **Independent measurement**: [Consumer Reports — 2025 Hyundai Ioniq 5 Road Test Report](https://inventory.consumerreports.org/cars/hyundai/ioniq-5/2025/road-test-report/) (Tier 2)

</details>

## Hyundai Ioniq 6 2025 RWD Long Range (18in wheels)

**EPA combined range:** 361 mi · **Starting MSRP:** $43,850 (delivered ≈ $45,345) · **NHTSA recalls (this model year):** 3

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🟠 HIGH | range | Ioniq 6 SE RWD LR 361 mi EPA; MotorTrend 70 mph test 291 mi (-19%) — a 70-mile shortfall on the 'efficiency leader' sedan. | ★★ B |

<details>
<summary>Full record detail (click to expand)</summary>

#### range / highway 70mph — 🟠 HIGH

_Hyundai advertises 361 mi EPA combined for the Ioniq 6 SE RWD Long Range — Hyundai's claimed EV efficiency leader. MotorTrend's instrumented 70 mph Road-Trip Range Test (using 95% of battery capacity) measured 291 miles, a 70-mile, 19% shortfall. SuperChevy's long-term real-world test concurred: 'the 2024 Hyundai Ioniq 6's EPA-Estimated 361-Mile Range Remains Out of Reach.' This is among the larger negative gaps in the Phase 1 dataset._

- **Gap**: -70 mi (-19.4%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 48362](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=48362) (Tier 1)
- **Independent measurement**: [SuperChevy / MotorTrend — Hyundai Ioniq 6 Yearlong Review (range test)](http://www.superchevy.com/reviews/2024-hyundai-ioniq-6-yearlong-review-update-6-road-trip-range-test) (Tier 2)

</details>

## Lucid Air 2025 Grand Touring AWD (19in wheels)

**EPA combined range:** 516 mi · **Starting MSRP:** $110,900 (delivered ≈ $112,400) · **NHTSA recalls (this model year):** 5

> ⚠️  **5 NHTSA recalls** — among the highest in this dataset. Components: BACK OVER PREVENTION, ELECTRICAL SYSTEM, POWER TRAIN. [Full list](https://www.nhtsa.gov/recalls?make=lucid&model=air&year=2025)

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🟠 HIGH | range | Lucid Air GT 516 mi EPA; CR 70 mph test 344 vs 396 EPA-at-time (-52 mi). C/D 75 mph: 410 mi (-21% from 516). | ★★★ A |
| 🟡 MODERATE | build warranty | Lucid Air 2025: 5 NHTSA recalls — including TWO driveshaft and TWO backup-camera campaigns. At $100K+ this is notable. | ★★★ A |
| 🟡 MODERATE | range | Lucid markets 'up to 516 mi'; choosing 21in wheels (popular cosmetic upgrade) drops EPA range to 469 mi — a 47-mile cliff. | ★★★ A |

<details>
<summary>Full record detail (click to expand)</summary>

#### range / highway 70mph — 🟠 HIGH

_Lucid advertises 516 mi EPA for the Air Grand Touring AWD with 19-inch wheels — the longest EPA range of any production EV. Consumer Reports' 70 mph test measured 344 mi against 396 mi EPA-at-test-time, a 52-mile gap (tied for largest with F-150 Lightning and Rivian R1S). Car and Driver's 75 mph test on a 2022 Grand Touring measured 410 mi — still the longest result in C/D's EV database, but 21% below the current 516 EPA. The Lucid Air is a long-range leader; even its shortfall puts it ahead of competitors. But the magnitude of the gap from headline number is substantial._

- **Gap**: -106 mi (-20.5%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 48371](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=48371) (Tier 1)
- **Independent measurement**: [Consumer Reports — Real-World EV Range Comparison (Lucid Air -52 mi gap)](https://www.consumerreports.org/cars/hybrids-evs/real-world-ev-range-tests-models-that-beat-epa-estimates-a1103288135/) (Tier 2)

#### build_warranty / nhtsa recall density — 🟡 MODERATE

_The Lucid Air 2025 is subject to 5 NHTSA recalls. Notable: two separate driveshaft recall campaigns (25V669000 and 26V193000) — having to issue a second driveshaft recall after the first suggests the original remedy was incomplete, a quality-process concern. Similarly, two separate backup camera software recalls. Lucid markets the Air at $100K+ with 'meticulously engineered' luxury positioning. The recall pattern does not match this positioning._

- **Manufacturer claim**: [Lucid Motors — Air marketing](https://lucidmotors.com/air) (Tier 4)
- **Independent measurement**: [NHTSA recalls.gov — Lucid Air 2025](https://www.nhtsa.gov/recalls?make=lucid&model=air&year=2025) (Tier 1)

#### range / wheel size cliff — 🟡 MODERATE

_Lucid Air Grand Touring's headline 516 mi range applies only to the 19-inch aero-optimized wheel configuration. Buyers selecting the more visually preferred 21-inch wheels lose 47 mi of EPA range (516 → 469 mi). The headline figure is what marketing emphasizes; the wheel-size cliff is documented in fine print but rarely featured. This is similar to other manufacturers (Tesla Model Y 311 mi vs 327 mi by wheel) but the magnitude in the Lucid case is among the largest in our dataset._

- **Gap**: -47 mi (-9.1%)
- **Manufacturer claim**: [Lucid — Air marketing and configurator pages](https://lucidmotors.com/air) (Tier 4)
- **Independent measurement**: [EPA fueleconomy.gov — Lucid Air 21in trim](https://www.fueleconomy.gov/feg/Find.do?action=sbs&make=Lucid&model=Air%20G%20Touring%20XR%20AWD%20with%2021%20inch%20wheels) (Tier 1)

</details>

## Rivian R1S 2025 Dual Max (20in)

**EPA combined range:** 410 mi · **Starting MSRP:** $89,900 (delivered ≈ $94,550) · **NHTSA recalls (this model year):** 9

> ⚠️  **9 NHTSA recalls** — among the highest in this dataset. Components: ELECTRICAL SYSTEM, EXTERIOR LIGHTING, SEAT BELTS, SUSPENSION, VEHICLE SPEED CONTROL. [Full list](https://www.nhtsa.gov/recalls?make=rivian&model=r1s&year=2025)

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🟠 HIGH | ui ergonomics | Rivian markets 'minimalist, uncluttered' interior; CR characterizes the same design as 'extremely distracting.' | ★★ B |
| 🟠 HIGH | build warranty | Rivian R1S 2025: 9 NHTSA recalls in first model year — safety-critical components (battery, brakes, ADAS, fasteners). | ★★★ A |
| 🟡 MODERATE | charging | Rivian highlights '28 mi/hr' Level 2; the underlying full-charge time is ~15 hours (longest of major EVs). | ★★ B |
| 🟡 MODERATE | charging | Rivian claims 220 kW peak; CR notes it 'hasn't seen anywhere close to that' in its testing. | ★★ B |
| 🟡 MODERATE | range | Rivian advertises 410 mi (R1S Dual Max); CR's 70 mph highway test measured 358 mi — 52-mile (13%) gap. | ★★★ A |

<details>
<summary>Full record detail (click to expand)</summary>

#### ui_ergonomics / touchscreen distraction — 🟠 HIGH

_Rivian markets the R1S interior as minimalist and uncluttered. Consumer Reports independently characterizes the same design as 'extremely distracting' because tasks as basic as adjusting air vents require touchscreen interaction. Euro NCAP began penalizing pure-touchscreen designs in 2026, requiring physical/voice controls for safety-critical functions. The marketing narrative ('minimalist') and the safety reality (distraction) point in opposite directions._

- **Manufacturer claim**: [Rivian — R1S marketing site](https://rivian.com/r1s) (Tier 4) · [archive](http://web.archive.org/web/20260423204730/https://rivian.com/r1s)
- **Independent measurement**: [Consumer Reports — 2025 Rivian R1S Reviews, Ratings, Prices](https://www.consumerreports.org/cars/rivian/r1s/2025/overview/) (Tier 2)

#### build_warranty / nhtsa recall density — 🟠 HIGH

_The Rivian R1S 2025 is subject to 9 NHTSA recalls in its first model year, the highest count among the 13 products in this dataset. Recalls span safety-critical systems: cruise control / steering column, traction battery grounding, ADAS software, headlights, suspension critical fasteners, and seat belt anchorages. Rivian's marketing emphasizes durability and engineering. The 9-recall density during initial fleet rollout is materially higher than industry norms (most products in our dataset have 0–3 recalls) and is not reflected in the brand assurance language._

- **Manufacturer claim**: [Rivian — R1S marketing site](https://rivian.com/r1s) (Tier 4) · [archive](http://web.archive.org/web/20260423204730/https://rivian.com/r1s)
- **Independent measurement**: [NHTSA recalls.gov — Rivian R1S 2025](https://www.nhtsa.gov/recalls?make=rivian&model=r1s&year=2025) (Tier 1)

#### charging / level2 15 hours — 🟡 MODERATE

_Rivian's Level 2 home-charging marketing focuses on '28 mi/hr' — a number that sounds reasonable in isolation. The corresponding full-charge time on the 140 kWh Max battery is ~15 hours, longer than a single overnight charging window from low SOC. Buyers without an 80A continuous circuit (uncommon in US homes) will not be able to fully recharge an R1S Dual Max overnight after a low-battery day. This is not deception per se — the EPA-mandated 240V time is published — but the 28 mi/hr framing emphasizes a metric that minimizes the salience of the underlying limitation._

- **Manufacturer claim**: [Consumer Reports — 2025 Rivian R1S Road Test Report (citing manufacturer claim)](https://www.consumerreports.org/cars/rivian/r1s/2025/road-test-report/) (Tier 2)
- **Independent measurement**: [Consumer Reports — 2025 Rivian R1S Road Test Report](https://www.consumerreports.org/cars/rivian/r1s/2025/road-test-report/) (Tier 2)

#### charging / peak dc unrealistic — 🟡 MODERATE

_Rivian advertises 220 kW peak DC fast-charging for the R1S Dual Max. Consumer Reports has not observed acceptance rates close to the advertised peak in their testing — they describe the system as 'supposedly capable of a max acceptance rate of 200 kilowatts, but we haven't seen anywhere close to that.' This goes beyond the typical 'sustained briefly' tactic — even the peak appears not to be reproducibly observed under independent test conditions._

- **Manufacturer claim**: [Rivian — R1S spec page](https://rivian.com/r1s) (Tier 4) · [archive](http://web.archive.org/web/20260423204730/https://rivian.com/r1s)
- **Independent measurement**: [Consumer Reports — 2025 Rivian R1S Reviews, Ratings, Prices](https://www.consumerreports.org/cars/rivian/r1s/2025/overview/) (Tier 2)

#### range / highway 70mph — 🟡 MODERATE

_Rivian advertises 410 mi EPA range for the R1S Dual Max — the longest claim of any three-row electric SUV on sale. Consumer Reports' 70 mph highway test measured 358 mi. The 52-mile gap (12.7%) is one of the largest CR has documented across 26 tested EVs, tied with the Ford F-150 Lightning. EPA combined-cycle methodology consistently overstates highway range for heavy SUVs._

- **Gap**: -52 mi (-12.7%)
- **Manufacturer claim**: [EPA fueleconomy.gov — 2025 Rivian R1S Dual Max](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=48433) (Tier 1)
- **Independent measurement**: [Consumer Reports — 2025 Rivian R1S Road Test Report](https://www.consumerreports.org/cars/rivian/r1s/2025/road-test-report/) (Tier 2)

</details>

## Tesla Cybertruck 2025 AWD (Dual Motor)

**EPA combined range:** 325 mi · **Starting MSRP:** $79,990 (delivered ≈ $82,485) · **NHTSA recalls (this model year):** 2

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🟠 HIGH | range | Cybertruck Dual Motor advertised 318 mi; MotorTrend 70 mph test measured 224 mi — 30% gap, among worst in their 56-EV database. | ★★★ A |
| 🟠 HIGH | software features | Promised 500 mi at announcement; delivered 320 mi. Range Extender accessory ($16K) cancelled May 2025, never shipped. | ★★★ A |

<details>
<summary>Full record detail (click to expand)</summary>

#### range / highway 70mph — 🟠 HIGH

_Tesla advertises 318 mi range for the Cybertruck Dual Motor (Foundation Series with all-terrain tires). MotorTrend's instrumented 70 mph Road-Trip Range Test measured 224 mi — a 94-mile, 29.6% gap. MotorTrend characterized this as 'among the worst performers in our database of 56 EVs.' Recharged's synthesis of multiple independent tests puts typical highway range in the mid-200s. The Cybertruck's brick-shaped aerodynamics and weight make it especially prone to highway-speed range collapse._

- **Gap**: -94 mi (-29.6%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 49123](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=49123) (Tier 1)
- **Independent measurement**: [MotorTrend — 2024 Tesla Cybertruck Dual Motor Real-World Range Test](https://www.motortrend.com/reviews/2024-tesla-cybertruck-dual-motor-real-world-range-and-fast-charging-test) (Tier 2)

#### software_features / announcement promise 500 mi — 🟠 HIGH

_At Cybertruck's November 2019 reveal, Tesla and Elon Musk publicly promised 500+ mi range for the top-spec tri-motor 'Cyberbeast.' The vehicle shipped in 2024 with 320 mi range. Tesla announced a $16,000 Range Extender accessory (a secondary battery pack consuming a third of the truck bed) to bridge the gap; the extender was repeatedly delayed, then cancelled in May 2025 with full refunds — never delivered to a single customer. The 500 mi promise was a key driver of $1,000-deposit pre-orders during 2019–2024._

- **Gap**: -180 mi (-36.0%)
- **Manufacturer claim**: [Tesla — Cybertruck announcement event materials (November 2019)](https://www.tesla.com/cybertruck) (Tier 4) · [archive](http://web.archive.org/web/20260207141007/https://www.tesla.com/cybertruck)
- **Independent measurement**: [InsideEVs — Tesla Cybertruck Range Extender cancelled officially](https://insideevs.com/news/758916/tesla-range-extender-cancelled-officially/) (Tier 2)

</details>

## Tesla Model 3 2025 Long Range AWD

**EPA combined range:** 346 mi · **Starting MSRP:** $47,490 (delivered ≈ $48,880) · **NHTSA recalls (this model year):** 3

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🟡 MODERATE | range | Tesla Model 3 LR AWD 346 mi EPA; typical 75 mph testing 300–310 mi (~12% gap); Out of Spec ideal conditions hit 370 mi. | ★★★ A |

<details>
<summary>Full record detail (click to expand)</summary>

#### range / highway 70mph — 🟡 MODERATE

_Tesla advertises 346 mi EPA combined for the 2025 Model 3 Long Range AWD. Recharged's synthesis of independent tests puts typical 75 mph highway range at 300–310 mi (~12–14% gap). Notably, Out of Spec's instrumented 70 mph test achieved 370 mi on the 'Highland' refresh — exceeding EPA — making this product a partial counter-example: in ideal conditions Model 3 can match or beat EPA, but typical highway driving still falls short._

- **Gap**: -41 mi (-11.8%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 48764](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=48764) (Tier 1)
- **Independent measurement**: [Recharged — 2025 Tesla Model 3 Range Test (synthesis)](https://recharged.com/articles/2025-tesla-model-3-range-test) (Tier 2)

</details>

## Volkswagen ID.4 2025 AWD Pro S

**EPA combined range:** 263 mi · **Starting MSRP:** $50,990 (delivered ≈ $52,385) · **NHTSA recalls (this model year):** 1

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| 🟡 MODERATE | range | VW ID.4 AWD Pro S advertised 263 mi EPA; Car and Driver 75 mph test 240 mi (~9% gap). | ★★★ A |

<details>
<summary>Full record detail (click to expand)</summary>

#### range / highway 70mph — 🟡 MODERATE

_VW advertises 263 mi EPA combined for the ID.4 AWD Pro S. Car and Driver's instrumented 75 mph highway test measured 240 mi — a 9% gap. Recharged owner data shows typical 70–75 mph range of 190–215 mi for the AWD trim, suggesting most owners see somewhat larger real-world gaps than the C/D test methodology captures. The relatively modest 9% gap places ID.4 in the middle of the dataset's distribution._

- **Gap**: -23 mi (-8.7%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 48774](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=48774) (Tier 1)
- **Independent measurement**: [Car and Driver — 2024 Volkswagen ID.4 Tested](http://m.caranddriver.com/reviews/a60009160/2024-volkswagen-id4-dual-motor-drive/) (Tier 2)

</details>

## Ford Mustang Mach-E 2025 AWD Extended Range (Premium / Select)

**EPA combined range:** 300 mi · **Starting MSRP:** $50,490 (delivered ≈ $52,485) · **NHTSA recalls (this model year):** 0

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| ℹ️  INFO | range | Counter-example: Mach-E AWD Extended matched its 300 mi EPA almost exactly in CR's 70 mph test (299 mi). | ★★★ A |

<details>
<summary>Full record detail (click to expand)</summary>

#### range / highway 70mph — ℹ️  INFO

_Counter-example record. Ford Mustang Mach-E AWD Extended Range advertises 300 mi EPA combined. Consumer Reports' 70 mph instrumented highway test measured 299 mi — within 1 mile of the rating. Recharged characterizes the Mach-E as 'no range fraud' that 'matches or slightly beats its EPA combined rating on the highway in mild weather.' This product is documented as a counter-example demonstrating that range claims can be honest._

- **Gap**: -1 mi (-0.3%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 49079](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=49079) (Tier 1)
- **Independent measurement**: [Recharged — Ford Mustang Mach-E Real World Highway Range Guide](https://recharged.com/articles/ford-mustang-mach-e-real-world-range-highway) (Tier 2)

</details>

## Mercedes-Benz EQS 450 Plus 2025 RWD

**EPA combined range:** 390 mi · **Starting MSRP:** $105,550 (delivered ≈ $106,700) · **NHTSA recalls (this model year):** 0

### What's advertised vs. what's real

| Severity | Axis | One-liner | Evidence |
|---|---|---|---|
| ℹ️  INFO | range | Counter-example: Mercedes EQS 450+ closely matches or beats EPA (CR 380 vs 350; Edmunds 422 vs 350). | ★★★ A |

<details>
<summary>Full record detail (click to expand)</summary>

#### range / highway 70mph — ℹ️  INFO

_Counter-example record. Mercedes-Benz EQS 450+ has historically beaten its EPA rating in independent tests. Consumer Reports' 70 mph test on the 580 4Matic measured 380 mi against the 350 mi EPA at the time (later increased to 390 mi). Edmunds tested a 450+ at 422 mi — 72 miles above EPA, the largest positive gap they have recorded for any EV. This product is recorded to demonstrate that EPA-vs-real-world divergence is not unidirectional: some manufacturers file conservative range estimates and over-deliver in independent testing._

- **Gap**: -10 mi (-2.6%)
- **Manufacturer claim**: [EPA fueleconomy.gov vehicle 48388](https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=48388) (Tier 1)
- **Independent measurement**: [Consumer Reports — 2025 Mercedes-Benz EQS Road Test Report](https://www.consumerreports.org/cars/mercedes-benz/eqs/2025/road-test-report/) (Tier 2)

</details>

## Polestar 2 2025 Dual Motor (19in wheels)

**EPA combined range:** 276 mi · **Starting MSRP:** $55,300 (delivered ≈ $56,795) · **NHTSA recalls (this model year):** 0

_No deception records yet for this product._

---

## Methodology and limitations

- Sources are tiered: Tier 1 (EPA, NHTSA, court rulings) > Tier 2 (Consumer Reports, Edmunds, MotorTrend, etc.) > Tier 3 (owner forums, with N≥10 to cite) > Tier 4 (manufacturer claims — treated as the *claim*, not the truth).
- Read [LIMITATIONS.md](LIMITATIONS.md) before drawing population-level conclusions: selection bias, single-unit testing, software-update effects, and absence of manufacturer response are all real.
- This report is auto-generated. The underlying records are at `data/products/`, `data/deceptions/`, `data/tactics/`. Run `validate.py` to verify schema and referential integrity.

_Total: 13 products · 28 deception records · 13 tactic patterns documented._