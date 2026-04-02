---
title: "Full-Gradient Successor Feature Representations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00686"
published: "2026-04-02"
fetched: "2026-04-03T07:23:31.769396"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Full-Gradient Successor Feature Representations
View PDF HTML (experimental)Abstract:Successor Features (SF) combined with Generalized Policy Improvement (GPI) provide a robust framework for transfer learning in Reinforcement Learning (RL) by decoupling environment dynamics from reward functions. However, standard SF learning methods typically rely on semi-gradient Temporal Difference (TD) updates. When combined with non-linear function approximation, semi-gradient methods lack robust convergence guarantees and can lead to instability, particularly in the multi-task setting where accurate feature estimation is critical for effective GPI. Inspired by Full Gradient DQN, we propose Full-Gradient Successor Feature Representations Q-Learning (FG-SFRQL), an algorithm that optimizes the successor features by minimizing the full Mean Squared Bellman Error. Unlike standard approaches, our method computes gradients with respect to parameters in both the online and target networks. We provide a theoretical proof of almost-sure convergence for FG-SFRQL and demonstrate empirically that minimizing the full residual leads to superior sample efficiency and transfer performance compared to semi-gradient baselines in both discrete and continuous domains.
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
