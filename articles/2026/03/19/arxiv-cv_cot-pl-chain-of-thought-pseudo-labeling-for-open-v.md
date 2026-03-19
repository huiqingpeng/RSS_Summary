---
title: "CoT-PL: Chain-of-Thought Pseudo-Labeling for Open-Vocabulary Object Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.14792"
published: "2026-03-19"
fetched: "2026-03-19T16:26:35.463865"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 16 Oct 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:CoT-PL: Chain-of-Thought Pseudo-Labeling for Open-Vocabulary Object Detection
View PDF HTML (experimental)Abstract:Open-vocabulary object detection (OVD) aims to recognize and localize object categories beyond the training set. Recent approaches leverage vision-language models to generate pseudo-labels using image-text alignment, allowing detectors to generalize to unseen classes without explicit supervision. However, these methods depend heavily on single-step image-text matching, neglecting the intermediate reasoning steps crucial for interpreting semantically complex visual contexts, such as crowding or occlusion. In this paper, we introduce CoT-PL, a framework that incorporates visual chain-of-thought reasoning into the pseudo-labeling process for OVD. It decomposes complex scene understanding into three interpretable steps-object localization, category recognition, and background grounding-where these intermediate reasoning states serve as rich supervision sources. Extensive experiments on standard OVD evaluation protocols demonstrate that CoT-PL achieves state-of-the-art performance with superior pseudo-labeling efficiency, outperforming the strong baseline by 9.4 AP50 for novel classes on OV-COCO and improving box and mask APr by 3.2 and 2.2, respectively, on OV-LVIS. Code and models are available at this https URL.
Submission history
From: Hojun Choi [view email][v1] Thu, 16 Oct 2025 15:27:10 UTC (10,522 KB)
[v2] Wed, 31 Dec 2025 05:45:29 UTC (10,512 KB)
[v3] Wed, 18 Mar 2026 06:53:55 UTC (31,880 KB)
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
