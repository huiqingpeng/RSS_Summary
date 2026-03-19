---
title: "Overcoming Barren Plateaus in Variational Quantum Circuits using a Two-Step Least Squares Approach"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2601.18060"
published: "2026-03-19"
fetched: "2026-03-19T17:08:00.609503"
---

Quantum Physics
[Submitted on 26 Jan 2026 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Overcoming Barren Plateaus in Variational Quantum Circuits using a Two-Step Least Squares Approach
View PDF HTML (experimental)Abstract:Variational Quantum Algorithms are a vital part of quantum computing. It is a blend of quantum and classical methods for tackling tough problems in machine learning, chemistry, and combinatorial optimization. Yet as these algorithms scale up, they cannot escape the barren-plateau phenomenon. As systems grow, gradients can vanish so quickly that training deep or randomly initialized circuits becomes nearly impossible. To overcome the barren plateau problem, we introduce a two-stage optimization framework. First comes the convex initialization stage. Here, we shape the quantum energy landscape, the Hilmaton landscape, into a smooth, low-energy basin. This step makes gradients easier to spot and keeps noise from derailing the process. Once we have gotten a stable gradient flow, we move to the second stage: nonconvex refinement. In this phase, we let the algorithm wander through different energy minima, making the model more expressive. We show that our proposed algorithm theoretically reduces the dependence on the condition number of the underlying quantum least squares approximate matrix via Riemannian manifold optimization. Finally, we used our two-stage solution to perform quantum cryptanalysis of quantum key distribution protocol (i.e., BB84) to determine the optimal cloning strategies. The simulation results showed that our proposed two-stage solution outperforms its random initialization counterpart.
Submission history
From: Samuel Asante Gyamerah [view email][v1] Mon, 26 Jan 2026 01:29:02 UTC (246 KB)
[v2] Mon, 16 Feb 2026 18:40:23 UTC (243 KB)
[v3] Tue, 17 Mar 2026 21:07:05 UTC (250 KB)
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
