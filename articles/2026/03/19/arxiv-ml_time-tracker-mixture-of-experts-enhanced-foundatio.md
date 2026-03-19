---
title: "Time Tracker: Mixture-of-Experts-Enhanced Foundation Time Series Forecasting Model with Decoupled Training Pipelines"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.15151"
published: "2026-03-19"
fetched: "2026-03-19T13:20:36.365388"
---

Computer Science > Machine Learning
[Submitted on 21 May 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Time Tracker: Mixture-of-Experts-Enhanced Foundation Time Series Forecasting Model with Decoupled Training Pipelines
View PDF HTML (experimental)Abstract:In the past few years, time series foundation models have achieved superior predicting accuracy. However, real-world time series often exhibit significant diversity in their temporal patterns across different time spans and domains, making it challenging for a single model architecture to fit all complex scenarios. In addition, time series data may have multiple variables exhibiting complex correlations between each other. Recent mainstream works have focused on modeling times series in a channel-independent manner in both pretraining and finetuning stages, overlooking the valuable inter-series dependencies. To this end, we propose Time Tracker for better predictions on multivariate time series data. Firstly, we leverage sparse mixture of experts (MoE) within Transformers to handle the modeling of diverse time series patterns, thereby alleviating the learning difficulties of a single model while improving its generalization. Besides, we propose Any-variate Attention, enabling a unified model structure to seamlessly handle both univariate and multivariate time series, thereby supporting channel-independent modeling during pretraining and channel-mixed modeling for this http URL, we design a graph learning module that constructs relations among sequences from frequency-domain features, providing more precise guidance to capture inter-series dependencies in channel-mixed modeling. Based on these advancements, Time Tracker achieves state-of-the-art performance in predicting accuracy, model generalization and adaptability.
Submission history
From: Aobo Liang [view email][v1] Wed, 21 May 2025 06:18:41 UTC (285 KB)
[v2] Wed, 18 Mar 2026 07:38:30 UTC (859 KB)
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
