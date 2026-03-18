---
title: "Predicting Biomedical Interactions with Probabilistic Model Selection for Graph Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2211.13231"
published: "2026-03-18"
fetched: "2026-03-18T17:08:20.682292"
---

Quantitative Biology > Quantitative Methods
[Submitted on 22 Nov 2022 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Predicting Biomedical Interactions with Probabilistic Model Selection for Graph Neural Networks
View PDF HTML (experimental)Abstract:Heterogeneous molecular entities and their interactions, commonly depicted as a network, are crucial for advancing our systems-level understanding of biology. With recent advancements in high-throughput data generation and a significant improvement in computational power, graph neural networks (GNNs) have demonstrated their effectiveness in predicting biomedical interactions. Since GNNs follow a neighborhood aggregation scheme, the number of graph convolution (GC) layers (i.e., depth) determines the neighborhood orders from which they can aggregate information, thereby significantly impacting the model's performance. However, it often relies on heuristics or extensive experimentation to determine an appropriate GNN depth for a given biomedical network. These methods can be unreliable or result in expensive computational overhead. Moreover, GNNs with more GC layers tend to exhibit poor calibration, leading to high confidence in incorrect predictions. To address these challenges, we propose a Bayesian model selection framework to jointly infer the most plausible number of GC layers supported by the data, apply dropout regularization, and learn network parameters. Experiments on four biomedical interaction datasets demonstrate that our method achieves superior performance over competing methods, providing well-calibrated predictions by allowing GNNs to adapt their depths to accommodate interaction information from various biomedical networks. Source code and data is available at: this https URL
Submission history
From: Paribesh Regmi [view email][v1] Tue, 22 Nov 2022 20:44:28 UTC (4,544 KB)
[v2] Sat, 3 Dec 2022 20:02:35 UTC (4,544 KB)
[v3] Tue, 17 Mar 2026 17:26:12 UTC (2,174 KB)
Current browse context:
q-bio.QM
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
