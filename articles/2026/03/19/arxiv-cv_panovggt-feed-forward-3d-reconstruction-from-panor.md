---
title: "PanoVGGT: Feed-Forward 3D Reconstruction from Panoramic Imagery"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17571"
published: "2026-03-19"
fetched: "2026-03-19T15:14:10.007794"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:PanoVGGT: Feed-Forward 3D Reconstruction from Panoramic Imagery
View PDF HTML (experimental)Abstract:Panoramic imagery offers a full 360° field of view and is increasingly common in consumer devices. However, it introduces non-pinhole distortions that challenge joint pose estimation and 3D reconstruction. Existing feed-forward models, built for perspective cameras, generalize poorly to this setting. We propose PanoVGGT, a permutation-equivariant Transformer framework that jointly predicts camera poses, depth maps, and 3D point clouds from one or multiple panoramas in a single forward pass. The model incorporates spherical-aware positional embeddings and a panorama-specific three-axis SO(3) rotation augmentation, enabling effective geometric reasoning in the spherical domain. To resolve inherent global-frame ambiguity, we further introduce a stochastic anchoring strategy during training. In addition, we contribute PanoCity, a large-scale outdoor panoramic dataset with dense depth and 6-DoF pose annotations. Extensive experiments on PanoCity and standard benchmarks demonstrate that PanoVGGT achieves competitive accuracy, strong robustness, and improved cross-domain generalization. Code and dataset will be released.
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
