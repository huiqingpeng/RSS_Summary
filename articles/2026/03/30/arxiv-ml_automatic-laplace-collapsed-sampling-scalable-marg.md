---
title: "Automatic Laplace Collapsed Sampling: Scalable Marginalisation of Latent Parameters via Automatic Differentiation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26644"
published: "2026-03-30"
fetched: "2026-03-31T07:26:22.077573"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Automatic Laplace Collapsed Sampling: Scalable Marginalisation of Latent Parameters via Automatic Differentiation
View PDF HTML (experimental)Abstract:We present Automatic Laplace Collapsed Sampling (ALCS), a general framework for marginalising latent parameters in Bayesian models using automatic differentiation, which we combine with nested sampling to explore the hyperparameter space in a robust and efficient manner. At each nested sampling likelihood evaluation, ALCS collapses the high-dimensional latent variables $z$ to a scalar contribution via maximum a posteriori (MAP) optimisation and a Laplace approximation, both computed using autodiff. This reduces the effective dimension from $d_\theta + d_z$ to just $d_\theta$, making Bayesian evidence computation tractable for high-dimensional settings without hand-derived gradients or Hessians, and with minimal model-specific engineering. The MAP optimisation and Hessian evaluation are parallelised across live points on GPU-hardware, making the method practical at scale. We also show that automatic differentiation enables local approximations beyond Laplace to parametric families such as the Student-$t$, which improves evidence estimates for heavy-tailed latents. We validate ALCS on a suite of benchmarks spanning hierarchical, time-series, and discrete-likelihood models and establish where the Gaussian approximation holds. This enables a post-hoc ESS diagnostic that localises failures across hyperparameter space without expensive joint sampling.
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
