---
title: "A Stability-Aware Frozen Euler Autoencoder for Physics-Informed Tracking in Continuum Mechanics (SAFE-PIT-CM)"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.13280"
published: "2026-03-20"
fetched: "2026-03-20T14:13:17.884331"
---

Computer Science > Machine Learning
[Submitted on 27 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:A Stability-Aware Frozen Euler Autoencoder for Physics-Informed Tracking in Continuum Mechanics (SAFE-PIT-CM)
View PDF HTML (experimental)Abstract:We introduce SAFE-PIT-CM, a Stability-Aware Frozen Euler autoencoder for Physics-Informed Tracking in Continuum Mechanics. The architecture embeds a frozen, differentiable PDE solver inside an autoencoder: a convolutional encoder maps each video frame to a latent field; the SAFE operator propagates it forward via sub-stepped finite differences; and a decoder reconstructs the video. Backpropagation through the frozen operator yields gradients that directly supervise an attention-based estimator for the diffusion coefficient alpha (alpha = D > 0), requiring no ground-truth labels.
The SAFE operator is the central contribution. In practice, temporal snapshots are saved at intervals far coarser than the simulation time step. A single forward Euler step at this coarse interval violates the von Neumann stability condition, causing alpha to collapse to an unphysical value. Sub-stepping the frozen stencil restores the original temporal resolution and numerical stability, enabling accurate parameter recovery across the full physically relevant range.
SAFE-PIT-CM is demonstrated on the diffusion equation, covering thermal diffusion in engineering metals. The model also supports test-time training (TTT): learning alpha from a single simulation with no pre-training, using only the physics loss as supervision. TTT achieves accuracy comparable to pre-trained inference. The architecture generalises to any PDE admitting a convolutional finite-difference discretisation and is inherently explainable -- every prediction traces to a physical coefficient and step-by-step PDE propagation.
Submission history
From: Emil Hovad [view email][v1] Fri, 27 Feb 2026 12:13:43 UTC (1,397 KB)
[v2] Wed, 18 Mar 2026 19:34:03 UTC (820 KB)
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
