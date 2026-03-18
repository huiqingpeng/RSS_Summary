---
title: "Towards Clinical Practice in CT-Based Pulmonary Disease Screening: An Efficient and Reliable Framework"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2412.01525"
published: "2026-03-18"
fetched: "2026-03-18T19:05:36.424365"
---

Electrical Engineering and Systems Science > Image and Video Processing
[Submitted on 2 Dec 2024 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:Towards Clinical Practice in CT-Based Pulmonary Disease Screening: An Efficient and Reliable Framework
View PDF HTML (experimental)Abstract:Deep learning models for pulmonary disease screening from Computed Tomography (CT) scans promise to alleviate the immense workload on radiologists. Still, their high computational cost, stemming from processing entire 3D volumes, remains a major barrier to widespread clinical adoption. Current sub-sampling techniques often compromise diagnostic integrity by introducing artifacts or discarding critical information. To overcome these limitations, we propose an Efficient and Reliable Framework (ERF) that fundamentally improves the practicality of automated CT analysis. Our framework introduces two core innovations: (1) A Cluster-based Sub-Sampling (CSS) method that efficiently selects a compact yet comprehensive subset of CT slices by optimizing for both representativeness and diversity. By integrating an efficient k-nearest neighbor search with an iterative refinement process, CSS bypasses the computational bottlenecks of previous methods while preserving vital diagnostic features. (2) An Ambiguity-aware Uncertainty Quantification (AUQ) mechanism, which enhances reliability by specifically targeting data ambiguity arising from subtle lesions and artifacts. Unlike standard uncertainty measures, AUQ leverages the predictive discrepancy between auxiliary classifiers to construct a specialized ambiguity score. By maximizing this discrepancy during training, the system effectively flags ambiguous samples where the model lacks confidence due to visual noise or intricate pathologies. Validated on two public datasets with 2,654 CT volumes across diagnostic tasks for 3 pulmonary diseases, ERF achieves diagnostic performance comparable to the full-volume analysis (over 90% accuracy and recall) while reducing processing time by more than 60%. This work represents a significant step towards deploying fast, accurate, and trustworthy AI-powered screening tools in time-sensitive clinical settings.
Submission history
From: Qian Shao [view email][v1] Mon, 2 Dec 2024 14:18:17 UTC (1,098 KB)
[v2] Tue, 3 Dec 2024 07:43:55 UTC (1,098 KB)
[v3] Thu, 12 Jun 2025 06:50:04 UTC (2,002 KB)
[v4] Tue, 17 Mar 2026 08:41:27 UTC (3,104 KB)
Current browse context:
eess.IV
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
