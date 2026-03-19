---
title: "Look Before You Fuse: 2D-Guided Cross-Modal Alignment for Robust 3D Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2507.16861"
published: "2026-03-19"
fetched: "2026-03-19T16:25:14.982460"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 21 Jul 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Look Before You Fuse: 2D-Guided Cross-Modal Alignment for Robust 3D Detection
View PDF HTML (experimental)Abstract:Integrating LiDAR and camera inputs into a unified Bird's-Eye-View (BEV) representation is crucial for enhancing 3D perception capabilities of autonomous vehicles. However, existing methods suffer from spatial misalignment between LiDAR and camera features, which causes inaccurate depth supervision in camera branch and erroneous fusion during cross-modal feature aggregation. The root cause of this misalignment lies in projection errors, stemming from calibration inaccuracies and rolling shutter this http URL key insight of this work is that locations of these projection errors are not random but highly predictable, as they are concentrated at object-background boundaries which 2D detectors can reliably identify. Based on this, our main motivation is to utilize 2D object priors to pre-align cross-modal features before fusion. To address local misalignment, we propose Prior Guided Depth Calibration (PGDC), which leverages 2D priors to alleviate misalignment and preserve correct cross-modal feature pairs. To resolve global misalignment, we introduce Discontinuity Aware Geometric Fusion (DAGF) to suppress residual noise from PGDC and explicitly enhance sharp depth transitions at object-background boundaries, yielding a structurally aware representation. To effectively utilize these aligned representations, we incorporate Structural Guidance Depth Modulator (SGDM), using a gated attention mechanism to efficiently fuse aligned depth and image features. Our method achieves SOTA performance on nuScenes validation dataset, with its mAP and NDS reaching 71.5% and 73.6% respectively. Additionally, on the Argoverse 2 validation set, we achieve a competitive mAP of 41.7%.
Submission history
From: Xiang Li [view email][v1] Mon, 21 Jul 2025 18:12:22 UTC (14,190 KB)
[v2] Thu, 7 Aug 2025 07:24:32 UTC (28,035 KB)
[v3] Wed, 18 Mar 2026 16:22:49 UTC (22,404 KB)
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
