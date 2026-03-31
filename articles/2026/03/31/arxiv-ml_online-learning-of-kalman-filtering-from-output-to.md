---
title: "Online Learning of Kalman Filtering: From Output to State Estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27159"
published: "2026-03-31"
fetched: "2026-04-01T07:22:26.062382"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Online Learning of Kalman Filtering: From Output to State Estimation
View PDF HTML (experimental)Abstract:In this paper, we study the problem of learning Kalman filtering with unknown system model in partially observed linear dynamical systems. We propose a unified algorithmic framework based on online optimization that can be used to solve both the output estimation and state estimation scenarios. By exploring the properties of the estimation error cost functions, such as conditionally strong convexity, we show that our algorithm achieves a $\log T$-regret in the horizon length $T$ for the output estimation scenario. More importantly, we tackle the more challenging scenario of learning Kalman filtering for state estimation, which is an open problem in the literature. We first characterize a fundamental limitation of the problem, demonstrating the impossibility of any algorithm to achieve sublinear regret in $T$. By further introducing a random query scheme into our algorithm, we show that a $\sqrt{T}$-regret is achievable when rendering the algorithm limited query access to more informative measurements of the system state in practice. Our algorithm and regret readily capture the trade-off between the number of queries and the achieved regret, and shed light on online learning problems with limited observations. We validate the performance of our algorithms using numerical examples.
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
