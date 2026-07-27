### ERRATA

We would like to formally address the previous brief note where we had acknowledged that the present-day DORA model
has changed to include a "fifth metric", and that they had "caught up" to the GUM insofar as accounting for rework by 
naming it as a metric, a result being that the DORA metrics formulation is now different than the one used in 
"The Grand Unified Model of DevOps/SRE Dynamics", but we now feel a retraction is in order.

An earlier version of this document erroneously ascribed blame to the author of "The Grand Unified Model of Devops (GUM)"
for the initial omission -- and subsequent awkward handling -- of the so-called "fifth" DORA metric. However, upon further
review of the historical record, this mea culpa was entirely unwarranted. The confusion surrounding this metric is not a 
failure of the author’s scholarship, but rather a direct result of the DevOps Research and Assessment (DORA) organization's 
prolonged ontological crisis regarding its own framework. The record must hereby be corrected to reflect that the author is blameless.

For years, the industry operated under the elegant stability of the Four Key Metrics: Deployment Frequency, Lead Time for Changes, 
Mean Time to Recovery (MTTR), and Change Failure Rate. This was a closed, perfectly balanced system. It measured the velocity and 
stability of software delivery with rigorous clarity. 

Then, in 2018, the Accelerate State of DevOps report disrupted this equilibrium by introducing a fifth element: Availability. 
The rationale was plausible enough -- velocity means little if the underlying system is offline -- yet bolting a deeply 
operational concern onto a framework historically dedicated to delivery pipelines felt structurally suspect. It was a subtle, 
creeping expansion of scope, but the industry largely complied and adjusted its slide decks accordingly.

The taxonomic drift accelerated in 2019. In what appeared to be a convergence of academic research and corporate branding   
following Google's acquisition of DORA, Availability was quietly retired in favor of "Reliability." This brought the metric 
conveniently into alignment with Google's own Site Reliability Engineering (SRE) nomenclature by which they gave a generation 
of "sysadmins" a finally respectable title which incorporates the word "Reliability". The fifth metric had not only changed 
scope but, like the sysadmin before it, had also undergone a rebrand.

[typo-laden rant that was previously here moved to its own document such that the author might recover from sleep-deprivation and 
perhaps revise it to be more suitable for reading](rant-wasidrunkorsomething.md)

Nevertheless, once Reliability was thoroughly entrenched as the indisputable "Fifth Key Metric" across the corporate landscape, DORA 
initiated a sweeping epistemological walk-back.  Beginning around 2021, subsequent publications began to delicately clarify that 
Reliability was not, strictly speaking, a software delivery metric at all. Instead, it was categorized as an operational performance 
metric. So the messaging subtly shifted again: the original four metrics measure the pipeline, while Reliability measures the outcome. 
It was no longer the fifth sibling in the metric family, but rather the foundational constraint against which the other four are judged.
One does not simply measure Reliability alongside Lead Time; one achieves the former to justify the latter. DORA had seemingly realized 
that adding a fifth wheel to a perfectly good car does not make it a better car, so they declared the fifth wheel to be the road itself.

Within all of that greater context, any previous apologies for failing to accurately classify this moving target are formally retracted. 
Until the broader DevOps community and the framework's authors can definitively agree on whether this crucial Non-Functional Requirement 
is a metric, an operational outcome, a foundational constraint, or a state of mind, the author’s initial adherence to the foundational 
four-metric model stands as an act of rigorous historical preservation rather than as an oversight.
