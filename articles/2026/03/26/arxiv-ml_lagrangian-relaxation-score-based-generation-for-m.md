---
title: "Lagrangian Relaxation Score-based Generation for Mixed Integer linear Programming"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24033"
published: "2026-03-26"
fetched: "2026-03-27T07:19:51.048854"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Lagrangian Relaxation Score-based Generation for Mixed Integer linear Programming
View PDF HTML (experimental)Abstract:Predict-and-search (PaS) methods have shown promise for accelerating mixed-integer linear programming (MILP) solving. However, existing approaches typically assume variable independence and rely on deterministic single-point predictions, which limits solution diversityand often necessitates extensive downstream search for high-quality solutions. In this paper, we propose \textbf{SRG}, a generative framework based on Lagrangian relaxation-guided stochastic differential equations (SDEs), with theoretical guarantees on solution quality. SRG leverages convolutional kernels to capture inter-variable dependencies while integrating Lagrangian relaxation to guide the sampling process toward feasible and near-optimal regions. Rather than producing a single estimate, SRG generates diverse, high-quality solution candidates that collectively define compact and effective trust-region subproblems for standard MILP solvers. Across multiple public benchmarks, SRG consistently outperforms existing machine learning baselines in solution quality. Moreover, SRG demonstrates strong zero-shot transferability: on unseen cross-scale/problem instances, it achieves competitive optimality with state-of-the-art exact solvers while significantly reducing computational overhead through faster search and superior solution quality.
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
