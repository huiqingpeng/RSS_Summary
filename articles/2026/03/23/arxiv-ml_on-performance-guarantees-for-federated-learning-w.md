---
title: "On Performance Guarantees for Federated Learning with Personalized Constraints"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19617"
published: "2026-03-23"
fetched: "2026-03-24T07:20:02.147174"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:On Performance Guarantees for Federated Learning with Personalized Constraints
View PDF HTML (experimental)Abstract:Federated learning (FL) has emerged as a communication-efficient algorithmic framework for distributed learning across multiple agents. While standard FL formulations capture unconstrained or globally constrained problems, many practical settings involve heterogeneous resource or model constraints, leading to optimization problems with agent-specific feasible sets. Here, we study a personalized constrained federated optimization problem in which each agent is associated with a convex local objective and a private constraint set. We propose PC-FedAvg, a method in which each agent maintains cross-estimates of the other agents' variables through a multi-block local decision vector. Each agent updates all blocks locally, penalizing infeasibility only in its own block. Moreover, the cross-estimate mechanism enables personalization without requiring consensus or sharing constraint information among agents. We establish communication-complexity rates of $\mathcal{O}(\epsilon^{-2})$ for suboptimality and $\mathcal{O}(\epsilon^{-1})$ for agent-wise infeasibility. Preliminary experiments on the MNIST and CIFAR-10 datasets validate our theoretical findings.
Submission history
From: Mohammadjavad Ebrahimi [view email][v1] Fri, 20 Mar 2026 03:49:28 UTC (221 KB)
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
