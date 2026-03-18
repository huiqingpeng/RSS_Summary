---
title: "SympFormer: Accelerated attention blocks via Inertial Dynamics on Density Manifolds"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16535"
published: "2026-03-18"
fetched: "2026-03-18T15:44:53.458924"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:SympFormer: Accelerated attention blocks via Inertial Dynamics on Density Manifolds
View PDF HTML (experimental)Abstract:Transformers owe much of their empirical success in natural language processing to the self-attention blocks. Recent perspectives interpret attention blocks as interacting particle systems, whose mean-field limits correspond to gradient flows of interaction energy functionals on probability density spaces equipped with Wasserstein-$2$-type metrics. We extend this viewpoint by introducing accelerated attention blocks derived from inertial Nesterov-type dynamics on density spaces. In our proposed architecture, tokens carry both spatial (feature) and velocity variables. The time discretization and the approximation of accelerated density dynamics yield Hamiltonian momentum attention blocks, which constitute the proposed accelerated attention architectures. In particular, for linear self-attention, we show that the attention blocks approximate a Stein variational gradient flow, using a bilinear kernel, of a potential energy. In this setting, we prove that elliptically contoured probability distributions are preserved by the accelerated attention blocks. We present implementable particle-based algorithms and demonstrate that the proposed accelerated attention blocks converge faster than the classical attention blocks while preserving the number of oracle calls.
Submission history
From: Viktor Stein (TU Berlin) [view email][v1] Tue, 17 Mar 2026 13:56:17 UTC (323 KB)
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
