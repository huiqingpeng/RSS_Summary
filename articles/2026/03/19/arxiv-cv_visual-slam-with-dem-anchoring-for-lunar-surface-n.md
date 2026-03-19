---
title: "Visual SLAM with DEM Anchoring for Lunar Surface Navigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17229"
published: "2026-03-19"
fetched: "2026-03-19T16:21:54.817347"
---

Computer Science > Robotics
[Submitted on 18 Mar 2026]
Title:Visual SLAM with DEM Anchoring for Lunar Surface Navigation
View PDF HTML (experimental)Abstract:Future lunar missions will require autonomous rovers capable of traversing tens of kilometers across challenging terrain while maintaining accurate localization and producing globally consistent maps. However, the absence of global positioning systems, extreme illumination, and low-texture regolith make long-range navigation on the Moon particularly difficult, as visual-inertial odometry pipelines accumulate drift over extended traverses. To address this challenge, we present a stereo visual simultaneous localization and mapping (SLAM) system that integrates learned feature detection and matching with global constraints from digital elevation models (DEMs). Our front-end employs learning-based feature extraction and matching to achieve robustness to illumination extremes and repetitive terrain, while the back-end incorporates DEM-derived height and surface-normal factors into a pose graph, providing absolute surface constraints that mitigate long-term drift. We validate our approach using both simulated lunar traverse data generated in Unreal Engine and real Moon/Mars analog data collected from Mt. Etna. Results demonstrate that DEM anchoring consistently reduces absolute trajectory error compared to baseline SLAM methods, lowering drift in long-range navigation even in repetitive or visually aliased terrain.
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
