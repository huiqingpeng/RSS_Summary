---
title: "ARCS: Autoregressive Circuit Synthesis with Topology-Aware Graph Attention and Spec Conditioning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29068"
published: "2026-04-01"
fetched: "2026-04-02T07:14:47.189321"
---

Computer Science > Machine Learning
[Submitted on 30 Mar 2026]
Title:ARCS: Autoregressive Circuit Synthesis with Topology-Aware Graph Attention and Spec Conditioning
View PDF HTML (experimental)Abstract:I present ARCS, a system for amortized analog circuit generation that produces complete, SPICE-simulatable designs (topology and component values) in milliseconds rather than the minutes required by search-based methods. A hybrid pipeline combining two learned generators (a graph VAE and a flow-matching model) with SPICE-based ranking achieves 99.9% simulation validity (reward 6.43/8.0) across 32 topologies using only 8 SPICE evaluations, 40x fewer than genetic algorithms. For single-model inference, a topology-aware Graph Transformer with Best-of-3 candidate selection reaches 85% simulation validity in 97ms, over 600x faster than random search. The key technical contribution is Group Relative Policy Optimization (GRPO): I identify a critical failure mode of REINFORCE (cross-topology reward distribution mismatch) and resolve it with per-topology advantage normalization, improving simulation validity by +9.6pp over REINFORCE in only 500 RL steps (10x fewer). Grammar-constrained decoding additionally guarantees 100% structural validity by construction via topology-aware token masking. ARCS does not yet match the per-design quality of search-based optimization (5.48 vs. 7.48 reward), but its >1000x speed advantage enables rapid prototyping, design-space exploration, and warm-starting search methods (recovering 96.6% of GA quality with 49% fewer simulations).
Submission history
From: Tushar Dhananjay Pathak [view email][v1] Mon, 30 Mar 2026 23:14:08 UTC (26 KB)
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
