---
title: "TALO: Pushing 3D Vision Foundation Models Towards Globally Consistent Online Reconstruction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.02341"
published: "2026-03-19"
fetched: "2026-03-19T16:28:54.662116"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 2 Dec 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:TALO: Pushing 3D Vision Foundation Models Towards Globally Consistent Online Reconstruction
View PDF HTML (experimental)Abstract:3D vision foundation models have shown strong generalization in reconstructing key 3D attributes from uncalibrated images through a single feed-forward pass. However, when deployed in online settings such as driving scenarios, predictions are made over temporal windows, making it non-trivial to maintain consistency across time. Recent strategies align consecutive predictions by solving global transformation, yet our analysis reveals their fundamental limitations in assumption validity, local alignment scope, and robustness under noisy geometry. In this work, we propose a higher-DOF and long-term alignment framework based on Thin Plate Spline, leveraging globally propagated control points to correct spatially varying inconsistencies. In addition, we adopt a point-agnostic submap registration design that is inherently robust to noisy geometry predictions. The proposed framework is fully plug-and-play, compatible with diverse 3D foundation models and camera configurations (e.g., monocular or surround-view). Extensive experiments demonstrate that our method consistently yields more coherent geometry and lower trajectory errors across multiple datasets, backbone models, and camera setups, highlighting its robustness and generality. Code is available at this https URL.
Submission history
From: Fengyi Zhang [view email][v1] Tue, 2 Dec 2025 02:22:20 UTC (40,529 KB)
[v2] Wed, 31 Dec 2025 06:29:09 UTC (40,530 KB)
[v3] Wed, 18 Mar 2026 06:22:57 UTC (40,545 KB)
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
