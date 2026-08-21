# Hierarchical Competence-Authority Topology (HCAT)

## A Formal Model for the Distribution of CRAP in Technical Organizations

### GUM Supplemental Note

---

## Abstract

Technical organizations routinely assign work to individuals who possess some combination of the competence to understand it, the responsibility to complete it, the authority to make decisions concerning it, and the permission necessary to alter the systems in question. Less routinely, these properties are assigned to the same individual.

This note introduces **Hierarchical Competence-Authority Topology (HCAT)**, a framework for examining the organizational distribution of **Competence, Responsibility, Authority, and Permission (CRAP)**. Rather than treating competence as an intrinsic property of an employee or authority as an intrinsic property of a job title, HCAT models their placement relative to one another and to the work being performed.

Several common organizational pathologies emerge naturally from this representation. These include the **Post Turtle Condition**, in which authority substantially exceeds relevant competence; **Putt Inversion**, in which competence substantially exceeds authority; **Delegated Impossibility**, in which responsibility exceeds authority; and **Permissionless Accountability**, in which responsibility is assigned without sufficient operational permission to fulfill it.

The framework further identifies a routing phenomenon termed the **Competence Gravity Well**, wherein repeated successful intervention causes unresolved work to migrate toward a competent actor regardless of formal ownership, scope, authority, or access. In sufficiently mature organizations, such an actor may become the **Organizational Default Route (ODR)**, receiving problems primarily because no more specific route exists.

HCAT provides a topology for analyzing CRAP.

The implications are discussed.

---

## 1. Introduction

Technical management has long recognized that organizational hierarchy and technical competence are related, although rarely in the direction implied by the org chart.

The Peter Principle proposes that individuals in hierarchies tend to be promoted until reaching roles for which their previous competence no longer predicts success. Putt later focused this observation specifically on technical organizations, arguing that technological understanding and managerial control tend to become separated as hierarchies develop. His resulting corollary was characteristically concise:

> Every technical hierarchy, in time, develops a competence inversion.

Putt's work originated in articles published during the 1970s and was collected into *Putt's Law and the Successful Technocrat* in 1981, later appearing in a revised Wiley-IEEE edition. It occupies a useful position between management theory and the considerably more rigorous discipline of noticing what management actually does.

These prior formulations describe important properties of hierarchy, but they do not fully capture a recurring problem in contemporary DevOps, SRE, infrastructure, cloud engineering, platform engineering, cybersecurity, database administration, and other disciplines whose primary organizational function is explaining to management why changing a box in one system did not change a completely different box in another system.

Consider a typical technical task.

An organization would like a thing to occur.

Person A understands the thing.
Person B owns the thing.
Person C is accountable for the thing.
Person D possesses the credentials required to modify the thing.
Person E is asked why the thing has not occurred.

This arrangement is generally regarded as a team.

The present work proposes that these apparently distinct organizational inconveniences may be studied through a common framework.

We call this framework **Hierarchical Competence-Authority Topology**, or **HCAT**.

Readers may observe that alternative lexical arrangements could produce other acronyms. This observation is correct but not actionable.

---

## 2. The CRAP State Vector

Let each organizational actor \(i\), relative to some task \(t\), possess four normalized quantities:

$$
C_i(t) = \text{relevant competence}
$$

$$
R_i(t) = \text{assigned responsibility}
$$

$$
A_i(t) = \text{effective authority}
$$

$$
P_i(t) = \text{operational permission or control}
$$

For convenience, we define the actor's state as:

$$
\mathbf{x}_i(t) =
\left(
C_i,
R_i,
A_i,
P_i
\right)
$$
This ordered tuple will hereafter be referred to as the **CRAP vector**.
No significance should be inferred from the ordering of these terms beyond the obvious significance.
Each component is task-dependent.
An accomplished network engineer may exhibit:
$$
C \approx 1
$$

when diagnosing BGP convergence and:

$$
C \approx 0.07
$$

when repairing an Oracle stored procedure, notwithstanding the fact that both tasks occur near computers.

Likewise, organizational authority is not equivalent to operational permission. A vice president may possess considerable authority to demand that an AWS resource be changed while possessing no IAM permission whatsoever to change it personally.

Conversely, an engineer may possess administrator credentials while having no organizational authority to use them for the requested purpose.

This distinction turns out to matter.

---

## 3. CRAP Alignment

HCAT assumes that successful execution is favored when the relevant CRAP dimensions are sufficiently aligned.

For a task requiring action, the desirable condition is approximately:

$$
C \sim R \sim A \sim P
$$

The symbol \(\sim\) is used deliberately rather than equality, as the quantities involved cannot actually be measured on a common physical scale, and doing so would be ridiculous.  We therefore normalize them to decimal values and proceed anyway.

A generalized local misalignment function may be written:

$$
M_i =
w_{CA}|C_i-A_i|
+
w_{RA}|R_i-A_i|
+
w_{RP}|R_i-P_i|
+
w_{CP}|C_i-P_i|
$$

where the \(w\) terms are weighting coefficients selected according to organizational context, empirical evidence, author preference, or whichever values make Figure 2 look most persuasive.

Low \(M_i\) indicates that competence, responsibility, authority, and control are reasonably colocated.

High \(M_i\) indicates **CRAP misalignment**.

Importantly, HCAT does not assert that every employee should possess equal authority, competence, responsibility, and system access.

It asserts only that organizations should avoid assigning responsibility for changing a system to someone who:

1. does not own it,
2. cannot access it,
3. is not authorized to alter it,
4. did not create the problem,
5. cannot even log into several of the affected environments,

and then repeatedly ask that individual why the work remains incomplete.  This is considered a high-\(M\) configuration.

---

## 4. HCAT Is a Topology, Not a Score

The central claim of HCAT is that organizational dysfunction frequently arises not because competence, authority, responsibility, or permission are absent, but because they are **located in different places**.

Suppose a task \(t\) requires four capabilities:

```text
understand the problem
decide what should happen
own the outcome
perform the change
```

An organization may possess all four.

Nevertheless:

```text
Engineer A       understands the problem
Director B       can authorize the work
Manager C        owns the outcome
Administrator D  has the credentials
Consultant E     gets asked about it every Tuesday
```

No resource deficit exists.
The difficulty is topological.
The CRAP is poorly distributed.
HCAT therefore models not merely actors but the paths by which work, questions, approvals, escalations, and blame move between them.

Let:

$$
G = (V,E)
$$

where \(V\) is the set of organizational actors and \(E\) represents the available routes through which work or accountability may travel.

A technically healthy organization attempts to route work toward a node possessing an appropriate CRAP configuration.  A sufficiently mature enterprise instead routes work according to calendar availability.

---

## 5. The Post Turtle Condition

The familiar "post turtle" describes an individual observed in a position for which the observer cannot readily infer a plausible self-propelled route.

The turtle:

1. did not climb onto the post itself,
2. appears poorly adapted to its current altitude,
3. cannot perform many useful turtle functions while there,
4. was therefore presumably placed there by some external mechanism.

HCAT formalizes this observation as the **Post Turtle Condition (PTC)**.

For actor \(i\):

$$
A_i \gg C_i
$$

That is, task-relevant authority substantially exceeds task-relevant competence.

A simple Post Turtle Coefficient may therefore be defined:

$$
PTC_i =
\frac{A_i}{C_i + \epsilon}
$$

where \(\epsilon\) is a small stabilizing term included because division by zero would otherwise make the organizational implications unnecessarily explicit.  Large values of \(PTC\) indicate considerable hierarchical elevation relative to demonstrated role-relevant understanding.  This formulation also makes clear that incompetence itself is not necessarily hazardous.

An inexperienced junior employee with low competence and low authority presents limited systemic danger:

$$
C \ll 1,\quad A \ll 1
$$

The same competence attached to substantial decision authority produces:

$$
C \ll A
$$

and therefore elevated Post Turtle risk.

A turtle on the ground is merely a turtle.

A turtle on a post has acquired an **authority multiplier**.

---

## 6. Putt Inversion

The inverse condition is equally important.

Let:

$$
C_i \gg A_i
$$

Here the actor understands the system but lacks sufficient organizational authority to direct its behavior.  We call this **Putt Inversion**, after Putt's observation that technical hierarchies tend to separate those who understand technology from those who manage it.

Post Turtle and Putt Inversion are therefore mirror states:

```text
Post Turtle:      A >> C
Putt Inversion:   C >> A
```

An organization may contain both simultaneously.  Indeed, this is often the preferred implementation.
One employee understands precisely what must be done but lacks authority to approve it.
Another possesses authority to approve it but does not understand why it is necessary.

A meeting is then scheduled so that both may exchange these properties verbally without actually transferring either one.  The meeting concludes with an action item.

---

## 7. Delegated Impossibility

A second HCAT pathology occurs when responsibility exceeds effective authority:

$$
R_i \gg A_i
$$

We term this **Delegated Impossibility**.

The individual is held responsible for an outcome while lacking the authority necessary to cause the organizations controlling its prerequisites to act.

A useful indicator is the **Accountability-Authority Ratio**:

$$
DAR_i =
\frac{R_i}{A_i+\epsilon}
$$

As:

$$
A_i \rightarrow 0
$$

while:

$$
R_i > 0
$$

then:

$$
DAR_i \rightarrow \infty
$$

This is the **organizational accountability singularity**.
Beyond this point, additional management pressure cannot produce additional execution because the responsible actor lacks the causal mechanisms required to affect the requested state.  Nevertheless, pressure is commonly increased.

This produces several secondary outputs:

- status reports,
- escalation emails,
- follow-up meetings,
- risk-register entries,
- increasingly elaborate explanations of the same dependency,
- requests for updated ETAs,
- and measurable growth in executive urgency.

None of these alters the blocked system.

This can surprise management.

---

## 8. Permissionless Accountability

A particularly useful special case occurs when:

$$
R_i \gg P_i
$$
This condition shall be called **Permissionless Accountability**.
The actor may fully understand the required work and may even be considered responsible for its completion, yet lacks the system permissions necessary to inspect or alter the relevant state.

For example, consider a generalized cloud environment in which an organization wishes to normalize a set of metadata tags.

A technical specialist is asked to remediate them.

However:

- the specialist lacks access to several affected accounts,
- the specialist lacks permission to enumerate the relevant metadata,
- the specialist lacks permission to modify it,
- the organization's Cloud Operations function owns the environments,
- that function possesses both the access and organizational authority required,
- and an access request submitted previously remains unresolved.

The organization may nevertheless continue routing the tagging question to the specialist.
This behavior initially appears irrational.  Under HCAT it is easily explained.

Responsibility has been assigned independently of permission:

$$
R_s > 0,\quad P_s \approx 0
$$

The obvious remediation is to increase \(P_s\), decrease \(R_s\), or reroute the task to another actor whose existing CRAP vector is better aligned.

Organizations frequently select a fourth option:

$$
U \uparrow
$$

where \(U\) is Management Urgency.  This has the advantage of requiring no IAM changes.

---

## 9. Responsibility Displacement

HCAT also permits responsibility itself to move through the organizational graph.

We define **Responsibility Displacement** as the migration of ownership away from the actor possessing formal authority or control and toward an actor perceived as more likely to produce a successful outcome.

Let \(q_i\) denote perceived problem-solving effectiveness.

Then, informally:

$$
Pr(R_i \uparrow) \propto q_i
$$

even where:

$$
A_i \not\uparrow
$$

and:

$$
P_i \not\uparrow
$$

This produces a familiar organizational state:

1```text
"You seem to know how this works."

therefore

"This is yours now."
```

The transition is subtle because competence genuinely is relevant to work assignment.

The pathological step occurs when competence is treated as a substitute for ownership, authority, staffing, access, or scope.  A person who can explain why a database migration is failing does not thereby become the database migration team.

A person who identifies an IAM dependency does not thereby acquire IAM permissions.  A person who has once restarted a printer successfully should conceal this fact indefinitely.

---

## 10. The Competence Gravity Well

Responsibility Displacement becomes self-reinforcing.
Suppose actor \(i\) repeatedly resolves ambiguous or cross-domain problems.
Their perceived competence \(q_i\) increases.
As \(q_i\) increases, unresolved work is increasingly routed toward them:

$$
\frac{dR_i}{dt} \propto q_i
$$

The additional work exposes the actor to more systems, teams, dependencies, and historical context.

Consequently:

\frac{dC_i}{dt} > 0
$$

which further increases \(q_i\), causing still more work to arrive.

Thus:

$$
C \uparrow
\rightarrow
R \uparrow
\rightarrow
context \uparrow
\rightarrow
C \uparrow
$$

This positive feedback loop is termed the **Competence Gravity Well**.

At sufficient mass, the individual begins attracting problems for which no plausible formal relationship exists.
A certificate problem arrives.
Then a DNS problem.
Then a database problem.
Then SMTP.
Then IAM.
Then an application nobody knew still existed.
Eventually someone asks about procurement.
The actor has become an organizational singularity.
---

## 11. The Organizational Default Route

At the terminal stage of the Competence Gravity Well, the organization develops an **Organizational Default Route (ODR)**.

In network routing, a default route receives traffic for which no more specific route is known.
In organizations, the corresponding mechanism is:

```text
Does anyone know who owns this?
             |
             no
             |
             v
       Send it to Dave.
```

The ODR is not necessarily the most qualified person for the task.
Rather, the ODR is the person with the strongest historical record of making poorly classified problems disappear.

This distinction is important.

Let \(S(t)\) denote specificity of ownership information available for task \(t\).

Then:

$$
S(t) \rightarrow 0
$$

implies:

$$
Pr(t \rightarrow ODR) \rightarrow 1
$$

This routing policy is highly efficient in the short term.  It is also self-destructive.  Every successful intervention strengthens the route.

The reward for effectively resolving organizational ambiguity is therefore additional organizational ambiguity.  Eventually the ODR saturates.

We define **Default Route Saturation (DRS)** as the condition in which an actor's incoming problem rate exceeds their ability to forward, resolve, or refuse improperly routed work.

Symptoms include:

- unexplained calendar density,
- ownership of systems absent from the job description,
- attendance at meetings beginning with "we just thought you might know,"
- being included on incidents solely because "you were helpful last time,"
- and the discovery that taking vacation constitutes a resilience test.

---

## 12. The Expertise Disclaimer Paradox

Competent technical practitioners often employ explicit uncertainty calibration.

Typical statements include:

```text
"I'm not an expert in this area."
"This is outside my primary domain."
"I think X is happening, but someone closer to the system should confirm."
"If there is a specialist here, they should drive."
```

These statements are generally intended to communicate epistemic boundaries.

They do not necessarily mean:

```text
"I have no idea what is happening."
```

A highly experienced generalist may possess enough adjacent knowledge to diagnose a problem correctly while still recognizing that a domain specialist has deeper expertise.

This creates the **Expertise Disclaimer Paradox**:

> Repeated successful performance by an actor who explicitly disclaims expertise may cause observers to infer that expertise was unnecessary rather than that the actor maintains a conservative threshold for claiming expertise.

The process is straightforward:

```text
competent actor
      |
      v
accurately disclaims expertise
      |
      v
solves problem anyway
      |
      v
observers retain outcome
but discard calibration
      |
      v
"apparently you don't need
an expert for this"
```

This can have unfortunate second-order effects.  Suppose two actors make the following statements.

Actor A:

```text
"I'm about 70% confident the issue is X.
Before changing anything, test Y."
```

Actor B:

```text
"It's X."
```

If X proves correct, an organization observing only prediction accuracy may score both actors equally.
An organization that also rewards expressed confidence may score Actor B higher.  Thus poor uncertainty calibration may become positively reinforced.  The resulting selection pressure favors certainty independently of knowledge.  HCAT therefore distinguishes **competence** from **performed certainty**.

This distinction is recommended.

---

## 13. The False Modesty Hazard

Expertise disclaimers create another problem when repeatedly issued by actors whose baseline competence is unusually broad.

If a person says:

```text
"I'm not a database expert."
```

and subsequently identifies the database problem, the organization updates.

If the same person later says:

```text
"I'm not a DNS expert."
```

and identifies the DNS problem, the organization updates again.

After sufficient repetitions, the phrase:

```text
"I'm not an expert."
```

may become operationally indistinguishable from:

```text
"I will now solve this."
```

This is undesirable.

Worse, less competent actors may imitate the disclaimer without reproducing the calibration underlying it.

The organization has now learned an incomplete ritual:

```text
1. Announce non-expertise.
2. Continue making decisions.
```

The omitted step:

```text
1.5 Determine whether you actually know what the hell you are doing.
```

is difficult to encode in policy.

We therefore caution against interpreting epistemic humility as evidence that domain expertise is optional.

The fact that a sufficiently experienced systems practitioner can reason across an unfamiliar subsystem does not imply that unfamiliarity is itself a qualification.

---

## 14. HCAT Failure Modes

The principal CRAP imbalances may be summarized as follows:

| Condition | Relationship | Interpretation |
|---|---|---|
| Post Turtle | \(A \gg C\) | Authority exceeds relevant competence |
| Putt Inversion | \(C \gg A\) | Competence exceeds authority |
| Delegated Impossibility | \(R \gg A\) | Responsibility exceeds decision authority |
| Permissionless Accountability | \(R \gg P\) | Responsibility exceeds operational control |
| Unaccountable Authority | \(A \gg R\) | Decision authority exists without corresponding ownership |
| Unused Expertise | \(C \gg R\) | Relevant competence exists but is not incorporated into execution |
| Competence Mismatch | \(R \gg C\) | Responsibility exceeds relevant competence |
| Unbounded Agency | \(P \gg C\) | Operational control exceeds demonstrated competence |

The final condition should be monitored carefully.

---

## 15. CRAP Propagation

HCAT failures rarely remain local.

Suppose actor \(i\) has high responsibility but insufficient permission:

$$
R_i \gg P_i
$$

The task cannot progress.

Management observes the lack of progress and increases urgency.

The actor responds by escalating to actor \(j\), who possesses permission but insufficient responsibility:

$$
P_j \gg R_j
$$

Actor \(j\) reasonably prioritizes other work.

Management therefore escalates again.

After several iterations, the organization may produce:

- three project managers,
- two directors,
- a severity-one bridge,
- an executive sponsor,
- a shared spreadsheet,
- and no person simultaneously possessing \(R\) and \(P\).

The original technical task remains unchanged.

We call this **CRAP propagation**.

The amount of organizational activity increases while effective alignment does not.

A rough expression is:

$$
Activity \uparrow
\not\Rightarrow
M \downarrow
$$

This result is left as an exercise for the reader's employer.

---

## 16. HCAT and Incident Response

HCAT is particularly useful during incidents because crises expose hidden organizational topology.
Under normal conditions, documentation may imply:

```text
Team A owns Service X.
```

During an outage, the actual topology becomes visible:

```text
Team A owns Service X.
Team B has production credentials.
Team C understands the application.
An engineer who left eight months ago understood the deployment.
The vendor owns the load balancer configuration.
Nobody owns DNS.

Scott is driving.
```


Incident response therefore provides an empirical method for discovering HCAT structure.

Observe:

1. who is contacted,
2. who can answer questions,
3. who can approve decisions,
4. who can execute changes,
5. who is blamed for delays.

These frequently identify five different people.

---

## 17. HCAT Intervention Strategy

Traditional organizational remediation often begins by asking:

> Who owns this?

HCAT recommends four questions instead:

```text
Who understands it?
Who is responsible for the outcome?
Who can authorize the decision?
Who can actually alter the system?
```

These correspond directly to:

$$
C,\;R,\;A,\;P
$$

If the answers differ substantially, the organization should resist the immediate temptation to schedule a recurring synchronization meeting.

Instead, one or more dimensions should be moved.

Examples include:

### 17.1 Increase Permission

Appropriate where:

$$
C,R,A > P
$$

Grant the responsible actor the access necessary to perform the work.

This technique is sometimes controversial because it requires completing the IAM ticket.

### 17.2 Transfer Responsibility

Appropriate where another actor already possesses the required competence, authority, and permission.

Formally:

$$
R_i \rightarrow R_j
$$

This is commonly called "letting the team that owns the thing do its job."

### 17.3 Increase Authority

Appropriate where competent actors repeatedly identify required action but cannot cause it to occur.

### 17.4 Acquire Competence

Appropriate where authority and control already exist but understanding does not.

Possible mechanisms include:

- training,
- consultation,
- documentation,
- hiring,
- asking someone,
- or, in extreme cases, checking before publicly declaring that the technology does not work that way.

### 17.5 Reduce Responsibility

This intervention is rarely considered because responsibility is inexpensive to assign.

It is nevertheless valid.

---

## 18. The HCAT Maturity Model

For organizations requiring a maturity model before acknowledging an observable fact, we provide one.

### Level 1: Accidental

CRAP is distributed primarily through historical circumstance.

Ownership is inferred from whoever last touched the system.

### Level 2: Documented

Roles and responsibilities are recorded.

The records are incorrect.

### Level 3: Managed

Responsibility and authority are generally aligned.

Permissions remain governed by a separate process with a six-week SLA.

### Level 4: Adaptive

Work is routed toward appropriately competent actors while authority and operational control are deliberately aligned with responsibility.

The organization can identify and correct CRAP misalignment before an incident exposes it.

### Level 5: Optimized

Level 4 has been renamed, placed in a branded quadrant, and certified by an external consultancy.
The organization now possesses an HCAT Transformation Roadmap.  No further improvement is measurable, although several workshops remain.

---

## 19. Discussion

HCAT should not be interpreted as an argument that technical experts should automatically hold managerial authority.

Such a conclusion would merely invert one form of misalignment into another.  Competence is contextual.

The engineer best able to diagnose a packet-loss problem is not automatically the person best suited to allocate a department's budget, resolve personnel disputes, or determine strategic investment.

Likewise, management competence is itself a legitimate competence.

The relevant question is whether decision authority concerning a technical system can interact effectively with the competence necessary to understand the consequences of those decisions.

The healthiest condition is therefore not:

$$
C = A
$$

but functional adjacency among the CRAP dimensions.  

- Authority must be reachable from competence.  
- Responsibility must be accompanied by control. 
- Permission must be bounded by competence and accountability.  

And work should not migrate indefinitely toward whoever happened to fix the previous unrelated emergency.  

HCAT therefore reframes organizational effectiveness as a routing problem.  The organization already contains much of what it needs.  The packets are simply going to strange places.

---

## 20. Limitations

Several limitations should be acknowledged.

First, competence cannot be reliably represented as a scalar quantity.  Second, authority is contextual and socially mediated.
Third, responsibility may be formal, perceived, implicit, retrospective, or assigned immediately after an outage.  Fourth, permission may consist of technical access, procedural authorization, political permission, or possession of the one password written on the whiteboard in Conference Room B.

Consequently, the CRAP vector cannot presently be measured with scientific precision.  This limitation is not expected to impede adoption by the management consulting industry.

Future work may therefore include development of:

- the HCAT Organizational Readiness Assessment,
- CRAP heat maps,
- CRAP radar charts,
- CRAP maturity dashboards,
- quarterly CRAP reviews,
- enterprise CRAP benchmarking,
- AI-assisted CRAP detection,
- and certification programs for organizations wishing to demonstrate that their CRAP conforms to industry best practices.

A subscription model is being considered.

---

## 21. Conclusion

Technical organizations do not fail solely because they lack competent people, adequate authority, clear responsibility, or sufficient operational permission.

They also fail because these capabilities are distributed independently and then treated as though an org chart causes them to coincide.

HCAT provides a framework for examining that distribution.

Its central construct, the CRAP vector,

$$
(C,R,A,P)
$$

captures four properties necessary for effective technical action:

**Competence** to understand what should be done.
**Responsibility** for ensuring that it happens.
**Authority** to make the necessary decisions.
**Permission** to alter the systems involved.
Misalignment among these dimensions produces recognizable organizational states.
When authority exceeds competence, we observe the **Post Turtle Condition**.
When competence exceeds authority, we observe **Putt Inversion**.
When responsibility exceeds authority, we observe **Delegated Impossibility**.
When responsibility exceeds permission, we observe **Permissionless Accountability**.

When a competent actor repeatedly compensates for these failures, work begins to migrate toward that actor through the **Competence Gravity Well**, potentially creating an **Organizational Default Route**.

These effects are neither exotic nor difficult to observe.

In many organizations, asking four questions is sufficient:

```text
Who knows?
Who owns?
Who decides?
Who can?
```

If the answers identify four different people, the organization may have an HCAT problem.  If the fifth answer is the consultant, it almost certainly does.

---

## References

Putt, A. *Putt's Law and the Successful Technocrat*. Original edition, 1981; revised edition, Wiley-IEEE Press, 2006.

Peter, L. J., and Hull, R. *The Peter Principle*. William Morrow, 1969.

Adams, S. *The Dilbert Principle*. HarperBusiness, 1996.

The Grand Unified Model of DevOps/SRE Dynamics (GUM), because apparently the existing literature had not yet contained enough equations.
