---
title: "Rethinking Reward Signals in Video GRPO: When Scores Become Targets"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.19356"
published: "2026-03-18"
fetched: "2026-03-18T18:29:32.738290"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 24 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Rethinking Reward Signals in Video GRPO: When Scores Become Targets
View PDF HTML (experimental)Abstract:Group Relative Policy Optimization (GRPO) enables stable and preference-oriented updates via group-wise comparisons for post-training video generation. However, GRPO directly optimizes reward-induced advantages. Under sustained optimization, the reward score can lose fidelity as a proxy for true video quality, consistent with the phenomenon described by Goodhart's Law. This leads to two recurring issues: (i) shortcut-driven optimization under composite objectives and (ii) reward saturation within prompt groups. To address these issues, we introduce TaRoS, a Target-Robust Reward Signaling framework for Video generation GRPO. TaRoS leverages component level performance assessment together with intra-group sparsity to organize multi-aspect rewards towards optimization objectives. In addition, it adaptively downweights components that exhibit saturation, thereby preserving effective optimization directions and mitigating redundancy. This maintains meaningful optimization directions and preserves within-group ranking separation, thereby preventing reward hacking and leading to more reliable policy updates. Extensive experiments show consistent improvements in visual fidelity, motion coherence, and text-video alignment over strong baselines.
Submission history
From: Rui Li [view email][v1] Mon, 24 Nov 2025 17:56:03 UTC (7,894 KB)
[v2] Tue, 17 Mar 2026 07:36:38 UTC (4,126 KB)
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
