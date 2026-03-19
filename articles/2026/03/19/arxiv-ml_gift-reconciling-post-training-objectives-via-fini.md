---
title: "GIFT: Reconciling Post-Training Objectives via Finite-Temperature Gibbs Initialization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.09233"
published: "2026-03-19"
fetched: "2026-03-19T14:11:11.778819"
---

Computer Science > Machine Learning
[Submitted on 14 Jan 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:GIFT: Reconciling Post-Training Objectives via Finite-Temperature Gibbs Initialization
View PDF HTML (experimental)Abstract:The prevailing post-training paradigm for Large Reasoning Models (LRMs) - Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL) - suffers from an intrinsic optimization mismatch: the rigid supervision inherent in SFT induces distributional collapse, thereby exhausting the exploration space necessary for subsequent RL. In this paper, we reformulate SFT to reconcile post-training objectives and propose Gibbs Initialization with Finite Temperature (GIFT). We characterize standard SFT as a degenerate zero-temperature limit that suppresses base priors. Conversely, GIFT incorporates supervision as a finite-temperature energy potential, establishing a distributional bridge that promotes objective consistency throughout the post-training pipeline. Our experiments demonstrate that GIFT significantly outperforms standard SFT and other competitive baselines when utilized for RL initialization, providing a mathematically principled pathway to preserve exploration and align the two post-training stages. Our code is available at this https URL.
Submission history
From: Zhengyang Zhao [view email][v1] Wed, 14 Jan 2026 07:13:57 UTC (105 KB)
[v2] Wed, 18 Mar 2026 13:05:20 UTC (98 KB)
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
