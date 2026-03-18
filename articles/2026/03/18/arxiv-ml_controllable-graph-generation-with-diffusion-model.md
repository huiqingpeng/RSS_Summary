---
title: "Controllable Graph Generation with Diffusion Models via Inference-Time Tree Search Guidance"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.10402"
published: "2026-03-18"
fetched: "2026-03-18T16:19:40.866834"
---

Computer Science > Machine Learning
[Submitted on 12 Oct 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Controllable Graph Generation with Diffusion Models via Inference-Time Tree Search Guidance
View PDF HTML (experimental)Abstract:Graph generation is a fundamental problem in graph learning with broad applications across Web-scale systems, knowledge graphs, and scientific domains such as drug and material discovery. Recent approaches leverage diffusion models for step-by-step generation, yet unconditional diffusion offers little control over desired properties, often leading to unstable quality and difficulty in incorporating new objectives. Inference-time guidance methods mitigate these issues by adjusting the sampling process without retraining, but they remain inherently local, heuristic, and limited in controllability. To overcome these limitations, we propose TreeDiff, a Monte Carlo Tree Search (MCTS) guided dual-space diffusion framework for controllable graph generation. TreeDiff is a plug-and-play inference-time method that expands the search space while keeping computation tractable. Specifically, TreeDiff introduces three key designs to make it practical and scalable: (1) a macro-step expansion strategy that groups multiple denoising updates into a single transition, reducing tree depth and enabling long-horizon exploration; (2) a dual-space denoising mechanism that couples efficient latent-space denoising with lightweight discrete correction in graph space, ensuring both scalability and structural fidelity; and (3) a dual-space verifier that predicts long-term rewards from partially denoised graphs, enabling early value estimation and removing the need for full rollouts. Extensive experiments on 2D and 3D molecular generation benchmarks, under both unconditional and conditional settings, demonstrate that TreeDiff achieves state-of-the-art performance. Notably, TreeDiff exhibits favorable inference-time scaling: it continues to improve with additional computation, while existing inference-time methods plateau early under limited resources.
Submission history
From: Zehong Wang [view email][v1] Sun, 12 Oct 2025 01:40:33 UTC (407 KB)
[v2] Tue, 17 Mar 2026 04:12:55 UTC (397 KB)
Current browse context:
cs.LG
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
