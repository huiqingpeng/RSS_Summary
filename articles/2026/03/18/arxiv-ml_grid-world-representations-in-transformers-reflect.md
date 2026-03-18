---
title: "Grid-World Representations in Transformers Reflect Predictive Geometry"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16689"
published: "2026-03-18"
fetched: "2026-03-18T15:45:56.399065"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Grid-World Representations in Transformers Reflect Predictive Geometry
View PDF HTML (experimental)Abstract:Next-token predictors often appear to develop internal representations of the latent world and its rules. The probabilistic nature of these models suggests a deep connection between the structure of the world and the geometry of probability distributions. In order to understand this link more precisely, we use a minimal stochastic process as a controlled setting: constrained random walks on a two-dimensional lattice that must reach a fixed endpoint after a predetermined number of steps. Optimal prediction of this process solely depends on a sufficient vector determined by the walker's position relative to the target and the remaining time horizon; in other words, the probability distributions are parametrized by the world's geometry. We train decoder-only transformers on prefixes sampled from the exact distribution of these walks and compare their hidden activations to the analytically derived sufficient vectors. Across models and layers, the learned representations align strongly with the ground-truth predictive vectors and are often low-dimensional. This provides a concrete example in which world-model-like representations can be directly traced back to the predictive geometry of the data itself. Although demonstrated in a simplified toy system, the analysis suggests that geometric representations supporting optimal prediction may provide a useful lens for studying how neural networks internalize grammatical and other structural constraints.
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
