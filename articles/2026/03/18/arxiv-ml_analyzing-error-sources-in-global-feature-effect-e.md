---
title: "Analyzing Error Sources in Global Feature Effect Estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15057"
published: "2026-03-18"
fetched: "2026-03-18T17:17:11.325168"
---

Statistics > Machine Learning
[Submitted on 16 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Analyzing Error Sources in Global Feature Effect Estimation
View PDF HTML (experimental)Abstract:Global feature effects such as partial dependence (PD) and accumulated local effects (ALE) plots are widely used to interpret black-box models. However, they are only estimates of true underlying effects, and their reliability depends on multiple sources of error. Despite the popularity of global feature effects, these error sources are largely unexplored. In particular, the practically relevant question of whether to use training or holdout data to estimate feature effects remains unanswered. We address this gap by providing a systematic, estimator-level analysis that disentangles sources of bias and variance for PD and ALE. To this end, we derive a mean-squared-error decomposition that separates model bias, estimation bias, model variance, and estimation variance, and analyze their dependence on model characteristics, data selection, and sample size. We validate our theoretical findings through an extensive simulation study across multiple data-generating processes, learners, estimation strategies (training data, validation data, and cross-validation), and sample sizes. Our results reveal that, while using holdout data is theoretically the cleanest, potential biases arising from the training data are empirically negligible and dominated by the impact of the usually higher sample size. The estimation variance depends on both the presence of interactions and the sample size, with ALE being particularly sensitive to the latter. Cross-validation-based estimation is a promising approach that reduces the model variance component, particularly for overfitting models. Our analysis provides a principled explanation of the sources of error in feature effect estimates and offers concrete guidance on choosing estimation strategies when interpreting machine learning models.
Submission history
From: Timo Heiß [view email][v1] Mon, 16 Mar 2026 10:12:51 UTC (230 KB)
[v2] Tue, 17 Mar 2026 10:23:11 UTC (230 KB)
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
