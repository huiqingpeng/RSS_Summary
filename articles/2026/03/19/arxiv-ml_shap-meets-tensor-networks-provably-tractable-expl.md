---
title: "SHAP Meets Tensor Networks: Provably Tractable Explanations with Parallelism"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.21599"
published: "2026-03-19"
fetched: "2026-03-19T14:08:07.242132"
---

Computer Science > Machine Learning
[Submitted on 24 Oct 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:SHAP Meets Tensor Networks: Provably Tractable Explanations with Parallelism
View PDF HTML (experimental)Abstract:Although Shapley additive explanations (SHAP) can be computed in polynomial time for simple models like decision trees, they unfortunately become NP-hard to compute for more expressive black-box models like neural networks - where generating explanations is often most critical. In this work, we analyze the problem of computing SHAP explanations for *Tensor Networks (TNs)*, a broader and more expressive class of models than those for which current exact SHAP algorithms are known to hold, and which is widely used for neural network abstraction and compression. First, we introduce a general framework for computing provably exact SHAP explanations for general TNs with arbitrary structures. Interestingly, we show that, when TNs are restricted to a *Tensor Train (TT)* structure, SHAP computation can be performed in *poly-logarithmic* time using *parallel* computation. Thanks to the expressiveness power of TTs, this complexity result can be generalized to many other popular ML models such as decision trees, tree ensembles, linear models, and linear RNNs, therefore tightening previously reported complexity results for these families of models. Finally, by leveraging reductions of binarized neural networks to Tensor Network representations, we demonstrate that SHAP computation can become *efficiently tractable* when the network's *width* is fixed, while it remains computationally hard even with constant *depth*. This highlights an important insight: for this class of models, width - rather than depth - emerges as the primary computational bottleneck in SHAP computation.
Submission history
From: Reda Marzouk [view email][v1] Fri, 24 Oct 2025 16:02:51 UTC (299 KB)
[v2] Wed, 18 Mar 2026 00:51:50 UTC (662 KB)
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
