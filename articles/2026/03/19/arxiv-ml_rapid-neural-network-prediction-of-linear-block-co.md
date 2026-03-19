---
title: "Rapid Neural Network Prediction of Linear Block Copolymer Free Energies"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17391"
published: "2026-03-19"
fetched: "2026-03-19T13:11:46.453493"
---

Condensed Matter > Soft Condensed Matter
[Submitted on 18 Mar 2026]
Title:Rapid Neural Network Prediction of Linear Block Copolymer Free Energies
View PDF HTML (experimental)Abstract:Free energies are fundamental quantities governing phase behavior and thermodynamic stability in polymer systems, yet their accurate computation often requires extensive simulations and post-processing techniques such as the Bennett Acceptance Ratio (BAR). While BAR provides reliable estimates when applied between closely related thermodynamic states, evaluating free energies across large changes in interaction strength typically requires a sequence of intermediate simulations to maintain sufficient phase-space overlap, substantially increasing computational cost. In this work we develop a machine learning framework for rapidly predicting excess free energies of linear diblock copolymer systems from simulation-derived energetic descriptors. Using dissipative particle dynamics simulations of freely-jointed chain polymers, we construct a dataset of per-chain energetic statistics, including heterogeneous interaction energies, homogeneous interaction energies, and bonded spring energies, and train feed-forward neural networks to learn the relationship between these descriptors and free energies computed using a stratified BAR procedure. The resulting models accurately reproduce the reference free energies across a range of chain lengths, compositions, and densities, including polymer architectures held out from training. In regimes where direct, brute-force BAR estimates become unreliable due to poor phase-space overlap, the neural network predictions remain consistent with the reference values. These results demonstrate that physically informed machine learning models can serve as efficient surrogates for expensive free-energy calculations and provide a promising approach for accelerating thermodynamic analysis of polymer systems.
Submission history
From: Alfredo Alexander-Katz [view email][v1] Wed, 18 Mar 2026 06:15:23 UTC (3,250 KB)
Current browse context:
cond-mat.soft
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
