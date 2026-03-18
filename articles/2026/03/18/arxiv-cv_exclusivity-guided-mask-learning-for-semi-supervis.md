---
title: "Exclusivity-Guided Mask Learning for Semi-Supervised Crowd Instance Segmentation and Counting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16241"
published: "2026-03-18"
fetched: "2026-03-18T18:08:40.546860"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:Exclusivity-Guided Mask Learning for Semi-Supervised Crowd Instance Segmentation and Counting
View PDF HTML (experimental)Abstract:Semi-supervised crowd analysis is a prominent area of research, as unlabeled data are typically abundant and inexpensive to obtain. However, traditional point-based annotations constrain performance because individual regions are inherently ambiguous, and consequently, learning fine-grained structural semantics from sparse anno tations remains an unresolved challenge. In this paper, we first propose an Exclusion-Constrained Dual-Prompt SAM (EDP-SAM), based on our Nearest Neighbor Exclusion Circle (NNEC) constraint, to generate mask supervision for current datasets. With the aim of segmenting individuals in dense scenes, we then propose Exclusivity-Guided Mask Learning (XMask), which enforces spatial separation through a discriminative mask objective. Gaussian smoothing and a differentiable center sampling strategy are utilized to improve feature continuity and training stability. Building on XMask, we present a semi-supervised crowd counting framework that uses instance mask priors as pseudo-labels, which contain richer shape information than traditional point cues. Extensive experiments on the ShanghaiTech A, UCF-QNRF, and JHU++ datasets (using 5%, 10%, and 40% labeled data) verify that our end-to-end model achieves state-of-the-art semi-supervised segmentation and counting performance, effectively bridging the gap between counting and instance segmentation within a unified framework.
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
