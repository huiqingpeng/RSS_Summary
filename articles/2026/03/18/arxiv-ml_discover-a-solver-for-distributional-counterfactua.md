---
title: "DISCOVER: A Solver for Distributional Counterfactual Explanations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16436"
published: "2026-03-18"
fetched: "2026-03-18T15:43:56.186815"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:DISCOVER: A Solver for Distributional Counterfactual Explanations
View PDF HTML (experimental)Abstract:Counterfactual explanations (CE) explain model decisions by identifying input modifications that lead to different predictions. Most existing methods operate at the instance level. Distributional Counterfactual Explanations (DCE) extend this setting by optimizing an optimal transport objective that balances proximity to a factual input distribution and alignment to a target output distribution, with statistical certification via chance constrained bounds. However, DCE relies on gradient based optimization, while many real-world tabular pipelines are dominated by non-differentiable models. We propose DISCOVER, a model-agnostic solver for distributional counterfactual explanations. DISCOVER preserves the original DCE objective and certification while replacing gradient descent with a sparse propose-and-select search paradigm. It exploits a sample-wise decomposition of the transport objective to compute per-row impact scores and enforce a top-$k$ intervention budget, focusing edits on the most influential samples. To guide candidate generation without predictor gradients, DISCOVER introduces an OT-guided cone sampling primitive driven by input-side transport geometry. Experiments on multiple tabular datasets demonstrate strong joint alignment of input and output distributions, extending distributional counterfactual reasoning to modern black box learning pipelines. A code repository is available at this https URL.
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
