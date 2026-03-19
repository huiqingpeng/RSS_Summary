---
title: "S-VGGT: Structure-Aware Subscene Decomposition for Scalable 3D Foundation Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17625"
published: "2026-03-19"
fetched: "2026-03-19T15:14:49.538286"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:S-VGGT: Structure-Aware Subscene Decomposition for Scalable 3D Foundation Models
View PDF HTML (experimental)Abstract:Feed-forward 3D foundation models face a key challenge: the quadratic computational cost introduced by global attention, which severely limits scalability as input length increases. Concurrent acceleration methods, such as token merging, operate at the token level. While they offer local savings, the required nearest-neighbor searches introduce undesirable overhead. Consequently, these techniques fail to tackle the fundamental issue of structural redundancy dominant in dense capture data. In this work, we introduce \textbf{S-VGGT}, a novel approach that addresses redundancy at the structural frame level, drastically shifting the optimization focus. We first leverage the initial features to build a dense scene graph, which characterizes structural scene redundancy and guides the subsequent scene partitioning. Using this graph, we softly assign frames to a small number of subscenes, guaranteeing balanced groups and smooth geometric transitions. The core innovation lies in designing the subscenes to share a common reference frame, establishing a parallel geometric bridge that enables independent and highly efficient processing without explicit geometric alignment. This structural reorganization provides strong intrinsic acceleration by cutting the global attention cost at its source. Crucially, S-VGGT is entirely orthogonal to token-level acceleration methods, allowing the two to be seamlessly combined for compounded speedups without compromising reconstruction fidelity. Code is available at this https URL.
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
