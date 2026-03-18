---
title: "Foundation-Model Surrogates Enable Data-Efficient Active Learning for Materials Discovery"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.12567"
published: "2026-03-18"
fetched: "2026-03-18T17:16:03.220371"
---

Condensed Matter > Materials Science
[Submitted on 13 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Foundation-Model Surrogates Enable Data-Efficient Active Learning for Materials Discovery
View PDF HTML (experimental)Abstract:Active learning (AL) has emerged as a powerful paradigm for accelerating materials discovery by iteratively steering experiments toward promising candidates, reducing the number of costly synthesis-and-characterization cycles needed to identify optimal materials. However, current AL relies predominantly on Gaussian Process (GP) and Random Forest (RF) surrogates, which suffer from complementary limitations: GP underfits complex composition-property landscapes due to rigid kernel assumptions, while RF produces unreliable heuristic uncertainty estimates in small-data regimes. This small-data challenge is pervasive in materials science, making reliable surrogate modeling extremely difficult with models trained from scratch on each new dataset. Here we propose In-Context Active Learning (ICAL), which addresses this bottleneck by replacing conventional surrogates with TabPFN, a transformer-based foundation model (FM) pre-trained on millions of synthetic regression tasks to meta-learn a universal prior over tabular data, upon which TabPFN performs principled Bayesian inference in a single forward pass without dataset-specific retraining, delivering strong small-data regression performance and well-calibrated predictive uncertainty (required for effective AL). We benchmark ICAL against GP and RF across 10 materials datasets and TabPFN wins on 8 out of 10 datasets, achieving a mean saving of 52% in extra evaluations relative to GP and 29.77% relative to RF. Cross-validation analysis confirms that TabPFN's advantage stems from superior uncertainty calibration, achieving the lowest Negative Log-Likelihood and Area Under the Sparsification Error curve among all surrogates. These results demonstrate that pre-trained FMs can serve as effective surrogates for active learning, enabling data-efficient discovery across diverse materials systems and small-data experimental sciences.
Submission history
From: Jianjun Hu [view email][v1] Fri, 13 Mar 2026 01:57:09 UTC (1,552 KB)
[v2] Tue, 17 Mar 2026 08:43:26 UTC (1,549 KB)
Current browse context:
cond-mat.mtrl-sci
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
