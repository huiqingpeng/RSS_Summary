---
title: "PDGMM-VAE: A Variational Autoencoder with Adaptive Per-Dimension Gaussian Mixture Model Priors for Nonlinear ICA"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23547"
published: "2026-03-27"
fetched: "2026-03-28T07:13:31.781965"
---

Statistics > Machine Learning
[Submitted on 20 Mar 2026]
Title:PDGMM-VAE: A Variational Autoencoder with Adaptive Per-Dimension Gaussian Mixture Model Priors for Nonlinear ICA
View PDF HTML (experimental)Abstract:Independent component analysis is a core framework within blind source separation for recovering latent source signals from observed mixtures under statistical independence assumptions. In this work, we propose PDGMM-VAE, a source-oriented variational autoencoder in which each latent dimension, interpreted explicitly as an individual source signal, is assigned its own Gaussian mixture model prior. Unlike conventional VAE formulations with a shared simple prior, the proposed framework imposes per-dimension heterogeneous prior constraints, enabling the model to capture diverse non-Gaussian source statistics and thereby promote source separation under a probabilistic encoder-decoder architecture. Importantly, the parameters of these per-dimension GMM priors are not fixed in advance, but are adaptively learned and automatically refined toward convergence together with the encoder and decoder parameters under the overall training objective. Within this formulation, the encoder serves as a demixing mapping from observations to latent sources, while the decoder reconstructs the observed mixtures from the inferred components. The proposed model provides a systematic study of an idea that had previously only been noted in our preliminary form, namely, equipping different latent sources with different GMM priors for ICA, and formulates it as a full VAE framework with end-to-end training and per-dimension prior learning. Experimental results on both linear and nonlinear mixing problems demonstrate that PDGMM-VAE can recover latent source signals and achieve satisfactory separation performance.
Submission history
From: Yuan-Hao Wei Dr. [view email][v1] Fri, 20 Mar 2026 08:54:35 UTC (2,020 KB)
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
