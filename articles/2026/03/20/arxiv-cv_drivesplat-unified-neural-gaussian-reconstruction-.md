---
title: "DriveSplat: Unified Neural Gaussian Reconstruction for Dynamic Driving Scenes"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.15376"
published: "2026-03-20"
fetched: "2026-03-20T16:12:37.041715"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 21 Aug 2025 (v1), last revised 19 Mar 2026 (this version, v4)]
Title:DriveSplat: Unified Neural Gaussian Reconstruction for Dynamic Driving Scenes
View PDF HTML (experimental)Abstract:Reconstructing large-scale dynamic driving scenes remains challenging due to the coexistence of static environments with extreme depth variation and diverse dynamic actors exhibiting complex motions. Existing Gaussian Splatting based methods have primarily focused on limited-scale or object-centric settings, and their applicability to large-scale dynamic driving scenes remains underexplored, particularly in the presence of extreme scale variation and non-rigid motions. In this work, we propose DriveSplat, a unified neural Gaussian framework for reconstructing dynamic driving scenes within a unified Gaussian-based representation. For static backgrounds, we introduce a scene-aware learnable level-of-detail (LOD) modeling strategy that explicitly accounts for near, intermediate, and far depth ranges in driving environments, enabling adaptive multi-scale Gaussian allocation. For dynamic actors, we use an object-centric formulation with neural Gaussian primitives, modeling motion through a global rigid transformation and handling non-rigid dynamics via a two-stage deformation that first adjusts anchors and subsequently updates the Gaussians. To further regularize the optimization, we incorporate dense depth and surface normal priors from pre-trained models as auxiliary supervision. Extensive experiments on the Waymo and KITTI benchmarks demonstrate that DriveSplat achieves state-of-the-art performance in novel-view synthesis while producing temporally stable and geometrically consistent reconstructions of dynamic driving scenes. Project page: this https URL.
Submission history
From: Cong Wang [view email][v1] Thu, 21 Aug 2025 09:14:50 UTC (17,855 KB)
[v2] Mon, 25 Aug 2025 03:28:49 UTC (17,855 KB)
[v3] Sun, 21 Sep 2025 15:08:43 UTC (17,853 KB)
[v4] Thu, 19 Mar 2026 09:20:46 UTC (35,938 KB)
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
