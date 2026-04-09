---
title: "A First Guess is Rarely the Final Answer: Learning to Search in the Travelling Salesperson Problem"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06940"
published: "2026-04-09"
fetched: "2026-04-10T07:05:09.927790"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:A First Guess is Rarely the Final Answer: Learning to Search in the Travelling Salesperson Problem
View PDF HTML (experimental)Abstract:Most neural solvers for the Traveling Salesperson Problem (TSP) are trained to output a single solution, even though practitioners rarely stop there: at test time, they routinely spend extra compute on sampling or post-hoc search. This raises a natural question: can the search procedure itself be learned? Neural improvement methods take this perspective by learning a policy that applies local modifications to a candidate solution, accumulating gains over an improvement trajectory. Yet learned improvement for TSP remains comparatively immature, with existing methods still falling short of robust, scalable performance. We argue that a key reason is design mismatch: many approaches reuse state representations, architectural choices, and training recipes inherited from single-solution methods, rather than being built around the mechanics of local search. This mismatch motivates NICO-TSP (Neural Improvement for Combinatorial Optimization): a 2-opt improvement framework for TSP. NICO-TSP represents the current tour with exactly $n$ edge tokens aligned with the neighborhood operator, scores 2-opt moves directly without tour positional encodings, and trains via a two-stage procedure: imitation learning to short-horizon optimal trajectories, followed by critic-free group-based reinforcement learning over longer rollouts. Under compute-matched evaluations that measure improvement as a function of both search steps and wall-clock time, NICO-TSP delivers consistently stronger and markedly more step-efficient improvement than prior learned and heuristic search baselines, generalizes far more reliably to larger out-of-distribution instances, and serves both as a competitive replacement for classical local search and as a powerful test-time refinement module for constructive solvers.
Submission history
From: Andoni Irazusta Garmendia [view email][v1] Wed, 8 Apr 2026 11:04:45 UTC (1,925 KB)
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
