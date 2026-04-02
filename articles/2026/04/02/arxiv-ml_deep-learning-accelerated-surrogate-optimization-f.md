---
title: "Deep Learning-Accelerated Surrogate Optimization for High-Dimensional Well Control in Stress-Sensitive Reservoirs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00352"
published: "2026-04-02"
fetched: "2026-04-03T07:20:44.799889"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Deep Learning-Accelerated Surrogate Optimization for High-Dimensional Well Control in Stress-Sensitive Reservoirs
View PDF HTML (experimental)Abstract:Production optimization in stress-sensitive unconventional reservoirs is governed by a nonlinear trade-off between pressure-driven flow and stress-induced degradation of fracture conductivity and matrix permeability. While higher drawdown improves short-term production, it accelerates permeability loss and reduces long-term recovery. Identifying optimal, time-varying control strategies requires repeated evaluations of fully coupled flow-geomechanics simulators, making conventional optimization computationally expensive.
We propose a deep learning-based surrogate optimization framework for high-dimensional well control. Unlike prior approaches that rely on predefined control parameterizations or generic sampling, our method treats well control as a continuous, high-dimensional problem and introduces a problem-informed sampling strategy that aligns training data with trajectories encountered during optimization. A neural network proxy is trained to approximate the mapping between bottomhole pressure trajectories and cumulative production using data from a coupled flow-geomechanics model.
The proxy is embedded within a constrained optimization workflow, enabling rapid evaluation of control strategies. Across multiple initializations, the surrogate achieves agreement with full-physics solutions within 2-5 percent, while reducing computational cost by up to three orders of magnitude. Discrepancies are mainly associated with trajectories near the boundary of the training distribution and local optimization effects.
This framework shows that combining surrogate modeling with problem-informed sampling enables scalable and reliable optimization for high-dimensional, simulator-based problems, with broader applicability to PDE-constrained systems.
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
