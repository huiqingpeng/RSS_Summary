---
title: "COREA: Coupled Relightable 3D Gaussians and SDFs for Efficient Normal Alignment"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.07107"
published: "2026-03-18"
fetched: "2026-03-18T18:30:29.355038"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 8 Dec 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:COREA: Coupled Relightable 3D Gaussians and SDFs for Efficient Normal Alignment
View PDF HTML (experimental)Abstract:We present COREA, the first unified three-tasks framework that couples an SDF and relightable 3D Gaussians (3DGS) to jointly support SH-based novel-view synthesis (NVS), surface reconstruction, and inverse physically-based rendering (inverse PBR). While recent relightable 3DGS methods have progressed, inverse PBR remains bottlenecked by normal estimation, as the discrete nature of 3DGS often yields oversmoothed and unstable normals. To address this limitation, COREA couples the complementary geometric properties of an SDF and relightable 3DGS on a shared underlying surface, where geometry-constrained relightable 3DGS provides reliable depth signals to anchor SDF geometry and the continuous SDF normal field provides spatially consistent supervision for Gaussian normal learning. We couple these signals through depth-guided alignment and normal supervision with normal-aware densification, and introduce Dual-Density Control to regulate densification by balancing photometric and geometric gradients for stable, memory-efficient training. Experiments on standard benchmarks show that COREA is the only framework that supports all three tasks, achieving competitive performance overall, with particularly superior results in inverse PBR.
Submission history
From: Jaeyoon Lee [view email][v1] Mon, 8 Dec 2025 02:41:42 UTC (6,995 KB)
[v2] Tue, 9 Dec 2025 04:58:05 UTC (6,995 KB)
[v3] Tue, 17 Mar 2026 07:33:30 UTC (22,024 KB)
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
