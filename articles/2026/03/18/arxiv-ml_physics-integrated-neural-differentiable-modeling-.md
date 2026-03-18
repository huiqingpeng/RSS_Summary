---
title: "Physics-integrated neural differentiable modeling for immersed boundary systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16277"
published: "2026-03-18"
fetched: "2026-03-18T15:42:19.632295"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Physics-integrated neural differentiable modeling for immersed boundary systems
View PDF HTML (experimental)Abstract:Accurately, efficiently, and stably computing complex fluid flows and their evolution near solid boundaries over long horizons remains challenging. Conventional numerical solvers require fine grids and small time steps to resolve near-wall dynamics, resulting in high computational costs, while purely data-driven surrogate models accumulate rollout errors and lack robustness under extrapolative conditions. To address these issues, this study extends existing neural PDE solvers by developing a physics-integrated differentiable framework for long-horizon prediction of immersed-boundary flows. A key design aspect of the framework includes an important improvement, namely the structural integration of physical principles into an end-to-end differentiable architecture incorporating a PDE-based intermediate velocity module and a multi-direct forcing immersed boundary module, both adhering to the pressure-projection procedure for incompressible flow computation. The computationally expensive pressure projection step is substituted with a learned implicit correction using ConvResNet blocks to reduce cost, and a sub-iteration strategy is introduced to separate the embedded physics module's stability requirement from the surrogate model's time step, enabling stable coarse-grid autoregressive rollouts with large effective time increments. The framework uses only single-step supervision for training, eliminating long-horizon backpropagation and reducing training time to under one hour on a single GPU. Evaluations on benchmark cases of flow past a stationary cylinder and a rotationally oscillating cylinder at Re=100 show the proposed model consistently outperforms purely data-driven, physics-loss-constrained, and coarse-grid numerical baselines in flow-field fidelity and long-horizon stability, while achieving an approximately 200-fold inference speedup over the high-resolution solver.
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
