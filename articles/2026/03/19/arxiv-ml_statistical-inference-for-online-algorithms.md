---
title: "Statistical Inference for Online Algorithms"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.17300"
published: "2026-03-19"
fetched: "2026-03-19T14:15:37.949020"
---

Statistics > Machine Learning
[Submitted on 22 May 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Statistical Inference for Online Algorithms
View PDF HTML (experimental)Abstract:The construction of confidence intervals and hypothesis tests for functionals is a cornerstone of statistical inference. Traditionally, the most efficient procedures - such as the Wald interval or the Likelihood Ratio Test - require both a point estimator and a consistent estimate of its asymptotic variance. However, when estimators are derived from online or sequential algorithms, computational constraints often preclude multiple passes over the data, complicating variance estimation. In this article, we propose a computationally efficient, rate-optimal wrapper method (HulC) that wraps around any online algorithm to produce asymptotically valid confidence regions bypassing the need for explicit asymptotic variance estimation. The method is provably valid for any online algorithm that yields an asymptotically normal estimator. We evaluate the practical performance of the proposed method primarily using Stochastic Gradient Descent (SGD) with Polyak-Ruppert averaging. Furthermore, we provide extensive numerical simulations comparing the performance of our approach (HulC) when used with other online algorithms, including implicit-SGD and ROOT-SGD.
Submission history
From: Selina Carter [view email][v1] Thu, 22 May 2025 21:31:49 UTC (11,327 KB)
[v2] Wed, 18 Mar 2026 14:52:57 UTC (2,439 KB)
Current browse context:
stat.ML
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
