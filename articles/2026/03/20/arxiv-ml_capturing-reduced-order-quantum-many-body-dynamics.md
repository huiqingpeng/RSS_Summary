---
title: "Capturing reduced-order quantum many-body dynamics out of equilibrium via neural ordinary differential equations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.13913"
published: "2026-03-20"
fetched: "2026-03-20T14:09:09.153544"
---

Computer Science > Machine Learning
[Submitted on 15 Dec 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Capturing reduced-order quantum many-body dynamics out of equilibrium via neural ordinary differential equations
View PDF HTML (experimental)Abstract:Out-of-equilibrium quantum many-body systems exhibit rapid correlation buildup that underlies many emerging phenomena. Exact wave-function methods to describe this scale exponentially with particle number; simpler mean-field approaches neglect essential two-particle correlations. The time-dependent two-particle reduced density matrix (TD2RDM) formalism offers a middle ground by propagating the two-particle reduced density matrix (2RDM) and closing the BBGKY hierarchy with a reconstruction of the three-particle cumulant. But the validity and existence of time-local reconstruction functionals ignoring memory effects remain unclear across different dynamical regimes. We show that a neural ODE model trained on exact 2RDM data (no dimensionality reduction) can reproduce its dynamics without any explicit three-particle information -- but only in parameter regions where the Pearson correlation between the two- and three-particle cumulants is large. In the anti-correlated or uncorrelated regime, the neural ODE fails, indicating that no simple time-local functional of the instantaneous two-particle cumulant can capture the evolution. The magnitude of the time-averaged three-particle-correlation buildup appears to be the primary predictor of success: For a moderate correlation buildup, both neural ODE predictions and existing TD2RDM reconstructions are accurate, whereas stronger values lead to systematic breakdowns. These findings pinpoint the need for memory-dependent kernels in the three-particle cumulant reconstruction for the latter regime. Our results place the neural ODE as a model-agnostic diagnostic tool that maps the regime of applicability of cumulant expansion methods and guides the development of non-local closure schemes. More broadly, the ability to learn high-dimensional RDM dynamics from limited data opens a pathway to fast, data-driven simulation of correlated quantum matter.
Submission history
From: Patrick Egenlauf [view email][v1] Mon, 15 Dec 2025 21:48:10 UTC (220 KB)
[v2] Thu, 19 Mar 2026 15:41:09 UTC (250 KB)
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
