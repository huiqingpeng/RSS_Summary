---
title: "On the Dynamic Regret of Following the Regularized Leader: Optimism with History Pruning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.22899"
published: "2026-03-19"
fetched: "2026-03-19T13:20:50.039756"
---

Computer Science > Machine Learning
[Submitted on 28 May 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:On the Dynamic Regret of Following the Regularized Leader: Optimism with History Pruning
View PDF HTML (experimental)Abstract:We revisit the Follow the Regularized Leader (FTRL) framework for Online Convex Optimization (OCO) over compact sets, focusing on achieving dynamic regret guarantees. Prior work has highlighted the framework's limitations in dynamic environments due to its tendency to produce "lazy" iterates. However, building on insights showing FTRL's ability to produce "agile" iterates, we show that it can indeed recover known dynamic regret bounds through optimistic composition of future costs and careful linearization of past costs, which can lead to pruning some of them. This new analysis of FTRL against dynamic comparators yields a principled way to interpolate between lazy and agile updates and offers several benefits, including refined control over regret terms, optimism without cyclic dependence, and the application of minimal recursive regularization akin to AdaFTRL. More broadly, we show that it is not the "lazy" projection style of FTRL that hinders (optimistic) dynamic regret, but the decoupling of the algorithm's state (linearized history) from its iterates, allowing the state to grow arbitrarily. Instead, pruning synchronizes these two when necessary.
Submission history
From: Naram Mhaisen [view email][v1] Wed, 28 May 2025 22:03:15 UTC (747 KB)
[v2] Thu, 25 Sep 2025 13:55:03 UTC (888 KB)
[v3] Wed, 18 Mar 2026 11:49:27 UTC (785 KB)
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
