---
title: "A Scalable Approach to Solving Simulation-Based Network Security Games"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.16564"
published: "2026-03-18"
fetched: "2026-03-18T17:04:23.684924"
---

Computer Science > Machine Learning
[Submitted on 18 Feb 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:A Scalable Approach to Solving Simulation-Based Network Security Games
View PDF HTML (experimental)Abstract:We introduce MetaDOAR, a lightweight meta-controller that augments the Double Oracle / PSRO paradigm with a learned, partition-aware filtering layer and Q-value caching to enable scalable multi-agent reinforcement learning on very large cyber-network environments. MetaDOAR learns a compact state projection from per node structural embeddings to rapidly score and select a small subset of devices (a top-k partition) on which a conventional low-level actor performs focused beam search utilizing a critic agent. Selected candidate actions are evaluated with batched critic forwards and stored in an LRU cache keyed by a quantized state projection and local action identifiers, dramatically reducing redundant critic computation while preserving decision quality via conservative k-hop cache invalidation. Empirically, MetaDOAR attains higher player payoffs than SOTA baselines on large network topologies, without significant scaling issues in terms of memory usage or training time. This contribution provide a practical, theoretically motivated path to efficient hierarchical policy learning for large-scale networked decision problems.
Submission history
From: Michael Lanier [view email][v1] Wed, 18 Feb 2026 16:07:01 UTC (603 KB)
[v2] Tue, 17 Mar 2026 14:41:01 UTC (601 KB)
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
