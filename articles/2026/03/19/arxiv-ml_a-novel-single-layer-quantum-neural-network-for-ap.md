---
title: "A Novel Single-Layer Quantum Neural Network for Approximate SRBB-Based Unitary Synthesis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2412.03083"
published: "2026-03-19"
fetched: "2026-03-19T14:14:24.195271"
---

Quantum Physics
[Submitted on 4 Dec 2024 (v1), last revised 18 Mar 2026 (this version, v4)]
Title:A Novel Single-Layer Quantum Neural Network for Approximate SRBB-Based Unitary Synthesis
View PDFAbstract:In this work, a novel quantum neural network is introduced as a means to approximate any unitary evolution through the Standard Recursive Block Basis (SRBB) and is subsequently redesigned with the number of CNOTs asymptotically reduced by an exponential contribution. This algebraic approach to the problem of unitary synthesis exploits Lie algebras and their topological features to obtain scalable parameterizations of unitary operators. First, the original SRBB-based scalability scheme, already known in the literature only from a theoretical point of view, is reformulated for efficient algorithm implementation and complexity management. Remarkably, 2-qubit operators emerge as a special case of the original scaling scheme. Furthermore, an algorithm is proposed to reduce the number of CNOT gates in the scalable variational quantum circuit, thus deriving a new implementable scaling scheme that requires only one layer of approximation. The single layer CNOT-reduced quantum neural network is implemented, and its performance is assessed with a variety of different unitary matrices, both sparse and dense, up to 6 qubits via the PennyLane library. The effectiveness of the approximation is measured with different metrics in relation to two optimizers: a gradient-based method and the Nelder-Mead method. The approximate CNOT-reduced SRBB-based synthesis algorithm is also tested on real hardware and compared with other valid approximation and decomposition methods available in the literature.
Submission history
From: Marco Mordacci [view email][v1] Wed, 4 Dec 2024 07:21:23 UTC (65 KB)
[v2] Thu, 26 Jun 2025 14:43:45 UTC (62 KB)
[v3] Wed, 11 Mar 2026 09:01:06 UTC (77 KB)
[v4] Wed, 18 Mar 2026 13:32:35 UTC (80 KB)
Current browse context:
quant-ph
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
