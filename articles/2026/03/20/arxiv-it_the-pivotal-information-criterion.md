---
title: "The Pivotal Information Criterion"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2603.04172"
published: "2026-03-20"
fetched: "2026-03-20T17:08:42.988678"
---

Mathematics > Statistics Theory
[Submitted on 4 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:The Pivotal Information Criterion
View PDF HTML (experimental)Abstract:The Bayesian and Akaike information criteria aim at finding a good balance between under- and over-fitting. They are extensively used every day by practitioners. Yet we contend they suffer from at least two afflictions: their penalty parameter $\lambda=\log n$ and $\lambda=2$ are too small, leading to many false discoveries, and their inherent (best subset) discrete optimization is infeasible in high dimension. We alleviate these issues with the pivotal information criterion: PIC is defined as a continuous optimization problem, and the PIC penalty parameter $\lambda$ is selected at the detection boundary (under pure noise). PIC's choice of $\lambda$ is the quantile of a statistic that we prove to be (asymptotically) pivotal, provided the loss function is appropriately transformed. As a result, simulations show a phase transition in the probability of exact support recovery with PIC, a phenomenon studied with no noise in compressed sensing. Applied on real data, for similar predictive performances, PIC selects the least complex model among state-of-the-art learners.
Submission history
From: Maxime Van Cutsem [view email][v1] Wed, 4 Mar 2026 15:26:32 UTC (712 KB)
[v2] Thu, 19 Mar 2026 15:35:12 UTC (712 KB)
Current browse context:
math.ST
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
Papers with Code (What is Papers with Code?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
