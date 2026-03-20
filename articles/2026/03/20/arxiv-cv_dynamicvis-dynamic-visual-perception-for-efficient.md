---
title: "DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2503.16426"
published: "2026-03-20"
fetched: "2026-03-20T16:10:55.466895"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 20 Mar 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models
View PDF HTML (experimental)Abstract:The advancement of RS technology has enabled high-resolution Earth observation; however, interpreting these images using modern VFMs remains a significant challenge. Unlike object-centric natural images, RS imagery is fundamentally characterized by extreme target sparsity and massive spatial redundancy. Key objects of interest (e.g., ships, vehicles) often occupy less than 1% of the spatial extent, surrounded by vast, target-free backgrounds. Existing VFMs predominantly rely on uniform dense processing (e.g., ViTs) and pixel-reconstruction pre-training paradigms (e.g., MAE). These approaches inherently waste substantial computational capacity on modeling redundant backgrounds and inadvertently dilute the feature representations of small, sparse targets. To bridge this structural misalignment, we propose DynamicVis, a visual foundation model explicitly tailored to the sparse nature of RS imagery. Architecturally, DynamicVis introduces a Dynamic Region-Aware SSM that bypasses uniform computation. It adaptively routes and incrementally models only task-relevant, high-salience tokens while employing a parameter-free integration for background context, drastically reducing the complexity of processing ultra-long 2D token sequences ($\sim$100,000). Crucially, to equip the network with robust spatial-selection capabilities, we propose a novel Region-Level Meta-Embedding Multi-Instance Learning (MIL) pre-training paradigm. Trained on a million-scale dataset, this paradigm explicitly disentangles sparse foreground instances from dense backgrounds in the latent semantic space, overcoming the semantic ambiguity of conventional pixel-reconstruction methods. Extensive evaluations across nine diverse downstream tasks reveal that DynamicVis exhibits exceptional efficacy, particularly dominating in sparse-target and instance-level perception tasks (e.g., small object detection, and change detection).
Submission history
From: Keyan Chen [view email][v1] Thu, 20 Mar 2025 17:59:54 UTC (29,221 KB)
[v2] Wed, 18 Mar 2026 02:46:02 UTC (28,381 KB)
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
