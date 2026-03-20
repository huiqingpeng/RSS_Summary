---
title: "SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18079"
published: "2026-03-20"
fetched: "2026-03-20T12:07:04.910736"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training
View PDF HTML (experimental)Abstract:Large Language Model (LLM) agents have shown strong results on multi-turn tool-use tasks, yet they operate in isolation during training, failing to leverage experiences accumulated across episodes. Existing experience-augmented methods address this by organizing trajectories into retrievable libraries, but they retrieve experiences only once based on the initial task description and hold them constant throughout the episode. In multi-turn settings where observations change at every step, this static retrieval becomes increasingly mismatched as episodes progress. We propose SLEA-RL (Step-Level Experience-Augmented Reinforcement Learning), a framework that retrieves relevant experiences at each decision step conditioned on the current observation. SLEA-RL operates through three components: (i) step-level observation clustering that groups structurally equivalent environmental states for efficient cluster-indexed retrieval; (ii) a self-evolving experience library that distills successful strategies and failure patterns through score-based admission and rate-limited extraction; and (iii) policy optimization with step-level credit assignment for fine-grained advantage estimation across multi-turn episodes. The experience library evolves alongside the policy through semantic analysis rather than gradient updates. Experiments on long-horizon multi-turn agent benchmarks demonstrate that SLEA-RL achieves superior performance compared to various reinforcement learning baselines.
Submission history
From: Prince Zizhuang Wang [view email][v1] Wed, 18 Mar 2026 07:16:18 UTC (5,146 KB)
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
