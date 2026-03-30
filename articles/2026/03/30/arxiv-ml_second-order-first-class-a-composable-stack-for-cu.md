---
title: "Second-Order, First-Class: A Composable Stack for Curvature-Aware Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25976"
published: "2026-03-30"
fetched: "2026-03-31T07:20:27.899175"
---

Computer Science > Machine Learning
[Submitted on 26 Mar 2026]
Title:Second-Order, First-Class: A Composable Stack for Curvature-Aware Training
View PDF HTML (experimental)Abstract:Second-order methods promise improved stability and faster convergence, yet they remain underused due to implementation overhead, tuning brittleness, and the lack of composable APIs. We introduce Somax, a composable Optax-native stack that treats curvature-aware training as a single JIT-compiled step governed by a static plan. Somax exposes first-class modules -- curvature operators, estimators, linear solvers, preconditioners, and damping policies -- behind a single step interface and composes with Optax by applying standard gradient transformations (e.g., momentum, weight decay, schedules) to the computed direction. This design makes typically hidden choices explicit and swappable. Somax separates planning from execution: it derives a static plan (including cadences) from module requirements, then runs the step through a specialized execution path that reuses intermediate results across modules. We report system-oriented ablations showing that (i) composition choices materially affect scaling behavior and time-to-accuracy, and (ii) planning reduces per-step overhead relative to unplanned composition with redundant recomputation.
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
