---
title: "Rethinking Vector Field Learning for Generative Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19218"
published: "2026-03-20"
fetched: "2026-03-20T16:06:03.099774"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 19 Mar 2026]
Title:Rethinking Vector Field Learning for Generative Segmentation
View PDF HTML (experimental)Abstract:Taming diffusion models for generative segmentation has attracted increasing attention. While existing approaches primarily focus on architectural tweaks or training heuristics, there remains a limited understanding of the intrinsic mismatch between continuous flow matching objectives and discrete perception tasks. In this work, we revisit diffusion segmentation from the perspective of vector field learning. We identify two key limitations of the commonly used flow matching objective: gradient vanishing and trajectory traversing, which result in slow convergence and poor class separation. To tackle these issues, we propose a principled vector field reshaping strategy that augments the learned velocity field with a detached distance-aware correction term. This correction introduces both attractive and repulsive interactions, enhancing gradient magnitudes near centroids while preserving the original diffusion training framework. Furthermore, we design a computationally efficient, quasi-random category encoding scheme inspired by Kronecker sequences, which integrates seamlessly with an end-to-end pixel neural field framework for pixel-level semantic alignment. Extensive experiments consistently demonstrate significant improvements over vanilla flow matching approaches, substantially narrowing the performance gap between generative segmentation and strong discriminative specialists.
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
