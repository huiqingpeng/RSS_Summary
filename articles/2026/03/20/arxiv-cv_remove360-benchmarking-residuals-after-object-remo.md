---
title: "Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.11431"
published: "2026-03-20"
fetched: "2026-03-20T16:12:25.951297"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 15 Aug 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian Splatting
View PDF HTML (experimental)Abstract:An object can disappear from a 3D scene, yet still be detectable. Even after visual removal, modern vision models may infer what was originally present. In this work, we introduce a novel benchmark and evaluation framework to quantify semantic residuals, the unintended cues left behind after object removal in 3D Gaussian Splatting. We conduct experiments across a diverse set of indoor and outdoor scenes, showing that current methods often preserve semantic information despite the absence of visual geometry. Notably, even when removal is followed by inpainting, residual cues frequently remain detectable by foundation models. We also present Remove360, a real-world dataset of pre- and post-removal RGB captures with object-level masks. Unlike prior datasets focused on isolated object instances, Remove360 contains complex, cluttered scenes that enable evaluation of object removal in full-scene settings. By leveraging the ground-truth post-removal images, we directly assess whether semantic presence is eliminated and whether downstream models can still infer what was removed. Our results reveal a consistent gap between geometric removal and semantic erasure, exposing critical limitations in existing 3D editing pipelines and highlighting the need for privacy-aware removal methods that eliminate recoverable cues, not only visible geometry. Dataset and evaluation code are publicly available.
Submission history
From: Simona Kocour [view email][v1] Fri, 15 Aug 2025 12:15:06 UTC (32,284 KB)
[v2] Thu, 19 Mar 2026 11:49:56 UTC (22,960 KB)
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
