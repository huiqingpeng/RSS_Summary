---
title: "Identifying Latent Actions and Dynamics from Offline Data via Demonstrator Diversity"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17577"
published: "2026-03-19"
fetched: "2026-03-19T12:14:01.799456"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Identifying Latent Actions and Dynamics from Offline Data via Demonstrator Diversity
View PDF HTML (experimental)Abstract:Can latent actions and environment dynamics be recovered from offline trajectories when actions are never observed? We study this question in a setting where trajectories are action-free but tagged with demonstrator identity. We assume that each demonstrator follows a distinct policy, while the environment dynamics are shared across demonstrators and identity affects the next observation only through the chosen action. Under these assumptions, the conditional next-observation distribution $p(o_{t+1}\mid o_t,e)$ is a mixture of latent action-conditioned transition kernels with demonstrator-specific mixing weights. We show that this induces, for each state, a column-stochastic nonnegative matrix factorization of the observable conditional distribution. Using sufficiently scattered policy diversity and rank conditions, we prove that the latent transitions and demonstrator policies are identifiable up to permutation of the latent action labels. We extend the result to continuous observation spaces via a Gram-determinant minimum-volume criterion, and show that continuity of the transition map over a connected state space upgrades local permutation ambiguities to a single global permutation. A small amount of labeled action data then suffices to fix this final ambiguity. These results establish demonstrator diversity as a principled source of identifiability for learning latent actions and dynamics from offline RL data.
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
