---
title: "MSNet and LS-Net: Scalable Multi-Scale Multi-Representation Networks for Time Series Classification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19315"
published: "2026-03-23"
fetched: "2026-03-24T07:16:48.096454"
---

Computer Science > Machine Learning
[Submitted on 14 Mar 2026]
Title:MSNet and LS-Net: Scalable Multi-Scale Multi-Representation Networks for Time Series Classification
View PDFAbstract:Time series classification (TSC) performance depends not only on architectural design but also on the diversity of input representations. In this work, we propose a scalable multi-scale convolutional framework that systematically integrates structured multi-representation inputs for univariate time series.
We introduce two architectures: MSNet, a hierarchical multi-scale convolutional network optimized for robustness and calibration, and LS-Net, a lightweight variant designed for efficiency-aware deployment. In addition, we adapt LiteMV -- originally developed for multivariate inputs -- to operate on multi-representation univariate signals, enabling cross-representation interaction.
We evaluate all models across 142 benchmark datasets under a unified experimental protocol. Critical Difference analysis confirms statistically significant performance differences among the top models. Results show that LiteMV achieves the highest mean accuracy, MSNet provides superior probabilistic calibration (lowest NLL), and LS-Net offers the best efficiency-accuracy tradeoff. Pareto analysis further demonstrates that multi-representation multi-scale modeling yields a flexible design space that can be tuned for accuracy-oriented, calibration-oriented, or resource-constrained settings.
These findings establish scalable multi-representation multi-scale learning as a principled and practical direction for modern TSC. Reference implementation of MSNet and LS-Net is available at: this https URL
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
