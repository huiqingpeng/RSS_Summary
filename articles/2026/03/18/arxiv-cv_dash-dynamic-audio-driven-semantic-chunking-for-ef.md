---
title: "DASH: Dynamic Audio-Driven Semantic Chunking for Efficient Omnimodal Token Compression"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15685"
published: "2026-03-18"
fetched: "2026-03-18T18:22:14.146911"
---

Computer Science > Multimedia
[Submitted on 15 Mar 2026]
Title:DASH: Dynamic Audio-Driven Semantic Chunking for Efficient Omnimodal Token Compression
View PDF HTML (experimental)Abstract:Omnimodal large language models (OmniLLMs) jointly process audio and visual streams, but the resulting long multimodal token sequences make inference prohibitively expensive. Existing compression methods typically rely on fixed window partitioning and attention-based pruning, which overlook the piecewise semantic structure of audio-visual signals and become fragile under aggressive token reduction. We propose Dynamic Audio-driven Semantic cHunking (DASH), a training-free framework that aligns token compression with semantic structure. DASH treats audio embeddings as a semantic anchor and detects boundary candidates via cosine-similarity discontinuities, inducing dynamic, variable-length segments that approximate the underlying piecewise-coherent organization of the sequence. These boundaries are projected onto video tokens to establish explicit cross-modal segmentation. Within each segment, token retention is determined by a tri-signal importance estimator that fuses structural boundary cues, representational distinctiveness, and attention-based salience, mitigating the sparsity bias of attention-only selection. This structure-aware allocation preserves transition-critical tokens while reducing redundant regions. Extensive experiments on AVUT, VideoMME, and WorldSense demonstrate that DASH maintains superior accuracy while achieving higher compression ratios compared to prior methods. Code is available at: this https URL.
Current browse context:
cs.MM
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
