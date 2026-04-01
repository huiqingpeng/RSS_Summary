---
title: "Stochastic Dimension Implicit Functional Projections for Exact Integral Conservation in High-Dimensional PINNs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29237"
published: "2026-04-01"
fetched: "2026-04-02T07:16:47.199805"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Stochastic Dimension Implicit Functional Projections for Exact Integral Conservation in High-Dimensional PINNs
View PDF HTML (experimental)Abstract:Enforcing exact macroscopic conservation laws, such as mass and energy, in neural partial differential equation (PDE) solvers is computationally challenging in high dimensions. Traditional discrete projections rely on deterministic quadrature that scales poorly and restricts mesh-free formulations like PINNs. Furthermore, high-order operators incur heavy memory overhead, and generic optimization often lacks convergence guarantees for non-convex conservation manifolds. To address this, we propose the Stochastic Dimension Implicit Functional Projection (SDIFP) framework. Instead of projecting discrete vectors, SDIFP applies a global affine transformation to the continuous network output. This yields closed-form solutions for integral constraints via detached Monte Carlo (MC) quadrature, bypassing spatial grid dependencies. For scalable training, we introduce a doubly-stochastic unbiased gradient estimator (DS-UGE). By decoupling spatial sampling from differential operator subsampling, the DS-UGE reduces memory complexity from $\mathcal{O}(M \times N_{\mathcal{L}})$ to $\mathcal{O}(N \times |\mathcal{I}|)$. SDIFP mitigates sampling variance, preserves solution regularity, and maintains $\mathcal{O}(1)$ inference efficiency, providing a scalable, mesh-free approach for solving conservative high-dimensional PDEs.
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
