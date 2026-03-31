---
title: "VAN-AD: Visual Masked Autoencoder with Normalizing Flow For Time Series Anomaly Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26842"
published: "2026-03-31"
fetched: "2026-04-01T07:19:57.654118"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:VAN-AD: Visual Masked Autoencoder with Normalizing Flow For Time Series Anomaly Detection
View PDF HTML (experimental)Abstract:Time series anomaly detection (TSAD) is essential for maintaining the reliability and security of IoT-enabled service systems. Existing methods require training one specific model for each dataset, which exhibits limited generalization capability across different target datasets, hindering anomaly detection performance in various scenarios with scarce training data. To address this limitation, foundation models have emerged as a promising direction. However, existing approaches either repurpose large language models (LLMs) or construct largescale time series datasets to develop general anomaly detection foundation models, and still face challenges caused by severe cross-modal gaps or in-domain heterogeneity. In this paper, we investigate the applicability of large-scale vision models to TSAD. Specifically, we adapt a visual Masked Autoencoder (MAE) pretrained on ImageNet to the TSAD task. However, directly transferring MAE to TSAD introduces two key challenges: overgeneralization and limited local perception. To address these challenges, we propose VAN-AD, a novel MAE-based framework for TSAD. To alleviate the over-generalization issue, we design an Adaptive Distribution Mapping Module (ADMM), which maps the reconstruction results before and after MAE into a unified statistical space to amplify discrepancies caused by abnormal patterns. To overcome the limitation of local perception, we further develop a Normalizing Flow Module (NFM), which combines MAE with normalizing flow to estimate the probability density of the current window under the global distribution. Extensive experiments on nine real-world datasets demonstrate that VAN-AD consistently outperforms existing state-of-the-art methods across multiple evaluation this http URL make our code and datasets available at this https URL.
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
