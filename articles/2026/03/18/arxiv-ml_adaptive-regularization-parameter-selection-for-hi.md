---
title: "Adaptive regularization parameter selection for high-dimensional inverse problems: A Bayesian approach with Tucker low-rank constraints"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16066"
published: "2026-03-18"
fetched: "2026-03-18T15:39:51.476268"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Adaptive regularization parameter selection for high-dimensional inverse problems: A Bayesian approach with Tucker low-rank constraints
View PDF HTML (experimental)Abstract:This paper introduces a novel variational Bayesian method that integrates Tucker decomposition for efficient high-dimensional inverse problem solving. The method reduces computational complexity by transforming variational inference from a high-dimensional space to a lower-dimensional core tensor space via Tucker decomposition. A key innovation is the introduction of per-mode precision parameters, enabling adaptive regularization for anisotropic structures. For instance, in directional image deblurring, learned parameters align with physical anisotropy, applying stronger regularization to critical directions (e.g., row vs. column axes). The method further estimates noise levels from data, eliminating reliance on prior knowledge of noise parameters (unlike conventional benchmarks such as the discrepancy principle (DP)). Experimental evaluations across 2D deblurring, 3D heat conduction, and Fredholm integral equations demonstrate consistent improvements in quantitative metrics (PSNR, SSIM) and qualitative visualizations (error maps, precision parameter trends) compared to L-curve criterion, generalized cross-validation (GCV), unbiased predictive risk estimator (UPRE), and DP. The approach scales to problems with 110,000 variables and outperforms existing methods by 0.73-2.09 dB in deblurring tasks and 6.75 dB in 3D heat conduction. Limitations include sensitivity to rank selection in Tucker decomposition and the need for theoretical analysis. Future work will explore automated rank selection and theoretical guarantees. This method bridges Bayesian theory and scalable computation, offering practical solutions for large-scale inverse problems in imaging, remote sensing, and scientific computing.
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
