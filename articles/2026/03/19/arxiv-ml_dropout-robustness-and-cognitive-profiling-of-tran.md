---
title: "Dropout Robustness and Cognitive Profiling of Transformer Models via Stochastic Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17811"
published: "2026-03-19"
fetched: "2026-03-19T12:16:38.006680"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Dropout Robustness and Cognitive Profiling of Transformer Models via Stochastic Inference
View PDF HTML (experimental)Abstract:Transformer-based language models are widely deployed for reasoning, yet their behavior under inference-time stochasticity remains underexplored. While dropout is common during training, its inference-time effects via Monte Carlo sampling lack systematic evaluation across architectures, limiting understanding of model reliability in uncertainty-aware applications.
This work analyzes dropout-induced variability across 19 transformer models using MC Dropout with 100 stochastic forward passes per sample. Dropout robustness is defined as maintaining high accuracy and stable predictions under stochastic inference, measured by standard deviation of per-run accuracies. A cognitive decomposition framework disentangles performance into memory and reasoning components. Experiments span five dropout configurations yielding 95 unique evaluations on 1,000 samples.
Results reveal substantial architectural variation. Smaller models demonstrate perfect prediction stability while medium-sized models exhibit notable volatility. Mid-sized models achieve the best overall performance; larger models excel at memory tasks. Critically, 53% of models suffer severe accuracy degradation under baseline MC Dropout, with task-specialized models losing up to 24 percentage points, indicating unsuitability for uncertainty quantification in these architectures. Asymmetric effects emerge: high dropout reduces memory accuracy by 27 percentage points while reasoning degrades only 1 point, suggesting memory tasks rely on stable representations that dropout disrupts. 84% of models demonstrate memory-biased performance.
This provides the first comprehensive MC Dropout benchmark for transformers, revealing dropout robustness is architecture-dependent and uncorrelated with scale. The cognitive profiling framework offers actionable guidance for model selection in uncertainty-aware applications.
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
