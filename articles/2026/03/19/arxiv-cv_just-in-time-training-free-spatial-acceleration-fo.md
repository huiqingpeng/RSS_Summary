---
title: "Just-in-Time: Training-Free Spatial Acceleration for Diffusion Transformers"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.10744"
published: "2026-03-19"
fetched: "2026-03-19T16:32:18.475756"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 11 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Just-in-Time: Training-Free Spatial Acceleration for Diffusion Transformers
View PDF HTML (experimental)Abstract:Diffusion Transformers have established a new state-of-the-art in image synthesis, but the high computational cost of iterative sampling severely hampers their practical deployment. While existing acceleration methods often focus on the temporal domain, they overlook the substantial spatial redundancy inherent in the generative process, where global structures emerge long before fine-grained details are formed. The uniform computational treatment of all spatial regions represents a critical inefficiency. In this paper, we introduce Just-in-Time (JiT), a novel training-free framework that addresses this challenge by acceleration in the spatial domain. JiT formulates a spatially approximated generative ordinary differential equation (ODE) that drives the full latent state evolution based on computations from a dynamically selected, sparse subset of anchor tokens. To ensure seamless transitions as new tokens are incorporated to expand the dimensions of the latent state, we propose a deterministic micro-flow, a simple and effective finite-time ODE that maintains both structural coherence and statistical correctness. Extensive experiments on the state-of-the-art FLUX.1-dev model demonstrate that JiT achieves up to a 7x speedup with nearly lossless performance, significantly outperforming existing acceleration methods and establishing a new and superior trade-off between inference speed and generation fidelity.
Submission history
From: Wenhao Sun [view email][v1] Wed, 11 Mar 2026 13:16:41 UTC (40,209 KB)
[v2] Wed, 18 Mar 2026 13:10:33 UTC (40,210 KB)
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
