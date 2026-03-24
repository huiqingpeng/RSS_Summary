---
title: "Joint Surrogate Learning of Objectives, Constraints, and Sensitivities for Efficient Multi-objective Optimization of Neural Dynamical Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20984"
published: "2026-03-24"
fetched: "2026-03-25T07:17:01.208293"
---

Computer Science > Machine Learning
[Submitted on 22 Mar 2026]
Title:Joint Surrogate Learning of Objectives, Constraints, and Sensitivities for Efficient Multi-objective Optimization of Neural Dynamical Systems
View PDF HTML (experimental)Abstract:Biophysical neural system simulations are among the most computationally demanding scientific applications, and their optimization requires navigating high-dimensional parameter spaces under numerous constraints that impose a binary feasible/infeasible partition with no gradient signal to guide the search. Here, we introduce DMOSOPT, a scalable optimization framework that leverages a unified, jointly learned surrogate model to capture the interplay between objectives, constraints, and parameter sensitivities. By learning a smooth approximation of both the objective landscape and the feasibility boundary, the joint surrogate provides a unified gradient that simultaneously steers the search toward improved objective values and greater constraint satisfaction, while its partial derivatives yield per-parameter sensitivity estimates that enable more targeted exploration. We validate the framework from single-cell dynamics to population-level network activity, spanning incremental stages of a neural circuit modeling workflow, and demonstrate efficient, effective optimization of highly constrained problems at supercomputing scale with substantially fewer problem evaluations. While motivated by and demonstrated in the context of computational neuroscience, the framework is general and applicable to constrained multi-objective optimization problems across scientific and engineering domains.
Submission history
From: Frithjof Gressmann [view email][v1] Sun, 22 Mar 2026 00:06:28 UTC (7,409 KB)
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
