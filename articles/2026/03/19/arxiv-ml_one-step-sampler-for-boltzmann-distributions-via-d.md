---
title: "One-Step Sampler for Boltzmann Distributions via Drifting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17579"
published: "2026-03-19"
fetched: "2026-03-19T12:14:11.680498"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:One-Step Sampler for Boltzmann Distributions via Drifting
View PDF HTML (experimental)Abstract:We present a drifting-based framework for amortized sampling of Boltzmann distributions defined by energy functions. The method trains a one-step neural generator by projecting samples along a Gaussian-smoothed score field from the current model distribution toward the target Boltzmann distribution. For targets specified only up to an unknown normalization constant, we derive a practical target-side drift from a smoothed energy and use two estimators: a local importance-sampling mean-shift estimator and a second-order curvature-corrected approximation. Combined with a mini-batch Gaussian mean-shift estimate of the sampler-side smoothed score, this yields a simple stop-gradient objective for stable one-step training. On a four-mode Gaussian-mixture Boltzmann target, our sampler achieves mean error $0.0754$, covariance error $0.0425$, and RBF MMD $0.0020$. Additional double-well and banana targets show that the same formulation also handles nonconvex and curved low-energy geometries. Overall, the results support drifting as an effective way to amortize iterative sampling from Boltzmann distributions into a single forward pass at test time.
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
