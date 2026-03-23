---
title: "Regret Analysis of Sleeping Competing Bandits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19700"
published: "2026-03-23"
fetched: "2026-03-24T07:21:24.150892"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Regret Analysis of Sleeping Competing Bandits
View PDF HTML (experimental)Abstract:The Competing Bandits framework is a recently emerging area that integrates multi-armed bandits in online learning with stable matching in game theory. While conventional models assume that all players and arms are constantly available, in real-world problems, their availability can vary arbitrarily over time. In this paper, we formulate this setting as Sleeping Competing Bandits. To analyze this problem, we naturally extend the regret definition used in existing competing bandits and derive regret bounds for the proposed model. We propose an algorithm that simultaneously achieves an asymptotic regret bound of $\mathrm{O}\left(NK\log T_{i}/\Delta^2\right)$ under reasonable assumptions, where $N$ is the number of players, $K$ is the number of arms, $T_{i}$ is the number of rounds of each player $p_i$, and $\Delta$ is the minimum reward gap. We also provide a regret lower bound of $\mathrm{\Omega}\left( N(K-N+1)\log T_{i}/\Delta^2 \right)$ under the same assumptions. This implies that our algorithm is asymptotically optimal in the regime where the number of arms $K$ is relatively larger than the number of players $N$.
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
