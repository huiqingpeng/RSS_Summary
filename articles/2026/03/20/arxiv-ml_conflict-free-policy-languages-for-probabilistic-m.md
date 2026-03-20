---
title: "Conflict-Free Policy Languages for Probabilistic ML Predicates: A Framework and Case Study with the Semantic Router DSL"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18174"
published: "2026-03-20"
fetched: "2026-03-20T12:08:28.443289"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Conflict-Free Policy Languages for Probabilistic ML Predicates: A Framework and Case Study with the Semantic Router DSL
View PDF HTML (experimental)Abstract:Conflict detection in policy languages is a solved problem -- as long as every rule condition is a crisp Boolean predicate. BDDs, SMT solvers, and NetKAT all exploit that assumption. But a growing class of routing and access-control systems base their decisions on probabilistic ML signals: embedding similarities, domain classifiers, complexity estimators. Two such signals, declared over categories the author intended to be disjoint, can both clear their thresholds on the same query and silently route it to the wrong model. Nothing in the compiler warns about this. We characterize the problem as a three-level decidability hierarchy -- crisp conflicts are decidable via SAT, embedding conflicts reduce to spherical cap intersection, and classifier conflicts are undecidable without distributional knowledge -- and show that for the embedding case, which dominates in practice, replacing independent thresholding with a temperature-scaled softmax partitions the embedding space into Voronoi regions where co-firing is impossible. No model retraining is needed. We implement the detection and prevention mechanisms in the Semantic Router DSL, a production routing language for LLM inference, and discuss how the same ideas apply to semantic RBAC and API gateway policy.
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
