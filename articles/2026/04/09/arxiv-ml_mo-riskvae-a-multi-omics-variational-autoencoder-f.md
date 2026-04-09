---
title: "MO-RiskVAE: A Multi-Omics Variational Autoencoder for Survival Risk Modeling in Multiple MyelomaMO-RiskVAE"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06267"
published: "2026-04-09"
fetched: "2026-04-10T07:04:55.060143"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:MO-RiskVAE: A Multi-Omics Variational Autoencoder for Survival Risk Modeling in Multiple MyelomaMO-RiskVAE
View PDF HTML (experimental)Abstract:Multimodal variational autoencoders (VAEs) have emerged as a powerful framework for survival risk modeling in multiple myeloma by integrating heterogeneous omics and clinical data. However, when trained under survival supervision, standard latent regularization strategies often fail to preserve prognostically relevant variation, leading to unstable or overly constrained representations. Despite numerous proposed variants, it remains unclear which aspects of latent design fundamentally govern performance in this setting. In this work, we conduct a controlled investigation of latent modeling choices for multimodal survival prediction within a unified extension of the MyeVAE framework. By systematically isolating regularization scale, posterior geometry, and latent space structure under identical architectures and optimization protocols, we show that survival-driven training is primarily sensitive to the magnitude and structure of latent regularization rather than the specific divergence formulation. In particular, moderate relaxation of KL regularization consistently improves survival discrimination, while alternative divergence mechanisms such as MMD and HSIC provide limited benefit without appropriate scaling. We further demonstrate that structuring the latent space can improve alignment between learned representations and survival risk gradients. A hybrid continuous--discrete formulation based on Gumbel--Softmax enhances global risk ordering in the continuous latent subspace, even though stable discrete subtype discovery does not emerge under survival supervision. Guided by these findings, we instantiate a robust multimodal survival model, termed MO-RiskVAE, which consistently improves risk stratification over the original MyeVAE without introducing additional supervision or complex training heuristics.
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
