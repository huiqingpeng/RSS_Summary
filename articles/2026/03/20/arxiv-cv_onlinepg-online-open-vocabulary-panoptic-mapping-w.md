---
title: "OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18510"
published: "2026-03-20"
fetched: "2026-03-20T15:10:52.953965"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting
View PDF HTML (experimental)Abstract:Open-vocabulary scene understanding with online panoptic mapping is essential for embodied applications to perceive and interact with environments. However, existing methods are predominantly offline or lack instance-level understanding, limiting their applicability to real-world robotic tasks. In this paper, we propose OnlinePG, a novel and effective system that integrates geometric reconstruction and open-vocabulary perception using 3D Gaussian Splatting in an online setting. Technically, to achieve online panoptic mapping, we employ an efficient local-to-global paradigm with a sliding window. To build local consistency map, we construct a 3D segment clustering graph that jointly leverages geometric and semantic cues, fusing inconsistent segments within sliding window into complete instances. Subsequently, to update the global map, we construct explicit grids with spatial attributes for the local 3D Gaussian map and fuse them into the global map via robust bidirectional bipartite 3D Gaussian instance matching. Finally, we utilize the fused VLM features inside the 3D spatial attribute grids to achieve open-vocabulary scene understanding. Extensive experiments on widely used datasets demonstrate that our method achieves better performance among online approaches, while maintaining real-time efficiency.
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
