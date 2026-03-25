---
title: "Beyond the Mean: Distribution-Aware Loss Functions for Bimodal Regression"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22328"
published: "2026-03-25"
fetched: "2026-03-26T07:11:44.009551"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Beyond the Mean: Distribution-Aware Loss Functions for Bimodal Regression
View PDF HTML (experimental)Abstract:Despite the strong predictive performance achieved by machine learning models across many application domains, assessing their trustworthiness through reliable estimates of predictive confidence remains a critical challenge. This issue arises in scenarios where the likelihood of error inferred from learned representations follows a bimodal distribution, resulting from the coexistence of confident and ambiguous predictions. Standard regression approaches often struggle to adequately express this predictive uncertainty, as they implicitly assume unimodal Gaussian noise, leading to mean-collapse behavior in such settings. Although Mixture Density Networks (MDNs) can represent different distributions, they suffer from severe optimization instability. We propose a family of distribution-aware loss functions integrating normalized RMSE with Wasserstein and Cramér distances. When applied to standard deep regression models, our approach recovers bimodal distributions without the volatility of mixture models. Validated across four experimental stages, our results show that the proposed Wasserstein loss establishes a new Pareto efficiency frontier: matching the stability of standard regression losses like MSE in unimodal tasks while reducing Jensen-Shannon Divergence by 45% on complex bimodal datasets. Our framework strictly dominates MDNs in both fidelity and robustness, offering a reliable tool for aleatoric uncertainty estimation in trustworthy AI systems.
Submission history
From: Abolfazl Mohammadi Seif [view email][v1] Fri, 20 Mar 2026 18:37:05 UTC (5,399 KB)
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
