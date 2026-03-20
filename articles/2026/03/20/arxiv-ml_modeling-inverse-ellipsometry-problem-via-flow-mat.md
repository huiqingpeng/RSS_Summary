---
title: "Modeling Inverse Ellipsometry Problem via Flow Matching with a Large-Scale Dataset"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2407.17869"
published: "2026-03-20"
fetched: "2026-03-20T14:04:38.910142"
---

Computer Science > Machine Learning
[Submitted on 25 Jul 2024 (v1), last revised 14 Mar 2026 (this version, v2)]
Title:Modeling Inverse Ellipsometry Problem via Flow Matching with a Large-Scale Dataset
View PDF HTML (experimental)Abstract:Inverse ellipsometry, i.e., reconstructing optical constants and film thickness from the measured phase difference $\Delta$ and amplitude ratio $\Psi$, is a fundamentally ill-posed problem. Traditional solutions rely on slow, expert-driven iterative fitting, while the development of machine learning approaches has been severely limited by the lack of large-scale, physically consistent datasets. To address this gap, we introduce \textbf{EllipBench}, a comprehensive benchmark comprising over 8 million high-precision samples spanning 98 thin-film materials and 5 substrates. Building upon this benchmark, we conduct a systematic evaluation of a broad spectrum of methods, including traditional machine learning models, deep neural networks, and Physics-Informed Neural Networks, and show that existing paradigms consistently struggle to fully resolve the inverse ellipsometry task. To better capture its inherent ambiguity, we further propose a novel \textbf{Decoupled Conditional Flow Matching (DCFM)} framework. Rather than formulating the problem as deterministic point-to-point regression, DCFM explicitly decouples geometric film thickness and incorporates it as a robust physical condition to guide a continuous vector field for modeling the inverse probability distribution of wavelength-dependent optical constants. Combined with a gradient detachment strategy and physics-based constraints, our joint architecture effectively mitigates intrinsic physical ambiguities and delivers a robust and accurate solution for inverse ellipsometry.
Submission history
From: Yiming Ma [view email][v1] Thu, 25 Jul 2024 08:42:23 UTC (3,126 KB)
[v2] Sat, 14 Mar 2026 13:04:51 UTC (7,293 KB)
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
