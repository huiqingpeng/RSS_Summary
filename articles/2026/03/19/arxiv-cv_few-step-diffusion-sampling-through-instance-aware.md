---
title: "Few-Step Diffusion Sampling Through Instance-Aware Discretizations"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17671"
published: "2026-03-19"
fetched: "2026-03-19T15:15:37.893203"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 18 Mar 2026]
Title:Few-Step Diffusion Sampling Through Instance-Aware Discretizations
View PDF HTML (experimental)Abstract:Diffusion and flow matching models generate high-fidelity data by simulating paths defined by Ordinary or Stochastic Differential Equations (ODEs/SDEs), starting from a tractable prior distribution. The probability flow ODE formulation enables the use of advanced numerical solvers to accelerate sampling. Orthogonal yet vital to solver design is the discretization strategy. While early approaches employed handcrafted heuristics and recent methods adopt optimization-based techniques, most existing strategies enforce a globally shared timestep schedule across all samples. This uniform treatment fails to account for instance-specific complexity in the generative process, potentially limiting performance. Motivated by controlled experiments on synthetic data, which reveals the suboptimality of global schedules under instance-specific dynamics, we propose an instance-aware discretization framework. Our method learns to adapt timestep allocations based on input-dependent priors, extending gradient-based discretization search to the conditional generative setting. Empirical results across diverse settings, including synthetic data, pixel-space diffusion, latent-space images and video flow matching models, demonstrate that our method consistently improves generation quality with marginal tuning cost compared to training and negligible inference overhead.
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
