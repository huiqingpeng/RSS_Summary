---
title: "HMAR: Hierarchical Modality-Aware Expert and Dynamic Routing Medical Image Retrieval Architecture"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16679"
published: "2026-03-18"
fetched: "2026-03-18T18:17:45.645614"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:HMAR: Hierarchical Modality-Aware Expert and Dynamic Routing Medical Image Retrieval Architecture
View PDF HTML (experimental)Abstract:Medical image retrieval (MIR) is a critical component of computer-aided diagnosis, yet existing systems suffer from three persistent limitations: uniform feature encoding that fails to account for the varying clinical importance of anatomical structures, ambiguous similarity metrics based on coarse classification labels, and an exclusive focus on global image similarity that cannot meet the clinical demand for fine-grained region-specific retrieval. We propose HMAR (Hierarchical Modality-Aware Expert and Dynamic Routing), an adaptive retrieval framework built on a Mixture-of-Experts (MoE) architecture. HMAR employs a dual-expert mechanism: Expert0 extracts global features for holistic similarity matching, while Expert1 learns position-invariant local representations for precise lesion-region retrieval. A two-stage contrastive learning strategy eliminates the need for expensive bounding-box annotations, and a sliding-window matching algorithm enables dense local comparison at inference time. Hash codes are generated via Kolmogorov-Arnold Network (KAN) layers for efficient Hamming-distance search. Experiments on the RadioImageNet-CT dataset (16 clinical patterns, 29,903 images) show that HMAR achieves mean Average Precision (mAP) of 0.711 and 0.724 for 64-bit and 128-bit hash codes, improving over the state-of-the-art ACIR method by 0.7% and 1.1%, respectively.
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
