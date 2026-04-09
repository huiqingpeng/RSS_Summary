---
title: "MENO: MeanFlow-Enhanced Neural Operators for Dynamical Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06881"
published: "2026-04-09"
fetched: "2026-04-10T07:05:08.797068"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:MENO: MeanFlow-Enhanced Neural Operators for Dynamical Systems
View PDF HTML (experimental)Abstract:Neural operators have emerged as powerful surrogates for dynamical systems due to their grid-invariant properties and computational efficiency. However, the Fourier-based neural operator framework inherently truncates high-frequency components in spectral space, resulting in the loss of small-scale structures and degraded prediction quality at high resolutions when trained on low-resolution data. While diffusion-based enhancement methods can recover multi-scale features, they introduce substantial inference overhead that undermines the efficiency advantage of neural operators. In this work, we introduce \textbf{M}eanFlow-\textbf{E}nhanced \textbf{N}eural \textbf{O}perators (MENO), a novel framework that achieves accurate all-scale predictions with minimal inference cost. By leveraging the improved MeanFlow method, MENO restores both small-scale details and large-scale dynamics with superior physical fidelity and statistical accuracy. We evaluate MENO on three challenging dynamical systems, including phase-field dynamics, 2D Kolmogorov flow, and active matter dynamics, at resolutions up to 256$\times$256. Across all benchmarks, MENO improves the power spectrum density accuracy by up to a factor of 2 compared to baseline neural operators while achieving 12$\times$ faster inference than the state-of-the-art Diffusion Denoising Implicit Model (DDIM)-enhanced counterparts, effectively bridging the gap between accuracy and efficiency. The flexibility and efficiency of MENO position it as an efficient surrogate model for scientific machine learning applications where both statistical integrity and computational efficiency are paramount.
Current browse context:
cs.LG
Change to browse by:
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
