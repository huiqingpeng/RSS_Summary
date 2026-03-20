---
title: "UEPS: Robust and Efficient MRI Reconstruction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18572"
published: "2026-03-20"
fetched: "2026-03-20T16:08:43.329018"
---

Electrical Engineering and Systems Science > Image and Video Processing
[Submitted on 19 Mar 2026]
Title:UEPS: Robust and Efficient MRI Reconstruction
View PDF HTML (experimental)Abstract:Deep unrolled models (DUMs) have become the state of the art for accelerated MRI reconstruction, yet their robustness under domain shift remains a critical barrier to clinical adoption. In this work, we identify coil sensitivity map (CSM) estimation as the primary bottleneck limiting generalization. To address this, we propose UEPS, a novel DUM architecture featuring three key innovations: (i) an Unrolled Expanded (UE) design that eliminates CSM dependency by reconstructing each coil independently; (ii) progressive resolution, which leverages k-space-to-image mapping for efficient coarse-to-fine refinement; and (iii) sparse attention tailored to MRI's 1D undersampling nature. These physics-grounded designs enable simultaneous gains in robustness and computational efficiency. We construct a large-scale zero-shot transfer benchmark comprising 10 out-of-distribution test sets spanning diverse clinical shifts -- anatomy, view, contrast, vendor, field strength, and coil configurations. Extensive experiments demonstrate that UEPS consistently and substantially outperforms existing DUM, end-to-end, diffusion, and untrained methods across all OOD tests, achieving state-of-the-art robustness with low-latency inference suitable for real-time deployment.
Current browse context:
eess.IV
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
