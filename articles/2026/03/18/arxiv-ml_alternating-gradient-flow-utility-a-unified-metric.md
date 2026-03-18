---
title: "Alternating Gradient Flow Utility: A Unified Metric for Structural Pruning and Dynamic Routing in Deep Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.12354"
published: "2026-03-18"
fetched: "2026-03-18T17:15:51.004770"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 12 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Alternating Gradient Flow Utility: A Unified Metric for Structural Pruning and Dynamic Routing in Deep Networks
View PDF HTML (experimental)Abstract:Efficient deep learning traditionally relies on static heuristics like weight magnitude or activation awareness (e.g., Wanda, RIA). While successful in unstructured settings, we observe a critical limitation when applying these metrics to the structural pruning of deep vision networks. These contemporary metrics suffer from a magnitude bias, failing to preserve critical functional pathways. To overcome this, we propose a decoupled kinetic paradigm inspired by Alternating Gradient Flow (AGF), utilizing an absolute feature-space Taylor expansion to accurately capture the network's structural "kinetic utility". First, we uncover a topological phase transition at extreme sparsity, where AGF successfully preserves baseline functionality and exhibits topological implicit regularization, avoiding the collapse seen in models trained from scratch. Second, transitioning to architectures without strict structural priors, we reveal a phenomenon of Sparsity Bottleneck in Vision Transformers (ViTs). Through a gradient-magnitude decoupling analysis, we discover that dynamic signals suffer from signal compression in converged models, rendering them suboptimal for real-time routing. Finally, driven by these empirical constraints, we design a hybrid routing framework that decouples AGF-guided offline structural search from online execution via zero-cost physical priors. We validate our paradigm on large-scale benchmarks: under a 75% compression stress test on ImageNet-1K, AGF effectively avoids the structural collapse where traditional metrics aggressively fall below random sampling. Furthermore, when systematically deployed for dynamic inference on ImageNet-100, our hybrid approach achieves Pareto-optimal efficiency. It reduces the usage of the heavy expert by approximately 50% (achieving an estimated overall cost of 0.92$\times$) without sacrificing the full-model accuracy.
Submission history
From: Tianhao Qian [view email][v1] Thu, 12 Mar 2026 18:19:21 UTC (3,428 KB)
[v2] Tue, 17 Mar 2026 07:35:13 UTC (3,428 KB)
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
