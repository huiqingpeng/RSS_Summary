---
title: "Wavelet-based Frame Selection by Detecting Semantic Boundary for Long Video Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.00512"
published: "2026-03-18"
fetched: "2026-03-18T18:33:22.783712"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 28 Feb 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Wavelet-based Frame Selection by Detecting Semantic Boundary for Long Video Understanding
View PDF HTML (experimental)Abstract:Frame selection is crucial due to high frame redundancy and limited context windows when applying Large Vision-Language Models (LVLMs) to long videos. Current methods typically select frames with high relevance to a given query, resulting in a disjointed set of frames that disregard the narrative structure of video. In this paper, we introduce Wavelet-based Frame Selection by Detecting Semantic Boundary (WFS-SB), a training-free framework that presents a new perspective: effective video understanding hinges not only on high relevance but, more importantly, on capturing semantic shifts - pivotal moments of narrative change that are essential to comprehending the holistic storyline of video. However, direct detection of abrupt changes in the query-frame similarity signal is often unreliable due to high-frequency noise arising from model uncertainty and transient visual variations. To address this, we leverage the wavelet transform, which provides an ideal solution through its multi-resolution analysis in both time and frequency domains. By applying this transform, we decompose the noisy signal into multiple scales and extract a clean semantic change signal from the coarsest scale. We identify the local extrema of this signal as semantic boundaries, which segment the video into coherent clips. Building on this, WFS-SB comprises a two-stage strategy: first, adaptively allocating a frame budget to each clip based on a composite importance score; and second, within each clip, employing the Maximal Marginal Relevance approach to select a diverse yet relevant set of frames. Extensive experiments show that WFS-SB significantly boosts LVLM performance, e.g., improving accuracy by 5.5% on VideoMME, 9.5% on MLVU, and 6.2% on LongVideoBench, consistently outperforming state-of-the-art methods. Our code is available at this https URL.
Submission history
From: Wang Chen [view email][v1] Sat, 28 Feb 2026 07:18:07 UTC (10,561 KB)
[v2] Tue, 17 Mar 2026 03:38:52 UTC (5,609 KB)
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
