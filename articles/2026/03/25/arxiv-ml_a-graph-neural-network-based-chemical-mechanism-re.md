---
title: "A graph neural network based chemical mechanism reduction method for combustion applications"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22318"
published: "2026-03-25"
fetched: "2026-03-26T07:10:34.917375"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:A graph neural network based chemical mechanism reduction method for combustion applications
View PDF HTML (experimental)Abstract:Direct numerical simulations of turbulent reacting flows involving millions of grid points and detailed chemical mechanisms with hundreds of species and thousands of reactions are computationally prohibitive. To address this challenge, we present two data-driven chemical mechanism reduction formulations based on graph neural networks (GNNs) with message-passing transformer layers that learn nonlinear dependencies among species and reactions. The first formulation, GNN-SM, employs a pre-trained surrogate model to guide reduction across a broad range of reactor conditions. The second formulation, GNN-AE, uses an autoencoder formulation to obtain highly compact mechanisms that remain accurate within the thermochemical regimes used during training. The approaches are demonstrated on detailed mechanisms for methane (53 species, 325 reactions), ethylene (96 species, 1054 reactions), and iso-octane (1034 species, 8453 reactions). GNN-SM achieves reductions comparable to the established graph-based method DRGEP while maintaining accuracy across a wide range of thermochemical states. In contrast, GNN-AE achieves up to 95% reduction in species and reactions and outperforms DRGEP within its target conditions. Overall, the proposed framework provides an automated, machine-learning-based pathway for chemical mechanism reduction that can complement traditional expert-guided analytical approaches.
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
