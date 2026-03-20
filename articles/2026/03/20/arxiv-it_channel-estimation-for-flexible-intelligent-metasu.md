---
title: "Channel Estimation for Flexible Intelligent Metasurfaces: From Model-Based Approaches to Neural Operators"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2508.00268"
published: "2026-03-20"
fetched: "2026-03-20T17:08:21.779064"
---

Computer Science > Information Theory
[Submitted on 1 Aug 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Channel Estimation for Flexible Intelligent Metasurfaces: From Model-Based Approaches to Neural Operators
View PDF HTML (experimental)Abstract:Flexible intelligent metasurfaces (FIMs) offer a new solution for wireless communications by introducing morphological degrees of freedom, dynamically morphing their three-dimensional shape to ensure multipath signals interfere constructively. However, realizing the desired performance gains in FIM systems is critically dependent on acquiring accurate channel state information across a continuous and high-dimensional deformation space. Therefore, this paper investigates this fundamental channel estimation problem for FIM assisted millimeter-wave communication systems. First, we develop model-based frameworks that structure the problem as either function approximation using interpolation and kernel methods or as a sparse signal recovery problem that leverages the inherent angular sparsity of millimeter-wave channels. To further advance the estimation capability beyond explicit assumptions in model-based channel estimation frameworks, we propose a deep learning-based framework using a Fourier neural operator (FNO). By parameterizing a global convolution operator in the Fourier domain, we design an efficient FNO architecture to learn the continuous operator that maps FIM shapes to channel responses with mesh-independent properties. Furthermore, we exploit a hierarchical FNO (H-FNO) architecture to efficiently capture the multi-scale features across a hierarchy of spatial resolutions. Numerical results demonstrate that the proposed H-FNO significantly outperforms the model-based benchmarks in estimation accuracy and pilot efficiency. In particular, the interpretability analysis show that the proposed H-FNO learns an anisotropic spatial filter adapted to the physical geometry of FIM and is capable of accurately reconstructing the non-linear channel response across the continuous deformation space.
Submission history
From: Jian Xiao [view email][v1] Fri, 1 Aug 2025 02:27:21 UTC (13,842 KB)
[v2] Sun, 25 Jan 2026 08:35:27 UTC (13,927 KB)
[v3] Thu, 19 Mar 2026 02:42:38 UTC (13,927 KB)
Current browse context:
cs.IT
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
