---
title: "Match4Annotate: Propagating Sparse Video Annotations via Implicit Neural Feature Matching"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.06471"
published: "2026-03-18"
fetched: "2026-03-18T19:03:03.317504"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 6 Mar 2026 (v1), last revised 16 Mar 2026 (this version, v2)]
Title:Match4Annotate: Propagating Sparse Video Annotations via Implicit Neural Feature Matching
View PDF HTML (experimental)Abstract:Acquiring per-frame video annotations remains a primary bottleneck for deploying computer vision in specialized domains such as medical imaging, where expert labeling is slow and costly. Label propagation offers a natural solution, yet existing approaches face fundamental limitations. Video trackers and segmentation models can propagate labels within a single sequence but require per-video initialization and cannot generalize across videos. Classic correspondence pipelines operate on detector-chosen keypoints and struggle in low-texture scenes, while dense feature matching and one-shot segmentation methods enable cross-video propagation but lack spatiotemporal smoothness and unified support for both point and mask annotations. We present Match4Annotate, a lightweight framework for both intra-video and inter-video propagation of point and mask annotations. Our method fits a SIREN-based implicit neural representation to DINOv3 features at test time, producing a continuous, high-resolution spatiotemporal feature field, and learns a smooth implicit deformation field between frame pairs to guide correspondence matching. We evaluate on three challenging clinical ultrasound datasets. Match4Annotate achieves state-of-the-art inter-video propagation, outperforming feature matching and one-shot segmentation baselines, while remaining competitive with specialized trackers for intra-video propagation. Our results show that lightweight, test-time-optimized feature matching pipelines have the potential to offer an efficient and accessible solution for scalable annotation workflows.
Submission history
From: Praneeth Namburi [view email][v1] Fri, 6 Mar 2026 16:56:46 UTC (11,108 KB)
[v2] Mon, 16 Mar 2026 19:49:06 UTC (20,510 KB)
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
