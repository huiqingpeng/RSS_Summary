---
title: "Prior-Informed Neural Network Initialization: A Spectral Approach for Function Parameterizing Architectures"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16376"
published: "2026-03-18"
fetched: "2026-03-18T15:43:23.764222"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Prior-Informed Neural Network Initialization: A Spectral Approach for Function Parameterizing Architectures
View PDF HTML (experimental)Abstract:Neural network architectures designed for function parameterization, such as the Bag-of-Functions (BoF) framework, bridge the gap between the expressivity of deep learning and the interpretability of classical signal processing. However, these models are inherently sensitive to parameter initialization, as traditional data-agnostic schemes fail to capture the structural properties of the target signals, often leading to suboptimal convergence. In this work, we propose a prior-informed design strategy that leverages the intrinsic spectral and temporal structure of the data to guide both network initialization and architectural configuration. A principled methodology is introduced that uses the Fast Fourier Transform to extract dominant seasonal priors, informing model depth and initial states, and a residual-based regression approach to parameterize trend components. Crucially, this structural alignment enables a substantial reduction in encoder dimensionality without compromising reconstruction fidelity. A supporting theoretical analysis provides guidance on trend estimation under finite-sample regimes. Extensive experiments on synthetic and real-world benchmarks demonstrate that embedding data-driven priors significantly accelerates convergence, reduces performance variability across trials, and improves computational efficiency. Overall, the proposed framework enables more compact and interpretable architectures while outperforming standard initialization baselines, without altering the core training procedure.
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
