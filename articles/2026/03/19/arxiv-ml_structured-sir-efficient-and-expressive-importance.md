---
title: "Structured SIR: Efficient and Expressive Importance-Weighted Inference for High-Dimensional Image Registration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17415"
published: "2026-03-19"
fetched: "2026-03-19T13:12:07.930322"
---

Electrical Engineering and Systems Science > Image and Video Processing
[Submitted on 18 Mar 2026]
Title:Structured SIR: Efficient and Expressive Importance-Weighted Inference for High-Dimensional Image Registration
View PDF HTML (experimental)Abstract:Image registration is an ill-posed dense vision task, where multiple solutions achieve similar loss values, motivating probabilistic inference. Variational inference has previously been employed to capture these distributions, however restrictive assumptions about the posterior form can lead to poor characterisation, overconfidence and low-quality samples. More flexible posteriors are typically bottlenecked by the complexity of high-dimensional covariance matrices required for dense 3D image registration.
In this work, we present a memory and computationally efficient inference method, Structured SIR, that enables expressive, multi-modal, characterisation of uncertainty with high quality samples. We propose the use of a Sampled Importance Resampling (SIR) algorithm with a novel memory-efficient high-dimensional covariance parameterisation as the sum of a low-rank covariance and a sparse, spatially structured Cholesky precision factor. This structure enables capturing complex spatial correlations while remaining computationally tractable.
We evaluate the efficacy of this approach in 3D dense image registration of brain MRI data, which is a very high-dimensional problem. We demonstrate that our proposed methods produces uncertainty estimates that are significantly better calibrated than those produced by variational methods, achieving equivalent or better accuracy. Crucially, we show that the model yields highly structured multi-modal posterior distributions, enable effective and efficient uncertainty quantification.
Current browse context:
eess.IV
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
