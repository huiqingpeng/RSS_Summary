---
title: "Score Distillation Beyond Acceleration: Generative Modeling from Corrupted Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.13377"
published: "2026-03-19"
fetched: "2026-03-19T13:20:21.027096"
---

Computer Science > Machine Learning
[Submitted on 19 May 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Score Distillation Beyond Acceleration: Generative Modeling from Corrupted Data
View PDF HTML (experimental)Abstract:Learning generative models directly from corrupted observations is a long standing challenge across natural and scientific domains. We introduce Restoration Score Distillation (RSD), a unified framework for learning high fidelity, one step generative models using only degraded data and the mapping $A$ may be the identity or a non invertible corruption operator (e.g., blur, masking, subsampling, Fourier acquisition). RSD first pretrains a corruption aware diffusion teacher on the observed measurements, then distills it into an efficient one step generator whose samples are statistically closer to the clean distribution p_X. The framework subsumes identity corruption (denoising task) as a special case of our general formulation. Empirically, RSD consistently reduces Frechet Inception Distance (FID) relative to corruption aware diffusion teachers across noisy generation (CIFAR 10, FFHQ, CelebA HQ, AFHQ v2), image restoration (Gaussian deblurring, random inpainting, super resolution, and mixtures with additive noise), and multi coil MRI without access to any clean images. The distilled generator inherits one step sampling efficiency, yielding up to 30x speedups over multi step diffusion while surpassing the teachers after substantially fewer training iterations. These results establish score distillation as a practical tool for generative modeling from corrupted data, not merely for acceleration. We provide theoretical support for the use of distillation in enhancing generation quality in the Appendix.
Submission history
From: Yasi Zhang [view email][v1] Mon, 19 May 2025 17:21:03 UTC (21,964 KB)
[v2] Tue, 17 Mar 2026 21:19:35 UTC (45,235 KB)
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
