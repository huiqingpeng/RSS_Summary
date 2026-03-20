---
title: "Latent Causal Modeling for 3D Brain MRI Counterfactuals"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2409.05585"
published: "2026-03-20"
fetched: "2026-03-20T16:10:12.054091"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 9 Sep 2024 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:Latent Causal Modeling for 3D Brain MRI Counterfactuals
View PDF HTML (experimental)Abstract:The number of samples in structural brain MRI studies is often too small to properly train deep learning models. Generative models show promise in addressing this issue by effectively learning the data distribution and generating high-fidelity MRI. However, they struggle to produce diverse, high-quality data outside the distribution defined by the training data. One way to address this issue is to use causal models developed for 3D volume counterfactuals. However, accurately modeling causality in high-dimensional spaces is challenging, so these models generally generate 3D brain MRIs of lower quality. To address these challenges, we propose a two-stage method that constructs a Structural Causal Model (SCM) within the latent space. In the first stage, we employ a VQ-VAE to learn a compact embedding of the MRI volume. Subsequently, we integrate our causal model into this latent space and execute a three-step counterfactual procedure using a closed-form Generalized Linear Model (GLM). Our experiments conducted on real-world high-resolution MRI data (1 mm) provided by the Alzheimer's Disease Neuroimaging Initiative (ADNI) and the National Consortium on Alcohol and Neurodevelopment in Adolescence (NCANDA) demonstrate that our method can generate high-quality 3D MRI counterfactuals.
Submission history
From: Wei Peng [view email][v1] Mon, 9 Sep 2024 13:15:03 UTC (21,691 KB)
[v2] Sat, 28 Feb 2026 07:26:49 UTC (4,530 KB)
[v3] Thu, 19 Mar 2026 04:04:57 UTC (4,530 KB)
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
