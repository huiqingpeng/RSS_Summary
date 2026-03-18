---
title: "RETRO SYNFLOW: Discrete Flow Matching for Accurate and Diverse Single-Step Retrosynthesis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2506.04439"
published: "2026-03-18"
fetched: "2026-03-18T16:18:21.902546"
---

Computer Science > Machine Learning
[Submitted on 4 Jun 2025 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:RETRO SYNFLOW: Discrete Flow Matching for Accurate and Diverse Single-Step Retrosynthesis
View PDF HTML (experimental)Abstract:A fundamental problem in organic chemistry is identifying and predicting the series of reactions that synthesize a desired target product molecule. Due to the combinatorial nature of the chemical search space, single-step reactant prediction -- i.e. single-step retrosynthesis -- remains challenging even for existing state-of-the-art template-free generative approaches to produce an accurate yet diverse set of feasible reactions. In this paper, we model single-step retrosynthesis planning and introduce RETRO SYNFLOW (RSF) a discrete flow-matching framework that builds a Markov bridge between the prescribed target product molecule and the reactant molecule. In contrast to past approaches, RSF employs a reaction center identification step to produce intermediate structures known as synthons as a more informative source distribution for the discrete flow. To further enhance diversity and feasibility of generated samples, we employ Feynman-Kac steering with Sequential Monte Carlo based resampling to steer promising generations at inference using a new reward oracle that relies on a forward-synthesis model. Empirically, we demonstrate \nameshort achieves $60.0 \%$ top-1 accuracy, which outperforms the previous SOTA by $20 \%$. We also substantiate the benefits of steering at inference and demonstrate that FK-steering improves top-$5$ round-trip accuracy by $19 \%$ over prior template-free SOTA methods, all while preserving competitive top-$k$ accuracy results.
Submission history
From: Robin Yadav [view email][v1] Wed, 4 Jun 2025 20:46:05 UTC (8,390 KB)
[v2] Mon, 16 Mar 2026 19:25:53 UTC (8,384 KB)
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
