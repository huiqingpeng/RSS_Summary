---
title: "PhasorFlow: A Python Library for Unit Circle Based Computing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15886"
published: "2026-03-18"
fetched: "2026-03-18T15:36:41.726034"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:PhasorFlow: A Python Library for Unit Circle Based Computing
View PDF HTML (experimental)Abstract:We present PhasorFlow, an open-source Python library introducing a computational paradigm operating on the $S^1$ unit circle. Inputs are encoded as complex phasors $z = e^{i\theta}$ on the $N$-Torus ($\mathbb{T}^N$). As computation proceeds via unitary wave interference gates, global norm is preserved while individual components drift into $\mathbb{C}^N$, allowing algorithms to natively leverage continuous geometric gradients for predictive learning. PhasorFlow provides three core contributions. First, we formalize the Phasor Circuit model ($N$ unit circle threads, $M$ gates) and introduce a 22-gate library covering Standard Unitary, Non-Linear, Neuromorphic, and Encoding operations with full matrix algebra simulation. Second, we present the Variational Phasor Circuit (VPC), analogous to Variational Quantum Circuits (VQC), enabling optimization of continuous phase parameters for classical machine learning tasks. Third, we introduce the Phasor Transformer, replacing expensive $QK^TV$ attention with a parameter-free, DFT-based token mixing layer inspired by FNet. We validate PhasorFlow on non-linear spatial classification, time-series prediction, financial volatility detection, and neuromorphic tasks including neural binding and oscillatory associative memory. Our results establish unit circle computing as a deterministic, lightweight, and mathematically principled alternative to classical neural networks and quantum circuits. It operates on classical hardware while sharing quantum mechanics' unitary foundations. PhasorFlow is available at this https URL.
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
