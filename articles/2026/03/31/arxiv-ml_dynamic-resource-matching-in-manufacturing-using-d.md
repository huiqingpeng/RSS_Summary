---
title: "Dynamic resource matching in manufacturing using deep reinforcement learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27066"
published: "2026-03-31"
fetched: "2026-04-01T07:21:19.748263"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Dynamic resource matching in manufacturing using deep reinforcement learning
View PDF HTML (experimental)Abstract:Matching plays an important role in the logical allocation of resources across a wide range of industries. The benefits of matching have been increasingly recognized in manufacturing industries. In particular, capacity sharing has received much attention recently. In this paper, we consider the problem of dynamically matching demand-capacity types of manufacturing resources. We formulate the multi-period, many-to-many manufacturing resource-matching problem as a sequential decision process. The formulated manufacturing resource-matching problem involves large state and action spaces, and it is not practical to accurately model the joint distribution of various types of demands. To address the curse of dimensionality and the difficulty of explicitly modeling the transition dynamics, we use a model-free deep reinforcement learning approach to find optimal matching policies. Moreover, to tackle the issue of infeasible actions and slow convergence due to initial biased estimates caused by the maximum operator in Q-learning, we introduce two penalties to the traditional Q-learning algorithm: a domain knowledge-based penalty based on a prior policy and an infeasibility penalty that conforms to the demand-supply constraints. We establish theoretical results on the convergence of our domain knowledge-informed Q-learning providing performance guarantee for small-size problems. For large-size problems, we further inject our modified approach into the deep deterministic policy gradient (DDPG) algorithm, which we refer to as domain knowledge-informed DDPG (DKDDPG). In our computational study, including small- and large-scale experiments, DKDDPG consistently outperformed traditional DDPG and other RL algorithms, yielding higher rewards and demonstrating greater efficiency in time and episodes.
Submission history
From: Saunak Kumar Panda [view email][v1] Sat, 28 Mar 2026 00:56:29 UTC (895 KB)
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
