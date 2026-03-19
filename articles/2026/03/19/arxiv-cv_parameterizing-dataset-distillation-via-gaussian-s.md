---
title: "Parameterizing Dataset Distillation via Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.26219"
published: "2026-03-19"
fetched: "2026-03-19T16:26:23.917965"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 30 Sep 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Parameterizing Dataset Distillation via Gaussian Splatting
View PDF HTML (experimental)Abstract:Dataset distillation aims to compress training data while preserving training-aware knowledge, alleviating the reliance on large-scale datasets in modern model training. Dataset parameterization provides a more efficient storage structure for dataset distillation, reducing redundancy and accommodating richer information. However, existing methods either rely on complex auxiliary modules or fail to balance representational capacity and efficiency. In this paper, we propose GSDD, a simple, novel, and effective dataset parameterization technique for Dataset Distillation based on Gaussian Splatting. We adapt CUDA-based splatting operators for parallel training in batch, enabling high-quality rendering with minimal computational and memory overhead. Gaussian primitives can effectively capture meaningful training features, allowing a sparse yet expressive representation of individual images. Leveraging both high representational capacity and efficiency, GSDD substantially increases the diversity of distilled datasets under a given storage budget, thereby improving distillation performance. Beyond achieving competitive results on multiple standard benchmarks, GSDD also delivers significant performance gains on large-scale datasets such as ImageNet-1K and on video distillation tasks. In addition, we conduct comprehensive benchmarks to evaluate the computational efficiency, memory footprint, and cross-GPU architectural stability of GSDD. Code is available on this https URL
Submission history
From: Chenyang Jiang [view email][v1] Tue, 30 Sep 2025 13:19:05 UTC (17,652 KB)
[v2] Tue, 2 Dec 2025 05:14:55 UTC (17,677 KB)
[v3] Wed, 18 Mar 2026 02:00:49 UTC (3,310 KB)
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
