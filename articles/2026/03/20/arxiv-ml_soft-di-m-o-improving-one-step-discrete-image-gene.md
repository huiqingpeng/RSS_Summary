---
title: "Soft-Di[M]O: Improving One-Step Discrete Image Generation with Soft Embeddings"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.22925"
published: "2026-03-20"
fetched: "2026-03-20T14:16:50.620270"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 26 Sep 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Soft-Di[M]O: Improving One-Step Discrete Image Generation with Soft Embeddings
View PDF HTML (experimental)Abstract:One-step generators distilled from Masked Diffusion Models (MDMs) compress multiple sampling steps into a single forward pass, enabling efficient text and image synthesis. However, they suffer two key limitations: they inherit modeling bias from the teacher, and their discrete token outputs block gradient flow, preventing post-distillation refinements such as adversarial training, reward-based fine-tuning, and Test-Time Embedding Optimization (TTEO). In this work, we introduce soft embeddings, a simple relaxation that replaces discrete tokens with the expected embeddings under the generator's output distribution. Soft embeddings preserve representation fidelity for one-step discrete generator while providing a fully differentiable continuous surrogate that is compatible with teacher backbones and tokenizer decoders. Integrating soft embeddings into the Di[M]O distillation framework (denoted Soft-Di[M]O) makes one-step generators end-to-end trainable and enables straightforward application of GAN-based refinement, differentiable reward fine-tuning, and TTEO. Empirically, across multiple MDM teachers (e.g., MaskBit, MaskGen), Soft-Di[M]O achieves state-of-the-art one-step results: improved class-to-image performance, a one-step FID of 1.56 on ImageNet-256 with GAN-based refinement, along with higher GenEval and HPS scores on text-to-image with reward fine-tuning, and further gains from TTEO.
Submission history
From: Yuanzhi Zhu [view email][v1] Fri, 26 Sep 2025 20:51:20 UTC (32,278 KB)
[v2] Thu, 19 Mar 2026 11:47:39 UTC (33,244 KB)
Current browse context:
cs.CV
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
