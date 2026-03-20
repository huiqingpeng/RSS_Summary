---
title: "Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18402"
published: "2026-03-20"
fetched: "2026-03-20T15:08:01.911379"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning
View PDF HTML (experimental)Abstract:We present Inst4DGS, an instance-decomposed 4D Gaussian Splatting (4DGS) approach with long-horizon per-Gaussian trajectories. While dynamic 4DGS has advanced rapidly, instance-decomposed 4DGS remains underexplored, largely due to the difficulty of associating inconsistent instance labels across independently segmented multi-view videos. We address this challenge by introducing per-video label-permutation latents that learn cross-video instance matches through a differentiable Sinkhorn layer, enabling direct multi-view supervision with consistent identity preservation. This explicit label alignment yields sharp decision boundaries and temporally stable identities without identity drift. To further improve efficiency, we propose instance-decomposed motion scaffolds that provide low-dimensional motion bases per object for long-horizon trajectory optimization. Experiments on Panoptic Studio and Neural3DV show that Inst4DGS jointly supports tracking and instance decomposition while achieving state-of-the-art rendering and segmentation quality. On the Panoptic Studio dataset, Inst4DGS improves PSNR from 26.10 to 28.36, and instance mIoU from 0.6310 to 0.9129, over the strongest baseline.
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
