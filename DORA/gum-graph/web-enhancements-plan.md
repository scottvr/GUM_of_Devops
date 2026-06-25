Plan
GUM Demo Upgrade Plan (Full Ambitious Set)
Summary
Implement a full v1.5 upgrade of the existing single-page demo to clearly separate instantaneous vs cumulative output, add time-based simulation and coupled-organization projection, and expand diagnostic/teaching affordances (baseline compare, sensitivity, waterfall, permalinks, light toasts) while preserving the current sweep panel behavior.

Key Changes
UI cleanup and correctness
Keep current architecture (index.html + doragum.css) and avoid file split in this pass.
CSS cleanup in doragum.css: remove duplicate/unused tokens, define missing --text-bright, remove broken --background/unused borrowed vars, keep DORA palette only.
HTML accessibility cleanup in index.html: add type="button" to all buttons, add explicit <label for> for each slider (retain current visual labels), and add missing aria-label where needed.
Rename primary output label from P_real — Realized Output to Instantaneous realized-output rate and normalize notation to P_inst/P_cum labels (no mixed unicode variants).
Keep existing parameter sweep panel and tabs intact as-is.
Model layer expansion
Refactor JS into explicit model functions: computeOmega, computeTerms, computePInst, computePCum, stepDebtOnlyState, stepCoupledState, simulateTrajectory.
Add urgency visible-activity coupling as optional term:
urgencyActivityBoost(U) = 1 + 0.25 * log1p(U)
Toggle-controlled in computePInst (urgencyBoost on/off).
Add healthy normalization calibration:
Compute Z = computeRawP(presets.healthy) at init.
Use calibrated output by default and show basis in UI copy.
Keep debt dynamics equation as current dTDR/dt = K1*U + K2*DF + K3*Cm - K4*R for paper-faithful mode.
Add projection modes:
Debt only (default): evolve only TDR.
Coupled organization: evolve TDR + morale/lead-time/CFR per bounded coupling step.
New Time Simulation tab and controls
Add top-level chart mode tabs in output area: Parameter Sweep and Time Simulation.
Time Simulation panel includes:
Horizon slider 0..36 periods (default 24).
Scrubber-first timeline (works without animation).
Play/Pause + speed options 0.25x, 1x, 4x, Ludicrous (16x).
Series toggles: P_inst, P_cumulative, TDR, optional Omega/Morale coupling.
Readout at current scrubbed time (t, projected TDR, P_inst, P_cum).
Adopt simulated state button:
Debt-only mode: copies projected TDR into live slider.
Coupled mode: copies evolved TDR, M, LT, CFR into live sliders.
Simulation defaults: dt=0.25, Euler integration, clamp bounded variables each step.
Diagnostics and presentation affordances
Add baseline pin/compare block:
Pin Baseline captures full current slider state and options.
Show deltas for P_inst, Omega, debt attenuation, urgency term.
Add sensitivity ranking block:
Local one-at-a-time sensitivity via finite difference around current state (±5% bounded perturbation), ranked by absolute impact on P_inst.
Add multiplicative waterfall block:
Show nominal throughput then multiplicative attenuations (M, Omega, remediation capacity, CFR/U term, debt drag) ending in realized output.
Add light, conference-safe toast notifications for toggles (coupled mode, urgency boost, baseline pinned, permalink copied).
Permalink/state sharing
Add URL query serialization and hydration for sliders + toggles + active tab/mode/scrub time.
On load: parse, clamp/validate, apply; fallback to defaults if invalid.
Add Copy Permalink action.
Public Interface / Data Shape Changes
URL contract adds keys for all slider vars and UI mode flags (tab, projectionMode, urgencyBoost, series, horizon, time, etc.).
Internal simulation row shape standardized:
{ time, P_inst, P_cum, TDR, dTDR, omega, debt_att, cfr_term, M, LT, CFR }
In debt-only mode, non-evolving fields remain current-policy constants.
Test Plan
Math/model checks
Healthy preset yields P_inst ≈ 1.0 under calibrated mode.
P_cum is monotonic non-decreasing when dt>0.
Debt-only mode evolves only TDR; coupled mode evolves extra fields within clamps.
Urgency boost toggle increases early U sweep output but high-U fragility still dominates.
UI behavior checks
Sweep panel unchanged and still draggable.
Time tab scrubber updates readout without animation.
Play/pause and speed changes update time correctly and stop at horizon.
Adopt simulated state writes correct slider values by mode.
Baseline compare, sensitivity ranking, and waterfall refresh on slider/mode changes.
Accessibility and robustness
All buttons have type="button".
Sliders are label-associated and keyboard operable.
Invalid URL params are safely clamped/ignored without breaking render.
Canvas labels consistently use P_inst/P_cum.
Assumptions and Defaults
Keep single-file JS in index.html for now (no module split in this pass).
Keep existing sweep chart visual design and interaction semantics.
Default projection mode is Debt only; coupled mode is explicitly marked speculative.
Default urgency-activity boost is off (demo toggle).
Header date copy is updated to match your upcoming presentation month/year (July 2026).
