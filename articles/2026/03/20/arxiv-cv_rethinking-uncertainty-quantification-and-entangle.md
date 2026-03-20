---
title: "Rethinking Uncertainty Quantification and Entanglement in Image Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18792"
published: "2026-03-20"
fetched: "2026-03-20T15:16:17.075719"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Rethinking Uncertainty Quantification and Entanglement in Image Segmentation
View PDF HTML (experimental)Abstract:Uncertainty quantification (UQ) is crucial in safety-critical applications such as medical image segmentation. Total uncertainty is typically decomposed into data-related aleatoric uncertainty (AU) and model-related epistemic uncertainty (EU). Many methods exist for modeling AU (such as Probabilistic UNet, Diffusion) and EU (such as ensembles, MC Dropout), but it is unclear how they interact when combined. Additionally, recent work has revealed substantial entanglement between AU and EU, undermining the interpretability and practical usefulness of the decomposition. We present a comprehensive empirical study covering a broad range of AU-EU model combinations, propose a metric to quantify uncertainty entanglement, and evaluate both across downstream UQ tasks. For out-of-distribution detection, ensembles exhibit consistently lower entanglement and superior performance. For ambiguity modeling and calibration the best models are dataset-dependent, with softmax/SSN-based methods performing well and Probabilistic UNets being less entangled. A softmax ensemble fares remarkably well on all tasks. Finally, we analyze potential sources of uncertainty entanglement and outline directions for mitigating this effect.
Submission history
From: Jakob Christensen [view email][v1] Thu, 19 Mar 2026 11:43:26 UTC (7,856 KB)
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
