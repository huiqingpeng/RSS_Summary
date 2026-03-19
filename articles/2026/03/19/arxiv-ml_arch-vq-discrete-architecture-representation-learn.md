---
title: "Arch-VQ: Discrete Architecture Representation Learning with Autoregressive Priors"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2503.22063"
published: "2026-03-19"
fetched: "2026-03-19T13:19:32.296703"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Arch-VQ: Discrete Architecture Representation Learning with Autoregressive Priors
View PDF HTML (experimental)Abstract:Existing neural architecture representation learning methods focus on continuous representation learning, typically using Variational Autoencoders (VAEs) to map discrete architectures onto a continuous Gaussian distribution. However, sampling from these spaces often leads to a high percentage of invalid or duplicate neural architectures, likely due to the unnatural mapping of inherently discrete architectural space onto a continuous space. In this work, we revisit architecture representation learning from a fundamentally discrete perspective. We propose Arch-VQ, a framework that learns a discrete latent space of neural architectures using a Vector-Quantized Variational Autoencoder (VQ-VAE), and models the latent prior with an autoregressive transformer. This formulation yields discrete architecture representations that are better aligned with the underlying search space while decoupling representation learning from prior modeling. Across NASBench-101, NASBench-201, and DARTS search spaces, Arch-VQ improves the quality of generated architectures, increasing the rate of valid and unique generations by 22%, 26%, and 135%, respectively, over state-of-the-art baselines. We further show that modeling discrete embeddings autoregressively enhances downstream neural predictor performance, establishing the practical utility of this discrete formulation.
Submission history
From: Deshani Geethika Poddenige [view email][v1] Fri, 28 Mar 2025 00:56:56 UTC (11,767 KB)
[v2] Wed, 18 Mar 2026 01:44:15 UTC (2,051 KB)
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
