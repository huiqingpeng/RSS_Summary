---
title: "Neighbor GRPO: Contrastive ODE Policy Optimization Aligns Flow Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.16955"
published: "2026-03-19"
fetched: "2026-03-19T14:17:42.042776"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 21 Nov 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Neighbor GRPO: Contrastive ODE Policy Optimization Aligns Flow Models
View PDF HTML (experimental)Abstract:Group Relative Policy Optimization (GRPO) has shown promise in aligning image and video generative models with human preferences. However, applying it to modern flow matching models is challenging because of its deterministic sampling paradigm. Current methods address this issue by converting Ordinary Differential Equations (ODEs) to Stochastic Differential Equations (SDEs), which introduce stochasticity. However, this SDE-based GRPO suffers from issues of inefficient credit assignment and incompatibility with high-order solvers for fewer-step sampling. In this paper, we first reinterpret existing SDE-based GRPO methods from a distance optimization perspective, revealing their underlying mechanism as a form of contrastive learning. Based on this insight, we propose Neighbor GRPO, a novel alignment algorithm that completely bypasses the need for SDEs. Neighbor GRPO generates a diverse set of candidate trajectories by perturbing the initial noise conditions of the ODE and optimizes the model using a softmax distance-based surrogate leaping policy. We establish a theoretical connection between this distance-based objective and policy gradient optimization, rigorously integrating our approach into the GRPO framework. Our method fully preserves the advantages of deterministic ODE sampling, including efficiency and compatibility with high-order solvers. We further introduce symmetric anchor sampling for computational efficiency and group-wise quasi-norm reweighting to address reward flattening. Extensive experiments demonstrate that Neighbor GRPO significantly outperforms SDE-based counterparts in terms of training cost, convergence speed, and generation quality.
Submission history
From: Dailan He [view email][v1] Fri, 21 Nov 2025 05:02:47 UTC (12,487 KB)
[v2] Wed, 18 Mar 2026 09:58:10 UTC (12,489 KB)
Current browse context:
cs.CV
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
