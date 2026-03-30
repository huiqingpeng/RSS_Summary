---
title: "Optimization Trade-offs in Asynchronous Federated Learning: A Stochastic Networks Approach"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26231"
published: "2026-03-30"
fetched: "2026-03-31T07:22:49.592424"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Optimization Trade-offs in Asynchronous Federated Learning: A Stochastic Networks Approach
View PDFAbstract:Synchronous federated learning scales poorly due to the straggler effect. Asynchronous algorithms increase the update throughput by processing updates upon arrival, but they introduce two fundamental challenges: gradient staleness, which degrades convergence, and bias toward faster clients under heterogeneous data distributions. Although algorithms such as AsyncSGD and Generalized AsyncSGD mitigate this bias via client-side task queues, most existing analyses neglect the underlying queueing dynamics and lack closed-form characterizations of the update throughput and gradient staleness. To close this gap, we develop a stochastic queueing-network framework for Generalized AsyncSGD that jointly models random computation times at the clients and the central server, as well as random uplink and downlink communication delays. Leveraging product-form network theory, we derive a closed-form expression for the update throughput, alongside closed-form upper bounds for both the communication round complexity and the expected wall-clock time required to reach an $\epsilon$-stationary point. These results formally characterize the trade-off between gradient staleness and wall-clock convergence speed. We further extend the framework to quantify energy consumption under stochastic timing, revealing an additional trade-off between convergence speed and energy efficiency. Building on these analytical results, we propose gradient-based optimization strategies to jointly optimize routing and concurrency. Experiments on EMNIST demonstrate reductions of 29%--46% in convergence time and 36%--49% in energy consumption compared to AsyncSGD.
Submission history
From: Celine Comte [view email] [via CCSD proxy][v1] Fri, 27 Mar 2026 09:53:53 UTC (3,781 KB)
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
