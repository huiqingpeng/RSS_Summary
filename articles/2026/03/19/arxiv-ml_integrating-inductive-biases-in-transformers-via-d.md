---
title: "Integrating Inductive Biases in Transformers via Distillation for Financial Time Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16985"
published: "2026-03-19"
fetched: "2026-03-19T12:06:20.968150"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Integrating Inductive Biases in Transformers via Distillation for Financial Time Series Forecasting
View PDF HTML (experimental)Abstract:Transformer-based models have been widely adopted for time-series forecasting due to their high representational capacity and architectural flexibility. However, many Transformer variants implicitly assume stationarity and stable temporal dynamics -- assumptions routinely violated in financial markets characterized by regime shifts and non-stationarity. Empirically, state-of-the-art time-series Transformers often underperform even vanilla Transformers on financial tasks, while simpler architectures with distinct inductive biases, such as CNNs and RNNs, can achieve stronger performance with substantially lower complexity. At the same time, no single inductive bias dominates across markets or regimes, suggesting that robust financial forecasting requires integrating complementary temporal priors. We propose TIPS (Transformer with Inductive Prior Synthesis), a knowledge distillation framework that synthesizes diverse inductive biases -- causality, locality, and periodicity -- within a unified Transformer. TIPS trains bias-specialized Transformer teachers via attention masking, then distills their knowledge into a single student model with regime-dependent alignment across inductive biases. Across four major equity markets, TIPS achieves state-of-the-art performance, outperforming strong ensemble baselines by 55%, 9%, and 16% in annual return, Sharpe ratio, and Calmar ratio, while requiring only 38% of the inference-time computation. Further analyses show that TIPS generates statistically significant excess returns beyond both vanilla Transformers and its teacher ensembles, and exhibits regime-dependent behavioral alignment with classical architectures during their profitable periods. These results highlight the importance of regime-dependent inductive bias utilization for robust generalization in non-stationary financial time series.
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
