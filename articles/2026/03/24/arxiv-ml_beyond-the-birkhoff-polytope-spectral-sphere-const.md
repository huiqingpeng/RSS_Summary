---
title: "Beyond the Birkhoff Polytope: Spectral-Sphere-Constrained Hyper-Connections"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20896"
published: "2026-03-24"
fetched: "2026-03-25T07:15:27.599647"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Beyond the Birkhoff Polytope: Spectral-Sphere-Constrained Hyper-Connections
View PDF HTML (experimental)Abstract:Hyper-Connections (HC) generalize residual connections into multiple streams, employing residual matrices for cross-stream feature mixing to enrich model expressivity. However, unconstrained mixing disrupts the identity mapping property intrinsic to the residual connection, causing unstable training. To address this, Manifold-Constrained Hyper-Connections (mHC) and its variant restrict these matrices to the Birkhoff polytope (doubly stochastic matrices) via Sinkhorn iterations or permutation-based parameterizations. We reveal three limitations of this polytope constraint: (1) identity degeneration, where learned matrices collapse around the identity and diminish cross-stream interactions, (2) an expressivity bottleneck, as the non-negativity constraint prevents subtractive feature disentanglement, and (3) parameterization inefficiencies, manifesting as unstable Sinkhorn iterations or the factorial-scaling overhead of permutation-based parameterizations. To overcome these flaws, we propose Spectral-Sphere-Constrained Hyper-Connections (sHC). By geometrically shifting the feasible set from a rigid polytope to a spectral norm sphere, sHC allows negative entries, unlocking subtractive interactions for selective feature diversification. This shift eliminates unstable Sinkhorn projections and factorial parameterization, enabling expressive, non-degenerate residual matrices while preserving training stability.
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
