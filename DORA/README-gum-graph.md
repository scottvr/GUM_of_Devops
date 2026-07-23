# how to read the "gum-graph" html visualizer/explorer
The html/js app is designed to visualize the math and meaning from the paper.
This README is dual-function; to document the app, and as my presentataion notes
when walking through it.

## the Z term 
Healthy - normalized to 1.000
everything else measured in units of "how many orgs of damage is this decision worth?"

# Navigation
## Session Controls
how the *app/demo* behaves, **not** what the org does.

### Freeze controls during simulation - checkbox, default ON
- **What:** When ON, the time simulation projects forward without writing its
  projected values back into the sliders. When OFF, scrubbing time lets the
  projection rewrite TDR (and in coupled mode M, LT, CFR) in the controls.
- **Model effect:** None - this is about who owns the sliders, you or the future.
- **On screen:** With freeze OFF in the Time tab, sliders visibly walk as you
  scrub. Toast + state chip confirm which regime you're in.

>Freeze is the difference between *forecasting* the organization and
>*becoming* it. We'll leave it on; we've all seen what happens otherwise.

### DORA Lens - checkbox, default ON
- **What:** Visual highlighting of the observed vs. latent split.
- **Model effect:** None. Purely epistemological.
- **On screen:** The four DORA rows get an amber edge and tint; everything
  latent (morale, urgency, mismatch, volatility, debt, remediation) dims to
  55% opacity.

>This is what your metrics vendor can see. Note that the dimmed
>rows are still *in the equation* - dimming a variable does not remove it
>fom your organization. It only removes it from your dashboard.

### Institutional Momentum Mode - checkbox, default ON (off = Strict Scientific Posture)
- **What:** Swaps the copy register across the page. Strict is the deadpan
  straight man; Momentum lets the satire surface.
- **Model effect:** None - same math, different honesty.
- **On screen:** Kicker flips between "A Structured Descriptive Model" and
  "A Grand Unified Model"; "Debt derivative" becomes "Debt Velocity Vector";
  the critical-regime diagnosis gains "Resume Driven Development detected";
  the Z line gains its rhetorical-manageability confession.

>The model has two postures: the one for the methods section and
>the one for the retro. The numbers are identical in both, which is rather
>the point.

### DF dynamics mode - select: Conservative (OG GUM) / Endogenous (Exploratory)
- **What:** Whether deployment frequency is an *input you claim* or an
  *outcome you earn*.
- **Model effect:** Conservative: DF_eff = the slider - DF is an observed
  policy input, faithful to the paper; latent terms never rewrite it.
  Endogenous: DF_eff = DF × A(t), the attenuation state - dysfunction erodes
  how often you actually ship, no matter what the roadmap says.
- **On screen:** Assumption banner text changes; in the Time tab the DF_policy
  and DF_eff tickers diverge; the waterfall's "Effective DF(t)/DF" factor
  drops below 1.000; velocity-driven debt accrual shrinks accordingly.

>Conservative mode believes your stated deploy frequency.
>Endogenous mode has met your organization.

### Quiet toasts - checkbox, default OFF
- **What:** Toast style: center-stage announcements vs. small bottom-right
  murmurs with shorter lifetimes.
- **Model effect:** None.

>Notifications, like urgency, are configurable in
>amplitude but not in existence.

### Pin Baseline / Copy Permalink - buttons
- **What:** Pin captures the complete current state as a comparison anchor;
  the Current vs Baseline card then shows absolute values and signed % deltas
  for P_inst, Ω, debt attenuation, and the urgency term as you move things.
  Permalink serializes *everything* - sliders, tabs, toggles, scrub time, even
  which sections are collapsed - into the URL.
- **Model effect:** None; instrumentation of the instrument.

>Pin Baseline is for before-and-after experiments: pin the org you
>have, then apply management. The permalink means any organizational
>pathology you can configure, you can also share. This is either a feature
>or a threat, depending on your role.

---

## Organizational Archetypes

*(Six presets spanning ~28 orders of magnitude of realized output. Every one
of these numbers is in units of 'healthy organizations'.)*

| Preset | P_inst | Felt urgency U_eff | Throughput vs healthy |
|---|---|---|---|
| Elite Performer | 69.0 | 0.50 (policy 0.50 - *dampened*) | 35.7× |
| High Performer | **1.000** (the anchor) | 1.27 (policy 1.00) | 1.00× |
| Under Pressure | 0.056 | 3.67 (policy 2.50) | **1.00×** |
| Legacy Bog | 0.0019 | 1.82 (policy 1.20) | 0.016× |
| Incident Loop | 9.0 × 10⁻¹⁴ | 6.28 (policy 4.00) | 0.017× |
| Max Entropy | 1.3 × 10⁻²⁶ | 7.54 (policy 4.80) | 0.0053× |
- **Elite Performer** - "High trust, low chaos." Note U_eff ≤ policy U: a
  healthy attenuation state *dampens* imposed urgency slightly. 
>In a coherent organization, a deadline is just information.
- **High Performer** - the calibration anchor; loads by default. 
>We normalized reality to the healthiest org we could responsibly imagine.
>Everything else on this list is a fraction of one of these.
- **Under Pressure** - the thesis demo. Throughput bar reads *exactly* 1.00×,
  identical to High Performer - the pipeline term is blind to distress -
  while realized output is 18× lower, all of it lost through the attenuation
  terms. 
>Same pipeline. Same deploy cadence. The dashboards agree
>everything is fine. This is Proposition 2 rendered as a bar chart: an
>increase in deployment-related activity does not, by itself, imply an
>increase in realized delivery value.
- **Legacy Bog** - debt-dominant but *calm* (low U, low E). Lead time of 48
  hours does the strangling; TDR 0.7 taxes what's left.
>Nobody here is panicking. That is the only nice thing the model has to say about it.
- **Incident Loop** - CFR 0.45 under U 4.0 puts an exponent of ~39 on the
  failure term: (0.55)^39 ≈ 10⁻¹¹.
>A 45% change-failure rate is survivable. A 45% change-failure rate 
>*under maximum urgency* is an extinction event. 
>Urgency doesn't change your failure rate - it changes what your failure rate costs.
- **Max Entropy** - subtitle "The literature review." Let the 1.3 × 10⁻²⁶ 
>sit in silence for a beat. -nothing. The number is the joke.

---

## DORA Delivery Variables

*(The observed layer - what the industry already measures, kept faithfully.)*

### DF - Deployment Frequency
- **Model:** Linear multiplier in the numerator - cadence scales output. But
  it also feeds debt: κ₂·DF_eff in the debt derivative - velocity mints debt.
  In endogenous mode, dysfunction erodes it.
- **On screen:** Throughput bar, waterfall's nominal-throughput line, and the
  "+k2·DF_eff·A: velocity-driven debt" grid cell all move.

>Shipping more is genuinely good - it's in the numerator. It is
>also a debt-accrual term. The model permits both facts at once, which is
>more than most quarterly reviews manage."

### LT - Lead Time for Changes (hrs)
- **Model:** Denominator - pure temporal friction. Nothing rescues you from a
  long lead time; it divides everything.
- **On screen:** Drag it right and the score falls smoothly; LT usually ranks
  high (negative) in the Sensitivity card.

>Lead time is friction. It has no redeeming exponent, no clever
>coupling. It just divides your output, hour by hour."

### CFR - Change Failure Rate
- **Model:** Enters as the *base* of (1−CFR)^(U_eff²). Alone, at low urgency,
  it's nearly benign. Under urgency the exponent detonates it.
- **On screen:** The CFR sweep tab has "Compare at U=1.0 / U=3.5" buttons -
  the same CFR curve drawn in two urgency regimes. Use this. It is the most
  persuasive chart in the app.

>Failure rate is not a cost. It's a *base*. Management urgency is
>the exponent. You can have either one safely. You cannot have both."

### MTTR - Mean Time to Restore (hrs)
- **Model:** Adds to the denominator alongside LT - recovery time is
  friction on the same axis as delivery time.

>The model doesn't distinguish time spent shipping from time spent
>un-shipping. Neither does your calendar.

---

## Organizational Perturbation Terms

*(The latent layer - what affects delivery but doesn't appear on dashboards.
With DORA Lens on, these are literally dimmed. They are not less real.)*

### M - Developer Morale Multiplier
- **Model:** Direct linear multiplier on output. But also a component of the
  attenuation state A(t) - low morale amplifies felt urgency and accelerates
  debt integration. Below 1.0 the paper calls it the degradation regime.
- **On screen:** Morale bar; the M sweep tab draws a dashed "M=1 threshold"
  line; in coupled-mode time simulation, M *erodes autonomously* under
  sustained urgency and debt pressure - you can watch it fall without
  touching the slider.

>Morale is the only variable here that multiplies everything and
>is measured by nothing. The model gives it a symbol. Your org gives it an
>annual survey.

### U - Management Urgency
- **Model:** The interesting one. U appears *nowhere in the numerator* - added
  pressure adds no output. It acts purely as an exponent on (1−CFR), and via
  felt urgency U_eff = U·(1 + 0.6·(1−A)): the worse your attenuation state,
  the more each unit of imposed urgency is experienced as. Healthy orgs
  dampen it (Elite: ×0.998); degraded orgs amplify it (Max Entropy: ×1.57).
  Also mints debt at κ₁·U_eff².
- **On screen:** The live note under the slider ("Currently felt as U_eff =
  …") turns red past ×1.35 amplification. The expanded equation shows the
  policy/felt pair. The U sweep is the default chart.

>Urgency is the only management input with no direct production
>term - it only changes what your fragility costs. And note the felt-urgency
>line: dysfunction amplifies the urgency that produces it. This is the
>model's one genuine feedback loop, and every practitioner in this call has
>lived inside it.

### Cm - Competence Mismatch
- **Model:** Exponential suppressor inside Ω = exp(−α·Cm − β·E), and a debt
  source (κ₃·Cm - mismatch-driven debt: wrong decisions compound).
- **On screen:** Coherence Ω bar falls; mismatch-driven debt cell rises.

>Competence mismatch both suppresses today's output and mints
>tomorrow's debt - misalignment between authority and ability is the only
>term in this model that charges you twice, with full procedural legitimacy.

### E - Executive Volatility
- **Model:** Exponential suppressor inside Ω only. Deliberately *not* a debt
  source - matching the paper's debt equation, which has no κ·E term.

>Volatility doesn't accrue debt - it doesn't stay pointed at
>anything long enough to. It just scrambles direction faster than the system
>can converge. Mismatch compounds; volatility dissipates.

---

## Debt and Remediation

### TDR - Technical Debt Ratio
- **Model:** The compounding drag: e^(−λ·TDR) multiplies everything. Also the
  app's one true *state variable* - in the Time tab it evolves via
  dTDR/dt = (κ₁U_eff² + κ₂DF_eff + κ₃Cm)·A − κ₄R.
- **On screen:** Debt-drag bar; the four-cell derivative grid (which sums to
  the displayed rate - auditable live); "accumulating / slowly growing /
  being paid down" trend word.

>Debt is not a penalty, it's an interest rate. The slider is where
>you are; the derivative underneath is where you're going. Most orgs report
>the first and are surprised by the second on a recurring basis.

### R - Remediation Rate
- **Model:** The deliberate asymmetry. (1−R) taxes visible throughput *now*;
  −κ₄·R pays debt down *later*. Raising R makes today's number worse,
  guaranteed, and tomorrow's trajectory better, invisibly.
- **On screen:** Raise R: score dips immediately; the debt derivative goes
  negative; run the time simulation and watch the trajectories cross.
  Warning: the Sensitivity card - which is local and instantaneous - will
  dutifully report R as *harmful*. It is telling the truth about this
  quarter.

>Here's the trap fully armed: every short-horizon measurement in
>this tool says remediation is bad. The sensitivity ranking says cut it.
>The score says cut it. Only the integral disagrees - and nobody reports
>the integral.

---

## Value and Sensitivity Constants

*(The knobs behind the curtain. these are
chosen with the same rigor as the phenomena they represent - illustratively.)*

- **V - Business Value per Change:** Scalar on the numerator. "Whether the
  deploys were worth deploying - a term the model includes and dashboards
  don't."
- **λ - Debt sensitivity:** How brutally TDR taxes output (steepness of
  e^(−λ·TDR)). "How much your architecture forgives."
- **α / β - Competence / Volatility sensitivity:** The Ω weights - how hard
  your particular organization's physics punish mismatch vs. churn. 
  
Every org has its own exchange rate between confusion and chaos; these are yours.
   

## The 90-second walkthrough

1. Click **High Performer** -> "1.000. This is the unit of reality."
2. Drag the **U sweep chart** rightward -> curve collapses -> "urgency-induced
   instability: the exponent at work."
3. **Time Simulation** tab -> **Play** at 1× -> debt accumulates, P_inst decays,
   diagnosis degrades -> "the integral nobody reports."
4. Click **Max Entropy** -> pause -> let 1.3 × 10⁻²⁶ speak.
5. Click **High Performer** again -> "and this is why R exists."
