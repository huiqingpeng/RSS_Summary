---
title: "AR-Flow VAE: A Structured Autoregressive Flow Prior Variational Autoencoder for Unsupervised Blind Source Separation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14441"
published: "2026-03-19"
fetched: "2026-03-19T14:19:51.543377"
---

Statistics > Machine Learning
[Submitted on 15 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:AR-Flow VAE: A Structured Autoregressive Flow Prior Variational Autoencoder for Unsupervised Blind Source Separation
View PDF HTML (experimental)Abstract:Blind source separation (BSS) seeks to recover latent source signals from observed mixtures. Variational autoencoders (VAEs) offer a natural perspective for this problem: the latent variables can be interpreted as source components, the encoder can be viewed as a demixing mapping from observations to sources, and the decoder can be regarded as a remixing process from inferred sources back to observations. In this work, we propose AR-Flow VAE, a novel VAE-based framework for BSS in which each latent source is endowed with a parameter-adaptive autoregressive flow prior. This prior significantly enhances the flexibility of latent source modeling, enabling the framework to capture complex non-Gaussian behaviors and structured dependencies, such as temporal correlations, that are difficult to represent with conventional priors. In addition, the structured prior design assigns distinct priors to different latent dimensions, thereby encouraging the latent components to separate into different source signals under heterogeneous prior constraints. Experimental results validate the effectiveness of the proposed architecture for blind source separation. More importantly, this work provides a foundation for future investigations into the identifiability and interpretability of AR-Flow VAE.
Submission history
From: Yuan-Hao Wei Dr. [view email][v1] Sun, 15 Mar 2026 15:35:51 UTC (1,611 KB)
[v2] Wed, 18 Mar 2026 07:48:18 UTC (1,611 KB)
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
