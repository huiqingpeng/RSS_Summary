---
title: "Federated Distributional Reinforcement Learning with Distributional Critic Regularization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17820"
published: "2026-03-19"
fetched: "2026-03-19T12:16:45.827166"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Federated Distributional Reinforcement Learning with Distributional Critic Regularization
View PDF HTML (experimental)Abstract:Federated reinforcement learning typically aggregates value functions or policies by parameter averaging, which emphasizes expected return and can obscure statistical multimodality and tail behavior that matter in safety-critical settings. We formalize federated distributional reinforcement learning (FedDistRL), where clients parametrize quantile value function critics and federate these networks only. We also propose TR-FedDistRL, which builds a per client, risk-aware Wasserstein barycenter over a temporal buffer. This local barycenter provides a reference region to constrain the parameter averaged critic, ensuring necessary distributional information is not averaged out during the federation process. The distributional trust region is implemented as a shrink-squash step around this reference. Under fixed-policy evaluation, the feasibility map is nonexpansive and the update is contractive in a probe-set Wasserstein metric under evaluation. Experiments on a bandit, multi-agent gridworld, and continuous highway environment show reduced mean-smearing, improved safety proxies (catastrophe/accident rate), and lower critic/policy drift versus mean-oriented and non-federated baselines.
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
