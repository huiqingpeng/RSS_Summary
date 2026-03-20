---
title: "Revisiting OmniAnomaly for Anomaly Detection: performance metrics and comparison with PCA-based models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18985"
published: "2026-03-20"
fetched: "2026-03-20T13:18:17.920092"
---

Statistics > Machine Learning
[Submitted on 19 Mar 2026]
Title:Revisiting OmniAnomaly for Anomaly Detection: performance metrics and comparison with PCA-based models
View PDF HTML (experimental)Abstract:Deep learning models have become the dominant approach for multivariate time series anomaly detection (MTSAD), often reporting substantial performance improvements over classical statistical methods. However, these gains are frequently evaluated under heterogeneous thresholding strategies and evaluation protocols, making fair comparisons difficult. This work revisits OmniAnomaly, a widely used stochastic recurrent model for MTSAD, and systematically compares it with a simple linear baseline based on Principal Component Analysis (PCA) on the Server Machine Dataset (SMD). Both methods are evaluated under identical thresholding and evaluation procedures, with experiments repeated across 100 runs for each of the 28 machines in the dataset. Performance is evaluated using Precision, Recall and F1-score at point-level, with and without point-adjustment, and under different aggregation strategies across machines and runs, with the corresponding standard deviations also reported. The results show large variability across machines and show that PCA can achieve performance comparable to OmniAnomaly, and even outperform it when point-adjustment is not applied. These findings question the added value of more complex architectures under current benchmarking practices and highlight the critical role of evaluation methodology in MTSAD research.
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
