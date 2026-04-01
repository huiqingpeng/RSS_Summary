---
title: "Differentiable Initialization-Accelerated CPU-GPU Hybrid Combinatorial Scheduling"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28943"
published: "2026-04-01"
fetched: "2026-04-02T07:11:34.180032"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:Differentiable Initialization-Accelerated CPU-GPU Hybrid Combinatorial Scheduling
View PDF HTML (experimental)Abstract:This paper presents a hybrid CPU-GPU framework for solving combinatorial scheduling problems formulated as Integer Linear Programming (ILP). While scheduling underpins many optimization tasks in computing systems, solving these problems optimally at scale remains a long-standing challenge due to their NP-hard nature. We introduce a novel approach that combines differentiable optimization with classical ILP solving. Specifically, we utilize differentiable presolving to rapidly generate high-quality partial solutions, which serve as warm-starts for commercial ILP solvers (CPLEX, Gurobi) and rising open-source solver HiGHS. This method enables significantly improved early pruning compared to state-of-the-art standalone solvers. Empirical results across industry-scale benchmarks demonstrate up to a $10\times$ performance gain over baselines, narrowing the optimality gap to $<0.1\%$. This work represents the first demonstration of utilizing differentiable optimization to initialize exact ILP solvers for combinatorial scheduling, opening new opportunities to integrate machine learning infrastructure with classical exact optimization methods across broader domains.
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
