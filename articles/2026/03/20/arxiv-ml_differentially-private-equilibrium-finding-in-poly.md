---
title: "Differentially Private Equilibrium Finding in Polymatrix Games"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2503.09538"
published: "2026-03-20"
fetched: "2026-03-20T14:14:52.872655"
---

Computer Science > Computer Science and Game Theory
[Submitted on 12 Mar 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Differentially Private Equilibrium Finding in Polymatrix Games
View PDF HTML (experimental)Abstract:We study equilibrium finding in polymatrix games under differential privacy constraints. Prior work in this area fails to achieve both high-accuracy equilibria and a low privacy budget. To better understand the fundamental limitations of differential privacy in games, we show hardness results establishing that no algorithm can simultaneously obtain high accuracy and a vanishing privacy budget as the number of players tends to infinity. This impossibility holds in two regimes: (i) We seek to establish equilibrium approximation guarantees in terms of Euclidean \emph{distance} to the equilibrium set, and (ii) The adversary has access to all communication channels. We then consider the more realistic setting in which the adversary can access only a bounded number of channels and propose a new distributed algorithm that: recovers strategies with simultaneously vanishing \emph{Nash gap} (in expected utility, also referred to as \emph{exploitability}) and \emph{privacy budget} as the number of players increases. Our approach leverages structural properties of polymatrix games. To our knowledge, this is the first paper that can achieve this in equilibrium computation. Finally, we also provide numerical results to justify our algorithm.
Submission history
From: Mingyang Liu [view email][v1] Wed, 12 Mar 2025 16:54:23 UTC (178 KB)
[v2] Wed, 18 Mar 2026 19:40:30 UTC (607 KB)
Current browse context:
cs.GT
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
