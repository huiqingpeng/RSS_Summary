---
title: "MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.10376"
published: "2026-03-18"
fetched: "2026-03-18T18:28:43.389808"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 13 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v5)]
Title:MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation
View PDF HTML (experimental)Abstract:Embodied navigation is a fundamental capability for robotic agents operating. Real-world deployment requires open vocabulary generalization and low training overhead, motivating zero-shot methods rather than task-specific RL training. However, existing zero-shot methods that build explicit 3D scene graphs often compress rich visual observations into text-only relations, leading to high construction cost, irreversible loss of visual evidence, and constrained vocabularies. To address these limitations, we introduce the Multi-modal 3D Scene Graph (M3DSG), which preserves visual cues by replacing textual relational edges with dynamically assigned images. Built on M3DSG, we propose MSGNav, a zero-shot navigation system that includes a Key Subgraph Selection module for efficient reasoning, an Adaptive Vocabulary Update module for open vocabulary support, and a Closed-Loop Reasoning module for accurate exploration reasoning. Additionally, we further identify the last mile problem in zero-shot navigation determining the feasible target location with a suitable final viewpoint, and propose a Visibility-based Viewpoint Decision module to explicitly resolve it. Comprehensive experimental results demonstrate that MSGNav achieves state-of-the-art performance on the challenging GOAT-Bench and HM3D-ObjNav benchmark. The code will be publicly available at this https URL.
Submission history
From: Xun Huang [view email][v1] Thu, 13 Nov 2025 14:51:21 UTC (2,174 KB)
[v2] Fri, 14 Nov 2025 12:20:45 UTC (2,127 KB)
[v3] Sat, 21 Feb 2026 18:56:19 UTC (8,813 KB)
[v4] Mon, 16 Mar 2026 08:45:56 UTC (12,189 KB)
[v5] Tue, 17 Mar 2026 10:25:08 UTC (13,868 KB)
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
