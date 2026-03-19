---
title: "UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17519"
published: "2026-03-19"
fetched: "2026-03-19T15:12:22.050568"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:UniSem: Generalizable Semantic 3D Reconstruction from Sparse Unposed Images
View PDF HTML (experimental)Abstract:Semantic-aware 3D reconstruction from sparse, unposed images remains challenging for feed-forward 3D Gaussian Splatting (3DGS). Existing methods often predict an over-complete set of Gaussian primitives under sparse-view supervision, leading to unstable geometry and inferior depth quality. Meanwhile, they rely solely on 2D segmenter features for semantic lifting, which provides weak 3D-level and limited generalizable supervision, resulting in incomplete 3D semantics in novel scenes. To address these issues, we propose UniSem, a unified framework that jointly improves depth accuracy and semantic generalization via two key components. First, Error-aware Gaussian Dropout (EGD) performs error-guided capacity control by suppressing redundancy-prone Gaussians using rendering error cues, producing meaningful, geometrically stable Gaussian representations for improved depth estimation. Second, we introduce a Mix-training Curriculum (MTC) that progressively blends 2D segmenter-lifted semantics with the model's own emergent 3D semantic priors, implemented with object-level prototype alignment to enhance semantic coherence and completeness. Extensive experiments on ScanNet and Replica show that UniSem achieves superior performance in depth prediction and open-vocabulary 3D segmentation across varying numbers of input views. Notably, with 16-view inputs, UniSem reduces depth Rel by 15.2% and improves open-vocabulary segmentation mAcc by 3.7% over strong baselines.
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
