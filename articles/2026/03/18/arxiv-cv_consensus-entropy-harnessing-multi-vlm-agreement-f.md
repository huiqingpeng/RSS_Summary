---
title: "Consensus Entropy: Harnessing Multi-VLM Agreement for Self-Verifying and Self-Improving OCR"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2504.11101"
published: "2026-03-18"
fetched: "2026-03-18T18:25:30.176532"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 15 Apr 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Consensus Entropy: Harnessing Multi-VLM Agreement for Self-Verifying and Self-Improving OCR
View PDF HTML (experimental)Abstract:Optical Character Recognition (OCR) is fundamental to Vision-Language Models (VLMs) and high-quality data generation for LLM training. Yet, despite progress in average OCR accuracy, state-of-the-art VLMs still struggle with detecting sample-level errors and lack effective unsupervised quality control. We introduce Consensus Entropy (CE), a training-free, model-agnostic metric that estimates output reliability by measuring inter-model agreement entropy. The core insight is that correct predictions converge in output space, while errors diverge. Based on CE, we develop CE-OCR, a lightweight multi-model framework that verifies outputs by ensemble agreement, selects the best outputs, and further improves efficiency through adaptive routing. Experiments demonstrate that CE is robust for quality verification, improving F1 scores by 42.1\% over VLM-as-Judge. CE-OCR achieves consistent OCR gains, outperforming self-consistency and single-model baselines at the same cost. Notably, CE requires no training or supervision, enabling plug-and-play integration.
Submission history
From: Yulong Zhang [view email][v1] Tue, 15 Apr 2025 11:51:18 UTC (9,664 KB)
[v2] Wed, 16 Apr 2025 03:22:14 UTC (9,664 KB)
[v3] Tue, 17 Mar 2026 10:40:23 UTC (9,852 KB)
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
