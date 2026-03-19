---
title: "Optimization-Embedded Active Multi-Fidelity Surrogate Learning for Multi-Condition Airfoil Shape Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17057"
published: "2026-03-19"
fetched: "2026-03-19T13:08:28.177633"
---

Physics > Fluid Dynamics
[Submitted on 17 Mar 2026]
Title:Optimization-Embedded Active Multi-Fidelity Surrogate Learning for Multi-Condition Airfoil Shape Optimization
View PDF HTML (experimental)Abstract:Active multi-fidelity surrogate modeling is developed for multi-condition airfoil shape optimization to reduce high-fidelity CFD cost while retaining RANS-level accuracy. The framework couples a low-fidelity-informed Gaussian process regression transfer model with uncertainty-triggered sampling and a synchronized elitism rule embedded in a hybrid genetic algorithm. Low-fidelity XFOIL evaluations provide inexpensive features, while sparse RANS simulations are adaptively allocated when predictive uncertainty exceeds a threshold; elite candidates are mandatorily validated at high fidelity, and the population is re-evaluated to prevent evolutionary selection based on outdated fitness values produced by earlier surrogate states. The method is demonstrated for a two-point problem at $Re=6\times10^6$ with cruise at $\alpha=2^\circ$ (maximize $E=L/D$) and take-off at $\alpha=10^\circ$ (maximize $C_L$) using a 12-parameter CST representation. Independent multi-fidelity surrogates per flight condition enable decoupled refinement. The optimized design improves cruise efficiency by 41.05% and take-off lift by 20.75% relative to the best first-generation individual. Over the full campaign, only 14.78% (cruise) and 9.5% (take-off) of evaluated individuals require RANS, indicating a substantial reduction in high-fidelity usage while maintaining consistent multi-point performance.
Submission history
From: Rodrigo Castellanos [view email][v1] Tue, 17 Mar 2026 18:43:11 UTC (8,852 KB)
Current browse context:
physics.flu-dyn
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
