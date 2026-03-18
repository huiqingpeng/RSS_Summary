---
title: "PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.13911"
published: "2026-03-18"
fetched: "2026-03-18T18:26:41.504811"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Aug 2025 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:PhysGM: Large Physical Gaussian Model for Feed-Forward 4D Synthesis
View PDF HTML (experimental)Abstract:Despite advances in physics-based 3D motion synthesis, current methods face key limitations: reliance on pre-reconstructed 3D Gaussian Splatting (3DGS) built from dense multi-view images with time-consuming per-scene optimization; physics integration via either inflexible, hand-specified attributes or unstable, optimization-heavy guidance from video models using Score Distillation Sampling (SDS); and naive concatenation of prebuilt 3DGS with physics modules, which ignores physical information embedded in appearance and yields suboptimal performance. To address these issues, we propose PhysGM, a feed-forward framework that jointly predicts 3D Gaussian representation and physical properties from a single image, enabling immediate simulation and high-fidelity 4D rendering. Unlike slow appearance-agnostic optimization methods, we first pre-train a physics-aware reconstruction model that directly infers both Gaussian and physical parameters. We further refine the model with Direct Preference Optimization (DPO), aligning simulations with the physically plausible reference videos and avoiding the high-cost SDS optimization. To address the absence of a supporting dataset for this task, we propose PhysAssets, a dataset of 50K+ 3D assets annotated with physical properties and corresponding reference videos. Experiments show that PhysGM produces high-fidelity 4D simulations from a single image in one minute, achieving a significant speedup over prior work while delivering realistic renderings. Our project page is at:this https URL
Submission history
From: Chunji Lv [view email][v1] Tue, 19 Aug 2025 15:10:30 UTC (9,367 KB)
[v2] Fri, 19 Dec 2025 08:13:38 UTC (16,618 KB)
[v3] Mon, 9 Mar 2026 09:25:33 UTC (16,728 KB)
[v4] Tue, 17 Mar 2026 07:51:18 UTC (16,728 KB)
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
