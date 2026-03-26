---
title: "Boost Like a (Var)Pro: Trust-Region Gradient Boosting via Variable Projection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23658"
published: "2026-03-26"
fetched: "2026-03-27T07:16:15.443811"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Boost Like a (Var)Pro: Trust-Region Gradient Boosting via Variable Projection
View PDFAbstract:Gradient boosting, a method of building additive ensembles from weak learners, has established itself as a practical and theoretically-motivated approach to approximate functions, especially using decision tree weak learners. Comparable methods for smooth parametric learners, such as neural networks, remain less developed in both training methodology and theory. To this end, we introduce \texttt{VPBoost} ({\bf V}ariable {\bf P}rojection {\bf Boost}ing), a gradient boosting algorithm for separable smooth approximators, i.e., models with a smooth nonlinear featurizer followed by a final linear mapping. \texttt{VPBoost} fuses variable projection, a training paradigm for separable models that enforces optimality of the linear weights, with a second-order weak learning strategy. The combination of second-order boosting, separable models, and variable projection give rise to a closed-form solution for the optimal linear weights and a natural interpretation of \VPBoost as a functional trust-region method. We thereby leverage trust-region theory to prove \VPBoost converges to a stationary point under mild geometric conditions and, under stronger assumptions, achieves a superlinear convergence rate. Comprehensive numerical experiments on synthetic data, image recognition, and scientific machine learning benchmarks demonstrate that \VPBoost learns an ensemble with improved evaluation metrics in comparison to gradient-descent-based boosting and attains competitive performance relative to an industry-standard decision tree boosting algorithm.
Submission history
From: Abhijit Chowdhary [view email][v1] Tue, 24 Mar 2026 19:01:07 UTC (2,649 KB)
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
