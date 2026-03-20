---
title: "LucidFlux: Caption-Free Photo-Realistic Image Restoration via a Large-Scale Diffusion Transformer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.22414"
published: "2026-03-20"
fetched: "2026-03-20T16:13:17.819587"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:LucidFlux: Caption-Free Photo-Realistic Image Restoration via a Large-Scale Diffusion Transformer
View PDF HTML (experimental)Abstract:Image restoration (IR) aims to recover images degraded by unknown mixtures while preserving semanticsconditions under which discriminative restorers and UNet-based diffusion priors often oversmooth, hallucinate, or drift. We present LucidFlux, a caption-free IR framework that adapts a large diffusion transformer (Flux.1) without image captions. Our LucidFlux introduces a lightweight dual-branch conditioner that injects signals from the degraded input and a lightly restored proxy to respectively anchor geometry and suppress artifacts. Then, a timestep- and layer-adaptive modulation schedule is designed to route these cues across the backbones hierarchy, in order to yield coarse-to-fine and context-aware updates that protect the global structure while recovering texture. After that, to avoid the latency and instability of text prompts or Vision-Language Model (VLM) captions, we enforce caption-free semantic alignment via SigLIP features extracted from the proxy. A scalable curation pipeline further filters large-scale data for structure-rich supervision. Across synthetic and in-the-wild benchmarks, our LucidFlux consistently outperforms strong open-source and commercial baselines, and ablation studies verify the necessity of each component. LucidFlux shows that, for large DiTs, when, where, and what to condition onrather than adding parameters or relying on text promptsis the governing lever for robust and caption-free image restoration in the wild.
Submission history
From: Song Fei [view email][v1] Fri, 26 Sep 2025 14:39:08 UTC (36,994 KB)
[v2] Thu, 23 Oct 2025 06:20:47 UTC (36,996 KB)
[v3] Thu, 19 Mar 2026 12:57:49 UTC (41,148 KB)
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
