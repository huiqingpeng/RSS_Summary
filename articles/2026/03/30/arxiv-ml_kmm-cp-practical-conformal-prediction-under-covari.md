---
title: "KMM-CP: Practical Conformal Prediction under Covariate Shift via Selective Kernel Mean Matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26415"
published: "2026-03-30"
fetched: "2026-03-31T07:23:55.828933"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:KMM-CP: Practical Conformal Prediction under Covariate Shift via Selective Kernel Mean Matching
View PDF HTML (experimental)Abstract:Uncertainty quantification is essential for deploying machine learning models in high-stakes domains such as scientific discovery and healthcare. Conformal Prediction (CP) provides finite-sample coverage guarantees under exchangeability, an assumption often violated in practice due to distribution shift. Under covariate shift, restoring validity requires importance weighting, yet accurate density-ratio estimation becomes unstable when training and test distributions exhibit limited support overlap. We propose KMM-CP, a conformal prediction framework based on Kernel Mean Matching (KMM) for covariate-shift correction. We show that KMM directly controls the bias-variance components governing conformal coverage error by minimizing RKHS moment discrepancy under explicit weight constraints, and establish asymptotic coverage guarantees under mild conditions. We then introduce a selective extension that identifies regions of reliable support overlap and restricts conformal correction to this subset, further improving stability in low-overlap regimes. Experiments on molecular property prediction benchmarks with realistic distribution shifts show that KMM-CP reduces coverage gap by over 50% compared to existing approaches. The code is available at this https URL.
Submission history
From: Siddhartha Laghuvarapu [view email][v1] Fri, 27 Mar 2026 13:44:42 UTC (348 KB)
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
