---
title: "Scalable Feature Learning on Huge Knowledge Graphs for Downstream Machine Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2507.00965"
published: "2026-03-18"
fetched: "2026-03-18T16:18:32.238889"
---

Computer Science > Machine Learning
[Submitted on 1 Jul 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Scalable Feature Learning on Huge Knowledge Graphs for Downstream Machine Learning
View PDF HTML (experimental)Abstract:Many machine learning tasks can benefit from external knowledge. Large knowledge graphs store such knowledge, and embedding methods can be used to distill it into ready-to-use vector representations for downstream applications. For this purpose, current models have however two limitations: they are primarily optimized for link prediction, via local contrastive learning, and their application to the largest graphs requires significant engineering effort due to GPU memory limits. To address these, we introduce SEPAL: a Scalable Embedding Propagation ALgorithm for large knowledge graphs designed to produce high-quality embeddings for downstream tasks at scale. The key idea of SEPAL is to ensure global embedding consistency by optimizing embeddings only on a small core of entities, and then propagating them to the rest of the graph with message passing. We evaluate SEPAL on 7 large-scale knowledge graphs and 46 downstream machine learning tasks. Our results show that SEPAL significantly outperforms previous methods on downstream tasks. In addition, SEPAL scales up its base embedding model, enabling fitting huge knowledge graphs on commodity hardware.
Submission history
From: Félix Lefebvre [view email][v1] Tue, 1 Jul 2025 17:15:35 UTC (668 KB)
[v2] Tue, 18 Nov 2025 13:24:36 UTC (679 KB)
[v3] Tue, 17 Mar 2026 14:52:11 UTC (831 KB)
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
