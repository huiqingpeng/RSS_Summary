---
title: "Neural Pushforward Samplers for the Fokker-Planck Equation on Embedded Riemannian Manifolds"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16239"
published: "2026-03-18"
fetched: "2026-03-18T16:11:23.060111"
---

Mathematics > Numerical Analysis
[Submitted on 17 Mar 2026]
Title:Neural Pushforward Samplers for the Fokker-Planck Equation on Embedded Riemannian Manifolds
View PDF HTML (experimental)Abstract:We extend the Weak Adversarial Neural Pushforward (WANPF) Method to the Fokker--Planck equation posed on a compact, smoothly embedded Riemannian manifold M in $R^n$. The key observation is that the weak formulation of the Fokker--Planck equation, together with the ambient-space representation of the Laplace--Beltrami operator via the tangential projection $P(x)$ and the mean-curvature vector $H(x)$, permits all integrals to be evaluated as expectations over samples lying on M, using test functions defined globally on $R^n$. A neural pushforward map is constrained to map the support of a base distribution into M at all times through a manifold retraction, so that probability conservation and manifold membership are enforced by construction. Adversarial ambient plane-wave test functions are chosen, and their Laplace--Beltrami operators are derived in closed form, enabling autodiff-free, mesh-free training. We present both a steady-state and a time-dependent formulation, derive explicit Laplace--Beltrami formulae for the sphere $S^{n-1}$ and the flat torus $T^n$, and demonstrate the method numerically on a double-well steady-state Fokker--Planck equation on $S^2$.
Current browse context:
math.NA
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
