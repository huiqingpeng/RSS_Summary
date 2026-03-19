---
title: "Test-Time 3D Occupancy Prediction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2503.08485"
published: "2026-03-19"
fetched: "2026-03-19T16:23:49.302462"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 11 Mar 2025 (v1), last revised 18 Mar 2026 (this version, v4)]
Title:Test-Time 3D Occupancy Prediction
View PDF HTML (experimental)Abstract:Self-supervised 3D occupancy prediction offers a promising solution for understanding complex driving scenes without requiring costly 3D annotations. However, training dense occupancy decoders to capture fine-grained geometry and semantics can demand hundreds of GPU hours, and once trained, such models struggle to adapt to varying voxel resolutions or novel object categories without extensive retraining. To overcome these limitations, we propose a practical and flexible test-time occupancy prediction framework termed TT-Occ. Our method incrementally constructs, optimizes, and voxelizes time-aware 3D Gaussians from raw sensor streams by integrating vision foundation models (VFMs) at runtime. The flexible representation of 3D Gaussians enables voxelization at arbitrary user-specified resolutions, while the strong generalization capability of VFMs supports accurate perception and open-vocabulary recognition without requiring any network training or fine-tuning. To validate the generality and effectiveness of our framework, we present two variants: a LiDAR-based version and a vision-centric version, and conduct extensive experiments on the Occ3D-nuScenes and nuCraft benchmarks under varying voxel resolutions. Experimental results show that TT-Occ significantly outperforms existing computationally expensive pretrained self-supervised counterparts. Code is available at this https URL.
Submission history
From: Fengyi Zhang [view email][v1] Tue, 11 Mar 2025 14:37:39 UTC (23,757 KB)
[v2] Fri, 6 Jun 2025 08:21:31 UTC (10,614 KB)
[v3] Fri, 5 Dec 2025 05:52:18 UTC (13,999 KB)
[v4] Wed, 18 Mar 2026 06:30:16 UTC (13,525 KB)
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
