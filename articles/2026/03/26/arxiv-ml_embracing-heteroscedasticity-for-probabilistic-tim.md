---
title: "Embracing Heteroscedasticity for Probabilistic Time Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24254"
published: "2026-03-26"
fetched: "2026-03-27T07:22:15.571773"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Embracing Heteroscedasticity for Probabilistic Time Series Forecasting
View PDF HTML (experimental)Abstract:Probabilistic time series forecasting (PTSF) aims to model the full predictive distribution of future observations, enabling both accurate forecasting and principled uncertainty quantification. A central requirement of PTSF is to embrace heteroscedasticity, as real-world time series exhibit time-varying conditional variances induced by nonstationary dynamics, regime changes, and evolving external conditions. However, most existing non-autoregressive generative approaches to PTSF, such as TimeVAE and $K^2$VAE, rely on MSE-based training objectives that implicitly impose a homoscedastic assumption, thereby fundamentally limiting their ability to model temporal heteroscedasticity. To address this limitation, we propose the Location-Scale Gaussian VAE (LSG-VAE), a simple but effective framework that explicitly parameterizes both the predictive mean and time-dependent variance through a location-scale likelihood formulation. This design enables LSG-VAE to faithfully capture heteroscedastic aleatoric uncertainty and introduces an adaptive attenuation mechanism that automatically down-weights highly volatile observations during training, leading to improved robustness in trend prediction. Extensive experiments on nine benchmark datasets demonstrate that LSG-VAE consistently outperforms fifteen strong generative baselines while maintaining high computational efficiency suitable for real-time deployment.
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
