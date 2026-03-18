---
title: "Dynamic Memory Transformer for Hyperspectral Image Classification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2504.13242"
published: "2026-03-18"
fetched: "2026-03-18T18:25:40.768635"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Apr 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Dynamic Memory Transformer for Hyperspectral Image Classification
View PDF HTML (experimental)Abstract:Hyperspectral image (HSI) classification (HSIC) requires effective modeling of complex spatial-spectral dependencies under limited labeled data and high dimensionality. While transformer-based models have shown strong capability in capturing long-range contextual information, they often introduce redundant attention patterns, which limits their effectiveness for fine-grained HSI analysis. To address these challenges, this paper proposes MemFormer, a lightweight transformer architecture for HSIC that incorporates a dynamic memory-enhanced attention mechanism. The proposed design augments multi-head self-attention with a compact global memory module that progressively aggregates contextual information across layers, enabling efficient modeling of long-range dependencies while reducing attention redundancy. In addition, a Spatial-Spectral Positional Embedding (SSPE) is used to jointly encode spatial continuity and spectral ordering, providing structurally consistent representations without relying on convolution-based positional encodings. Extensive experiments conducted on three benchmark hyperspectral datasets, including Indian Pines, WHU-Hi-HanChuan, and WHU-Hi-HongHu, demonstrate that MemFormer achieves superior classification performance compared to representative convolutional, hybrid, and transformer-based methods. On the Indian Pines dataset, MemFormer attains an overall accuracy of up to 99.55\%, average accuracy of 99.38\%, and a $\kappa$ coefficient of 99.49\%, highlighting its effectiveness and efficiency for HSIC.
Submission history
From: Muhammad Ahmad [view email][v1] Thu, 17 Apr 2025 17:43:34 UTC (4,752 KB)
[v2] Tue, 17 Mar 2026 12:29:55 UTC (4,658 KB)
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
