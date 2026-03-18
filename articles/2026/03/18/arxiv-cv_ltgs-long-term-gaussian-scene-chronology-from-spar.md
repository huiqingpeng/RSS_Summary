---
title: "LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.09881"
published: "2026-03-18"
fetched: "2026-03-18T18:27:45.186645"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 10 Oct 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates
View PDF HTML (experimental)Abstract:Recent advances in novel-view synthesis can create the photo-realistic visualization of real-world environments from conventional camera captures. However, the everyday environment experiences frequent scene changes, which require dense observations, both spatially and temporally, that an ordinary setup cannot cover. We propose long-term Gaussian scene chronology from sparse-view updates, coined LTGS, an efficient scene representation that can embrace everyday changes from highly under-constrained casual captures. Given an incomplete and unstructured 3D Gaussian Splatting (3DGS) representation obtained from an initial set of input images, we robustly model the long-term chronology of the scene despite abrupt movements and subtle environmental variations. We construct objects as template Gaussians, which serve as structural, reusable priors for shared object tracks. Then, the object templates undergo a further refinement pipeline that modulates the priors to adapt to temporally varying environments given few-shot observations. Once trained, our framework is generalizable across multiple time steps through simple transformations, significantly enhancing the scalability for a temporal evolution of 3D environments. As existing datasets do not explicitly represent the long-term real-world changes with a sparse capture setup, we collect real-world datasets to evaluate the practicality of our pipeline. Experiments demonstrate that our framework achieves superior reconstruction quality compared to other baselines while enabling fast and light-weight updates.
Submission history
From: Minkwan Kim [view email][v1] Fri, 10 Oct 2025 21:36:49 UTC (3,094 KB)
[v2] Tue, 17 Mar 2026 07:15:22 UTC (3,833 KB)
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
