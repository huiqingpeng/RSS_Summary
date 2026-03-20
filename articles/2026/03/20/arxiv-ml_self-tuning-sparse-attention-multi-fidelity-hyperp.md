---
title: "Self-Tuning Sparse Attention: Multi-Fidelity Hyperparameter Optimization for Transformer Acceleration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18417"
published: "2026-03-20"
fetched: "2026-03-20T12:11:17.455387"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Self-Tuning Sparse Attention: Multi-Fidelity Hyperparameter Optimization for Transformer Acceleration
View PDF HTML (experimental)Abstract:Sparse attention mechanisms promise to break the quadratic bottleneck of long-context transformers, yet production adoption remains limited by a critical usability gap: optimal hyperparameters vary substantially across layers and models, and current methods (e.g., SpargeAttn) rely on manual grid search to identify them. We propose AFBS-BO (Adaptive Fidelity Binary Search with Bayesian Optimization), a fully automated framework that discovers optimal layer- and head-specific hyperparameters without human intervention. Our hybrid algorithm combines Bayesian Optimization for global exploration with binary search for local refinement, leveraging multi-fidelity evaluation across sequence lengths to reduce tuning cost. On Llama-2-7B, AFBS-BO accelerates hyperparameter discovery by 3.4x with 8.8x fewer evaluations than grid search, and identifies high-sparsity configurations that outperform existing sparse attention baselines while closely matching dense attention quality. By transforming sparse attention from a manually tuned heuristic into a self-optimizing primitive, AFBS-BO enables plug-and-play acceleration across diverse transformer architectures and domains.
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
