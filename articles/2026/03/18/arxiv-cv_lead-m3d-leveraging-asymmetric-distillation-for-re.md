---
title: "LeAD-M3D: Leveraging Asymmetric Distillation for Real-Time Monocular 3D Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.05663"
published: "2026-03-18"
fetched: "2026-03-18T18:30:10.753439"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 5 Dec 2025 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:LeAD-M3D: Leveraging Asymmetric Distillation for Real-Time Monocular 3D Detection
View PDFAbstract:Real-time monocular 3D object detection remains challenging due to severe depth ambiguity, viewpoint shifts, and the high computational cost of 3D reasoning. Existing approaches either rely on LiDAR or geometric priors to compensate for missing depth or sacrifice efficiency to achieve competitive accuracy. We introduce LeAD-M3D, a monocular 3D detector that achieves state-of-the-art accuracy and real-time inference without extra modalities. Our method is enabled by three key components. Asymmetric Augmentation Denoising Distillation (A2D2) transfers geometric knowledge from a clean-image teacher to a MixUp-noised student via a quality- and importance-weighted depth-feature loss, enabling stronger depth reasoning without LiDAR. 3D-aware Consistent Matching (CM$_{\text{3D}}$) improves prediction-to-ground truth assignment by integrating 3D MGIoU into the matching score, yielding stable and precise supervision. Finally, Confidence-Gated 3D Inference (CGI$_{\text{3D}}$) accelerates inference by restricting expensive 3D regression to confident regions. Together, these contributions set a new Pareto frontier for monocular 3D detection: LeAD-M3D achieves state-of-the-art accuracy on KITTI and Waymo, and the best reported car AP on Rope3D, while running up to 3.6$\,\times$ faster than prior high-accuracy models (e.g., MonoDiff). LeAD-M3D demonstrates that high fidelity and real-time monocular 3D detection is simultaneously attainable, without LiDAR, stereo, or strong geometric assumptions.
Submission history
From: Christoph Reich [view email][v1] Fri, 5 Dec 2025 12:08:18 UTC (14,237 KB)
[v2] Mon, 16 Mar 2026 21:00:28 UTC (20,162 KB)
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
