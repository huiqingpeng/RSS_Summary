---
title: "Enhancing the Parameterization of Reservoir Properties for Data Assimilation Using Deep VAE-GAN"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18766"
published: "2026-03-20"
fetched: "2026-03-20T12:15:36.766969"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Enhancing the Parameterization of Reservoir Properties for Data Assimilation Using Deep VAE-GAN
View PDFAbstract:Currently, the methods called Iterative Ensemble Smoothers, especially the method called Ensemble Smoother with Multiple Data Assimilation (ESMDA) can be considered state-of-the-art for history matching in petroleum reservoir simulation. However, this approach has two important limitations: the use of an ensemble with finite size to represent the distributions and the Gaussian assumption in parameter and data uncertainties. This latter is particularly important because many reservoir properties have non-Gaussian distributions. Parameterization involves mapping non-Gaussian parameters to a Gaussian field before the update and then mapping them back to the original domain to forward the ensemble through the reservoir simulator. A promising approach to perform parameterization is through deep learning models. Recent studies have shown that Generative Adversarial Networks (GAN) performed poorly concerning data assimilation, but generated more geologically plausible realizations of the reservoir, while the Variational Autoencoder (VAE) performed better than the GAN in data assimilation, but generated less geologically realistic models. This work is innovative in combining the strengths of both to implement a deep learning model called Variational Autoencoder Generative Adversarial Network (VAE-GAN) integrated with ESMDA. The methodology was applied in two case studies, one case being categorical and the other with continuous values of permeability. Our findings demonstrate that by applying the VAE-GAN model we can obtain high quality reservoir descriptions (just like GANs) and a good history matching on the production curves (just like VAEs) simultaneously.
Submission history
From: Marcio Augusto Sampaio M. A. Sampaio [view email][v1] Thu, 19 Mar 2026 11:20:20 UTC (2,968 KB)
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
