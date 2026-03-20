---
title: "Blind to Position, Biased in Language: Probing Mid-Layer Representational Bias in Vision-Language Encoders for Zero-Shot Language-Grounded Spatial Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.23098"
published: "2026-03-20"
fetched: "2026-03-20T16:13:25.994241"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 27 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Blind to Position, Biased in Language: Probing Mid-Layer Representational Bias in Vision-Language Encoders for Zero-Shot Language-Grounded Spatial Understanding
View PDFAbstract:Vision-Language Encoders (VLEs) are widely adopted as the backbone of zero-shot referring image segmentation (RIS), enabling text-guided localization without task-specific training. However, prior works underexplored the underlying biases within mid-layer representations that preserve positional and language-specific information. Through layer-wise investigation, we reveal that the conventionally used final-layer multimodal embeddings prioritize global semantic alignment, leading to two coupled consequences. First, vision embeddings exhibit weak sensitivity to positional cues. Second, multilingual text embeddings form language-dependent geometric shifts within the shared space. Motivated by these findings, we identify an underexplored pathway within VLE mid-layers to construct a spatial map, applicable for improving zero-shot RIS by 1-7 mIoU on nine RefCOCO benchmarks. Furthermore, leveraging mixed-language mid-layer embeddings yields enhanced spatial grounding accuracy (+7-8 mIoU and IoU@50), albeit with increased inference cost, and also improves performance on the zero-shot text-to-image retrieval task. Our work opens up the discussion about the effects of effective representational bias probing of VLEs for enhanced spatial grounding.
Submission history
From: Na Min An [view email][v1] Sat, 27 Sep 2025 04:12:10 UTC (17,440 KB)
[v2] Thu, 19 Mar 2026 14:55:22 UTC (42,444 KB)
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
