---
title: "Fusion Complexity Inversion: Why Simpler Cross View Modules Outperform SSMs and Cross View Attention Transformers for Pasture Biomass Regression"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.07819"
published: "2026-03-18"
fetched: "2026-03-18T17:14:46.426340"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 8 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Fusion Complexity Inversion: Why Simpler Cross View Modules Outperform SSMs and Cross View Attention Transformers for Pasture Biomass Regression
View PDF HTML (experimental)Abstract:Accurate estimation of pasture biomass from agricultural imagery is critical for sustainable livestock management, yet existing methods are limited by the small, imbalanced, and sparsely annotated datasets typical of real world monitoring. In this study, adaptation of vision foundation models to agricultural regression is systematically evaluated on the CSIRO Pasture Biomass benchmark, a 357 image dual view dataset with laboratory validated, component wise ground truth for five biomass targets, through 17 configurations spanning four backbones (EfficientNet-B3 to DINOv3-ViT-L), five cross view fusion mechanisms, and a 4x2 metadata factorial. A counterintuitive principle, termed "fusion complexity inversion", is uncovered: on scarce agricultural data, a two layer gated depthwise convolution (R^2 = 0.903) outperforms cross view attention transformers (0.833), bidirectional SSMs (0.819), and full Mamba (0.793, below the no fusion baseline). Backbone pretraining scale is found to monotonically dominate all architectural choices, with the DINOv2 -> DINOv3 upgrade alone yielding +5.0 R^2 points. Training only metadata (species, state, and NDVI) is shown to create a universal ceiling at R^2 ~ 0.829, collapsing an 8.4 point fusion spread to 0.1 points. Actionable guidelines for sparse agricultural benchmarks are established: backbone quality should be prioritized over fusion complexity, local modules preferred over global alternatives, and features unavailable at inference excluded.
Submission history
From: Mridankan Mandal [view email][v1] Sun, 8 Mar 2026 21:41:01 UTC (23,078 KB)
[v2] Tue, 17 Mar 2026 09:14:25 UTC (23,078 KB)
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
