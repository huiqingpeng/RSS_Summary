---
title: "Finite-time analysis of Multi-timescale Stochastic Optimization Algorithms"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29380"
published: "2026-04-01"
fetched: "2026-04-02T07:17:38.100602"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Finite-time analysis of Multi-timescale Stochastic Optimization Algorithms
View PDF HTML (experimental)Abstract:We present a finite-time analysis of two smoothed functional stochastic approximation algorithms for simulation-based optimization. The first is a two time-scale gradient-based method, while the second is a three time-scale Newton-based algorithm that estimates both the gradient and the Hessian of the objective function $J$. Both algorithms involve zeroth order estimates for the gradient/Hessian. Although the asymptotic convergence of these algorithms has been established in prior work, finite-time guarantees of two-timescale stochastic optimization algorithms in zeroth order settings have not been provided previously. For our Newton algorithm, we derive mean-squared error bounds for the Hessian estimator and establish a finite-time bound on $\min\limits_{0 \le m \le T} \mathbb{E}\| \nabla J(\theta(m)) \|^2$, showing convergence to first-order stationary points. The analysis explicitly characterizes the interaction between multiple time-scales and the propagation of estimation errors. We further identify step-size choices that balance dominant error terms and achieve near-optimal convergence rates. We also provide corresponding finite-time guarantees for the gradient algorithm under the same framework. The theoretical results are further validated through experiments on the Continuous Mountain Car environment.
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
