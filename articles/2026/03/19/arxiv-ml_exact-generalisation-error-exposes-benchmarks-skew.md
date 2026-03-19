---
title: "Exact Generalisation Error Exposes Benchmarks Skew Graph Neural Networks Success (or Failure)"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.10337"
published: "2026-03-19"
fetched: "2026-03-19T14:16:42.246384"
---

Statistics > Machine Learning
[Submitted on 12 Sep 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Exact Generalisation Error Exposes Benchmarks Skew Graph Neural Networks Success (or Failure)
View PDF HTML (experimental)Abstract:Graph Neural Networks (GNNs) have become the standard method for learning from networks across fields ranging from biology to social systems, yet a principled understanding of what enables them to extract meaningful representations, or why performance varies drastically between similar models, remains elusive. These questions can be answered through the generalisation error, which measures the discrepancy between a model's predictions and the true values it is meant to recover. Although several works have derived generalisation error bounds, learning theoretical bounds are typically loose, restricted to a single architecture, and offer limited insight into what governs generalisation in practice. In this work, we take a fundamentally different approach by deriving the exact generalisation error for a broad range of linear GNNs, including convolutional, PageRank-based, and attention-based models, through the lens of signal processing. Our exact generalisation error exposes a strong benchmark bias in existing literature: commonly used datasets exhibit high alignment between node features and the graph structure, inherently favouring architectures that rely on it. We further show that the similarity between connected nodes (homophily) decisively governs which architectures are best suited for a given graph, thereby explaining how specific benchmark properties systematically shape the reported performance in the literature. Together, these results explain when and why GNNs can effectively leverage structure and feature information, supporting the reliable application of GNNs.
Submission history
From: Nil Ayday [view email][v1] Fri, 12 Sep 2025 15:18:36 UTC (1,731 KB)
[v2] Wed, 18 Mar 2026 12:48:12 UTC (1,447 KB)
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
