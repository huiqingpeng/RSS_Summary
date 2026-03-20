---
title: "Measuring 3D Spatial Geometric Consistency in Dynamic Generated Videos"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19048"
published: "2026-03-20"
fetched: "2026-03-20T15:18:36.545634"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Measuring 3D Spatial Geometric Consistency in Dynamic Generated Videos
View PDF HTML (experimental)Abstract:Recent generative models can produce high-fidelity videos, yet they often exhibit 3D spatial geometric inconsistencies. Existing evaluation methods fail to accurately characterize these inconsistencies: fidelity-centric metrics like FVD are insensitive to geometric distortions, while consistency-focused benchmarks often penalize valid foreground dynamics. To address this gap, we introduce SGC, a metric for evaluating 3D \textbf{S}patial \textbf{G}eometric \textbf{C}onsistency in dynamically generated videos. We quantify geometric consistency by measuring the divergence among multiple camera poses estimated from distinct local regions. Our approach first separates static from dynamic regions, then partitions the static background into spatially coherent sub-regions. We predict depth for each pixel, estimate a local camera pose for each subregion, and compute the divergence among these poses to quantify geometric consistency. Experiments on real and generative videos demonstrate that SGC robustly quantifies geometric inconsistencies, effectively identifying critical failures missed by existing metrics.
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
