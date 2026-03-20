---
title: "Theory and interpretability of Quantum Extreme Learning Machines: a Pauli-transfer matrix approach"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.18377"
published: "2026-03-20"
fetched: "2026-03-20T15:04:11.823105"
---

Quantum Physics
[Submitted on 20 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Theory and interpretability of Quantum Extreme Learning Machines: a Pauli-transfer matrix approach
View PDF HTML (experimental)Abstract:Quantum reservoir computers (QRCs) have emerged as a promising approach to quantum machine learning, since they utilize the natural dynamics of quantum systems for data processing and are simple to train. Here, we consider $n$-qubit quantum extreme learning machines (QELMs) with initial-state encoding and continuous-time reservoir dynamics. QELMs are memoryless QRCs capable of various ML tasks, such as image classification and time series forecasting. We apply the Pauli transfer matrix (PTM) formalism to theoretically analyze the influence of encoding, reservoir dynamics, and measurement operations (including temporal multiplexing) on the QELM performance. This formalism makes explicit that the encoding determines the complete set of (nonlinear) features available to this type of QELM, while the quantum channels linearly transform these features before they are probed by the chosen measurement operators. Optimizing such a QELM can therefore be cast as a decoding problem in which one shapes the channel-induced transformations such that task-relevant features become available to the regressor, effectively reversing the information scrambling of a unitary. We show how operator spreading under unitary evolution determines feature decodability, which underlies the nonlinear processing capacity of the reservoir. The PTM formalism yields a nonlinear vector (auto-)regression model as the classical representation of a QELM. As a specific application, we focus on learning nonlinear dynamical systems and show that a QELM trained on such trajectories learns a surrogate-approximation to the underlying flow map.
Submission history
From: Markus Gross [view email][v1] Fri, 20 Feb 2026 17:33:27 UTC (1,524 KB)
[v2] Wed, 18 Mar 2026 21:55:37 UTC (1,691 KB)
Current browse context:
quant-ph
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
