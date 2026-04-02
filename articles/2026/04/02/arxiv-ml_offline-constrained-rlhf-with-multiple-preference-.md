---
title: "Offline Constrained RLHF with Multiple Preference Oracles"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00200"
published: "2026-04-02"
fetched: "2026-04-03T07:18:12.675525"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Offline Constrained RLHF with Multiple Preference Oracles
View PDF HTML (experimental)Abstract:We study offline constrained reinforcement learning from human feedback with multiple preference oracles. Motivated by applications that trade off performance with safety or fairness, we aim to maximize target population utility subject to a minimum protected group welfare constraint. From pairwise comparisons collected under a reference policy, we estimate oracle-specific rewards via maximum likelihood and analyze how statistical uncertainty propagates through the dual program. We cast the constrained objective as a KL-regularized Lagrangian whose primal optimizer is a Gibbs policy, reducing learning to a convex dual problem. We propose a dual-only algorithm that ensures high-probability constraint satisfaction and provide the first finite-sample performance guarantees for offline constrained preference learning. Finally, we extend our theoretical analysis to accommodate multiple constraints and general f-divergence regularization.
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
