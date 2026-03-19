---
title: "Robust estimation of heterogeneous treatment effects in randomized trials leveraging external data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2507.03681"
published: "2026-03-19"
fetched: "2026-03-19T14:16:23.010922"
---

Statistics > Machine Learning
[Submitted on 4 Jul 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Robust estimation of heterogeneous treatment effects in randomized trials leveraging external data
View PDF HTML (experimental)Abstract:Randomized trials are typically designed to detect average treatment effects but often lack the statistical power to uncover individual-level treatment effect heterogeneity, limiting their value for personalized decision-making. To address this, we propose the QR-learner, a model-agnostic learner that estimates conditional average treatment effects (CATE) within the trial population by leveraging external data from other trials or observational studies. The proposed method is robust: it can reduce the mean squared error relative to a trial-only CATE learner, and is guaranteed to recover the true CATE even when the external data are not aligned with the trial. Moreover, we introduce a procedure that combines the QR-learner with a trial-only CATE learner and show that it asymptotically matches or exceeds both component learners in terms of mean squared error. We examine the performance of our approach in simulation studies and apply the methods to a real-world dataset, demonstrating improvements in both CATE estimation and statistical power for detecting heterogeneous effects.
Submission history
From: Rickard Karlsson [view email][v1] Fri, 4 Jul 2025 16:01:05 UTC (123 KB)
[v2] Wed, 15 Oct 2025 13:31:04 UTC (152 KB)
[v3] Wed, 18 Mar 2026 16:15:55 UTC (166 KB)
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
