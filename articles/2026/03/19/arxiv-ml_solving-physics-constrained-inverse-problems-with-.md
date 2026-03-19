---
title: "Solving physics-constrained inverse problems with conditional flow matching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14135"
published: "2026-03-19"
fetched: "2026-03-19T14:19:43.342700"
---

Statistics > Machine Learning
[Submitted on 14 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Solving physics-constrained inverse problems with conditional flow matching
View PDF HTML (experimental)Abstract:This study presents a conditional flow matching framework for solving physics-constrained Bayesian inverse problems. In this setting, samples from the joint distribution of inferred variables and measurements are assumed available, while explicit evaluation of the prior and likelihood densities is not required. We derive a simple and self-contained formulation of both the unconditional and conditional flow matching algorithms, tailored specifically to inverse problems. In the conditional setting, a neural network is trained to learn the velocity field of a probability flow ordinary differential equation that transports samples from a chosen source distribution directly to the posterior distribution conditioned on observed measurements. This black-box formulation accommodates nonlinear, high-dimensional, and potentially non-differentiable forward models without restrictive assumptions on the noise model. We further analyze the behavior of the learned velocity field in the regime of finite training data. Under mild architectural assumptions, we show that overtraining can induce degenerate behavior in the generated conditional distributions, including variance collapse and a phenomenon termed selective memorization, wherein generated samples concentrate around training data points associated with similar observations. A simplified theoretical analysis explains this behavior, and numerical experiments confirm it in practice. We demonstrate that standard early-stopping criteria based on monitoring test loss effectively mitigate such degeneracy. The proposed method is evaluated on several physics-based inverse problems. We investigate the impact of different choices of source distributions, including Gaussian and data-informed priors. Across these examples, conditional flow matching accurately captures complex, multimodal posterior distributions while maintaining computational efficiency.
Submission history
From: Agnimitra Dasgupta [view email][v1] Sat, 14 Mar 2026 21:43:48 UTC (5,342 KB)
[v2] Tue, 17 Mar 2026 21:08:17 UTC (5,339 KB)
Current browse context:
stat.ML
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
