---
title: "The Spectral Edge Thesis: A Mathematical Framework for Intra-Signal Phase Transitions in Neural Network Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.28964"
published: "2026-04-01"
fetched: "2026-04-02T07:14:03.220094"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:The Spectral Edge Thesis: A Mathematical Framework for Intra-Signal Phase Transitions in Neural Network Training
View PDF HTML (experimental)Abstract:We develop the spectral edge thesis: phase transitions in neural network training -- grokking, capability gains, loss plateaus -- are controlled by the spectral gap of the rolling-window Gram matrix of parameter updates. In the extreme aspect ratio regime (parameters $P \sim 10^8$, window $W \sim 10$), the classical BBP detection threshold is vacuous; the operative structure is the intra-signal gap separating dominant from subdominant modes at position $k^* = \mathrm{argmax}\, \sigma_j/\sigma_{j+1}$.
From three axioms we derive: (i) gap dynamics governed by a Dyson-type ODE with curvature asymmetry, damping, and gradient driving; (ii) a spectral loss decomposition linking each mode's learning contribution to its Davis--Kahan stability coefficient; (iii) the Gap Maximality Principle, showing that $k^*$ is the unique dynamically privileged position -- its collapse is the only one that disrupts learning, and it sustains itself through an $\alpha$-feedback loop requiring no assumption on the optimizer. The adiabatic parameter $\mathcal{A} = \|\Delta G\|_F / (\eta\, g^2)$ controls circuit stability: $\mathcal{A} \ll 1$ (plateau), $\mathcal{A} \sim 1$ (phase transition), $\mathcal{A} \gg 1$ (forgetting).
Tested across six model families (150K--124M parameters): gap dynamics precede every grokking event (24/24 with weight decay, 0/24 without), the gap position is optimizer-dependent (Muon: $k^*=1$, AdamW: $k^*=2$ on the same model), and 19/20 quantitative predictions are confirmed. The framework is consistent with the edge of stability, Tensor Programs, Dyson Brownian motion, the Lottery Ticket Hypothesis, and neural scaling laws.
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
