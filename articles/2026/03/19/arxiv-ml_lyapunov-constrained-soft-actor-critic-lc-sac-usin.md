---
title: "Lyapunov Constrained Soft Actor-Critic (LC-SAC) using Koopman Operator Theory for Quadrotor Trajectory Tracking"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.04132"
published: "2026-03-19"
fetched: "2026-03-19T14:18:18.134140"
---

Electrical Engineering and Systems Science > Systems and Control
[Submitted on 4 Feb 2026 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Lyapunov Constrained Soft Actor-Critic (LC-SAC) using Koopman Operator Theory for Quadrotor Trajectory Tracking
View PDF HTML (experimental)Abstract:Reinforcement Learning (RL) has achieved remarkable success in solving complex sequential decision-making problems. However, its application to safety-critical physical systems remains constrained by the lack of stability guarantees. Standard RL algorithms prioritize reward maximization, often yielding policies that may induce oscillations or unbounded state divergence. There has been significant work in incorporating Lyapunov-based stability guarantees in RL algorithms with key challenges being selecting a candidate Lyapunov function, computational complexity by using excessive function approximators and conservative policies by incorporating stability criterion in the learning process. In this work we propose a novel Lyapunov-constrained Soft Actor-Critic (LC-SAC) algorithm using Koopman operator theory. We propose use of extended dynamic mode decomposition (EDMD) to produce a linear approximation of the system and use this approximation to derive a closed form solution for candidate Lyapunov function. This derived Lyapunov function is incorporated in the SAC algorithm to further provide guarantees for a policy that stabilizes the nonlinear system. The results are evaluated trajectory tracking of a 2D Quadrotor environment based on safe-control-gym. The proposed algorithm shows training convergence and decaying violations for Lyapunov stability criterion compared to baseline vanilla SAC algorithm. GitHub Repository: this https URL
Submission history
From: Dhruv Kushwaha [view email][v1] Wed, 4 Feb 2026 01:51:05 UTC (2,902 KB)
[v2] Fri, 6 Feb 2026 19:54:40 UTC (2,902 KB)
[v3] Tue, 17 Mar 2026 20:15:47 UTC (2,902 KB)
Current browse context:
eess.SY
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
