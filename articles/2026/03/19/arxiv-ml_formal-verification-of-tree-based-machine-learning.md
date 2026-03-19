---
title: "Formal verification of tree-based machine learning models for lateral spreading"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16983"
published: "2026-03-19"
fetched: "2026-03-19T12:06:14.074923"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Formal verification of tree-based machine learning models for lateral spreading
View PDF HTML (experimental)Abstract:Machine learning models for geotechnical hazard prediction can achieve high accuracy while learning physically inconsistent relationships from sparse or biased training data. Current remedies (post-hoc explainability, such as SHAP and LIME, and training-time constraints) either diagnose individual predictions approximately or restrict model capacity without providing exhaustive guarantees. This paper encodes trained tree ensembles as logical formulas in a Satisfiability Modulo Theories (SMT) solver and checks physical specifications across the entire input domain, not just sampled points. Four geotechnical specifications (water table depth, PGA monotonicity, distance safety, and flat-ground safety) are formalized as decidable logical formulas and verified via SMT against both XGBoost ensembles and Explainable Boosting Machines (EBMs) trained on the 2011 Christchurch earthquake lateral spreading dataset (7,291 sites, four features). The SMT solver either produces a concrete counterexample where a specification fails or proves that no violation exists. The unconstrained EBM (80.1% accuracy) violates all four specifications. A fully constrained EBM (67.2%) satisfies three of four specifications, demonstrating that iterative constraint application guided by verification can progressively improve physical consistency. A Pareto analysis of 33 model variants reveals a persistent trade-off, as none of the variants studied achieve both greater than 80% accuracy and full compliance with the specified set. SHAP analysis of specification counterexamples shows that the offending feature can rank last, demonstrating that post-hoc explanations do not substitute for formal verification. These results establish a verify-fix-verify engineering loop and a formal certification for deploying physically consistent ML models in safety-critical geotechnical applications.
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
