---
title: "DSO: Dual-Scale Neural Operators for Stable Long-term Fluid Dynamics Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26800"
published: "2026-03-31"
fetched: "2026-04-01T07:18:37.918600"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:DSO: Dual-Scale Neural Operators for Stable Long-term Fluid Dynamics Forecasting
View PDF HTML (experimental)Abstract:Long-term fluid dynamics forecasting is a critically important problem in science and engineering. While neural operators have emerged as a promising paradigm for modeling systems governed by partial differential equations (PDEs), they often struggle with long-term stability and precision. We identify two fundamental failure modes in existing architectures: (1) local detail blurring, where fine-scale structures such as vortex cores and sharp gradients are progressively smoothed, and (2) global trend deviation, where the overall motion trajectory drifts from the ground truth during extended rollouts. We argue that these failures arise because existing neural operators treat local and global information processing uniformly, despite their inherently different evolution characteristics in physical systems. To bridge this gap, we propose the Dual-Scale Neural Operator (DSO), which explicitly decouples information processing into two complementary modules: depthwise separable convolutions for fine-grained local feature extraction and an MLP-Mixer for long-range global aggregation. Through numerical experiments on vortex dynamics, we demonstrate that nearby perturbations primarily affect local vortex structure while distant perturbations influence global motion trends, providing empirical validation for our design choice. Extensive experiments on turbulent flow benchmarks show that DSO achieves state-of-the-art accuracy while maintaining robust long-term stability, reducing prediction error by over 88% compared to existing neural operators.
Current browse context:
cs.LG
Change to browse by:
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
