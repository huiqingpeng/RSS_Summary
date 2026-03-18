---
title: "Refining Few-Step Text-to-Multiview Diffusion via Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.20107"
published: "2026-03-18"
fetched: "2026-03-18T16:17:36.497100"
---

Computer Science > Machine Learning
[Submitted on 26 May 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Refining Few-Step Text-to-Multiview Diffusion via Reinforcement Learning
View PDF HTML (experimental)Abstract:Text-to-multiview (T2MV) diffusion models have shown great promise in generating multiple views of a scene from a single text prompt. While few-step backbones enable real-time T2MV generation, they often compromise key aspects of generation quality, such as per-view fidelity and cross-view consistency. Reinforcement learning (RL) finetuning offers a potential solution, yet existing approaches designed for single-image diffusion do not readily extend to the few-step T2MV setting, as they neglect cross-view coordination and suffer from weak learning signals in few-step regimes. To address this, we propose MVC-ZigAL, a tailored RL finetuning framework for few-step T2MV diffusion models. Specifically, its core insights are: (1) a new MDP formulation that jointly models all generated views and assesses their collective quality via a joint-view reward; (2) a novel advantage learning strategy that exploits the performance gains of a self-refinement sampling scheme over standard sampling, yielding stronger learning signals for effective RL finetuning; and (3) a unified RL framework that extends advantage learning with a Lagrangian dual formulation for multiview-constrained optimization, balancing single-view and joint-view objectives through adaptive primal-dual updates under a self-paced threshold curriculum that harmonizes exploration and constraint enforcement. Collectively, these designs enable robust and balanced RL finetuning for few-step T2MV diffusion models, yielding substantial gains in both per-view fidelity and cross-view consistency. Code is available at this https URL.
Submission history
From: Ziyi Zhang [view email][v1] Mon, 26 May 2025 15:11:26 UTC (7,920 KB)
[v2] Tue, 17 Mar 2026 15:09:09 UTC (12,127 KB)
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
