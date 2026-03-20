---
title: "Combining T-learning and DR-learning: a framework for oracle-efficient estimation of causal contrasts"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2402.01972"
published: "2026-03-20"
fetched: "2026-03-20T14:13:59.307895"
---

Statistics > Machine Learning
[Submitted on 3 Feb 2024 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Combining T-learning and DR-learning: a framework for oracle-efficient estimation of causal contrasts
View PDFAbstract:We introduce efficient plug-in (EP) learning, a novel framework for the estimation of heterogeneous causal contrasts, such as the conditional average treatment effect and conditional relative risk. The EP-learning framework enjoys the same oracle efficiency as Neyman-orthogonal learning strategies, such as DR-learning and R-learning, while addressing some of their primary drawbacks: (i) their practical applicability can be hindered by non-convex loss functions; and (ii) they may suffer from poor performance and instability due to inverse probability weighting and pseudo-outcomes that violate bounds. To overcome these issues, the EP-learner leverages an efficient plug-in estimator of the population risk function for the causal contrast. In doing so, it inherits the stability of plug-in strategies such as T-learning, while improving on their efficiency. Under reasonable conditions, EP-learners based on empirical risk minimization are oracle-efficient, exhibiting asymptotic equivalence to the minimizer of an oracle-efficient one-step debiased estimator of the population risk function. In simulation experiments, we show that EP-learners of the conditional average treatment effect and conditional relative risk outperform state-of-the-art competitors, including the T-learner, R-learner, and DR-learner. Open-source implementations of the proposed methods are available in our \texttt{R} package \texttt{hte3}.
Submission history
From: Lars Van Der Laan [view email][v1] Sat, 3 Feb 2024 00:47:50 UTC (578 KB)
[v2] Thu, 19 Mar 2026 16:15:16 UTC (582 KB)
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
