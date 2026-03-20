---
title: "Neural Networks as Local-to-Global Computations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14831"
published: "2026-03-20"
fetched: "2026-03-20T15:05:11.886764"
---

Mathematics > Algebraic Topology
[Submitted on 16 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Neural Networks as Local-to-Global Computations
View PDFAbstract:We construct a cellular sheaf from any feedforward ReLU neural network by placing one vertex for each intermediate quantity in the forward pass and encoding each computational step - affine transformation, activation, output - as a restriction map on an edge. The restricted coboundary operator on the free coordinates is unitriangular, so its determinant is $1$ and the restricted Laplacian is positive definite for every activation pattern. It follows that the relative cohomology vanishes and the forward pass output is the unique harmonic extension of the boundary data. The sheaf heat equation converges exponentially to this output despite the state-dependent switching introduced by piecewise linear activations. Unlike the forward pass, the heat equation propagates information bidirectionally across layers, enabling pinned neurons that impose constraints in both directions, training through local discrepancy minimization without a backward pass, and per-edge diagnostics that decompose network behavior by layer and operation type. We validate the framework experimentally on small synthetic tasks, confirming the convergence theorems and demonstrating that sheaf-based training, while not yet competitive with stochastic gradient descent, obeys quantitative scaling laws predicted by the theory.
Submission history
From: Vicente Bosca [view email][v1] Mon, 16 Mar 2026 05:23:31 UTC (2,874 KB)
[v2] Thu, 19 Mar 2026 01:33:04 UTC (2,874 KB)
Current browse context:
math.AT
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
