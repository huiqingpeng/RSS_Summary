---
title: "Diagnosing Non-Markovian Observations in Reinforcement Learning via Prediction-Based Violation Scoring"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27389"
published: "2026-03-31"
fetched: "2026-04-01T07:23:20.675757"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Diagnosing Non-Markovian Observations in Reinforcement Learning via Prediction-Based Violation Scoring
View PDF HTML (experimental)Abstract:Reinforcement learning algorithms assume that observations satisfy the Markov property, yet real-world sensors frequently violate this assumption through correlated noise, latency, or partial observability. Standard performance metrics conflate Markov breakdowns with other sources of suboptimality, leaving practitioners without diagnostic tools for such violations. This paper introduces a prediction-based scoring method that quantifies non-Markovian structure in observation trajectories. A random forest first removes nonlinear Markov-compliant dynamics; ridge regression then tests whether historical observations reduce prediction error on the residuals beyond what the current observation provides. The resulting score is bounded in [0, 1] and requires no causal graph construction. Evaluation spans six environments (CartPole, Pendulum, Acrobot, HalfCheetah, Hopper, Walker2d), three algorithms (PPO, A2C, SAC), controlled AR(1) noise at six intensity levels, and 10 seeds per condition. In post-hoc detection, 7 of 16 environment-algorithm pairs, primarily high-dimensional locomotion tasks, show significant positive monotonicity between noise intensity and the violation score (Spearman rho up to 0.78, confirmed under repeated-measures analysis); under training-time noise, 13 of 16 pairs exhibit statistically significant reward degradation. An inversion phenomenon is documented in low-dimensional environments where the random forest absorbs the noise signal, causing the score to decrease as true violations grow, a failure mode analyzed in detail. A practical utility experiment demonstrates that the proposed score correctly identifies partial observability and guides architecture selection, fully recovering performance lost to non-Markovian observations. Source code to reproduce all results is provided at this https URL.
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
