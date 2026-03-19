---
title: "PowerModelsGAT-AI: Physics-Informed Graph Attention for Multi-System Power Flow with Continual Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16879"
published: "2026-03-19"
fetched: "2026-03-19T12:18:48.548297"
---

Electrical Engineering and Systems Science > Systems and Control
[Submitted on 24 Feb 2026]
Title:PowerModelsGAT-AI: Physics-Informed Graph Attention for Multi-System Power Flow with Continual Learning
View PDF HTML (experimental)Abstract:Solving the alternating current power flow equations in real time is essential for secure grid operation, yet classical Newton-Raphson solvers can be slow under stressed conditions. Existing graph neural networks for power flow are typically trained on a single system and often degrade on different systems. We present PowerModelsGAT-AI, a physics-informed graph attention network that predicts bus voltages and generator injections. The model uses bus-type-aware masking to handle different bus types and balances multiple loss terms, including a power-mismatch penalty, using learned weights. We evaluate the model on 14 benchmark systems (4 to 6,470 buses) and train a unified model on 13 of these under N-2 (two-branch outage) conditions, achieving an average normalized mean absolute error of 0.89% for voltage magnitudes and R^2 > 0.99 for voltage angles. We also show continual learning: when adapting a base model to a new 1,354-bus system, standard fine-tuning causes severe forgetting with error increases exceeding 1000% on base systems, while our experience replay and elastic weight consolidation strategy keeps error increases below 2% and in some cases improves base-system performance. Interpretability analysis shows that learned attention weights correlate with physical branch parameters (susceptance: r = 0.38; thermal limits: r = 0.22), and feature importance analysis supports that the model captures established power flow relationships.
Submission history
From: Chidozie Ezeakunne [view email][v1] Tue, 24 Feb 2026 15:29:49 UTC (23,767 KB)
Current browse context:
eess.SY
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
