---
title: "SenseShift6D: Multimodal RGB-D Benchmarking for Robust 6D Pose Estimation across Environment and Sensor Variations"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2507.05751"
published: "2026-03-20"
fetched: "2026-03-20T16:12:18.832136"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 8 Jul 2025 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:SenseShift6D: Multimodal RGB-D Benchmarking for Robust 6D Pose Estimation across Environment and Sensor Variations
View PDF HTML (experimental)Abstract:Recent advances on 6D object pose estimation have achieved high performance on representative benchmarks such as LM-O, YCB-V, and T-Less. However, these datasets were captured under fixed illumination and camera settings, leaving the impact of real-world variations in illumination, exposure, gain or depth-sensor mode largely unexplored. To bridge this gap, we introduce SenseShift6D, the first RGB-D dataset that physically sweeps 13 RGB exposures, 9 RGB gains, auto-exposure, 4 depth-capture modes, and 5 illumination levels. For six common household objects, we acquire 198.8k RGB and 20.0k depth images (i.e., 795.4k RGB-D scenes), providing 1,380 unique sensor-lighting permutations per object pose. Experiments with state-of-the-art pretrained, generalizable pose estimators reveal substantial performance variation across lighting and sensor settings, despite their large-scale pretraining. Strikingly, even instance-level estimators-trained and tested on identical objects and backgrounds-exhibit pronounced sensitivity to environmental and sensor shifts. These findings establish sensor- and environment-aware robustness as an underexplored yet essential dimension for real-world deployment, and motivate SenseShift6D as a necessary benchmark for the community. Finally, to illustrate the opportunity enabled by this benchmark, we evaluate test-time multimodal sensor selection without retraining. An idealized (oracle) controller yields remarkable gains of up to +16.7 pp for generalizable models, whereas a practical consistency-based proxy improves performance only marginally, highlighting substantial headroom and the need for future research on reliable sensor-aware adaptation.
Submission history
From: Yegyu Han [view email][v1] Tue, 8 Jul 2025 07:54:07 UTC (12,491 KB)
[v2] Sat, 11 Oct 2025 05:58:53 UTC (43,208 KB)
[v3] Thu, 19 Mar 2026 07:18:06 UTC (43,504 KB)
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
