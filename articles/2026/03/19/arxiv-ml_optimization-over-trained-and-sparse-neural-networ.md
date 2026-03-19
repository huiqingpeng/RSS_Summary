---
title: "Optimization over Trained (and Sparse) Neural Networks: A Surrogate within a Surrogate"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.01985"
published: "2026-03-19"
fetched: "2026-03-19T14:15:14.401434"
---

Mathematics > Optimization and Control
[Submitted on 4 May 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Optimization over Trained (and Sparse) Neural Networks: A Surrogate within a Surrogate
View PDF HTML (experimental)Abstract:In constraint learning, we use a neural network as a surrogate for part of the constraints or of the objective function of an optimization model. However, the tractability of the resulting model is heavily influenced by the size of the neural network used as a surrogate. One way to obtain a more tractable surrogate is by pruning the neural network first. In this work, we consider how to approach the setting in which the neural network is actually a given: how can we solve an optimization model embedding a large and predetermined neural network? We propose surrogating the neural network itself by pruning it, which leads to a sparse and more tractable optimization model, for which we hope to still obtain good solutions with respect to the original neural network. For network verification and function maximization models, that indeed leads to better solutions within a time limit, especially -- and surprisingly -- if we skip the standard retraining step known as finetuning. Hence, a pruned network with worse inference for lack of finetuning can be a better surrogate.
Submission history
From: Thiago Serra [view email][v1] Sun, 4 May 2025 04:49:19 UTC (248 KB)
[v2] Tue, 30 Dec 2025 15:27:24 UTC (237 KB)
[v3] Wed, 18 Mar 2026 01:49:36 UTC (241 KB)
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
