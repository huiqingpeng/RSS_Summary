---
title: "Open-o3-Video: Grounded Video Reasoning with Explicit Spatio-Temporal Evidence"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.20579"
published: "2026-03-20"
fetched: "2026-03-20T16:14:54.669921"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 23 Oct 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Open-o3-Video: Grounded Video Reasoning with Explicit Spatio-Temporal Evidence
View PDF HTML (experimental)Abstract:Most video reasoning models only generate textual reasoning traces without indicating when and where key evidence appears. Recent models such as OpenAI-o3 have sparked wide interest in evidence-centered reasoning for images, yet extending this ability to videos is more challenging due to the need for joint temporal tracking and spatial localization across dynamic scenes. We introduce Open-o3-Video, a non-agent framework that integrates explicit spatio-temporal evidence into video reasoning by highlighting key timestamps, objects, and bounding boxes, making the reasoning process traceable and verifiable. To enable this capability, we first construct high-quality datasets STGR that provide unified spatio-temporal supervision, which is absent in existing resources. We further adopt a cold-start reinforcement learning strategy with specially designed rewards that jointly encourage answer accuracy, temporal alignment, and spatial precision. On the V-STAR benchmark, Open-o3-Video achieves state-of-the-art performance, improving mAM by 14.4% and mLGM by 24.2% over the Qwen2.5-VL baseline, and shows consistent gains across a range of video understanding benchmarks. Beyond accuracy, the grounded reasoning traces produced by Open-o3-Video support confidence-aware test-time scaling, improving answer reliability.
Submission history
From: Jiahao Meng [view email][v1] Thu, 23 Oct 2025 14:05:56 UTC (14,421 KB)
[v2] Wed, 18 Mar 2026 16:54:37 UTC (15,821 KB)
Current browse context:
cs.CV
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
