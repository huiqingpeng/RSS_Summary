---
title: "Autonomous Adaptive Solver Selection for Chemistry Integration via Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00264"
published: "2026-04-02"
fetched: "2026-04-03T07:19:44.086742"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Autonomous Adaptive Solver Selection for Chemistry Integration via Reinforcement Learning
View PDF HTML (experimental)Abstract:The computational cost of stiff chemical kinetics remains a dominant bottleneck in reacting-flow simulation, yet hybrid integration strategies are typically driven by hand-tuned heuristics or supervised predictors that make myopic decisions from instantaneous local state. We introduce a constrained reinforcement learning (RL) framework that autonomously selects between an implicit BDF integrator (CVODE) and a quasi-steady-state (QSS) solver during chemistry integration. Solver selection is cast as a Markov decision process. The agent learns trajectory-aware policies that account for how present solver choices influence downstream error accumulation, while minimizing computational cost under a user-prescribed accuracy tolerance enforced through a Lagrangian reward with online multiplier adaptation. Across sampled 0D homogeneous reactor conditions, the RL-adaptive policy achieves a mean speedup of approximately $3\times$, with speedups ranging from $1.11\times$ to $10.58\times$, while maintaining accurate ignition delays and species profiles for a 106-species \textit{n}-dodecane mechanism and adding approximately $1\%$ inference overhead. Without retraining, the 0D-trained policy transfers to 1D counterflow diffusion flames over strain rates $10$--$2000~\mathrm{s}^{-1}$, delivering consistent $\approx 2.2\times$ speedup relative to CVODE while preserving near-reference temperature accuracy and selecting CVODE at only $12$--$15\%$ of space-time points. Overall, the results demonstrate the potential of the proposed reinforcement learning framework to learn problem-specific integration strategies while respecting accuracy constraints, thereby opening a pathway toward adaptive, self-optimizing workflows for multiphysics systems with spatially heterogeneous stiffness.
Submission history
From: Opeoluwa Owoyele [view email][v1] Tue, 31 Mar 2026 21:44:58 UTC (1,799 KB)
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
