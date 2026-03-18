---
title: "Mamba2D: A Natively Multi-Dimensional State-Space Model for Vision Tasks"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2412.16146"
published: "2026-03-18"
fetched: "2026-03-18T18:24:58.861963"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 20 Dec 2024 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Mamba2D: A Natively Multi-Dimensional State-Space Model for Vision Tasks
View PDF HTML (experimental)Abstract:State-Space Models (SSMs) have emerged as an efficient alternative to transformers, yet existing visual SSMs retain deeply ingrained biases from their origins in natural language processing. In this paper, we address these limitations by introducing M2D-SSM, a ground-up re-derivation of selective state-space techniques for multidimensional data. Unlike prior works that apply 1D SSMs directly to images through arbitrary rasterised scanning, our M2D-SSM employs a single 2D scan that factors in both spatial dimensions natively. On ImageNet-1K classification, M2D-T achieves 84.0% top-1 accuracy with only 27M parameters, surpassing all prior SSM-based vision models at that size. M2D-S further achieves 85.3%, establishing state-of-the-art results among SSM-based architectures. Across downstream tasks, Mamba2D achieves 52.2 box AP on MS-COCO object detection (3$\times$ schedule) and 51.7 mIoU on ADE20K segmentation, demonstrating strong generalisation and efficiency at scale. Source code is available at this https URL.
Submission history
From: Enis Baty [view email][v1] Fri, 20 Dec 2024 18:50:36 UTC (689 KB)
[v2] Fri, 17 Jan 2025 10:56:33 UTC (689 KB)
[v3] Tue, 17 Mar 2026 16:43:00 UTC (9,094 KB)
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
