---
title: "Stochastic Gradient Descent in the Saddle-to-Saddle Regime of Deep Linear Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06366"
published: "2026-04-09"
fetched: "2026-04-10T07:04:57.463826"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:Stochastic Gradient Descent in the Saddle-to-Saddle Regime of Deep Linear Networks
View PDF HTML (experimental)Abstract:Deep linear networks (DLNs) are used as an analytically tractable model of the training dynamics of deep neural networks. While gradient descent in DLNs is known to exhibit saddle-to-saddle dynamics, the impact of stochastic gradient descent (SGD) noise on this regime remains poorly understood. We investigate the dynamics of SGD during training of DLNs in the saddle-to-saddle regime. We model the training dynamics as stochastic Langevin dynamics with anisotropic, state-dependent noise. Under the assumption of aligned and balanced weights, we derive an exact decomposition of the dynamics into a system of one-dimensional per-mode stochastic differential equations. This establishes that the maximal diffusion along a mode precedes the corresponding feature being completely learned. We also derive the stationary distribution of SGD for each mode: in the absence of label noise, its marginal distribution along specific features coincides with the stationary distribution of gradient flow, while in the presence of label noise it approximates a Boltzmann distribution. Finally, we confirm experimentally that the theoretical results hold qualitatively even without aligned or balanced weights. These results establish that SGD noise encodes information about the progression of feature learning but does not fundamentally alter the saddle-to-saddle dynamics.
Submission history
From: Guillaume Corlouer [view email][v1] Tue, 7 Apr 2026 18:43:08 UTC (9,506 KB)
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
