```
this used to be situated in the middle of the apology-retraction errata update.
then some weeks later apparently that hangover was done and I re-read it.
the incoherence is shocking, but some points I want to save to revise at a later date.
```

Around this same time, engineering organizations were learning what their Devs already knew - the Ops part of DevOps requires 
a distinct set of knowledge and skills, which by and large software developers had not spent their careers... developing. 
Further, the fact that management was now able to classify what used to be CapEx as OpEx by moving to the cloud, Executive 
Intuition told them that surely just like the On-prem datacenters of recent past, that they could excise entire Cost Centers 
full of Reliability Engineers, too, and that now since Infrastructure is Code, developers can easily add "do DevOps" to their 
list of responsibilities. That is certainly a way one could read the SRE book and to interpret the DevOps philosophy; it is just 
not the way any practitioner of Dev, or Ops, or of DevOps would do so.

It may be the case that visibility into spend, outside of the development cycle itself  - which had already been duly appointed 
with measurable attrbutes surfaced as metrics - has not been clearly instrumented after changing operational models, infrastructure, 
headcount, and the metrics themselves, as discussed here. Organizations that had previously maintained "functionality" to be  
synonymous with "feature", may have to update their understanding about what a Non-Functional Requirement is once it is their 
entire site that becomes "non-functional". Whether a given system was highly-stable, interemittently available, poorly or 
well-secured, the production application run state was no longer "someone else's problem" for software engineering orgs. 

While management offered support by way of words like "Kubernetes" and "orchestration", believing that abstracting away many of 
the layers beneath the lowest level of Infrastructure understood by even many experienced application developers would prevent 
them from needing to understand it at all, as it turns out - a poorly behaving component may remain in a suboptimal state with 
no directly-visible impact to the larger system, allowing an application service to achieve apparently stable "uptime", just as 
an area changing color from black and white at a high enough frequency on a 50% duty cycle can give the appearance of a gray 
steady-state; having many short-lived disposable virtualized containers come into and out of existence by some poorly understood 
mechanism may be fine if your application is gray, and cost is not a concern.  

As teams adjust to this new *NoOps-without-calling-it-NoOps* reality, they may begin to see that their 100% availability was 
camouflaged (in gray) by 200% Cloud spend. Regardless, Reliability is now at least partially a concern of the application 
software engineering organizationa, and even without any further changes, may continue to weigh more heavily on the developers.

It was then evidently decided that two years had been enough time for developers to have learned a career's worth of Infrastructure 
Operations, Monitoring, and Automation experience - and to grow accustomed to being in on-call rotations - all while continuing to 
ship features and fix bugs. It should be noted that much of the tooling, processes, procedures, and code required to support the 
design, setup, configuration, maintenance, integration, hosting, routing, migration, deployment, instrumentation and automation of  
the systems that run the systems that contain the applications being developed - no matter how well-documented - will make little 
sense to the developer if it is written in languages foreign to them.

Developers, like anyone, have a natural aversion to sleep-deprivation. Coupling that aversion with high-stress situations involving 
management that isn't likely to understand what they're seeing yet nevertheless inexplicably insist on watching a screenshare from 
the on-call respurce responding in real-time to a Sev-1 Incident at 3:00am is empirically proven to heighten the *instinct* to avoid 
such situations, yet it does not automatically increase the *ability* to do so.  
