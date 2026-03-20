---
title: "Fast and Interpretable Autoregressive Estimation with Neural Network Backpropagation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19041"
published: "2026-03-20"
fetched: "2026-03-20T13:19:29.979257"
---

Statistics > Machine Learning
[Submitted on 19 Mar 2026]
Title:Fast and Interpretable Autoregressive Estimation with Neural Network Backpropagation
View PDF HTML (experimental)Abstract:Autoregressive (AR) models remain widely used in time series analysis due to their interpretability, but convencional parameter estimation methods can be computationally expensive and prone to convergence issues. This paper proposes a Neural Network (NN) formulation of AR estimation by embedding the autoregressive structure directly into a feedforward NN, enabling coefficient estimation through backpropagation while preserving interpretability. Simulation experiments on 125,000 synthetic AR(p) time series with short-term dependence (1 <= p <= 5) show that the proposed NN-based method consistently recovers model coefficients for all series, while Conditional Maximum Likelihood (CML) fails to converge in approximately 55% of cases. When both methods converge, estimation accuracy is comparable with negligible differences in relative error, R2 and, perplexity/likelihood. However, when CML fails, the NN-based approach still provides reliable estimates. In all cases, the NN estimator achieves substantial computational gains, reaching a median speedup of 12.6x and up to 34.2x for higher model orders. Overall, results demonstrate that gradient-descent NN optimization can provide a fast and efficient alternative for interpretable AR parameter estimation.
Submission history
From: Sonia Gouveia PhD [view email][v1] Thu, 19 Mar 2026 15:38:12 UTC (8,302 KB)
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
