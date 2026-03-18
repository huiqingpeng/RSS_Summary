---
title: "Unlocking 3D Affordance Segmentation with 2D Semantic Knowledge"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.08316"
published: "2026-03-18"
fetched: "2026-03-18T18:27:29.088311"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 9 Oct 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Unlocking 3D Affordance Segmentation with 2D Semantic Knowledge
View PDF HTML (experimental)Abstract:Affordance segmentation aims to decompose 3D objects into parts that serve distinct functional roles, enabling models to reason about object interactions rather than mere recognition. Existing methods, mostly following the paradigm of 3D semantic segmentation or prompt-based frameworks, struggle when geometric cues are weak or ambiguous, as sparse point clouds provide limited functional information. To overcome this limitation, we leverage the rich semantic knowledge embedded in large-scale 2D Vision Foundation Models (VFMs) to guide 3D representation learning through a cross-modal alignment mechanism. Specifically, we propose Cross-Modal Affinity Transfer (CMAT), a pretraining strategy that compels the 3D encoder to align with the semantic structures induced by lifted 2D features. CMAT is driven by a core affinity alignment objective, supported by two auxiliary losses, geometric reconstruction and feature diversity, which together encourage structured and discriminative feature learning. Built upon the CMAT-pretrained backbone, we employ a lightweight affordance segmentor that injects text or visual prompts into the learned 3D space through an efficient cross-attention interface, enabling dense and prompt-aware affordance prediction while preserving the semantic organization established during pretraining. Extensive experiments demonstrate consistent improvements over previous state-of-the-art methods in both accuracy and efficiency.
Submission history
From: Yu Huang [view email][v1] Thu, 9 Oct 2025 15:01:26 UTC (7,108 KB)
[v2] Tue, 17 Mar 2026 06:58:24 UTC (6,596 KB)
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
