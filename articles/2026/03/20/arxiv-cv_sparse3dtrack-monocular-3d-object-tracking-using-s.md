---
title: "Sparse3DTrack: Monocular 3D Object Tracking Using Sparse Supervision"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18298"
published: "2026-03-20"
fetched: "2026-03-20T16:07:47.214978"
---

Computer Science > Robotics
[Submitted on 18 Mar 2026]
Title:Sparse3DTrack: Monocular 3D Object Tracking Using Sparse Supervision
View PDF HTML (experimental)Abstract:Monocular 3D object tracking aims to estimate temporally consistent 3D object poses across video frames, enabling autonomous agents to reason about scene dynamics. However, existing state-of-the-art approaches are fully supervised and rely on dense 3D annotations over long video sequences, which are expensive to obtain and difficult to scale. In this work, we address this fundamental limitation by proposing the first sparsely supervised framework for monocular 3D object tracking. Our approach decomposes the task into two sequential sub-problems: 2D query matching and 3D geometry estimation. Both components leverage the spatio-temporal consistency of image sequences to augment a sparse set of labeled samples and learn rich 2D and 3D representations of the scene. Leveraging these learned cues, our model automatically generates high-quality 3D pseudolabels across entire videos, effectively transforming sparse supervision into dense 3D track annotations. This enables existing fully-supervised trackers to effectively operate under extreme label sparsity. Extensive experiments on the KITTI and nuScenes datasets demonstrate that our method significantly improves tracking performance, achieving an improvement of up to 15.50 p.p. while using at most four ground truth annotations per track.
Current browse context:
cs.RO
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
