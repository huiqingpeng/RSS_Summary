---
title: "DSS-GAN: Directional State Space GAN with Mamba backbone for Class-Conditional Image Synthesis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17637"
published: "2026-03-19"
fetched: "2026-03-19T12:15:08.148933"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:DSS-GAN: Directional State Space GAN with Mamba backbone for Class-Conditional Image Synthesis
View PDF HTML (experimental)Abstract:We present DSS-GAN, the first generative adversarial network to employ Mamba as a hierarchical generator backbone for noise-to-image synthesis. The central contribution is Directional Latent Routing (DLR), a novel conditioning mechanism that decomposes the latent vector into direction-specific subvectors, each jointly projected with a class embedding to produce a feature-wise affine modulation of the corresponding Mamba scan. Unlike conventional class conditioning that injects a global signal, DLR couples class identity and latent structure along distinct spatial axes of the feature map, applied consistently across all generative scales. DSS-GAN achieves improved FID, KID, and precision-recall scores compared to StyleGAN2-ADA across multiple tested datasets. Analysis of the latent space reveals that directional subvectors exhibit measurable specialization: perturbations along individual components produce structured, direction-correlated changes in the synthesized image.
Submission history
From: Aleksander Ogonowski [view email][v1] Wed, 18 Mar 2026 11:58:47 UTC (22,307 KB)
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
