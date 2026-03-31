---
title: "Central-to-Local Adaptive Generative Diffusion Framework for Improving Gene Expression Prediction in Data-Limited Spatial Transcriptomics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26827"
published: "2026-03-31"
fetched: "2026-04-01T07:19:21.869863"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Central-to-Local Adaptive Generative Diffusion Framework for Improving Gene Expression Prediction in Data-Limited Spatial Transcriptomics
View PDF HTML (experimental)Abstract:Spatial Transcriptomics (ST) provides spatially resolved gene expression profiles within intact tissue architecture, enabling molecular analysis in histological context. However, the high cost, limited throughput, and restricted data sharing of ST experiments result in severe data scarcity, constraining the development of robust computational models. To address this limitation, we present a Central-to-Local adaptive generative diffusion framework for ST (C2L-ST) that integrates large-scale morphological priors with limited molecular guidance. A global central model is first pretrained on extensive histopathology datasets to learn transferable morphological representations, and institution-specific local models are then adapted through lightweight gene-conditioned modulation using a small number of paired image-gene spots. This strategy enables the synthesis of realistic and molecularly consistent histology patches under data-limited conditions. The generated images exhibit high visual and structural fidelity, reproduce cellular composition, and show strong embedding overlap with real data across multiple organs, reflecting both realism and diversity. When incorporated into downstream training, synthetic image-gene pairs improve gene expression prediction accuracy and spatial coherence, achieving performance comparable to real data while requiring only a fraction of sampled spots. C2L-ST provides a scalable and data-efficient framework for molecular-level data augmentation, offering a domain-adaptive and generalizable approach for integrating histology and transcriptomics in spatial biology and related fields.
Current browse context:
cs.LG
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
