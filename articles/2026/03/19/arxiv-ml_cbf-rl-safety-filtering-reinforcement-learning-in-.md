---
title: "CBF-RL: Safety Filtering Reinforcement Learning in Training with Control Barrier Functions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.14959"
published: "2026-03-19"
fetched: "2026-03-19T14:17:25.299440"
---

Computer Science > Robotics
[Submitted on 16 Oct 2025 (v1), last revised 18 Mar 2026 (this version, v5)]
Title:CBF-RL: Safety Filtering Reinforcement Learning in Training with Control Barrier Functions
View PDF HTML (experimental)Abstract:Reinforcement learning (RL), while powerful and expressive, can often prioritize performance at the expense of safety. Yet safety violations can lead to catastrophic outcomes in real-world deployments. Control Barrier Functions (CBFs) offer a principled method to enforce dynamic safety -- traditionally deployed online via safety filters. While the result is safe behavior, the fact that the RL policy does not have knowledge of the CBF can lead to conservative behaviors. This paper proposes CBF-RL, a framework for generating safe behaviors with RL by enforcing CBFs in training. CBF-RL has two key attributes: (1) minimally modifying a nominal RL policy to encode safety constraints via a CBF term, (2) and safety filtering of the policy rollouts in training. Theoretically, we prove that continuous-time safety filters can be deployed via closed-form expressions on discrete-time roll-outs. Practically, we demonstrate that CBF-RL internalizes the safety constraints in the learned policy -- both enforcing safer actions and biasing towards safer rewards -- enabling safe deployment without the need for an online safety filter. We validate our framework through ablation studies on navigation tasks and on the Unitree G1 humanoid robot, where CBF-RL enables safer exploration, faster convergence, and robust performance under uncertainty, enabling the humanoid robot to avoid obstacles and climb stairs safely in real-world settings without a runtime safety filter.
Submission history
From: Lizhi Yang [view email][v1] Thu, 16 Oct 2025 17:58:58 UTC (6,695 KB)
[v2] Sun, 19 Oct 2025 01:26:45 UTC (6,695 KB)
[v3] Thu, 5 Mar 2026 18:52:25 UTC (13,520 KB)
[v4] Fri, 13 Mar 2026 05:44:22 UTC (14,770 KB)
[v5] Wed, 18 Mar 2026 15:28:16 UTC (14,770 KB)
Current browse context:
cs.RO
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
