---
title: "A Theoretical Framework for Energy-Aware Gradient Pruning in Federated Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22465"
published: "2026-03-25"
fetched: "2026-03-26T07:14:50.448251"
---

Computer Science > Machine Learning
[Submitted on 23 Mar 2026]
Title:A Theoretical Framework for Energy-Aware Gradient Pruning in Federated Learning
View PDF HTML (experimental)Abstract:Federated Learning (FL) is constrained by the communication and energy limitations of decentralized edge devices. While gradient sparsification via Top-K magnitude pruning effectively reduces the communication payload, it remains inherently energy-agnostic. It assumes all parameter updates incur identical downstream transmission and memory-update costs, ignoring hardware realities. We formalize the pruning process as an energy-constrained projection problem that accounts for the hardware-level disparities between memory-intensive and compute-efficient operations during the post-backpropagation phase. We propose Cost-Weighted Magnitude Pruning (CWMP), a selection rule that prioritizes parameter updates based on their magnitude relative to their physical cost. We demonstrate that CWMP is the optimal greedy solution to this constrained projection and provide a probabilistic analysis of its global energy efficiency. Numerical results on a non-IID CIFAR-10 benchmark show that CWMP consistently establishes a superior performance-energy Pareto frontier compared to the Top-K baseline.
Submission history
From: Emmanouil M. Athanasakos [view email][v1] Mon, 23 Mar 2026 18:31:07 UTC (114 KB)
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
