---
title: "FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.02691"
published: "2026-03-20"
fetched: "2026-03-20T16:14:07.692242"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 3 Oct 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min
View PDF HTML (experimental)Abstract:Gaussian Splatting has become a leading reconstruction technique, known for its high-quality novel view synthesis and detailed reconstruction. However, most existing methods require dense, calibrated views. Reconstructing from free sparse images often leads to poor surface due to limited overlap and overfitting. We introduce FSFSplatter, a new approach for fast surface reconstruction from free sparse images. Our method integrates end-to-end dense Gaussian initialization, camera parameter estimation, and geometry-enhanced scene optimization. Specifically, FSFSplatter employs a large Transformer to encode multi-view images and generates a dense and geometrically consistent Gaussian scene initialization via a self-splitting Gaussian head. It eliminates local floaters through contribution-based pruning and mitigates overfitting to limited views by leveraging depth and multi-view feature supervision with differentiable camera parameters during rapid optimization. FSFSplatter outperforms current state-of-the-art methods on widely used DTU, Replica, and BlendedMVS datasets.
Submission history
From: Yibin Zhao [view email][v1] Fri, 3 Oct 2025 03:17:00 UTC (5,201 KB)
[v2] Sun, 12 Oct 2025 08:49:40 UTC (9,264 KB)
[v3] Thu, 19 Mar 2026 08:27:28 UTC (8,462 KB)
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
