---
title: "PFGNet: A Fully Convolutional Frequency-Guided Peripheral Gating Network for Efficient Spatiotemporal Predictive Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.20537"
published: "2026-03-20"
fetched: "2026-03-20T16:17:46.166618"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 24 Feb 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:PFGNet: A Fully Convolutional Frequency-Guided Peripheral Gating Network for Efficient Spatiotemporal Predictive Learning
View PDF HTML (experimental)Abstract:Spatiotemporal predictive learning (STPL) aims to forecast future frames from past observations and is essential across a wide range of applications. Compared with recurrent or hybrid architectures, pure convolutional models offer superior efficiency and full parallelism, yet their fixed receptive fields limit their ability to adaptively capture spatially varying motion patterns. Inspired by biological center-surround organization and frequency-selective signal processing, we propose PFGNet, a fully convolutional framework that dynamically modulates receptive fields through pixel-wise frequency-guided gating. The core Peripheral Frequency Gating (PFG) block extracts localized spectral cues and adaptively fuses multi-scale large-kernel peripheral responses with learnable center suppression, effectively forming spatially adaptive band-pass filters. To maintain efficiency, all large kernels are decomposed into separable 1D convolutions ($1 \times k$ followed by $k \times 1$), reducing per-channel computational cost from $O(k^2)$ to $O(2k)$. PFGNet enables structure-aware spatiotemporal modeling without recurrence or attention. Experiments on Moving MNIST, TaxiBJ, Human3.6M, and KTH show that PFGNet delivers SOTA or near-SOTA forecasting performance with substantially fewer parameters and FLOPs. Our code is available at this https URL.
Submission history
From: Xinyong Cai [view email][v1] Tue, 24 Feb 2026 04:31:12 UTC (2,843 KB)
[v2] Thu, 19 Mar 2026 14:37:55 UTC (2,851 KB)
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
