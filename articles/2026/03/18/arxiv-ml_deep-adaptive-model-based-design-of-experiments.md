---
title: "Deep Adaptive Model-Based Design of Experiments"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16146"
published: "2026-03-18"
fetched: "2026-03-18T16:11:01.518498"
---

Statistics > Machine Learning
[Submitted on 17 Mar 2026]
Title:Deep Adaptive Model-Based Design of Experiments
View PDF HTML (experimental)Abstract:Model-based design of experiments (MBDOE) is essential for efficient parameter estimation in nonlinear dynamical systems. However, conventional adaptive MBDOE requires costly posterior inference and design optimization between each experimental step, precluding real-time applications. We address this by combining Deep Adaptive Design (DAD), which amortizes sequential design into a neural network policy trained offline, with differentiable mechanistic models. For dynamical systems with known governing equations but uncertain parameters, we extend sequential contrastive training objectives to handle nuisance parameters and propose a transformer-based policy architecture that respects the temporal structure of dynamical systems. We demonstrate the approach on four systems of increasing complexity: a fed-batch bioreactor with Monod kinetics, a Haldane bioreactor with uncertain substrate inhibition, a two-compartment pharmacokinetic model with nuisance clearance parameters, and a DC motor for real-time deployment.
Current browse context:
stat.ML
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
