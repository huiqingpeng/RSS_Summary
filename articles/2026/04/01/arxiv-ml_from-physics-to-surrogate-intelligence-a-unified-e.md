---
title: "From Physics to Surrogate Intelligence: A Unified Electro-Thermo-Optimization Framework for TSV Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29268"
published: "2026-04-01"
fetched: "2026-04-02T07:17:11.209913"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:From Physics to Surrogate Intelligence: A Unified Electro-Thermo-Optimization Framework for TSV Networks
View PDF HTML (experimental)Abstract:High-density through-substrate vias (TSVs) enable 2.5D/3D heterogeneous integration but introduce significant signal-integrity and thermal-reliability challenges due to electrical coupling, insertion loss, and self-heating. Conventional full-wave finite-element method (FEM) simulations provide high accuracy but become computationally prohibitive for large design-space exploration. This work presents a scalable electro-thermal modeling and optimization framework that combines physics-informed analytical modeling, graph neural network (GNN) surrogates, and full-wave sign-off validation. A multi-conductor analytical model computes broadband S-parameters and effective anisotropic thermal conductivities of TSV arrays, achieving $5\%-10\%$ relative Frobenius error (RFE) across array sizes up to $15x15$. A physics-informed GNN surrogate (TSV-PhGNN), trained on analytical data and fine-tuned with HFSS simulations, generalizes to larger arrays with RFE below $2\%$ and nearly constant variance. The surrogate is integrated into a multi-objective Pareto optimization framework targeting reflection coefficient, insertion loss, worst-case crosstalk (NEXT/FEXT), and effective thermal conductivity. Millions of TSV configurations can be explored within minutes, enabling exhaustive layout and geometric optimization that would be infeasible using FEM alone. Final designs are validated with Ansys HFSS and Mechanical, showing strong agreement. The proposed framework enables rapid electro-thermal co-design of TSV arrays while reducing per-design evaluation time by more than six orders of magnitude.
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
