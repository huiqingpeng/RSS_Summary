---
title: "Evolved Sample Weights for Bias Mitigation: Effectiveness Depends on the Fairness Objective"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.20909"
published: "2026-03-20"
fetched: "2026-03-20T14:08:51.701720"
---

Computer Science > Machine Learning
[Submitted on 25 Nov 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Evolved Sample Weights for Bias Mitigation: Effectiveness Depends on the Fairness Objective
View PDF HTML (experimental)Abstract:Machine learning models trained on real-world data may inadvertently make biased predictions that negatively impact marginalized communities. Reweighting, which assigns a weight to each data point used during model training, can mitigate such bias, though sometimes at the cost of predictive accuracy. In this paper, we investigated this trade-off by comparing three methods for generating these weights: (1) evolving them using a Genetic Algorithm (GA), (2) computing them using only dataset characteristics, and (3) assigning equal weights to all data points. Model performance under each strategy was evaluated using paired predictive and fairness metrics. We used two predictive metrics (accuracy and area under the Receiver Operating Characteristic curve) and two fairness metrics (demographic parity and subgroup false negative fairness). By conducting experiments on eleven publicly available datasets (including two medical datasets), we show that evolved sample weights can produce models that achieve better trade-offs between fairness and predictive performance than alternative weighting methods. However, the magnitude of these benefits depends strongly on the choice of fairness objective. Our experiments reveal that the evolved weights were most effective when optimizing for demographic parity-independent of choice of the performance objective-yielding better performance than other weighting strategies on the largest number of datasets.
Submission history
From: Anil Saini [view email][v1] Tue, 25 Nov 2025 22:50:59 UTC (304 KB)
[v2] Wed, 18 Mar 2026 21:43:34 UTC (379 KB)
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
