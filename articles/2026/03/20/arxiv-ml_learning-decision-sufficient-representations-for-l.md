---
title: "Learning Decision-Sufficient Representations for Linear Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18551"
published: "2026-03-20"
fetched: "2026-03-20T13:14:28.853187"
---

Mathematics > Optimization and Control
[Submitted on 19 Mar 2026]
Title:Learning Decision-Sufficient Representations for Linear Optimization
View PDF HTML (experimental)Abstract:We study how to construct compressed datasets that suffice to recover optimal decisions in linear programs with an unknown cost vector $c$ lying in a prior set $\mathcal{C}$. Recent work by Bennouna et al. provides an exact geometric characterization of sufficient decision datasets (SDDs) via an intrinsic decision-relevant dimension $d^\star$. However, their algorithm for constructing minimum-size SDDs requires solving mixed-integer programs. In this paper, we establish hardness results showing that computing $d^\star$ is NP-hard and deciding whether a dataset is globally sufficient is coNP-hard, thereby resolving a recent open problem posed by Bennouna et al. To address this worst-case intractability, we introduce pointwise sufficiency, a relaxation that requires sufficiency for an individual cost vector. Under nondegeneracy, we provide a polynomial-time cutting-plane algorithm for constructing pointwise-sufficient decision datasets. In a data-driven regime with i.i.d.\ costs, we further propose a cumulative algorithm that aggregates decision-relevant directions across samples, yielding a stable compression scheme of size at most $d^\star$. This leads to a distribution-free PAC guarantee: with high probability over the training sample, the pointwise sufficiency failure probability on a fresh draw is at most $\tilde{O}(d^\star/n)$, and this rate is tight up to logarithmic factors. Finally, we apply decision-sufficient representations to contextual linear optimization, obtaining compressed predictors with generalization bounds scaling as $\tilde{O}(\sqrt{d^\star/n})$ rather than $\tilde{O}(\sqrt{d/n})$, where $d$ is the ambient cost dimension.
Current browse context:
math.OC
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
