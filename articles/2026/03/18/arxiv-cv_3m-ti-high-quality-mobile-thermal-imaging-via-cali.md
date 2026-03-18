---
title: "3M-TI: High-Quality Mobile Thermal Imaging via Calibration-free Multi-Camera Cross-Modal Diffusion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.19117"
published: "2026-03-18"
fetched: "2026-03-18T18:29:26.840387"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 24 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:3M-TI: High-Quality Mobile Thermal Imaging via Calibration-free Multi-Camera Cross-Modal Diffusion
View PDF HTML (experimental)Abstract:The miniaturization of thermal sensors for mobile platforms inherently limits their spatial resolution and textural fidelity, leading to blurry and less informative images. Existing thermal super-resolution (SR) methods can be grouped into single-image and RGB-guided approaches: the former struggles to recover fine structures from limited information, while the latter relies on accurate and laborious cross-camera calibration, which hinders practical deployment and robustness. Here, we propose 3M-TI, a calibration-free Multi-camera cross-Modality diffusion framework for Mobile Thermal Imaging. At its core, 3M-TI integrates a cross-modal self-attention module (CSM) into the diffusion UNet, replacing the original self-attention layers to adaptively align thermal and RGB features throughout the denoising process, without requiring explicit camera calibration. This design enables the diffusion network to leverage its generative prior to enhance spatial resolution, structural fidelity, and texture detail in the super-resolved thermal images. Extensive evaluations on real-world mobile thermal cameras and public benchmarks validate our superior performance, achieving state-of-the-art results in both visual quality and quantitative metrics. More importantly, the thermal images enhanced by 3M-TI lead to substantial gains in critical downstream tasks like object detection and segmentation, underscoring its practical value for robust mobile thermal perception systems. More materials: this https URL.
Submission history
From: Xiaoyun Yuan [view email][v1] Mon, 24 Nov 2025 13:48:47 UTC (4,694 KB)
[v2] Mon, 16 Mar 2026 05:48:23 UTC (4,503 KB)
[v3] Tue, 17 Mar 2026 07:59:40 UTC (4,503 KB)
Current browse context:
cs.CV
Change to browse by:
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
