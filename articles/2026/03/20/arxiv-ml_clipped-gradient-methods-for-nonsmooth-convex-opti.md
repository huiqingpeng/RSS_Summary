---
title: "Clipped Gradient Methods for Nonsmooth Convex Optimization under Heavy-Tailed Noise: A Refined Analysis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.23178"
published: "2026-03-20"
fetched: "2026-03-20T14:17:59.313081"
---

Mathematics > Optimization and Control
[Submitted on 29 Dec 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Clipped Gradient Methods for Nonsmooth Convex Optimization under Heavy-Tailed Noise: A Refined Analysis
View PDF HTML (experimental)Abstract:Optimization under heavy-tailed noise has become popular recently, since it better fits many modern machine learning tasks, as captured by empirical observations. Concretely, instead of a finite second moment on gradient noise, a bounded ${\frak p}$-th moment where ${\frak p}\in(1,2]$ has been recognized to be more realistic (say being upper bounded by $\sigma_{\frak l}^{\frak p}$ for some $\sigma_{\frak l}\ge0$). A simple yet effective operation, gradient clipping, is known to handle this new challenge successfully. Specifically, Clipped Stochastic Gradient Descent (Clipped SGD) guarantees a high-probability rate ${\cal O}(\sigma_{\frak l}\ln(1/\delta)T^{1/{\frak p}-1})$ (resp. ${\cal O}(\sigma_{\frak l}^2\ln^2(1/\delta)T^{2/{\frak p}-2})$) for nonsmooth convex (resp. strongly convex) problems, where $\delta\in(0,1]$ is the failure probability and $T\in\mathbb{N}$ is the time horizon. In this work, we provide a refined analysis for Clipped SGD and offer two faster rates, ${\cal O}(\sigma_{\frak l}d_{\rm eff}^{-1/2{\frak p}}\ln^{1-1/{\frak p}}(1/\delta)T^{1/{\frak p}-1})$ and ${\cal O}(\sigma_{\frak l}^2d_{\rm eff}^{-1/{\frak p}}\ln^{2-2/{\frak p}}(1/\delta)T^{2/{\frak p}-2})$, than the aforementioned best results, where $d_{\rm eff}\ge1$ is a quantity we call the $\textit{generalized effective dimension}$. Our analysis improves upon the existing approach on two sides: better utilization of Freedman's inequality and finer bounds for clipping error under heavy-tailed noise. In addition, we extend the refined analysis to convergence in expectation and obtain new rates that break the known lower bounds. Lastly, to complement the study, we establish new lower bounds for both high-probability and in-expectation convergence. Notably, the in-expectation lower bounds match our new upper bounds, indicating the optimality of our refined analysis for convergence in expectation.
Submission history
From: Zijian Liu [view email][v1] Mon, 29 Dec 2025 03:35:53 UTC (55 KB)
[v2] Thu, 19 Mar 2026 16:58:28 UTC (280 KB)
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
