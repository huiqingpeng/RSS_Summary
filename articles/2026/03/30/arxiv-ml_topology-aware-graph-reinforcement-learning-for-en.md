---
title: "Topology-Aware Graph Reinforcement Learning for Energy Storage Systems Optimal Dispatch in Distribution Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26264"
published: "2026-03-30"
fetched: "2026-03-31T07:23:16.523985"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Topology-Aware Graph Reinforcement Learning for Energy Storage Systems Optimal Dispatch in Distribution Networks
View PDF HTML (experimental)Abstract:Optimal dispatch of energy storage systems (ESSs) in distribution networks involves jointly improving operating economy and voltage security under time-varying conditions and possible topology changes. To support fast online decision making, we develop a topology-aware Reinforcement Learning architecture based on Twin Delayed Deep Deterministic Policy Gradient (TD3), which integrates graph neural networks (GNNs) as graph feature encoders for ESS dispatch. We conduct a systematic investigation of three GNN variants: graph convolutional networks (GCNs), topology adaptive graph convolutional networks (TAGConv), and graph attention networks (GATs) on the 34-bus and 69-bus systems, and evaluate robustness under multiple topology reconfiguration cases as well as cross-system transfer between networks with different system sizes. Results show that GNN-based controllers consistently reduce the number and magnitude of voltage violations, with clearer benefits on the 69-bus system and under reconfiguration; on the 69-bus system, TD3-GCN and TD3-TAGConv also achieve lower saved cost relative to the NLP benchmark than the NN baseline. We also highlight that transfer gains are case-dependent, and zero-shot transfer between fundamentally different systems results in notable performance degradation and increased voltage magnitude violations. This work is available at: this https URL and this https URL.
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
