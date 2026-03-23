---
title: "Deep Hilbert--Galerkin Methods for Infinite-Dimensional PDEs and Optimal Control"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19463"
published: "2026-03-23"
fetched: "2026-03-24T07:18:20.030241"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Deep Hilbert--Galerkin Methods for Infinite-Dimensional PDEs and Optimal Control
View PDF HTML (experimental)Abstract:We develop deep learning-based approximation methods for fully nonlinear second-order PDEs on separable Hilbert spaces, such as HJB equations for infinite-dimensional control, by parameterizing solutions via Hilbert--Galerkin Neural Operators (HGNOs). We prove the first Universal Approximation Theorems (UATs) which are sufficiently powerful to address these problems, based on novel topologies for Hessian terms and corresponding novel continuity assumptions on the fully nonlinear operator. These topologies are non-sequential and non-metrizable, making the problem delicate. In particular, we prove UATs for functions on Hilbert spaces, together with their Fréchet derivatives up to second order, and for unbounded operators applied to the first derivative, ensuring that HGNOs are able to approximate all the PDE terms. For control problems, we further prove UATs for optimal feedback controls in terms of our approximating value function HGNO.
We develop numerical training methods, which we call Deep Hilbert--Galerkin and Hilbert Actor-Critic (reinforcement learning) Methods, for these problems by minimizing the $L^2_\mu(H)$-norm of the residual of the PDE on the whole Hilbert space, not just a projected PDE to finite dimensions. This is the first paper to propose such an approach. The models considered arise in many applied sciences, such as functional differential equations in physics and Kolmogorov and HJB PDEs related to controlled PDEs, SPDEs, path-dependent systems, partially observed stochastic systems, and mean-field SDEs. We numerically solve examples of Kolmogorov and HJB PDEs related to the optimal control of deterministic and stochastic heat and Burgers' equations, demonstrating the promise of our deep learning-based approach.
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
