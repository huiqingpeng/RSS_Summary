---
title: "Bundle Adjustment in the Eager Mode"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2409.12190"
published: "2026-03-19"
fetched: "2026-03-19T17:05:01.605816"
---

Computer Science > Robotics
[Submitted on 18 Sep 2024 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Bundle Adjustment in the Eager Mode
View PDF HTML (experimental)Abstract:Bundle adjustment (BA) is a critical technique in various robotic applications such as simultaneous localization and mapping (SLAM), augmented reality (AR), and photogrammetry. BA optimizes parameters such as camera poses and 3D landmarks to align them with observations. With the growing importance of deep learning in perception systems, there is an increasing need to integrate BA with deep learning frameworks for enhanced reliability and performance. However, widely-used C++-based BA libraries, such as GTSAM, g$^2$o, and Ceres Solver, lack native integration with modern deep learning libraries like PyTorch. This limitation affects their flexibility, ease of debugging, and overall implementation efficiency. To address this gap, we introduce an eager-mode BA library seamlessly integrated with PyTorch with high efficiency. Our approach includes a sparsity-aware auto-differentiation design and GPU-accelerated sparse operations designed for 2nd-order optimization. Our eager-mode BA on GPU demonstrates substantial runtime efficiency, achieving an average speedup of 18.5$\times$, 22$\times$, and 23$\times$ across all benchmarks compared to GTSAM, g$^2$o, and Ceres, respectively.
Submission history
From: Zitong Zhan [view email][v1] Wed, 18 Sep 2024 17:59:29 UTC (1,859 KB)
[v2] Mon, 21 Jul 2025 23:13:56 UTC (12,166 KB)
[v3] Tue, 17 Mar 2026 18:28:38 UTC (12,163 KB)
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
