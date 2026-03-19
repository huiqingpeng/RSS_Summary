---
title: "Towards Infinitely Long Neural Simulations: Self-Refining Neural Surrogate Models for Dynamical Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17750"
published: "2026-03-19"
fetched: "2026-03-19T12:16:12.506008"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Towards Infinitely Long Neural Simulations: Self-Refining Neural Surrogate Models for Dynamical Systems
View PDF HTML (experimental)Abstract:Recent advances in autoregressive neural surrogate models have enabled orders-of-magnitude speedups in simulating dynamical systems. However, autoregressive models are generally prone to distribution drift: compounding errors in autoregressive rollouts that severely degrade generation quality over long time horizons. Existing work attempts to address this issue by implicitly leveraging the inherent trade-off between short-time accuracy and long-time consistency through hyperparameter tuning. In this work, we introduce a unifying mathematical framework that makes this tradeoff explicit, formalizing and generalizing hyperparameter-based strategies in existing approaches. Within this framework, we propose a robust, hyperparameter-free model implemented as a conditional diffusion model that balances short-time fidelity with long-time consistency by construction. Our model, Self-refining Neural Surrogate model (SNS), can be implemented as a standalone model that refines its own autoregressive outputs or as a complementary model to existing neural surrogates to ensure long-time consistency. We also demonstrate the numerical feasibility of SNS through high-fidelity simulations of complex dynamical systems over arbitrarily long time horizons.
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
