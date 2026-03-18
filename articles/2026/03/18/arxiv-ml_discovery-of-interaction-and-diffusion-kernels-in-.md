---
title: "Discovery of interaction and diffusion kernels in particle-to-mean-field multi-agent systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15927"
published: "2026-03-18"
fetched: "2026-03-18T15:37:59.823533"
---

Computer Science > Machine Learning
[Submitted on 16 Mar 2026]
Title:Discovery of interaction and diffusion kernels in particle-to-mean-field multi-agent systems
View PDF HTML (experimental)Abstract:We propose a data-driven framework to learn interaction kernels in stochastic multi-agent systems. Our approach aims at identifying the functional form of nonlocal interaction and diffusion terms directly from trajectory data, without any a priori knowledge of the underlying interaction structure. Starting from a discrete stochastic binary-interaction model, we formulate the inverse problem as a sequence of sparse regression tasks in structured finite-dimensional spaces spanned by compactly supported basis functions, such as piecewise linear polynomials. In particular, we assume that pairwise interactions between agents are not directly observed and that only limited trajectory data are available. To address these challenges, we propose two complementary identification strategies. The first based on random-batch sampling, which compensates for latent interactions while preserving the statistical structure of the full dynamics in expectation. The second based on a mean-field approximation, where the empirical particle density reconstructed from the data defines a continuous nonlocal regression problem. Numerical experiments demonstrate the effectiveness and robustness of the proposed framework, showing accurate reconstruction of both interaction and diffusion kernels even from partially observed. The method is validated on benchmark models, including bounded-confidence and attraction-repulsion dynamics, where the two proposed strategies achieve comparable levels of accuracy.
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
