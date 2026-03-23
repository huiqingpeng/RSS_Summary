---
title: "Two-Time-Scale Learning Dynamics: A Population View of Neural Network Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19808"
published: "2026-03-23"
fetched: "2026-03-24T07:22:17.258236"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Two-Time-Scale Learning Dynamics: A Population View of Neural Network Training
View PDF HTML (experimental)Abstract:Population-based learning paradigms, including evolutionary strategies, Population-Based Training (PBT), and recent model-merging methods, combine fast within-model optimisation with slower population-level adaptation. Despite their empirical success, a general mathematical description of the resulting collective training dynamics remains incomplete. We introduce a theoretical framework for neural network training based on two-time-scale population dynamics. We model a population of neural networks as an interacting agent system in which network parameters evolve through fast noisy gradient updates of SGD/Langevin type, while hyperparameters evolve through slower selection--mutation dynamics. We prove the large-population limit for the joint distribution of parameters and hyperparameters and, under strong time-scale separation, derive a selection--mutation equation for the hyperparameter density. For each fixed hyperparameter, the fast parameter dynamics relaxes to a Boltzmann--Gibbs measure, inducing an effective fitness for the slow evolution. The averaged dynamics connects population-based learning with bilevel optimisation and classical replicator--mutator models, yields conditions under which the population mean moves toward the fittest hyperparameter, and clarifies the role of noise and diversity in balancing optimisation and exploration. Numerical experiments illustrate both the large-population regime and the reduced two-time-scale dynamics, and indicate that access to the effective fitness, either in closed form or through population-level estimation, can improve population-level updates.
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
