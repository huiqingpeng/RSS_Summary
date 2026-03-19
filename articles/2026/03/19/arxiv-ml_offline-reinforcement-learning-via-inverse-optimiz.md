---
title: "Offline Reinforcement Learning via Inverse Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.20030"
published: "2026-03-19"
fetched: "2026-03-19T13:18:55.534672"
---

Computer Science > Machine Learning
[Submitted on 27 Feb 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Offline Reinforcement Learning via Inverse Optimization
View PDFAbstract:Inspired by the recent successes of Inverse Optimization (IO) across various application domains, we propose a novel offline Reinforcement Learning (ORL) algorithm for continuous state and action spaces, leveraging the convex loss function called ``sub-optimality loss'' from the IO literature. To mitigate the distribution shift commonly observed in ORL problems, we further employ a robust and non-causal Model Predictive Control (MPC) expert steering a nominal model of the dynamics using in-hindsight information stemming from the model mismatch. Unlike the existing literature, our robust MPC expert enjoys an exact and tractable convex reformulation. In the second part of this study, we show that the IO hypothesis class, trained by the proposed convex loss function, enjoys ample expressiveness and {reliably recovers teacher behavior in MuJoCo benchmarks. The method achieves competitive results compared to widely-used baselines in sample-constrained settings, despite using} orders of magnitude fewer parameters. To facilitate the reproducibility of our results, we provide an open-source package implementing the proposed algorithms and the experiments. The code is available at this https URL.
Submission history
From: Tolga Ok [view email][v1] Thu, 27 Feb 2025 12:11:44 UTC (454 KB)
[v2] Thu, 16 Oct 2025 13:55:37 UTC (160 KB)
[v3] Wed, 18 Mar 2026 11:19:02 UTC (463 KB)
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
