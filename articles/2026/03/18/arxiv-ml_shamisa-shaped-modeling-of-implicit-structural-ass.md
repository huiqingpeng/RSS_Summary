---
title: "SHAMISA: SHAped Modeling of Implicit Structural Associations for Self-supervised No-Reference Image Quality Assessment"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.13669"
published: "2026-03-18"
fetched: "2026-03-18T17:16:22.523042"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 14 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:SHAMISA: SHAped Modeling of Implicit Structural Associations for Self-supervised No-Reference Image Quality Assessment
View PDF HTML (experimental)Abstract:No-Reference Image Quality Assessment (NR-IQA) aims to estimate perceptual quality without access to a reference image of pristine quality. Learning an NR-IQA model faces a fundamental bottleneck: its need for a large number of costly human perceptual labels. We propose SHAMISA, a non-contrastive self-supervised framework that learns from unlabeled distorted images by leveraging explicitly structured relational supervision. Unlike prior methods that impose rigid, binary similarity constraints, SHAMISA introduces implicit structural associations, defined as soft, controllable relations that are both distortion-aware and content-sensitive, inferred from synthetic metadata and intrinsic feature structure. A key innovation is our compositional distortion engine, which generates an uncountable family of degradations from continuous parameter spaces, grouped so that only one distortion factor varies at a time. This enables fine-grained control over representational similarity during training: images with shared distortion patterns are pulled together in the embedding space, while severity variations produce structured, predictable shifts. We integrate these insights via dual-source relation graphs that encode both known degradation profiles and emergent structural affinities to guide the learning process throughout training. A convolutional encoder is trained under this supervision and then frozen for inference, with quality prediction performed by a linear regressor on its features. Extensive experiments on synthetic, authentic, and cross-dataset NR-IQA benchmarks demonstrate that SHAMISA achieves strong overall performance with improved cross-dataset generalization and robustness, all without human quality annotations or contrastive losses.
Submission history
From: Mahdi Naseri [view email][v1] Sat, 14 Mar 2026 00:37:26 UTC (7,265 KB)
[v2] Tue, 17 Mar 2026 17:34:31 UTC (7,265 KB)
Current browse context:
cs.CV
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
