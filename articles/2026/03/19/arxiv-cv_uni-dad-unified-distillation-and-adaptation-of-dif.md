---
title: "Uni-DAD: Unified Distillation and Adaptation of Diffusion Models for Few-step Few-shot Image Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.18281"
published: "2026-03-19"
fetched: "2026-03-19T16:27:57.870573"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 23 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Uni-DAD: Unified Distillation and Adaptation of Diffusion Models for Few-step Few-shot Image Generation
View PDF HTML (experimental)Abstract:Diffusion models (DMs) produce high-quality images, yet their sampling remains costly when adapted to new domains. Distilled DMs are faster but typically remain confined within their teacher's domain. Thus, fast and high-quality generation for novel domains relies on two-stage pipelines: Adapt-then-Distill or Distill-then-Adapt. However, both add design complexity and often degrade quality or diversity. We introduce Uni-DAD, a single-stage pipeline that unifies DM distillation and adaptation. It couples two training signals: (i) a dual-domain distribution-matching distillation (DMD) objective that guides the student toward the distributions of the source teacher and a target teacher, and (ii) a multi-head generative adversarial network (GAN) loss that encourages target realism across multiple feature scales. The source domain distillation preserves diverse source knowledge, while the multi-head GAN stabilizes training and reduces overfitting, especially in few-shot regimes. The inclusion of a target teacher facilitates adaptation to more structurally distant domains. We evaluate Uni-DAD on two comprehensive benchmarks for few-shot image generation (FSIG) and subject-driven personalization (SDP) using diffusion backbones. It delivers better or comparable quality to state-of-the-art (SoTA) adaptation methods even with less than 4 sampling steps, and often surpasses two-stage pipelines in quality and diversity. Code: this https URL.
Submission history
From: Yara Bahram [view email][v1] Sun, 23 Nov 2025 04:22:42 UTC (10,569 KB)
[v2] Tue, 17 Mar 2026 20:31:44 UTC (13,711 KB)
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
