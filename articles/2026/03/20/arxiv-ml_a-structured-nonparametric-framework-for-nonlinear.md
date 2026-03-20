---
title: "A Structured Nonparametric Framework for Nonlinear Accelerated Failure Time Models (KAN-AFT)"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.20305"
published: "2026-03-20"
fetched: "2026-03-20T14:17:47.234553"
---

Statistics > Machine Learning
[Submitted on 23 Dec 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:A Structured Nonparametric Framework for Nonlinear Accelerated Failure Time Models (KAN-AFT)
View PDF HTML (experimental)Abstract:Accelerated failure time (AFT) models provide a direct and interpretable time-scale description of covariate effects in lifetime data analysis, but classical formulations rely on linear predictors and are therefore limited in their ability to represent nonlinear relationships. Moreover, in heterogeneous clinical settings with complex covariate structures and varying censoring mechanisms, standard survival models such as the Cox proportional hazards model or AFT formulations may be inadequate due to restrictive structural assumptions.
We propose a structured nonparametric extension of the AFT framework in which the regression function governing log-survival time is an unknown smooth function represented through Kolmogorov--Arnold representations. We formalize the nonlinear AFT estimand under independent right-censoring and show that the proposed function class strictly contains the classical linear AFT model as a special case. Estimation is carried out through a unified framework that accommodates several censoring-adjusted losses such as Buckley--James, inverse probability of censoring weight and transformation methods. Structural regularization and pruning promote parsimony, and symbolic approximation yields analytic representations of learned component functions. Simulation studies show that the method recovers linear structure when appropriate and captures nonlinear effects when present. Applications to multiple clinical datasets demonstrate competitive predictive performance and transparent covariate-effect estimation.
Submission history
From: Kattumannil Sudheesh Dr [view email][v1] Tue, 23 Dec 2025 12:16:06 UTC (79 KB)
[v2] Wed, 18 Mar 2026 04:27:24 UTC (927 KB)
Current browse context:
stat.ML
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
