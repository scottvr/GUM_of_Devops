# Tokenmaxxing
## On Converting an AI Expense into an Organizational Accomplishment

The Grand Unified Model of DevOps/SRE Dynamics (GUM) includes a small number of organizational proxies for its latent terms. Many more, and considerably more potent, proxies were originally drafted for publication. They were omitted out of concern that publishing an extensive catalog of coercive measurement techniques might encourage organizations to use them as an extensive catalog of coercive measurement techniques.

With the development of the Grand Unified Tool (GUT), the subsequent representational hardening of GUM 1.5, and the ongoing preparation of GUM 2.0, it has become necessary to revisit the relationship among measures, metrics, indicators, KPIs, targets, and incentives.

This supplemental note provides that foundation through a case study in Tokenmaxxing: the organizational practice of treating token consumption as evidence of productive AI adoption.

The argument is simple:

> Token consumption is a metered input. Once elevated from measure to indicator, KPI, target, and incentive, it ceases to be a reliable indicator of productive AI adoption and begins actively distorting the work it was intended to improve.

## 1. A Brief Terminological Misadventure

### 1.1 Measure and Metric in Mathematics

In mathematics, a measure assigns a non-negative number to measurable subsets of a set. Given a sigma-algebra $\Sigma$ over a set $X$:

$$
\mu: \Sigma \to [0, \infty].
$$

It assigns zero to the empty set and is countably additive over pairwise disjoint measurable sets.

A metric defines a notion of distance between points in a set:

$$
d: M \times M \to \mathbb{R}.
$$

It is non-negative, symmetric, satisfies the triangle inequality, and equals zero only when its arguments are identical.

For example, the measure of the interval $[a,b]$ is:

$$
b-a.
$$

The Euclidean metric between $(a,b)$ and $(c,d)$ is:

$$
\sqrt{(a-c)^2 + (b-d)^2}.
$$

### 1.2 Organizational Use

What does this distinction have to do with production dashboards, DORA delivery metrics, or organizational KPIs?

Absolutely nothing.

The formal mathematical distinction is not the distinction ordinarily intended by management dashboards. The reuse of mathematical terminology in organizational measurement is another mild symptom of the science envy endemic to the field.

For present purposes:

- **A measure** is a direct observation or count: a raw value.
- **A metric** is a measure, or combination of measures, interpreted for some purpose: a raw value with context.
- **An indicator** is a metric interpreted as evidence of a broader condition.
- **A KPI** is an indicator granted institutional importance because it is believed to represent progress toward an objective.
- **A target** is a desired value, threshold, direction, or ranking assigned to the KPI.
- **An incentive** attaches consequences to reaching, missing, or appearing to reach the target.

The terminology is not used consistently. Dashboards commonly call every number a metric, including raw counts. An OKR may incorporate one or more KPIs as evidence that progress has been made toward an objective. This does not make the evidence valid. It makes the evidence official.

The organizational transformation can be summarized as:

```text
observation
    -> interpretation
    -> inference
    -> institutional importance
    -> prescription
    -> consequence
```

Or, in the terminology used here:

```text
measure
    -> metric
    -> indicator
    -> KPI
    -> target
    -> incentive
```

Each transition adds meaning or force that was not present in the original observation.

For example:

**Measure:**

```text
8 failed changes
```

**Metric:**

```text
8 failed changes / 96 total changes = 8.3% change failure rate
```

**Indicator:**

```text
change failure rate is interpreted as evidence of delivery quality
```

**KPI:**

```text
change failure rate is reviewed as an organizational performance indicator
```

**Target:**

```text
change failure rate <= 10%
```

**Incentive:**

```text
rankings, compensation, status, or executive scrutiny depend on the target
```

The measure reports an observation. The metric places it in context. The indicator assigns broader meaning. The KPI makes that meaning institutionally important. The target prescribes the desired result. The incentive gives the prescription operational force.

## 2. Relevance to GUM

A taxonomy of organizational measurement would not, by itself, justify a GUM Supplemental Note.

The important point is that incompetence, dishonesty, and malice are not required for accepted measurement practices to produce catastrophe. Once an observable proxy is made consequential, participants can rationally optimize it while degrading the condition it was intended to represent.

A team held below a change-failure-rate target may respond by:

- Reclassifying failed changes.
- Redefining what constitutes a deployment.
- Delaying the declaration of failure.
- Excluding selected services or change classes.
- Transferring high-risk work outside the measured boundary.
- Avoiding changes likely to damage the reported rate.
- Negotiating the numerator.
- Negotiating the denominator.

At no stage is irrationality required. The organization communicates its objective in prose but implements it through incentives. Participants may understand the intended objective perfectly while still adapting rationally to the specification that carries operational force.

## 3. Case Study: Tokenmaxxing

### 3.1 Observation

An employee or agent sends requests to an AI model.

Those requests consume input tokens, output tokens, cached tokens, and sometimes reasoning tokens.

### 3.2 Measures

The organization can directly observe:

- Input tokens consumed.
- Output tokens generated.
- Reasoning tokens consumed.
- Number of model calls.
- Number of agent sessions.
- Dollar cost.
- Runtime.

These are direct observations of resource consumption. They answer:

> What resources were consumed by this workload?

They do not answer:

> What useful result did this workload produce?

### 3.3 Metrics

The organization begins deriving comparative values:

- Tokens per employee.
- Tokens per day.
- Tokens per coding session.
- Tokens per pull request.
- AI sessions per engineer.
- Percentage of employees using AI weekly.
- AI expenditure per team.

Some derived values may become legitimate operational metrics:

- Tokens per completed task.
- Cost per accepted change.
- Tokens per resolved incident.
- Tokens per successful experiment.
- Inference cost per validated outcome.

These may help compare models, tools, prompts, languages, workflows, or task classes. Their usefulness depends on whether the numerator describes a meaningful and consistently evaluated result.

### 3.4 Indicator

Then comes the first unearned inferential step:

> High token use indicates extensive AI adoption.

Zero recorded consumption strongly suggests an absence of activity within the measured system. High consumption establishes that activity occurred. It does not establish that the activity was useful.

The inference is already lossy:

```text
token consumption ~= AI activity
```

It does not follow that:

```text
token consumption = useful AI-assisted work
```

Token consumption alone cannot distinguish among:

- Useful exploration.
- Repeated failed attempts.
- Needlessly large context.
- Poorly configured agents.
- Redundant parallel work.
- Generated code later discarded.
- Genuine high-value automation.
- Deliberate inflation of usage.

The same observed token count may arise from any of these causes.

### 3.5 KPI

Management now elevates the indicator to a KPI:

> KPI: AI token consumption per employee.

The stated objective may be reasonable:

> Objective: accelerate productive organizational AI adoption.

But the selected proxy describes **input consumption**, not adoption quality.

The assumed causal chain is:

```text
more tokens
    -> more AI use
    -> greater AI fluency
    -> more work produced
    -> greater business value
```

Each arrow requires evidence.

A green dashboard does not provide evidence.

### 3.6 Target

The indicator becomes normative:

- Employees should increase token usage.
- Teams should rank highly on AI consumption.
- Managers should encourage maximum utilization.

At this stage, the organization has converted a **cost-bearing input** into a desired **output**.

This is unusually perverse because resource consumption is ordinarily minimized subject to achieving a result. CPU time, cloud spend, bandwidth, storage, operations, and labor hours are treated as costs incurred in production.

The organization has therefore selected a metered expense and declared its maximization to be evidence of progress.

### 3.7 Incentive

Leaderboards, recognition, management attention, performance discussions, or cultural status attach consequences to the number.

Employees now correctly infer:

- The organization says it values useful AI adoption.
- The organization can observe token consumption.
- Token consumption appears on the dashboard.
- Therefore, token consumption is what the organization can reward.

This is a rational adaptation to the observable reward function.

### 3.8 Gaming and Behavioral Adaptation

The implemented reward function admits several predictable adaptations:

- Use larger models than necessary.
- Include oversized context windows.
- Run more agents in parallel.
- Request verbose output.
- Avoid caching or context reuse.
- Re-run satisfactory work.
- Delegate trivial operations to an agent.
- Generate many alternatives that nobody reviews.
- Leave loops running longer.
- Prefer workflows that expose metered usage.
- Avoid efficient local or deterministic tools.

A conventional command may complete the work quickly and earn no visible AI-usage credit. An agent may complete the same work less efficiently while incrementing the favored counter.

No dishonesty is required. Employees need only reorganize their work sincerely around what management visibly rewards.

### 3.9 The Goodhart Failure

The measured quantity now loses value as an indicator of meaningful AI adoption.

The organization can no longer tell whether increased consumption reflects productive adoption because it has itself created alternative causes for the increase.

The original inference was:

> High token consumption may suggest substantial AI activity.

After incentives are introduced, the inference becomes:

> High token consumption may suggest substantial AI activity, metric optimization, inefficiency, poor tooling, or some combination of the four.

The organization has entered Goodhart territory.

The proxy is no longer merely imperfect. It has become endogenous to the reward system built around it.

### 3.10 The Campbell Failure

Campbell's Law takes the argument beyond degradation of the indicator.

Pressure on the measure corrupts the process being monitored:

- Engineering choices become less efficient.
- Model and tool selection becomes distorted.
- Costs rise independently of value.
- Employees learn performative rather than effective AI use.
- Useful non-AI tools are displaced.
- Security and intellectual-property exposure may increase.
- Management receives increasingly misleading adoption data.
- Genuine skeptics and careful users may appear unproductive.

The attempt to govern AI adoption through token counts degrades both the count and the adoption process itself.

### 3.11 The Complete Transformation

**Objective:**

Improve productive organizational use of AI.

**Measure:**

Tokens consumed.

**Metric:**

Tokens consumed per employee or team.

**Indicator:**

High consumption is interpreted as high AI adoption.

**KPI:**

Employee or team token usage appears on management dashboards.

**Target:**

Employees are encouraged or expected to maximize consumption.

**Incentive:**

Rankings, recognition, status, or performance consequences.

**Adaptation:**

Users select token-intensive behavior regardless of marginal value.

**Goodhart effect:**

Token consumption ceases to reliably indicate useful AI adoption.

**Campbell effect:**

Work practices, costs, tool choices, reporting, and organizational learning are corrupted by pressure to raise the indicator.

**Observed dashboard result:**

AI adoption rises dramatically.

**Possible underlying reality:**

The organization has become better at consuming AI, not necessarily better at producing anything.

## 4. Tokens Belong in the Denominator

The particularly elegant absurdity is that token consumption is not even a defective approximation of output in the same way that lines of code might be. It is primarily a metered input and therefore an exceptionally poor output metric.

By the same reasoning, CPU utilization would measure developer productivity and fuel consumption would measure driver effectiveness.

Both resources may be necessary.

Neither resource is the product.

Tokens belong in the denominator:

```text
completed useful outcomes / token cost
accepted changes / token cost
validated defects removed / token cost
time saved / token cost
business value produced / inference cost
```

Even these ratios require care. "Useful outcome," "accepted change," "validated defect," "time saved," and "business value" are not self-validating terms. They require definitions, controls, and evidence.

Still, these formulations preserve the correct direction of concern: produce a useful result while treating token consumption as a cost, constraint, or optimization variable.

**Token consumption is a metered input. Its consumption is not the product.**

## Conclusion

Token consumption is a useful measure of token consumption.

It may support cost accounting, capacity planning, model comparison, anomaly detection, and the evaluation of particular workflows. It may also provide weak evidence that some form of AI activity occurred. None of these properties makes it a measure of productive AI adoption, engineering effectiveness, employee fluency, or business value.

The failure begins when the organization moves carelessly from observation to interpretation:

```text
tokens were consumed
    -> AI was used
    -> useful work occurred
    -> capability improved
    -> value was produced
```

Each arrow introduces an inference that must be demonstrated rather than decorated with a dashboard.

Once token consumption becomes a KPI, target, or source of status, the organization creates additional reasons for tokens to be consumed. The resulting increase can no longer be attributed confidently to useful adoption because management has deliberately introduced metric optimization as a competing cause.

This is not principally a story about dishonest employees, foolish managers, or defective AI tools. It is a routine GUM-compatible interaction among proxies, incentives, local optimization, and incomplete observability. Participants may behave sincerely and rationally throughout while collectively producing an expensive simulation of progress.

Tokens are an input to AI-assisted work. Their consumption may be necessary, excessive, efficient, wasteful, productive, or performative. The count alone cannot distinguish among these states.

Organizations wishing to improve AI-enabled work should evaluate useful outcomes subject to token cost rather than treating token cost itself as the outcome. Tokens belong in the denominator, the budget, or the diagnostic telemetry.

They do not belong on the victory banner.

The organization that rewards token consumption will become very good at consuming tokens.

This result should not be confused with becoming good at anything else.
