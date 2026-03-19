---
title: "Unified Policy Value Decomposition for Rapid Adaptation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17947"
published: "2026-03-19"
fetched: "2026-03-19T12:18:29.755648"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Unified Policy Value Decomposition for Rapid Adaptation
View PDF HTML (experimental)Abstract:Rapid adaptation in complex control systems remains a central challenge in reinforcement learning. We introduce a framework in which policy and value functions share a low-dimensional coefficient vector - a goal embedding - that captures task identity and enables immediate adaptation to novel tasks without retraining representations. During pretraining, we jointly learn structured value bases and compatible policy bases through a bilinear actor-critic decomposition. The critic factorizes as Q = sum_k G_k(g) y_k(s,a), where G_k(g) is a goal-conditioned coefficient vector and y_k(s,a) are learned value basis functions. This multiplicative gating - where a context signal scales a set of state-dependent bases - is reminiscent of gain modulation observed in Layer 5 pyramidal neurons, where top-down inputs modulate the gain of sensory-driven responses without altering their tuning. Building on Successor Features, we extend the decomposition to the actor, which composes a set of primitive policies weighted by the same coefficients G_k(g). At test time the bases are frozen and G_k(g) is estimated zero-shot via a single forward pass, enabling immediate adaptation to novel tasks without any gradient update. We train a Soft Actor-Critic agent on the MuJoCo Ant environment under a multi-directional locomotion objective, requiring the agent to walk in eight directions specified as continuous goal vectors. The bilinear structure allows each policy head to specialize to a subset of directions, while the shared coefficient layer generalizes across them, accommodating novel directions by interpolating in goal embedding space. Our results suggest that shared low-dimensional goal embeddings offer a general mechanism for rapid, structured adaptation in high-dimensional control, and highlight a potentially biologically plausible principle for efficient transfer in complex reinforcement learning systems.
Submission history
From: Cristiano Capone [view email][v1] Wed, 18 Mar 2026 17:19:56 UTC (3,631 KB)
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
