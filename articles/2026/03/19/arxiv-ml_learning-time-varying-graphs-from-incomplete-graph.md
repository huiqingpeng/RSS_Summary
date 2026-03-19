---
title: "Learning Time-Varying Graphs from Incomplete Graph Signals"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.17903"
published: "2026-03-19"
fetched: "2026-03-19T14:17:33.785798"
---

Statistics > Machine Learning
[Submitted on 19 Oct 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Learning Time-Varying Graphs from Incomplete Graph Signals
View PDF HTML (experimental)Abstract:This paper tackles the challenging problem of jointly inferring time-varying network topologies and imputing missing data from partially observed graph signals. We propose a unified non-convex optimization framework to simultaneously recover a sequence of graph Laplacian matrices while reconstructing the unobserved signal entries. Unlike conventional decoupled methods, our integrated approach facilitates a bidirectional flow of information between the graph and signal domains, yielding superior robustness, particularly in high missing-data regimes. To capture realistic network dynamics, we introduce a fused-lasso type regularizer on the sequence of Laplacians. This penalty promotes temporal smoothness by penalizing large successive changes, thereby preventing spurious variations induced by noise while still permitting gradual topological evolution. For solving the joint optimization problem, we develop an efficient Alternating Direction Method of Multipliers (ADMM) algorithm, which leverages the problem's structure to yield closed-form solutions for both the graph and signal subproblems. This design ensures scalability to large-scale networks and long time horizons. On the theoretical front, despite the inherent non-convexity, we establish a convergence guarantee, proving that the proposed ADMM scheme converges to a stationary point. Furthermore, we derive non-asymptotic statistical guarantees, providing high-probability error bounds for the graph estimator as a function of sample size, signal smoothness, and the intrinsic temporal variability of the graph. Extensive numerical experiments validate the approach, demonstrating that it significantly outperforms state-of-the-art baselines in both convergence speed and the joint accuracy of graph learning and signal recovery.
Submission history
From: Chuansen Peng [view email][v1] Sun, 19 Oct 2025 11:12:13 UTC (872 KB)
[v2] Wed, 18 Mar 2026 09:17:00 UTC (1,332 KB)
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
