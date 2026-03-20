---
title: "1S-DAug: One-Shot Data Augmentation for Robust Few-Shot Generalization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.00114"
published: "2026-03-20"
fetched: "2026-03-20T15:03:40.973491"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 27 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:1S-DAug: One-Shot Data Augmentation for Robust Few-Shot Generalization
View PDF HTML (experimental)Abstract:Few-shot learning (FSL) challenges model generalization to novel classes based on just a few shots of labeled examples, a testbed where traditional test-time augmentations fail to be effective. We introduce 1S-DAug, a one-shot generative augmentation operator that synthesizes diverse yet faithful variants from just one example image at test time. 1S-DAug couples traditional geometric perturbations with controlled noise injection and a denoising diffusion process conditioned on the original image. The generated images are then encoded and aggregated, alongside the original image, into a combined representation for more robust FSL predictions. Integrated as a training-free model-agnostic plugin, 1S-DAug consistently improves FSL across standard benchmarks of 4 different datasets without any model parameter update, including achieving up to 20\% proportional accuracy improvement on the miniImagenet 5-way-1-shot benchmark. Code will be released.
Submission history
From: Yunwei Bai [view email][v1] Tue, 27 Jan 2026 08:01:47 UTC (16,862 KB)
[v2] Thu, 19 Mar 2026 00:00:52 UTC (16,861 KB)
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
