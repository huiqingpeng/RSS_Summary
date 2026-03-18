---
title: "Shuffling the Stochastic Mirror Descent via Dual Lipschitz Continuity and Kernel Conditioning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16042"
published: "2026-03-18"
fetched: "2026-03-18T16:09:40.383413"
---

Mathematics > Optimization and Control
[Submitted on 17 Mar 2026]
Title:Shuffling the Stochastic Mirror Descent via Dual Lipschitz Continuity and Kernel Conditioning
View PDF HTML (experimental)Abstract:The global Lipschitz smoothness condition underlies most convergence and complexity analyses via two key consequences: the descent lemma and the gradient Lipschitz continuity. How to study the performance of optimization algorithms in the absence of Lipschitz smoothness remains an active area. The relative smoothness framework from Bauschke-Bolte-Teboulle (2017) and Lu-Freund-Nesterov (2018) provides an extended descent lemma, ensuring convergence of Bregman-based proximal gradient methods and their vanilla stochastic counterparts. However, many widely used techniques (e.g., momentum schemes, random reshuffling, and variance reduction) additionally require the Lipschitz-type bound for gradient deviations, leaving their analysis under relative smoothness an open area. To resolve this issue, we introduce the dual kernel conditioning (DKC) regularity condition to regulate the local relative curvature of the kernel functions. Combined with the relative smoothness, DKC provides a dual Lipschitz continuity for gradients: even though the gradient mapping is not Lipschitz in the primal space, it preserves Lipschitz continuity in the dual space induced by a mirror map. We verify that DKC is widely satisfied by popular kernels and is closed under affine composition and conic combination. With these novel tools, we establish the first complexity bounds as well as the iterate convergence of random reshuffling mirror descent for constrained nonconvex relative smooth problems.
Current browse context:
math.OC
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
