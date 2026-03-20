---
title: "Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.03714"
published: "2026-03-20"
fetched: "2026-03-20T14:14:35.931739"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 6 Feb 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment
View PDF HTML (experimental)Abstract:We present Universal Sparse Autoencoders (USAEs), a framework for uncovering and aligning interpretable concepts spanning multiple pretrained deep neural networks. Unlike existing concept-based interpretability methods, which focus on a single model, USAEs jointly learn a universal concept space that can reconstruct and interpret the internal activations of multiple models at once. Our core insight is to train a single, overcomplete sparse autoencoder (SAE) that ingests activations from any model and decodes them to approximate the activations of any other model under consideration. By optimizing a shared objective, the learned dictionary captures common factors of variation-concepts-across different tasks, architectures, and datasets. We show that USAEs discover semantically coherent and important universal concepts across vision models; ranging from low-level features (e.g., colors and textures) to higher-level structures (e.g., parts and objects). Overall, USAEs provide a powerful new method for interpretable cross-model analysis and offers novel applications, such as coordinated activation maximization, that open avenues for deeper insights in multi-model AI systems
Submission history
From: Harrish Thasarathan [view email][v1] Thu, 6 Feb 2025 02:06:16 UTC (46,350 KB)
[v2] Wed, 18 Mar 2026 21:16:08 UTC (15,006 KB)
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
