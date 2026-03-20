---
title: "ARTEMIS: A Neuro Symbolic Framework for Economically Constrained Market Dynamics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18107"
published: "2026-03-20"
fetched: "2026-03-20T12:07:34.481380"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:ARTEMIS: A Neuro Symbolic Framework for Economically Constrained Market Dynamics
View PDF HTML (experimental)Abstract:Deep learning models in quantitative finance often operate as black boxes, lacking interpretability and failing to incorporate fundamental economic principles such as no-arbitrage constraints. This paper introduces ARTEMIS (Arbitrage-free Representation Through Economic Models and Interpretable Symbolics), a novel neuro-symbolic framework combining a continuous-time Laplace Neural Operator encoder, a neural stochastic differential equation regularised by physics-informed losses, and a differentiable symbolic bottleneck that distils interpretable trading rules. The model enforces economic plausibility via two novel regularisation terms: a Feynman-Kac PDE residual penalising local no-arbitrage violations, and a market price of risk penalty bounding the instantaneous Sharpe ratio. We evaluate ARTEMIS against six strong baselines on four datasets: Jane Street, Optiver, Time-IMM, and DSLOB (a synthetic crash regime). Results demonstrate ARTEMIS achieves state-of-the-art directional accuracy, outperforming all baselines on DSLOB (64.96%) and Time-IMM (96.0%). A comprehensive ablation study confirms each component's contribution: removing the PDE loss reduces directional accuracy from 64.89% to 50.32%. Underperformance on Optiver is attributed to its long sequence length and volatility-focused target. By providing interpretable, economically grounded predictions, ARTEMIS bridges the gap between deep learning's power and the transparency demanded in quantitative finance.
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
