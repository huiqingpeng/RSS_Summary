---
title: "Relaxed Efficient Acquisition of Context and Temporal Features"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.11370"
published: "2026-03-18"
fetched: "2026-03-18T17:05:39.526239"
---

Computer Science > Machine Learning
[Submitted on 11 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Relaxed Efficient Acquisition of Context and Temporal Features
View PDF HTML (experimental)Abstract:In many biomedical applications, measurements are not freely available at inference time: each laboratory test, imaging modality, or assessment incurs financial cost, time burden, or patient risk. Longitudinal active feature acquisition (LAFA) seeks to optimize predictive performance under such constraints by adaptively selecting measurements over time, yet the problem remains inherently challenging due to temporally coupled decisions (missed early measurements cannot be revisited, and acquisition choices influence all downstream predictions). Moreover, real-world clinical workflows typically begin with an initial onboarding phase, during which relatively stable contextual descriptors (e.g., demographics or baseline characteristics) are collected once and subsequently condition longitudinal decision-making. Despite its practical importance, the efficient selection of onboarding context has not been studied jointly with temporally adaptive acquisition. We therefore propose REACT (Relaxed Efficient Acquisition of Context and Temporal features), an end-to-end differentiable framework that simultaneously optimizes (i) selection of onboarding contextual descriptors and (ii) adaptive feature--time acquisition plans for longitudinal measurements under cost constraints. REACT employs a Gumbel--Sigmoid relaxation with straight-through estimation to enable gradient-based optimization over discrete acquisition masks, allowing direct backpropagation from prediction loss and acquisition cost. Across real-world longitudinal health and behavioral datasets, REACT achieves improved predictive performance at lower acquisition costs compared to existing longitudinal acquisition baselines, demonstrating the benefit of modeling onboarding and temporally coupled acquisition within a unified optimization framework.
Submission history
From: Yunni Qu [view email][v1] Wed, 11 Mar 2026 23:17:13 UTC (7,202 KB)
[v2] Mon, 16 Mar 2026 15:15:44 UTC (7,202 KB)
[v3] Tue, 17 Mar 2026 03:53:46 UTC (7,202 KB)
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
