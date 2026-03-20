---
title: "Vector Optimization with Gaussian Process Bandits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2412.02484"
published: "2026-03-20"
fetched: "2026-03-20T14:05:03.707574"
---

Computer Science > Machine Learning
[Submitted on 3 Dec 2024 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Vector Optimization with Gaussian Process Bandits
View PDF HTML (experimental)Abstract:We study black-box vector optimization with Gaussian process bandits, where there is an incomplete order relation on objective vectors described by a polyhedral convex cone. Existing black-box vector optimization approaches either suffer from high sample complexity or lack theoretical guarantees. We propose Vector Optimization with Gaussian Process (VOGP), an adaptive elimination algorithm that identifies Pareto optimal solutions sample efficiently by exploiting the smoothness of the objective function. We establish theoretical guarantees, deriving information gain-based and kernel-specific sample complexity bounds. Finally, we conduct a thorough empirical evaluation of VOGP and compare it with the state-of-the-art multi-objective and vector optimization algorithms on several real-world and synthetic datasets, emphasizing VOGP's efficiency (e.g., $\sim18\times$ lower sample complexity on average). We also provide heuristic adaptations of VOGP for cases where the design space is continuous and where the Gaussian process model lacks access to the true kernel hyperparameters. This work opens a new frontier in sample-efficient multi-objective black-box optimization by incorporating preference structures while maintaining theoretical guarantees and practical efficiency.
Submission history
From: İlter Onat Korkmaz [view email][v1] Tue, 3 Dec 2024 14:47:46 UTC (623 KB)
[v2] Wed, 18 Mar 2026 19:03:13 UTC (1,202 KB)
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
