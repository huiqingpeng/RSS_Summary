---
title: "Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17112"
published: "2026-03-19"
fetched: "2026-03-19T13:09:20.563223"
---

Computer Science > Artificial Intelligence
[Submitted on 17 Mar 2026]
Title:Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching
View PDF HTML (experimental)Abstract:A common architectural pattern in advanced AI reasoning systems is the symbolic graph network: specialized agents or modules connected by delegation edges, routing tasks through a dynamic execution graph. Current schedulers optimize load and fitness but are geometry-blind: they do not model how failures propagate differently in tree-like versus cyclic regimes. In tree-like delegation, a single failure can cascade exponentially; in dense cyclic graphs, failures tend to self-limit. We identify this observability gap, quantify its system-level cost, and propose a lightweight mitigation.
We formulate online geometry control for route-risk estimation on time-indexed execution graphs with route-local failure history. Our approach combines (i) a Euclidean spatio-temporal propagation baseline, (ii) a hyperbolic route-risk model with temporal decay (and optional burst excitation), and (iii) a learned geometry selector over structural features. The selector is a compact MLP (9->12->1) using six topology statistics plus three geometry-aware signals: BFS shell-growth slope, cycle-rank norm, and fitted Poincare curvature. On the Genesis 3 benchmark distribution, adaptive switching improves win rate in the hardest non_tree regime from 64-72% (fixed hyperbolic variants) to 92%, and achieves 87.2% overall win rate.
To measure total system value, we compare against Genesis 3 routing without any spatio-temporal sidecar, using only native bandit/LinUCB signals (team fitness and mean node load). This baseline achieves 50.4% win rate overall and 20% in tree-like regimes; the full sidecar recovers 87.2% overall (+36.8 pp), with +48 to +68 pp gains in tree-like settings, consistent with a cascade-sensitivity analysis. Overall, a 133-parameter sidecar substantially mitigates geometry-blind failure propagation in one high-capability execution-graph system.
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
