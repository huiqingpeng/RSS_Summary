---
title: "Q-BIOLAT: Binary Latent Protein Fitness Landscapes for QUBO-Based Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27526"
published: "2026-03-31"
fetched: "2026-04-01T07:25:20.009331"
---

Computer Science > Machine Learning
[Submitted on 29 Mar 2026]
Title:Q-BIOLAT: Binary Latent Protein Fitness Landscapes for QUBO-Based Optimization
View PDF HTML (experimental)Abstract:Protein fitness optimization is inherently a discrete combinatorial problem, yet most learning-based approaches rely on continuous representations and are primarily evaluated through predictive accuracy. We introduce Q-BIOLAT, a framework for modeling and optimizing protein fitness landscapes in compact binary latent spaces. Starting from pretrained protein language model embeddings, we construct binary latent representations and learn a quadratic unconstrained binary optimization (QUBO) surrogate that captures unary and pairwise interactions.
Beyond its formulation, Q-BIOLAT provides a representation-centric perspective on protein fitness modeling. We show that representations with similar predictive performance can induce fundamentally different optimization landscapes. In particular, learned autoencoder-based representations collapse after binarization, producing degenerate latent spaces that fail to support combinatorial search, whereas simple structured representations such as PCA yield high-entropy, decodable, and optimization-friendly latent spaces.
Across multiple datasets and data regimes, we demonstrate that classical combinatorial optimization methods, including simulated annealing, genetic algorithms, and greedy hill climbing, are highly effective in structured binary latent spaces. By expressing the objective in QUBO form, our approach connects modern machine learning with discrete and quantum-inspired optimization.
Our implementation and dataset are publicly available at: this https URL
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
