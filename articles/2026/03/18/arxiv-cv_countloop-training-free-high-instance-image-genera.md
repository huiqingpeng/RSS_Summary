---
title: "CountLoop: Training-Free High-Instance Image Generation via Iterative Agent Guidance"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.16644"
published: "2026-03-18"
fetched: "2026-03-18T18:26:52.103830"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Aug 2025 (v1), last revised 16 Mar 2026 (this version, v3)]
Title:CountLoop: Training-Free High-Instance Image Generation via Iterative Agent Guidance
View PDF HTML (experimental)Abstract:Diffusion models excel at photorealistic synthesis but struggle with precise object counts, especially in high-density settings. We introduce COUNTLOOP, a training-free framework that achieves precise instance control through iterative, structured feedback. Our method alternates between synthesis and evaluation: a VLM-based planner generates structured scene layouts, while a VLM-based critic provides explicit feedback on object counts, spatial arrangements, and visual quality to refine the layout iteratively. Instance-driven attention masking and cumulative attention composition further prevent semantic leakage, ensuring clear object separation even in densely occluded scenes. Evaluations on COCO-Count, T2I-CompBench, and two newly introduced high instance benchmarks show that COUNTLOOP reduces counting error by up to 57% and achieves the highest or comparable spatial quality scores across all benchmarks, while maintaining photorealism.
Submission history
From: Anindya Mondal [view email][v1] Mon, 18 Aug 2025 11:28:02 UTC (453,961 KB)
[v2] Sun, 7 Dec 2025 21:18:36 UTC (27,974 KB)
[v3] Mon, 16 Mar 2026 23:45:34 UTC (35,394 KB)
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
