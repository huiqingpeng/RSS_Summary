---
title: "GLU: Global-Local-Uncertainty Fusion for Scalable Spatiotemporal Reconstruction and Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26023"
published: "2026-03-30"
fetched: "2026-03-31T07:20:41.517561"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:GLU: Global-Local-Uncertainty Fusion for Scalable Spatiotemporal Reconstruction and Forecasting
View PDF HTML (experimental)Abstract:Digital twins of complex physical systems are expected to infer unobserved states from sparse measurements and predict their evolution in time, yet these two functions are typically treated as separate tasks. Here we present GLU, a Global-Local-Uncertainty framework that formulates sparse reconstruction and dynamic forecasting as a unified state-representation problem and introduces a structured latent assembly to both tasks. The central idea is to build a structured latent state that combines a global summary of system-level organization, local tokens anchored to available measurements, and an uncertainty-driven importance field that weights observations according to the physical informativeness. For reconstruction, GLU uses importance-aware adaptive neighborhood selection to retrieve locally relevant information while preserving global consistency and allowing flexible query resolution on arbitrary geometries. Across a suite of challenging benchmarks, GLU consistently improves reconstruction fidelity over reduced-order, convolutional, neural operator, and attention-based baselines, better preserving multi-scale structures. For forecasting, a hierarchical Leader-Follower Dynamics module evolves the latent state with substantially reduced memory growth, maintains stable rollout behavior and delays error accumulation in nonlinear dynamics. On a realistic turbulent combustion dataset, it further preserves not only sharp fronts and broadband structures in multiple physical fields, but also their cross-channel thermo-chemical couplings. Scalability tests show that these gains are achieved with substantially lower memory growth than comparable attention-based baselines. Together, these results establish GLU as a flexible and computationally practical paradigm for sparse digital twins.
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
