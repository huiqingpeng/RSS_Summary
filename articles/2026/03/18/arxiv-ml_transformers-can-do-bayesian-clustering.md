---
title: "Transformers can do Bayesian Clustering"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.24318"
published: "2026-03-18"
fetched: "2026-03-18T16:20:13.989679"
---

Computer Science > Machine Learning
[Submitted on 28 Oct 2025 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:Transformers can do Bayesian Clustering
View PDF HTML (experimental)Abstract:Bayesian clustering accounts for uncertainty but is computationally demanding at scale. Furthermore, real-world datasets often contain missing values, and simple imputation ignores the associated uncertainty, resulting in suboptimal results. We present Cluster-PFN, a Transformer-based model that extends Prior-Data Fitted Networks (PFNs) to unsupervised Bayesian clustering. Trained entirely on synthetic datasets generated from a finite Gaussian Mixture Model (GMM) prior, Cluster-PFN learns to estimate the posterior distribution over both the number of clusters and the cluster assignments. Our method estimates the number of clusters more accurately than handcrafted model selection procedures such as AIC, BIC and Variational Inference (VI), and achieves clustering quality competitive with VI while being orders of magnitude faster. Cluster-PFN can be trained on complex priors that include missing data, outperforming imputation-based baselines on real-world genomic datasets, at high missingness. These results show that the Cluster-PFN can provide scalable and flexible Bayesian clustering.
Submission history
From: Prajit Bhaskaran [view email][v1] Tue, 28 Oct 2025 11:36:31 UTC (1,673 KB)
[v2] Tue, 3 Feb 2026 16:10:52 UTC (1,670 KB)
[v3] Wed, 18 Feb 2026 07:57:06 UTC (1,670 KB)
[v4] Tue, 17 Mar 2026 11:40:34 UTC (1,670 KB)
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
