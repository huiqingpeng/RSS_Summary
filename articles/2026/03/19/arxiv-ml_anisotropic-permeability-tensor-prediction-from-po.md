---
title: "Anisotropic Permeability Tensor Prediction from Porous Media Microstructure via Physics-Informed Progressive Transfer Learning with Hybrid CNN-Transformer"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17532"
published: "2026-03-19"
fetched: "2026-03-19T12:12:59.255677"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Anisotropic Permeability Tensor Prediction from Porous Media Microstructure via Physics-Informed Progressive Transfer Learning with Hybrid CNN-Transformer
View PDF HTML (experimental)Abstract:Accurate prediction of permeability tensors from pore-scale microstructure images is essential for subsurface flow modeling, yet direct numerical simulation requires hours per sample, fundamentally limiting large-scale uncertainty quantification and reservoir optimization workflows. A physics-informed deep learning framework is presented that resolves this bottleneck by combining a MaxViT hybrid CNN-Transformer architecture with progressive transfer learning and differentiable physical constraints. MaxViT's multi-axis attention mechanism simultaneously resolves grain-scale pore-throat geometry via block-local operations and REV-scale connectivity statistics through grid-global operations, providing the spatial hierarchy that permeability tensor prediction physically requires. Training on 20000 synthetic porous media samples spanning three orders of magnitude in permeability, a three-phase progressive curriculum advances from an ImageNet-pretrained baseline with D4-equivariant augmentation and tensor transformation, through component-weighted loss prioritizing off-diagonal coupling, to frozen-backbone transfer learning with porosity conditioning via Feature-wise Linear Modulation (FiLM). Onsager reciprocity and positive definiteness are enforced via differentiable penalty terms. On a held-out test set of 4000 samples, the framework achieves variance-weighted R2 = 0.9960 (R2_Kxx = 0.9967, R2_Kxy = 0.9758), a 33% reduction in unexplained variance over the supervised baseline. The results offer three transferable principles for physics-informed scientific machine learning: large-scale visual pretraining transfers effectively across domain boundaries; physical constraints are most robustly integrated as differentiable architectural components; and progressive training guided by diagnostic failure-mode analysis enables unambiguous attribution of performance gains across methodological stages.
Submission history
From: Mohammad Nooraiepour [view email][v1] Wed, 18 Mar 2026 09:41:01 UTC (3,926 KB)
Current browse context:
cs.LG
Change to browse by:
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
