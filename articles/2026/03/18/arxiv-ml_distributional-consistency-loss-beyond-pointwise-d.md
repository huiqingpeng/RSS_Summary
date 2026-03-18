---
title: "Distributional Consistency Loss: Beyond Pointwise Data Terms in Inverse Problems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.13972"
published: "2026-03-18"
fetched: "2026-03-18T16:19:49.934023"
---

Computer Science > Machine Learning
[Submitted on 15 Oct 2025 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Distributional Consistency Loss: Beyond Pointwise Data Terms in Inverse Problems
View PDF HTML (experimental)Abstract:Recovering true signals from noisy measurements is a central challenge in inverse problems spanning medical imaging, geophysics, and signal processing. Current methods balance prior signal priors (regularization) with agreement with noisy data (data-fidelity). Conventional data-fidelity loss functions, such as mean-squared error (MSE) or negative log-likelihood, seek pointwise agreement with noisy measurements, often leading to overfitting to noise. In this work, we instead evaluate data-fidelity collectively by testing whether the observed measurements are statistically consistent with the noise distributions implied by the current estimate. We introduce distributional consistency (DC) loss, a data-fidelity objective that replaces pointwise matching with distribution-level calibration. DC loss acts as a direct and practical plug-in replacement for standard data consistency terms: i) it is compatible with modern unsupervised regularizers that operate without paired measurement-ground-truth data, ii) it is optimized in the same way as traditional losses, and iii) it avoids overfitting to measurement noise without early stopping or priors. Its scope naturally fits many practical inverse problems where the measurement-noise distribution is known and where the measured dataset consists of many independent noisy values. We demonstrate efficacy in two key example application areas: i) in image denoising with deep image prior, using DC instead of MSE loss removes the need for early stopping and achieves higher PSNR; ii) in medical image reconstruction from Poisson-noisy data, DC loss reduces artifacts in highly-iterated reconstructions and enhances the efficacy of hand-crafted regularization. These results position DC loss as a statistically grounded, performance-enhancing alternative to conventional fidelity losses for an important class of unsupervised noise-dominated inverse problems.
Submission history
From: George Webber [view email][v1] Wed, 15 Oct 2025 18:01:23 UTC (13,075 KB)
[v2] Tue, 17 Mar 2026 13:39:21 UTC (14,696 KB)
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
