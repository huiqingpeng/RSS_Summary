---
title: "From Causal Discovery to Dynamic Causal Inference in Neural Time Series"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20980"
published: "2026-03-24"
fetched: "2026-03-25T07:16:53.645751"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:From Causal Discovery to Dynamic Causal Inference in Neural Time Series
View PDF HTML (experimental)Abstract:Time-varying causal models provide a powerful framework for studying dynamic scientific systems, yet most existing approaches assume that the underlying causal network is known a priori - an assumption rarely satisfied in real-world domains where causal structure is uncertain, evolving, or only indirectly observable. This limits the applicability of dynamic causal inference in many scientific settings. We propose Dynamic Causal Network Autoregression (DCNAR), a two-stage neural causal modeling framework that integrates data-driven causal discovery with time-varying causal inference. In the first stage, a neural autoregressive causal discovery model learns a sparse directed causal network from multivariate time series. In the second stage, this learned structure is used as a structural prior for a time-varying neural network autoregression, enabling dynamic estimation of causal influence without requiring pre-specified network structure. We evaluate the scientific validity of DCNAR using behavioral diagnostics that assess causal necessity, temporal stability, and sensitivity to structural change, rather than predictive accuracy alone. Experiments on multi-country panel time-series data demonstrate that learned causal networks yield more stable and behaviorally meaningful dynamic causal inferences than coefficient-based or structure-free alternatives, even when forecasting performance is comparable. These results position DCNAR as a general framework for using AI as a scientific instrument for dynamic causal reasoning under structural uncertainty.
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
