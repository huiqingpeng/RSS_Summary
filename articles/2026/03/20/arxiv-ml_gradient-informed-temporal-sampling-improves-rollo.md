---
title: "Gradient-Informed Temporal Sampling Improves Rollout Accuracy in PDE Surrogate Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18237"
published: "2026-03-20"
fetched: "2026-03-20T12:08:49.779212"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Gradient-Informed Temporal Sampling Improves Rollout Accuracy in PDE Surrogate Training
View PDF HTML (experimental)Abstract:Researchers train neural simulators on uniformly sampled numerical simulation data. But under the same budget, does systematically sampled data provide the most effective information? A fundamental yet unformalized problem is how to sample training data for neural simulators so as to maximize rollout accuracy. Existing data sampling methods either tend to collapse into locally high-information-density regions, or preserve diversity but remain insufficiently model-specific, often leading to performance that is no better than uniform sampling. To address this, we propose a data sampling method tailored to neural simulators, Gradient-Informed Temporal Sampling (GITS). GITS jointly optimizes pilot-model local gradients and set-level temporal coverage, thereby effectively balancing model specificity and dynamical information. Compared with multiple sampling baselines, the data selected by GITS achieves lower rollout error across multiple PDE systems, model backbones and sample ratios. Furthermore, ablation studies demonstrate the necessity and complementarity of the two optimization objectives in GITS. In addition, we analyze the successful sampling patterns of GITS as well as the typical PDE systems and model backbones on which GITS fails.
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
