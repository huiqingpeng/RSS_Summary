---
title: "Hyperparameter Trajectory Inference with Conditional Lagrangian Optimal Transport"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.01771"
published: "2026-03-19"
fetched: "2026-03-19T14:12:38.072588"
---

Computer Science > Machine Learning
[Submitted on 2 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Hyperparameter Trajectory Inference with Conditional Lagrangian Optimal Transport
View PDF HTML (experimental)Abstract:Neural networks (NNs) often have critical behavioural trade-offs that are set at design time with hyperparameters-such as reward weights in reinforcement learning or quantile targets in regression. Post-deployment, however, user preferences can evolve, making initial settings undesirable, necessitating potentially expensive retraining. To circumvent this, we introduce the task of Hyperparameter Trajectory Inference (HTI): to learn, from observed data, how a NN's conditional output distribution changes with its hyperparameters, and construct a surrogate model that approximates the NN at unobserved hyperparameter settings. HTI requires extending existing trajectory inference approaches to incorporate conditions, exacerbating the challenge of ensuring inferred paths are feasible. We propose an approach based on conditional Lagrangian optimal transport, jointly learning the Lagrangian function governing hyperparameter-induced dynamics along with the associated optimal transport maps and geodesics between observed marginals, which form the surrogate model. We incorporate inductive biases based on the manifold hypothesis and least-action principles into the learned Lagrangian, improving surrogate model feasibility. We empirically demonstrate that our approach reconstructs NN outputs across various hyperparameter spectra better than other alternatives.
Submission history
From: Harry Amad [view email][v1] Mon, 2 Mar 2026 11:55:02 UTC (722 KB)
[v2] Tue, 3 Mar 2026 12:35:37 UTC (721 KB)
[v3] Wed, 18 Mar 2026 09:09:11 UTC (721 KB)
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
