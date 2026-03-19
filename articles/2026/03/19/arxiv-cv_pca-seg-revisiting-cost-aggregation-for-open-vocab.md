---
title: "PCA-Seg: Revisiting Cost Aggregation for Open-Vocabulary Semantic and Part Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17520"
published: "2026-03-19"
fetched: "2026-03-19T15:12:33.075319"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:PCA-Seg: Revisiting Cost Aggregation for Open-Vocabulary Semantic and Part Segmentation
View PDF HTML (experimental)Abstract:Recent advances in vision-language models (VLMs) have garnered substantial attention in open-vocabulary semantic and part segmentation (OSPS). However, existing methods extract image-text alignment cues from cost volumes through a serial structure of spatial and class aggregations, leading to knowledge interference between class-level semantics and spatial context. Therefore, this paper proposes a simple yet effective parallel cost aggregation (PCA-Seg) paradigm to alleviate the above challenge, enabling the model to capture richer vision-language alignment information from cost volumes. Specifically, we design an expert-driven perceptual learning (EPL) module that efficiently integrates semantic and contextual streams. It incorporates a multi-expert parser to extract complementary features from multiple perspectives. In addition, a coefficient mapper is designed to adaptively learn pixel-specific weights for each feature, enabling the integration of complementary knowledge into a unified and robust feature embedding. Furthermore, we propose a feature orthogonalization decoupling (FOD) strategy to mitigate redundancy between the semantic and contextual streams, which allows the EPL module to learn diverse knowledge from orthogonalized features. Extensive experiments on eight benchmarks show that each parallel block in PCA-Seg adds merely 0.35M parameters while achieving state-of-the-art OSPS performance.
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
