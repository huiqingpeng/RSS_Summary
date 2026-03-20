---
title: "Multiscale Switch for Semi-Supervised and Contrastive Learning in Medical Ultrasound Image Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18655"
published: "2026-03-20"
fetched: "2026-03-20T15:14:26.173917"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Multiscale Switch for Semi-Supervised and Contrastive Learning in Medical Ultrasound Image Segmentation
View PDF HTML (experimental)Abstract:Medical ultrasound image segmentation faces significant challenges due to limited labeled data and characteristic imaging artifacts including speckle noise and low-contrast boundaries. While semi-supervised learning (SSL) approaches have emerged to address data scarcity, existing methods suffer from suboptimal unlabeled data utilization and lack robust feature representation mechanisms. In this paper, we propose Switch, a novel SSL framework with two key innovations: (1) Multiscale Switch (MSS) strategy that employs hierarchical patch mixing to achieve uniform spatial coverage; (2) Frequency Domain Switch (FDS) with contrastive learning that performs amplitude switching in Fourier space for robust feature representations. Our framework integrates these components within a teacher-student architecture to effectively leverage both labeled and unlabeled data. Comprehensive evaluation across six diverse ultrasound datasets (lymph nodes, breast lesions, thyroid nodules, and prostate) demonstrates consistent superiority over state-of-the-art methods. At 5\% labeling ratio, Switch achieves remarkable improvements: 80.04\% Dice on LN-INT, 85.52\% Dice on DDTI, and 83.48\% Dice on Prostate datasets, with our semi-supervised approach even exceeding fully supervised baselines. The method maintains parameter efficiency (1.8M parameters) while delivering superior performance, validating its effectiveness for resource-constrained medical imaging applications. The source code is publicly available at this https URL
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
