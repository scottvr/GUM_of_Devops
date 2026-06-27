Initial load baselineAction: Open page with no query params.
Expect: Left sections default state (first open, others collapsed), state chip visible, Current vs Baseline says no baseline pinned.

Urgency toggle is reversible (no drift)Setup: vizMode = sweep (Parameter Sweep tab), do not touch sliders.
Action: Toggle Enable urgency activity boost ON, then OFF, then ON, then OFF.
Expect: Score/equation returns to same OFF value each time OFF is selected (no cumulative drift).

Urgency toggle in time mode does not silently rewrite controlsSetup: vizMode = time, freeze OFF, set t=0 first.
Action: Toggle urgency ON/OFF a few times without moving time.
Expect: Sliders do not “walk” unexpectedly; state reflects toggle only.

Freeze behavior is explicit and consistentSetup: vizMode = time, move t to mid-horizon (e.g. 8-12).
Action: Toggle freeze ON then OFF.
Expect:ON: projection does not write into controls.
OFF: time projection can write projected values into relevant controls.
Toast and state chip match actual behavior.


Adopt simulated state claritySetup A: projectionMode = debt, t=0.
Action: Click Adopt simulated state.
Expect: “No control changes...” toast (or equivalent).
Setup B: move to later t, click again.
Expect: TDR changes; toast lists changed fields.
Setup C: switch to projectionMode = coupled, later t, click adopt.
Expect: TDR/M/LT/CFR can change; toast lists changed keys.

Pin baseline semantics are understandableSetup: Pick any state, click Pin Baseline.
Action: Change one or two sliders.
Expect: Current vs Baseline shows:pinned context line (mode/projection/freeze/time/preset/custom)
absolute current vs baseline values
signed percent deltas.


Preset highlight integrityAction: Click a preset (e.g. High Performer).
Expect: matching preset button active.
Action: Move any slider slightly.
Expect: preset highlight clears (shows effectively custom state).

Collapsible left panel URL persistenceAction: Collapse/expand a custom combination of sections.
Action: Copy permalink, open in new tab.
Expect: Same collapsed/open pattern restored.

URL round-trip for major stateAction: Set non-default values for tab, projection mode, freeze, urgency toggle, time, sweep axis, series toggles.
Action: Copy permalink and open.
Expect: UI restores those states accurately; state chip and controls agree.

KaTeX still rendersAction: Hard refresh.
Expect: Equation area still properly rendered (no raw delimiters visible).
