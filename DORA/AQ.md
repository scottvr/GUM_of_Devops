# AQ
### Asked Questions (with no mention of Frequency)

---

- *"Your slider says U=1 but the equation says 1.27?"* 

Felt urgency: the attenuation state amplifies imposed pressure. 
The UI labels it, the note under the slider explains it
might be the best talking point that surfaces from the UI

- *"The debt grid terms — do they sum to the rate?"* 

Yes, exactly (to display rounding). 
The κ's are the paper's; the inputs are felt/effective quantities 
weighted by A(t), stated in the note  above the grid.

- *"Where do the constants come from?"* 

The same place your story-point velocity targets come from, 
but with the derivation shown.

- *"Is this a joke?"* — 

The paper is satirical. The structure is not. Three
peer-reviewed papers this cycle formalized the pipeline, the developer,
and the debt. This model merely adds the thing that keeps perturbing all
three.


- Failure Rate (CFR) and Lead Time (LT)—already capture this friction as lagging indicators? Why do we need a complex new calculus to measure social dysfunction if the resulting delivery delay is already showing up in the baseline math?

If it isn't clear, I am not lobbying for the literal addition of these metrics, or casting any 
aspersions on the DORA metrics themselves. (Well, that's not entirely true; I have written an 
unpublished screed about the ontological crisis of "the fifth metric", Reliability, but that's
neither here nor there,) Rather, I wrote the paper, and in the specific voice that it's in, i
primarily as a way to more loudly and less politely state things that Nathen and company have 
repeated every year when the big report comes out, which is something along the lines of "please 
don't use DORA metrics like that" and maybe "did you skip the part about the DORA Capabilities? 
We really think you should read that too before you go instrumenting..."  

These folks are too nice for that. But I think there has been a real need for someone to call 
attention to the dysfunction of the org, that might be helped by the Capabilities, but only wants to focus on the metrics, and to abuse them, wielding them as a cudgel, or making them the target in 
flagrant violation of Goodhart... and maybe I needed to do some venting, around the topic of misaligned incentives. ...  a cathartic expression of practitioner resentment, bordering at times on practitioner rage.

All that said though, I would like to refer back to what I said earlier: it is intentionally humorous,
but it is not a "joke paper". And some of that humor takes shape as absurdity. What should remind you 
that it is not "just a joke" is that there is a non-zero number of managers who read the GUM and think i
it failed by not explicitly enumerating more proxies in more detail. That's where absurdity becomes 
frightening and not at all funny. So to bring that back around to your question specifically: while those 
metrics may be seen as lagging indicators that the astute may ascribe to their root cause with some
analysis, I would argue that they should be explicitly called out, and refined because they are not just
latent variables that are lagging indicators, they feed back into the system they emerge from too, in the
shape of compounding or exponential decay. i

The organization itself is not a neutral substrate, it shapes
the delivery mechanism and the variables within.


- *You noted in your literature review that once technical bottlenecks are automated away, the friction simply relocates ... If DevOps just moves the traffic jam higher up the org chart, are we actually getting faster, or are we just waiting faster? And can [GUM fix it]?*

This question is timely, especially as we adopt more - and *more capable* - Transformer models as agentic
developers; even without shifting the burden, we're already rapidly moving increasingly to a "hurry up 
and wait" state. And I think as we do this it is revealing more and more that writing code was never 
the bottleneck in the first place. Get machines to write code faster, now the bottleneck is review; get
agents to take that on too, now the bottleneck is QA. We can do this exercise repeatedly and find new
technical or human resource constraints as the bottleneck at each iteration. 

And so to take a step back to a central point of the GUM, the problem is not any specific organism 
within the organization, the problems are systemic and belong to the whole of the organization. I do 
not claim to have the answers on how to fix the sociotechnical problems within any particular 
organization, but I do claim that the larger system that any team operates in - that is, the software 
factory organization itself - is the root cause of any symptoms displayed by the folks living and working
within it and a direct contributor to - perhaps the main factor in - determining the delivery rate, and
more importantly in my view, the quality of the product ultimately produced.
