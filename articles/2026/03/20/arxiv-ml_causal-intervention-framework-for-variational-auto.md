---
title: "Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.03530"
published: "2026-03-20"
fetched: "2026-03-20T14:05:59.553857"
---

Computer Science > Machine Learning
[Submitted on 6 May 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability
View PDFAbstract:Mechanistic interpretability of deep learning models has emerged as a crucial research direction for understanding the functioning of neural networks. While significant progress has been made in interpreting discriminative models like transformers, understanding generative models such as Variational Autoencoders (VAEs) remains challenging. This paper introduces a comprehensive causal intervention framework for mechanistic interpretability of VAEs. We develop techniques to identify and analyze "circuit motifs" in VAEs, examining how semantic factors are encoded, processed, and disentangled through the network layers. Our approach uses targeted interventions at different levels: input manipulations, latent space perturbations, activation patching, and causal mediation analysis. We apply our framework to both synthetic datasets with known causal relationships and standard disentanglement benchmarks. Results show that our interventions can successfully isolate functional circuits, map computational graphs to causal graphs of semantic factors, and distinguish between polysemantic and monosemantic units. Furthermore, we introduce metrics for causal effect strength, intervention specificity, and circuit modularity that quantify the interpretability of VAE components. Experimental results demonstrate clear differences between VAE variants, with FactorVAE achieving higher disentanglement scores (0.084) and effect strengths (mean 4.59) compared to standard VAE (0.064, 3.99) and Beta-VAE (0.051, 3.43). Our framework advances the mechanistic understanding of generative models and provides tools for more transparent and controllable VAE architectures.
Submission history
From: Dip Roy [view email][v1] Tue, 6 May 2025 13:40:59 UTC (1,825 KB)
[v2] Tue, 17 Mar 2026 23:40:44 UTC (1,518 KB)
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
