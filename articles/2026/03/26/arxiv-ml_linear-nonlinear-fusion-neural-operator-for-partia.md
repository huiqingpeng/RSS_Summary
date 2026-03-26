---
title: "Linear-Nonlinear Fusion Neural Operator for Partial Differential Equations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24143"
published: "2026-03-26"
fetched: "2026-03-27T07:21:23.612351"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Linear-Nonlinear Fusion Neural Operator for Partial Differential Equations
View PDF HTML (experimental)Abstract:Neural operator learning directly constructs the mapping relationship from the equation parameter space to the solution space, enabling efficient direct inference in practical applications without the need for repeated solution of partial differential equations (PDEs) - an advantage that is difficult to achieve with traditional numerical methods. In this work, we find that explicitly decoupling linear and nonlinear effects within such operator mappings leads to markedly improved learning efficiency. This yields a novel network structure, namely the Linear-Nonlinear Fusion Neural Operator (LNF-NO), which models operator mappings via the multiplicative fusion of a linear component and a nonlinear component, thus achieving a lightweight and interpretable representation. This linear-nonlinear decoupling enables efficient capture of complex solution features at the operator level while maintaining stability and generality. LNF-NO naturally supports multiple functional inputs and is applicable to both regular grids and irregular geometries. Across a diverse suite of PDE operator-learning benchmarks, including nonlinear Poisson-Boltzmann equations and multi-physics coupled systems, LNF-NO is typically substantially faster to train than Deep Operator Networks (DeepONet) and Fourier Neural Operators (FNO), while achieving comparable or better accuracy in most cases. On the tested 3D Poisson-Boltzmann case, LNF-NO attains the best accuracy among the compared models and trains approximately 2.7x faster than a 3D FNO baseline.
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
