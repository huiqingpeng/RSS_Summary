---
title: "Towards One-step Causal Video Generation via Adversarial Self-Distillation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.01419"
published: "2026-03-19"
fetched: "2026-03-19T16:27:05.271216"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 3 Nov 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Towards One-step Causal Video Generation via Adversarial Self-Distillation
View PDF HTML (experimental)Abstract:Recent hybrid video generation models combine autoregressive temporal dynamics with diffusion-based spatial denoising, but their sequential, iterative nature leads to error accumulation and long inference times. In this work, we propose a distillation-based framework for efficient causal video generation that enables high-quality synthesis with extremely limited denoising steps. Our approach builds upon the Distribution Matching Distillation (DMD) framework and proposes a novel Adversarial Self-Distillation (ASD) strategy, which aligns the outputs of the student model's n-step denoising process with its (n+1)-step version at the distribution level. This design provides smoother supervision by bridging small intra-student gaps and more informative guidance by combining teacher knowledge with locally consistent student behavior, substantially improving training stability and generation quality in extremely few-step scenarios (e.g., 1-2 steps). In addition, we present a First-Frame Enhancement (FFE) strategy, which allocates more denoising steps to the initial frames to mitigate error propagation while applying larger skipping steps to later frames. Extensive experiments on VBench demonstrate that our method surpasses state-of-the-art approaches in both one-step and two-step video generation. Notably, our framework produces a single distilled model that flexibly supports multiple inference-step settings, eliminating the need for repeated re-distillation and enabling efficient, high-quality video synthesis.
Submission history
From: Yangqi Yang [view email][v1] Mon, 3 Nov 2025 10:12:47 UTC (5,065 KB)
[v2] Wed, 18 Mar 2026 06:33:59 UTC (10,281 KB)
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
