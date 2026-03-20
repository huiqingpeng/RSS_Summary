---
title: "Sharpness Aware Surrogate Training for Spiking Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18039"
published: "2026-03-20"
fetched: "2026-03-20T13:07:46.178694"
---

Computer Science > Neural and Evolutionary Computing
[Submitted on 14 Mar 2026]
Title:Sharpness Aware Surrogate Training for Spiking Neural Networks
View PDF HTML (experimental)Abstract:Surrogate gradients are a standard tool for training spiking neural networks (SNNs), but conventional hard forward or surrogate backward training couples a nonsmooth forward model with a biased gradient estimator. We study sharpness aware Surrogate Training (SAST), which applies sharpness aware Minimization (SAM) to a surrogate forward SNN trained by backpropagation. In this formulation, the optimization target is an ordinary smooth empirical risk, so the training gradient is exact for the auxiliary model being optimized. Under explicit boundedness and contraction assumptions, we derive compact state stability and input Lipschitz bounds, establish smoothness of the surrogate objective, provide a first order SAM approximation bound, and prove a nonconvex convergence guarantee for stochastic SAST with an independent second minibatch. We also isolate a local mechanism proposition, stated separately from the unconditional guarantees, that links per sample parameter gradient control to smaller input gradient norms under local Jacobian conditioning. Empirically, we evaluate clean accuracy, hard spike transfer, corruption robustness, and training overhead on N-MNIST and DVS Gesture. The clearest practical effect is transfer gap reduction: on N-MNIST, hard spike accuracy rises from 65.7% to 94.7% (best at $\rho=0.30$) while surrogate forward accuracy remains high; on DVS Gesture, hard spike accuracy improves from 31.8% to 63.3% (best at $\rho=0.40$). We additionally specify the compute matched, calibration, and theory alignment controls required for a final practical assessment.
Submission history
From: Maximilian Nicholson Mr [view email][v1] Sat, 14 Mar 2026 01:26:26 UTC (292 KB)
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
