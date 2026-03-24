---
title: "Bounded Coupled AI Learning Dynamics in Tri-Hierarchical Drone Swarms"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20333"
published: "2026-03-24"
fetched: "2026-03-25T07:07:42.397654"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Bounded Coupled AI Learning Dynamics in Tri-Hierarchical Drone Swarms
View PDFAbstract:Modern autonomous multi-agent systems combine heterogeneous learning mechanisms operating at different timescales. An open question remains: can one formally guarantee that coupled dynamics of such mechanisms stay within the admissible operational regime? This paper studies a tri-hierarchical swarm learning system where three mechanisms act simultaneously: (1) local Hebbian online learning at individual agent level (fast timescale, 10-100 ms); (2) multi-agent reinforcement learning (MARL) for tactical group coordination (medium timescale, 1-10 s); (3) meta-learning (MAML) for strategic adaptation (slow timescale, 10-100 s). Four results are established. The Bounded Total Error Theorem shows that under contractual constraints on learning rates, Lipschitz continuity of inter-level mappings, and weight stabilization, total suboptimality admits a component-wise upper bound uniform in time. The Bounded Representation Drift Theorem gives a worst-case estimate of how Hebbian updates affect coordination-level embeddings during one MARL cycle. The Meta-Level Compatibility Theorem provides sufficient conditions under which strategic adaptation preserves lower-level invariants. The Non-Accumulation Theorem proves that error does not grow unboundedly over time.
Submission history
From: Oleksii Bychkov S. [view email][v1] Fri, 20 Mar 2026 07:23:32 UTC (578 KB)
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
