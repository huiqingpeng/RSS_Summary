---
title: "Lie Generator Networks for Nonlinear Partial Differential Equations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29264"
published: "2026-04-01"
fetched: "2026-04-02T07:17:02.150459"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Lie Generator Networks for Nonlinear Partial Differential Equations
View PDFAbstract:Linear dynamical systems are fully characterized by their eigenspectra, accessible directly from the generator of the dynamics. For nonlinear systems governed by partial differential equations, no equivalent theory exists. We introduce Lie Generator Network--Koopman (LGN-KM), a neural operator that lifts nonlinear dynamics into a linear latent space and learns the continuous-time Koopman generator ($L_k$) through a decomposition $L_k = S - D_k$, where $S$ is skew-symmetric representing conservative inter-modal coupling, and $D_k$ is a positive-definite diagonal encoding modal dissipation. This architectural decomposition enforces stability and enables interpretability through direct spectral access to the learned dynamics. On two-dimensional Navier--Stokes turbulence, the generator recovers the known dissipation scaling and a complete multi-branch dispersion relation from trajectory data alone with no physics supervision. Independently trained models at different flow regimes recover matched gauge-invariant spectral structure, exposing a gauge freedom in the Koopman lifting. Because the generator is provably stable, it enables guaranteed long-horizon stability, continuous-time evaluation at arbitrary time, and physics-informed cross-viscosity model transfer.
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
