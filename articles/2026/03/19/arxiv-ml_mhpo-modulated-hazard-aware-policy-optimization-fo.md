---
title: "MHPO: Modulated Hazard-aware Policy Optimization for Stable Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16929"
published: "2026-03-19"
fetched: "2026-03-19T12:05:41.606122"
---

Computer Science > Machine Learning
[Submitted on 14 Mar 2026]
Title:MHPO: Modulated Hazard-aware Policy Optimization for Stable Reinforcement Learning
View PDF HTML (experimental)Abstract:Regulating the importance ratio is critical for the training stability of Group Relative Policy Optimization (GRPO) based frameworks. However, prevailing ratio control methods, such as hard clipping, suffer from non-differentiable boundaries and vanishing gradient regions, failing to maintain gradient fidelity. Furthermore, these methods lack a hazard-aware mechanism to adaptively suppress extreme deviations, leaving the optimization process vulnerable to abrupt policy shifts. To address these challenges, we propose Modulated Hazard-aware Policy Optimization (MHPO), a novel framework designed for robust and stable reinforcement learning. The proposed MHPO introduces a Log-Fidelity Modulator (LFM) to map unbounded importance ratios into a bounded, differentiable domain. This mechanism effectively prevents high-variance outlier tokens from destabilizing the loss landscape while ensuring global gradient stability. Complementarily, a Decoupled Hazard Penalty (DHP) integrates cumulative hazard functions from survival analysis to independently regulate positive and negative policy shifts. By shaping the optimization landscape with hazard-aware penalties, the proposed MHPO achieves fine-grained regulation of asymmetric policy shifts simultaneously mitigating mode collapse from over-expansion and preventing policy erosion from catastrophic contraction within a stabilized trust region. Extensive evaluations on diverse reasoning benchmarks across both text-based and vision-language tasks demonstrate that MHPO consistently outperforms existing methods, achieving superior performance while significantly enhancing training stability.
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
