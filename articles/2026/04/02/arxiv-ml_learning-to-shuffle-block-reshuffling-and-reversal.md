---
title: "Learning to Shuffle: Block Reshuffling and Reversal Schemes for Stochastic Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00260"
published: "2026-04-02"
fetched: "2026-04-03T07:19:36.419555"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Learning to Shuffle: Block Reshuffling and Reversal Schemes for Stochastic Optimization
View PDF HTML (experimental)Abstract:Shuffling strategies for stochastic gradient descent (SGD), including incremental gradient, shuffle-once, and random reshuffling, are supported by rigorous convergence analyses for arbitrary within-epoch permutations. In particular, random reshuffling is known to improve optimization constants relative to cyclic and shuffle-once schemes. However, existing theory offers limited guidance on how to design new data-ordering schemes that further improve optimization constants or stability beyond random reshuffling. In this paper, we design a pipeline using a large language model (LLM)-guided program evolution framework to discover an effective shuffling rule for without-replacement SGD. Abstracting from this instance, we identify two fundamental structural components: block reshuffling and paired reversal. We analyze these components separately and show that block reshuffling strictly reduces prefix-gradient variance constants within the unified shuffling framework, yielding provable improvements over random reshuffling under mild conditions. Separately, we show that paired reversal symmetrizes the epoch map and cancels the leading order-dependent second-order term, reducing order sensitivity from quadratic to cubic in the step size. Numerical experiments with the discovered algorithm validate the theory and demonstrate consistent gains over standard shuffling schemes across convex and nonconvex benchmarks.
Current browse context:
cs.LG
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
