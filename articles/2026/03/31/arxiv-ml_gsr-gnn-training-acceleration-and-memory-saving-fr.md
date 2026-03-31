---
title: "GSR-GNN: Training Acceleration and Memory-Saving Framework of Deep GNNs on Circuit Graph"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27156"
published: "2026-03-31"
fetched: "2026-04-01T07:22:21.255392"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:GSR-GNN: Training Acceleration and Memory-Saving Framework of Deep GNNs on Circuit Graph
View PDF HTML (experimental)Abstract:Graph Neural Networks (GNNs) show strong promise for circuit analysis, but scaling to modern large-scale circuit graphs is limited by GPU memory and training cost, especially for deep models. We revisit deep GNNs for circuit graphs and show that, when trainable, they significantly outperform shallow architectures, motivating an efficient, domain-specific training framework. We propose Grouped-Sparse-Reversible GNN (GSR-GNN), which enables training GNNs with up to hundreds of layers while reducing both compute and memory overhead. GSR-GNN integrates reversible residual modules with a group-wise sparse nonlinear operator that compresses node embeddings without sacrificing task-relevant information, and employs an optimized execution pipeline to eliminate fragmented activation storage and reduce data movement. On sampled circuit graphs, GSR-GNN achieves up to 87.2\% peak memory reduction and over 30$\times$ training speedup with negligible degradation in correlation-based quality metrics, making deep GNNs practical for large-scale EDA workloads.
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
