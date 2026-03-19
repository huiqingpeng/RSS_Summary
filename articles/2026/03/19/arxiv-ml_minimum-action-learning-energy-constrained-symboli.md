---
title: "Minimum-Action Learning: Energy-Constrained Symbolic Model Selection for Physical Law Identification from Noisy Data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16951"
published: "2026-03-19"
fetched: "2026-03-19T12:05:58.447417"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Minimum-Action Learning: Energy-Constrained Symbolic Model Selection for Physical Law Identification from Noisy Data
View PDF HTML (experimental)Abstract:Identifying physical laws from noisy observational data is a central challenge in scientific machine learning. We present Minimum-Action Learning (MAL), a framework that selects symbolic force laws from a pre-specified basis library by minimizing a Triple-Action functional combining trajectory reconstruction, architectural sparsity, and energy-conservation enforcement. A wide-stencil acceleration-matching technique reduces noise variance by 10,000x, transforming an intractable problem (SNR ~0.02) into a learnable one (SNR ~1.6); this preprocessing is the critical enabler shared by all methods tested, including SINDy variants. On two benchmarks -- Kepler gravity and Hooke's law -- MAL recovers the correct force law with Kepler exponent p = 3.01 +/- 0.01 at ~0.07 kWh (40% reduction vs. prediction-error-only baselines). The raw correct-basis rate is 40% for Kepler and 90% for Hooke; an energy-conservation-based criterion discriminates the true force law in all cases, yielding 100% pipeline-level identification. Basis library sensitivity experiments show that near-confounders degrade selection (20% with added r^{-2.5} and r^{-1.5}), while distant additions are harmless, and the conservation diagnostic remains informative even when the correct basis is absent. Direct comparison with noise-robust SINDy variants, Hamiltonian Neural Networks, and Lagrangian Neural Networks confirms MAL's distinct niche: interpretable, energy-constrained model selection that combines symbolic basis identification with dynamical rollout validation.
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
