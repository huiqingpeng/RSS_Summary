---
title: "Alternating Diffusion for Proximal Sampling with Zeroth Order Queries"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19633"
published: "2026-03-23"
fetched: "2026-03-24T07:20:23.477306"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Alternating Diffusion for Proximal Sampling with Zeroth Order Queries
View PDF HTML (experimental)Abstract:This work introduces a new approximate proximal sampler that operates solely with zeroth-order information of the potential function. Prior theoretical analyses have revealed that proximal sampling corresponds to alternating forward and backward iterations of the heat flow. The backward step was originally implemented by rejection sampling, whereas we directly simulate the dynamics. Unlike diffusion-based sampling methods that estimate scores via learned models or by invoking auxiliary samplers, our method treats the intermediate particle distribution as a Gaussian mixture, thereby yielding a Monte Carlo score estimator from directly samplable distributions. Theoretically, when the score estimation error is sufficiently controlled, our method inherits the exponential convergence of proximal sampling under isoperimetric conditions on the target distribution. In practice, the algorithm avoids rejection sampling, permits flexible step sizes, and runs with a deterministic runtime budget. Numerical experiments demonstrate that our approach converges rapidly to the target distribution, driven by interactions among multiple particles and by exploiting parallel computation.
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
