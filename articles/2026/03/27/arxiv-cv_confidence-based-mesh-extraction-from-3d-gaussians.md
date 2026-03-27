---
title: "Confidence-Based Mesh Extraction from 3D Gaussians"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24725"
published: "2026-03-27"
fetched: "2026-03-28T07:15:56.668133"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 25 Mar 2026]
Title:Confidence-Based Mesh Extraction from 3D Gaussians
View PDF HTML (experimental)Abstract:Recently, 3D Gaussian Splatting (3DGS) greatly accelerated mesh extraction from posed images due to its explicit representation and fast software rasterization. While the addition of geometric losses and other priors has improved the accuracy of extracted surfaces, mesh extraction remains difficult in scenes with abundant view-dependent effects. To resolve the resulting ambiguities, prior works rely on multi-view techniques, iterative mesh extraction, or large pre-trained models, sacrificing the inherent efficiency of 3DGS. In this work, we present a simple and efficient alternative by introducing a self-supervised confidence framework to 3DGS: within this framework, learnable confidence values dynamically balance photometric and geometric supervision. Extending our confidence-driven formulation, we introduce losses which penalize per-primitive color and normal variance and demonstrate their benefits to surface extraction. Finally, we complement the above with an improved appearance model, by decoupling the individual terms of the D-SSIM loss. Our final approach delivers state-of-the-art results for unbounded meshes while remaining highly efficient.
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
