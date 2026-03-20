---
title: "Remedying Target-Domain Astigmatism for Cross-Domain Few-Shot Object Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18541"
published: "2026-03-20"
fetched: "2026-03-20T15:11:24.673956"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Remedying Target-Domain Astigmatism for Cross-Domain Few-Shot Object Detection
View PDF HTML (experimental)Abstract:Cross-domain few-shot object detection (CD-FSOD) aims to adapt pretrained detectors from a source domain to target domains with limited annotations, suffering from severe domain shifts and data scarcity problems. In this work, we find a previously overlooked phenomenon: models exhibit dispersed and unfocused attention in target domains, leading to imprecise localization and redundant predictions, just like a human cannot focus on visual objects. Therefore, we call it the target-domain Astigmatism problem. Analysis on attention distances across transformer layers reveals that regular fine-tuning inherently shows a trend to remedy this problem, but results are still far from satisfactory, which we aim to enhance in this paper. Biologically inspired by the human fovea-style visual system, we enhance the fine-tuning's inherent trend through a center-periphery attention refinement framework, which contains (1) a Positive Pattern Refinement module to reshape attention toward semantic objects using class-specific prototypes, simulating the visual center region; (2) a Negative Context Modulation module to enhance boundary discrimination by modeling background context, simulating the visual periphery region; and (3) a Textual Semantic Alignment module to strengthen center-periphery distinction through cross-modal cues. Our bio-inspired approach transforms astigmatic attention into focused patterns, substantially improving adaptation to target domains. Experiments on six challenging CD-FSOD benchmarks consistently demonstrate improved detection accuracy and establish new state-of-the-art results.
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
