---
title: "Multi-Agent Reinforcement Learning Counteracts Delayed CSI in Multi-Satellite Systems"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2603.16470"
published: "2026-03-18"
fetched: "2026-03-18T19:08:24.821066"
---

Computer Science > Information Theory
[Submitted on 17 Mar 2026]
Title:Multi-Agent Reinforcement Learning Counteracts Delayed CSI in Multi-Satellite Systems
View PDF HTML (experimental)Abstract:The integration of satellite communication networks with next-generation (NG) technologies is a promising approach towards global connectivity. However, the quality of services is highly dependant on the availability of accurate channel state information (CSI). Channel estimation in satellite communications is challenging due to the high propagation delay between terrestrial users and satellites, which results in outdated CSI observations on the satellite side. In this paper, we study the downlink transmission of multiple satellites acting as distributed base stations (BS) to mobile terrestrial users. We propose a multi-agent reinforcement learning (MARL) algorithm which aims for maximising the sum-rate of the users, while coping with the outdated CSI. We design a novel bi-level optimisation, procedure themes as dual stage proximal policy optimisation (DS-PPO), for tackling the problem of large continuous action spaces as well as of independent and non-identically distributed (non-IID) environments in MARL. Specifically, the first stage of DS-PPO maximises the sum-rate for an individual satellite and the second stage maximises the sum-rate when all the satellites cooperate to form a distributed multi-antenna BS. Our numerical results demonstrate the robustness of DS-PPO to CSI imperfections as well as the sum-rate improvement attached by the use of DS-PPO. In addition, we provide the convergence analysis for the DS-PPO along with the computational complexity.
Submission history
From: Marios Aristodemou [view email][v1] Tue, 17 Mar 2026 12:58:22 UTC (495 KB)
Current browse context:
cs.IT
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
