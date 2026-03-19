---
title: "DeepStage: Learning Autonomous Defense Policies Against Multi-Stage APT Campaigns"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16969"
published: "2026-03-19"
fetched: "2026-03-19T13:07:09.459687"
---

Computer Science > Cryptography and Security
[Submitted on 17 Mar 2026]
Title:DeepStage: Learning Autonomous Defense Policies Against Multi-Stage APT Campaigns
View PDF HTML (experimental)Abstract:This paper presents DeepStage, a deep reinforcement learning (DRL) framework for adaptive, stage-aware defense against Advanced Persistent Threats (APTs). The enterprise environment is modeled as a partially observable Markov decision process (POMDP), where host provenance and network telemetry are fused into unified provenance graphs. Building on our prior work, StageFinder, a graph neural encoder and an LSTM-based stage estimator infer probabilistic attacker stages aligned with the MITRE ATT&CK framework. These stage beliefs, combined with graph embeddings, guide a hierarchical Proximal Policy Optimization (PPO) agent that selects defense actions across monitoring, access control, containment, and remediation. Evaluated in a realistic enterprise testbed using CALDERA-driven APT playbooks, DeepStage achieves a stage-weighted F1-score of 0.89, outperforming a risk-aware DRL baseline by 21.9%. The results demonstrate effective stage-aware and cost-efficient autonomous cyber defense.
Current browse context:
cs.CR
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
