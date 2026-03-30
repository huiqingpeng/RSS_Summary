---
title: "A Boltzmann-machine-enhanced Transformer For DNA Sequence Classification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26465"
published: "2026-03-30"
fetched: "2026-03-31T07:24:25.331564"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:A Boltzmann-machine-enhanced Transformer For DNA Sequence Classification
View PDF HTML (experimental)Abstract:DNA sequence classification requires not only high predictive accuracy but also the ability to uncover latent site interactions, combinatorial regulation, and epistasis-like higher-order dependencies. Although the standard Transformer provides strong global modeling capacity, its softmax attention is continuous, dense, and weakly constrained, making it better suited for information routing than explicit structure discovery. In this paper, we propose a Boltzmann-machine-enhanced Transformer for DNA sequence classification. Built on multi-head attention, the model introduces structured binary gating variables to represent latent query-key connections and constrains them with a Boltzmann-style energy function. Query-key similarity defines local bias terms, learnable pairwise interactions capture synergy and competition between edges, and latent hidden units model higher-order combinatorial dependencies. Since exact posterior inference over discrete gating graphs is intractable, we use mean-field variational inference to estimate edge activation probabilities and combine it with Gumbel-Softmax to progressively compress continuous probabilities into near-discrete gates while preserving end-to-end differentiability. During training, we jointly optimize classification and energy losses, encouraging the model to achieve accurate prediction while favoring low-energy, stable, and interpretable structures. We further derive the framework from the energy function and variational free energy to the mean-field fixed-point equations, Gumbel-Softmax relaxation, and the final joint objective. The proposed framework provides a unified view of integrating Boltzmann machines, differentiable discrete optimization, and Transformers for structured learning on biological sequences.
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
