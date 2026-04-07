---
title: "CoLA: Cross-Modal Low-rank Adaptation for Multimodal Downstream Tasks"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2604.03314"
published: "2026-04-07"
fetched: "2026-04-08T07:02:46.840631"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 1 Apr 2026]
Title:CoLA: Cross-Modal Low-rank Adaptation for Multimodal Downstream Tasks
View PDF HTML (experimental)Abstract:Foundation models have revolutionized AI, but adapting them efficiently for multimodal tasks, particularly in dual-stream architectures composed of unimodal encoders, such as DINO and BERT, remains a significant challenge. Parameter-Efficient Fine-Tuning (PEFT) methods like Low-Rank Adaptation (LoRA) enable lightweight adaptation, yet they operate in isolation within each modality, limiting their ability in capturing cross-modal interactions. In this paper, we take a step in bridging this gap with Cross-Modal Low-Rank Adaptation (CoLA), a novel PEFT framework that extends LoRA by introducing a dedicated inter-modal adaptation pathway alongside the standard intra-modal one. This dual-path design enables CoLA to adapt unimodal foundation models to multimodal tasks effectively, without interference between modality-specific and cross-modal learning. We evaluate CoLA across a range of vision-language (RefCOCO, RefCOCO+, RefCOCOg) and audio-visual (AVE, AVS) benchmarks, where it consistently outperforms LORA, achieving a relative gain of around 3\% and 2\%, respectively, while maintaining parameter efficiency. Notably, CoLA enables the first multi-task PEFT framework for visual grounding, bridging a key gap in efficient multimodal adaptation.
Submission history
From: Wish Suharitdamrong [view email][v1] Wed, 1 Apr 2026 01:37:24 UTC (1,240 KB)
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
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
