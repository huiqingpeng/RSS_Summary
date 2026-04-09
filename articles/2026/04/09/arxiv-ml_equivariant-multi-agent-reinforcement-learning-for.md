---
title: "Equivariant Multi-agent Reinforcement Learning for Multimodal Vehicle-to-Infrastructure Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06914"
published: "2026-04-09"
fetched: "2026-04-10T07:05:09.347176"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:Equivariant Multi-agent Reinforcement Learning for Multimodal Vehicle-to-Infrastructure Systems
View PDF HTML (experimental)Abstract:In this paper, we study a vehicle-to-infrastructure (V2I) system where distributed base stations (BSs) acting as road-side units (RSUs) collect multimodal (wireless and visual) data from moving vehicles. We consider a decentralized rate maximization problem, where each RSU relies on its local observations to optimize its resources, while all RSUs must collaborate to guarantee favorable network performance. We recast this problem as a distributed multi-agent reinforcement learning (MARL) problem, by incorporating rotation symmetries in terms of vehicles' locations. To exploit these symmetries, we propose a novel self-supervised learning framework where each BS agent aligns the latent features of its multimodal observation to extract the positions of the vehicles in its local region. Equipped with this sensing data at each RSU, we train an equivariant policy network using a graph neural network (GNN) with message passing layers, such that each agent computes its policy locally, while all agents coordinate their policies via a signaling scheme that overcomes partial observability and guarantees the equivariance of the global policy. We present numerical results carried out in a simulation environment, where ray-tracing and computer graphics are used to collect wireless and visual data. Results show the generalizability of our self-supervised and multimodal sensing approach, achieving more than two-fold accuracy gains over baselines, and the efficiency of our equivariant MARL training, attaining more than 50% performance gains over standard approaches.
Submission history
From: Charbel Bou Chaaya [view email][v1] Wed, 8 Apr 2026 10:13:29 UTC (7,692 KB)
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
