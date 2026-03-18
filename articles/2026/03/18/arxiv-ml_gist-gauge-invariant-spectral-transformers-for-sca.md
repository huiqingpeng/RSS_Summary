---
title: "GIST: Gauge-Invariant Spectral Transformers for Scalable Graph Neural Operators"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16849"
published: "2026-03-18"
fetched: "2026-03-18T16:04:10.163952"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:GIST: Gauge-Invariant Spectral Transformers for Scalable Graph Neural Operators
View PDF HTML (experimental)Abstract:Adapting transformer positional encoding to meshes and graph-structured data presents significant computational challenges: exact spectral methods require cubic-complexity eigendecomposition and can inadvertently break gauge invariance through numerical solver artifacts, while efficient approximate methods sacrifice gauge symmetry by design. Both failure modes cause catastrophic generalization in inductive learning, where models trained with one set of numerical choices fail when encountering different spectral decompositions of similar graphs or discretizations of the same mesh. We propose GIST (Gauge-Invariant Spectral Transformers), a new graph transformer architecture that resolves this challenge by achieving end-to-end $\mathcal{O}(N)$ complexity through random projections while algorithmically preserving gauge invariance via inner-product-based attention on the projected embeddings. We prove GIST achieves discretization-invariant learning with bounded mismatch error, enabling parameter transfer across arbitrary mesh resolutions for neural operator applications. Empirically, GIST matches state-of-the-art on standard graph benchmarks (e.g., achieving 99.50% micro-F1 on PPI) while uniquely scaling to mesh-based Neural Operator benchmarks with up to 750K nodes, achieving state-of-the-art aerodynamic prediction on the challenging DrivAerNet and DrivAerNet++ datasets.
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
