---
title: "EFF-Grasp: Energy-Field Flow Matching for Physics-Aware Dexterous Grasp Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16151"
published: "2026-03-18"
fetched: "2026-03-18T18:06:37.886867"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 17 Mar 2026]
Title:EFF-Grasp: Energy-Field Flow Matching for Physics-Aware Dexterous Grasp Generation
View PDF HTML (experimental)Abstract:Denoising generative models have recently become the dominant paradigm for dexterous grasp generation, owing to their ability to model complex grasp distributions from large-scale data. However, existing diffusion-based methods typically formulate generation as a stochastic differential equation (SDE), which often requires many sequential denoising steps and introduces trajectory instability that can lead to physically infeasible grasps. In this paper, we propose EFF-Grasp, a novel Flow-Matching-based framework for physics-aware dexterous grasp generation. Specifically, we reformulate grasp synthesis as a deterministic ordinary differential equation (ODE) process, which enables efficient and stable generation through smooth probability flows. To further enforce physical feasibility, we introduce a training-free physics-aware energy guidance strategy. Our method defines an energy-guided target distribution using adapted explicit physical energy functions that capture key grasp constraints, and estimates the corresponding guidance term via a local Monte Carlo approximation during inference. In this way, EFF-Grasp dynamically steers the generation trajectory toward physically feasible regions without requiring additional physics-based training or simulation feedback. Extensive experiments on five benchmark datasets show that EFF-Grasp achieves superior performance in grasp quality and physical feasibility, while requiring substantially fewer sampling steps than diffusion-based baselines.
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
