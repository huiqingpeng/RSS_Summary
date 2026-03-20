---
title: "Online Convex Optimization with Heavy Tails: Old Algorithms, New Regrets, and Applications"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2508.07473"
published: "2026-03-20"
fetched: "2026-03-20T14:06:51.649535"
---

Computer Science > Machine Learning
[Submitted on 10 Aug 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Online Convex Optimization with Heavy Tails: Old Algorithms, New Regrets, and Applications
View PDF HTML (experimental)Abstract:In Online Convex Optimization (OCO), when the stochastic gradient has a finite variance, many algorithms provably work and guarantee a sublinear regret. However, limited results are known if the gradient estimate has a heavy tail, i.e., the stochastic gradient only admits a finite $\mathsf{p}$-th central moment for some $\mathsf{p}\in\left(1,2\right]$. Motivated by it, this work examines different old algorithms for OCO (e.g., Online Gradient Descent) in the more challenging heavy-tailed setting. Under the standard bounded domain assumption, we establish new regrets for these classical methods without any algorithmic modification. Remarkably, these regret bounds are fully optimal in all parameters (can be achieved even without knowing $\mathsf{p}$), suggesting that OCO with heavy tails can be solved effectively without any extra operation (e.g., gradient clipping). Our new results have several applications. A particularly interesting one is the first provable and optimal convergence result for nonsmooth nonconvex optimization under heavy-tailed noise without gradient clipping. Furthermore, we explore broader settings (e.g., smooth OCO) and extend our ideas to optimistic algorithms to handle different cases simultaneously.
Submission history
From: Zijian Liu [view email][v1] Sun, 10 Aug 2025 20:17:38 UTC (51 KB)
[v2] Tue, 30 Dec 2025 05:49:16 UTC (53 KB)
[v3] Thu, 19 Mar 2026 15:31:02 UTC (56 KB)
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
