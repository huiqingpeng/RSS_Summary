---
title: "Causally-Guided Diffusion for Stable Feature Selection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20930"
published: "2026-03-24"
fetched: "2026-03-25T07:16:12.013780"
---

Computer Science > Machine Learning
[Submitted on 21 Mar 2026]
Title:Causally-Guided Diffusion for Stable Feature Selection
View PDF HTML (experimental)Abstract:Feature selection is fundamental to robust data-centric AI, but most existing methods optimize predictive performance under a single data distribution. This often selects spurious features that fail under distribution shifts. Motivated by principles from causal invariance, we study feature selection from a stability perspective and introduce Causally-Guided Diffusion for Stable Feature Selection (CGDFS). In CGDFS, we formalized feature selection as approximate posterior inference over feature subsets, whose posterior mass favors low prediction error and low cross-environment variance. Our framework combines three key insights: First, we formulate feature selection as stability-aware posterior sampling. Here, causal invariance serves as a soft inductive bias rather than explicit causal discovery. Second, we train a diffusion model as a learned prior over plausible continuous selection masks, combined with a stability-aware likelihood that rewards invariance across environments. This diffusion prior captures structural dependencies among features and enables scalable exploration of the combinatorially large selection space. Third, we perform guided annealed Langevin sampling that combines the diffusion prior with the stability objective, which yields a tractable, uncertainty-aware posterior inference that avoids discrete optimization and produces robust feature selections. We evaluate CGDFS on open-source real-world datasets exhibiting distribution shifts. Across both classification and regression tasks, CGDFS consistently selects more stable and transferable feature subsets, which leads to improved out-of-distribution performance and greater selection robustness compared to sparsity-based, tree-based, and stability-selection baselines.
Submission history
From: Arun Vignesh Malarkkan [view email][v1] Sat, 21 Mar 2026 20:14:00 UTC (1,332 KB)
Current browse context:
cs.LG
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
