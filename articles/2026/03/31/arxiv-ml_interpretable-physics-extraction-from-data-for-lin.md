---
title: "Interpretable Physics Extraction from Data for Linear Dynamical Systems using Lie Generator Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27442"
published: "2026-03-31"
fetched: "2026-04-01T07:24:07.954966"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Interpretable Physics Extraction from Data for Linear Dynamical Systems using Lie Generator Networks
View PDFAbstract:When the system is linear, why should learning be nonlinear? Linear dynamical systems, the analytical backbone of control theory, signal processing and circuit analysis, have exact closed-form solutions via the state transition matrix. Yet when system parameters must be inferred from data, recent neural approaches offer flexibility at the cost of physical guarantees: Neural ODEs provide flexible trajectory approximation but may violate physical invariants, while energy preserving architectures do not natively represent dissipation essential to real-world systems. We introduce Lie Generator Networks (LGN), which learn a structured generator A and compute trajectories directly via matrix exponentiation. This shift from integration to exponentiation preserves structure by construction. By parameterizing A = S - D (skew-symmetric minus positive diagonal), stability and dissipation emerge from the underlying architecture and are not introduced during training via the loss function. LGN provides a unified framework for linear conservative, dissipative, and time-varying systems. On a 100-dimensional stable RLC ladder, standard derivative-based least-squares system identification can yield unstable eigenvalues. The unconstrained LGN yields stable but physically incorrect spectra, whereas LGN-SD recovers all 100 eigenvalues with over two orders of magnitude lower mean eigenvalue error than unconstrained alternatives. Critically, these eigenvalues reveal poles, natural frequencies, and damping ratios which are interpretable physics that black-box networks do not provide.
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
