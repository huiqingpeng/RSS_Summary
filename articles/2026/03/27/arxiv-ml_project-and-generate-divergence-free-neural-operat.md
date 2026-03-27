---
title: "Project and Generate: Divergence-Free Neural Operators for Incompressible Flows"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24500"
published: "2026-03-27"
fetched: "2026-03-28T07:10:32.122193"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Project and Generate: Divergence-Free Neural Operators for Incompressible Flows
View PDF HTML (experimental)Abstract:Learning-based models for fluid dynamics often operate in unconstrained function spaces, leading to physically inadmissible, unstable simulations. While penalty-based methods offer soft regularization, they provide no structural guarantees, resulting in spurious divergence and long-term collapse. In this work, we introduce a unified framework that enforces the incompressible continuity equation as a hard, intrinsic constraint for both deterministic and generative modeling. First, to project deterministic models onto the divergence-free subspace, we integrate a differentiable spectral Leray projection grounded in the Helmholtz-Hodge decomposition, which restricts the regression hypothesis space to physically admissible velocity fields. Second, to generate physically consistent distributions, we show that simply projecting model outputs is insufficient when the prior is incompatible. To address this, we construct a divergence-free Gaussian reference measure via a curl-based pushforward, ensuring the entire probability flow remains subspace-consistent by construction. Experiments on 2D Navier-Stokes equations demonstrate exact incompressibility up to discretization error and substantially improved stability and physical consistency.
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
