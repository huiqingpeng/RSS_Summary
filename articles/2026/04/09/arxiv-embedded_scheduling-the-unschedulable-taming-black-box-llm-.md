---
title: "Scheduling the Unschedulable: Taming Black-Box LLM Inference at Scale"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2604.06970"
published: "2026-04-09"
fetched: "2026-04-10T07:04:50.386607"
---

Computer Science > Distributed, Parallel, and Cluster Computing
[Submitted on 8 Apr 2026]
Title:Scheduling the Unschedulable: Taming Black-Box LLM Inference at Scale
View PDF HTML (experimental)Abstract:When output token counts can be predicted at submission time (Gan et al., 2026), client-side scheduling against a black-box LLM API becomes semi-clairvoyant: decisions condition on coarse token priors even though the provider's internals remain hidden. We decompose this boundary problem into three separable concerns: allocation (inter-class share via adaptive DRR), ordering (intra-class sequencing with feasible-set scoring), and overload control (explicit admit/defer/reject on a cost ladder). An information ladder experiment shows that coarse magnitude priors -- not class labels alone -- are the practical threshold for useful client control; removing magnitude inflates short-request P95 by up to $5.8\times$ and degrades deadline satisfaction. Under balanced / high congestion the full stack achieves 100% completion, 100% deadline satisfaction, and useful goodput of $4.2 \pm 1.6$ SLO-meeting requests/s with short P95 within tens of milliseconds of quota-tiered isolation. A predictor-noise sweep confirms graceful degradation under up to 60% multiplicative error. Heavy-dominated regimes separate policies on completion, tail, and interpretable shedding. We further compare short-priority allocation (biased toward interactive traffic) with Fair Queuing (round-robin across classes): Fair Queuing achieves +32% short-request P90 improvement over FIFO with only +17% long-request overhead, versus Short-Priority's +27% / +116% trade-off -- demonstrating that the allocation layer accommodates different fairness objectives without changing the remaining stack. We contribute the three-layer client-side decomposition, controlled evaluation of joint metrics across regimes, allocation-policy alternatives, and overload-policy evidence linking cost-ladder shedding to the stated service objective.
Current browse context:
cs.DC
References & Citations
export BibTeX citation
Loading...
Bibliographic and Citation Tools
Bibliographic Explorer (What is the Explorer?)
Connected Papers (What is Connected Papers?)
Litmaps (What is Litmaps?)
scite Smart Citations (What are Smart Citations?)
Code, Data and Media Associated with this Article
alphaXiv (What is alphaXiv?)
CatalyzeX Code Finder for Papers (What is CatalyzeX?)
DagsHub (What is DagsHub?)
Gotit.pub (What is GotitPub?)
Hugging Face (What is Huggingface?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
