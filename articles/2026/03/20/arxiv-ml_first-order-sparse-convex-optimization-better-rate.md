---
title: "First-Order Sparse Convex Optimization: Better Rates with Sparse Updates"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2506.19075"
published: "2026-03-20"
fetched: "2026-03-20T14:15:51.914716"
---

Mathematics > Optimization and Control
[Submitted on 23 Jun 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:First-Order Sparse Convex Optimization: Better Rates with Sparse Updates
View PDF HTML (experimental)Abstract:It was recently established that for convex optimization problems with sparse optimal solutions (be it entry-wise sparsity or matrix rank-wise sparsity) it is possible to design first-order methods with linear convergence rates that depend on an improved mixed-norm condition number of the form $\frac{\beta_1{}s}{\alpha_2}$, where $\beta_1$ is the $\ell_1$-Lipschitz continuity constant of the gradient, $\alpha_2$ is the $\ell_2$-quadratic growth constant, and $s$ is the sparsity of optimal solutions. However, beyond the improved convergence rate, these methods are unable to leverage the sparsity of optimal solutions towards improving the runtime of each iteration as well, which may still be prohibitively high for high-dimensional problems. In this work, we establish that linear convergence rates which depend on this improved condition number can be obtained using only sparse updates, which may result in overall significantly improved running times. Moreover, our methods are considerably easier to implement.
Submission history
From: Dan Garber [view email][v1] Mon, 23 Jun 2025 19:44:37 UTC (175 KB)
[v2] Sun, 27 Jul 2025 14:25:17 UTC (175 KB)
[v3] Thu, 19 Mar 2026 15:35:07 UTC (298 KB)
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
