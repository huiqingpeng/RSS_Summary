---
title: "Gaussian Joint Embeddings For Self-Supervised Representation Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26799"
published: "2026-03-31"
fetched: "2026-04-01T07:18:29.011837"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:Gaussian Joint Embeddings For Self-Supervised Representation Learning
View PDF HTML (experimental)Abstract:Self-supervised representation learning often relies on deterministic predictive architectures to align context and target views in latent space. While effective in many settings, such methods are limited in genuinely multi-modal inverse problems, where squared-loss prediction collapses towards conditional averages, and they frequently depend on architectural asymmetries to prevent representation collapse. In this work, we propose a probabilistic alternative based on generative joint modeling. We introduce Gaussian Joint Embeddings (GJE) and its multi-modal extension, Gaussian Mixture Joint Embeddings (GMJE), which model the joint density of context and target representations and replace black-box prediction with closed-form conditional inference under an explicit probabilistic model. This yields principled uncertainty estimates and a covariance-aware objective for controlling latent geometry. We further identify a failure mode of naive empirical batch optimization, which we term the Mahalanobis Trace Trap, and develop several remedies spanning parametric, adaptive, and non-parametric settings, including prototype-based GMJE, conditional Mixture Density Networks (GMJE-MDN), topology-adaptive Growing Neural Gas (GMJE-GNG), and a Sequential Monte Carlo (SMC) memory bank. In addition, we show that standard contrastive learning can be interpreted as a degenerate non-parametric limiting case of the GMJE framework. Experiments on synthetic multi-modal alignment tasks and vision benchmarks show that GMJE recovers complex conditional structure, learns competitive discriminative representations, and defines latent densities that are better suited to unconditional sampling than deterministic or unimodal baselines.
Submission history
From: Yongchao Huang Dr. [view email][v1] Thu, 26 Mar 2026 00:54:54 UTC (1,607 KB)
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
