---
title: "On the Degrees of Freedom of Gridded Control Points in Learning-Based Medical Image Registration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16940"
published: "2026-03-19"
fetched: "2026-03-19T16:21:07.341968"
---

Electrical Engineering and Systems Science > Image and Video Processing
[Submitted on 15 Mar 2026]
Title:On the Degrees of Freedom of Gridded Control Points in Learning-Based Medical Image Registration
View PDF HTML (experimental)Abstract:Many registration problems are ill-posed in homogeneous or noisy regions, and dense voxel-wise decoders can be unnecessarily high-dimensional. A sparse control-point parameterisation provides a compact, smooth deformation representation while reducing memory and improving stability. This work investigates the required control points for learning-based registration network development. We present GridReg, a learning-based registration framework that replaces dense voxel-wise decoding with displacement predictions at a sparse grid of control points. This design substantially cuts the parameter count and memory while retaining registration accuracy. Multiscale 3D encoder feature maps are flattened into a 1D token sequence with positional encoding to retain spatial context. The model then predicts a sparse gridded deformation field using a cross-attention module. We further introduce grid-adaptive training, enabling an adaptive model to operate at multiple grid sizes at inference without retraining. This work quantitatively demonstrates the benefits of using sparse grids. Using three data sets for registering prostate gland, pelvic organs and neurological structures, the results suggested a significant improvement with the usage of grid-controled displacement field. Alternatively, the superior registration performance was obtained using the proposed approach, with a similar or less computational cost, compared with existing algorithms that predict DDFs or displacements sampled on scattered key points.
Current browse context:
eess.IV
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
