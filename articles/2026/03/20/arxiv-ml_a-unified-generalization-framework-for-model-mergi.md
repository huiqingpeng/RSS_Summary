---
title: "A Unified Generalization Framework for Model Merging: Trade-offs, Non-Linearity, and Scaling Laws"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.21690"
published: "2026-03-20"
fetched: "2026-03-20T14:10:01.253925"
---

Computer Science > Machine Learning
[Submitted on 29 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:A Unified Generalization Framework for Model Merging: Trade-offs, Non-Linearity, and Scaling Laws
View PDF HTML (experimental)Abstract:Model merging efficiently aggregates capabilities from multiple fine-tuned models into a single one, operating purely in parameter space without original data or expensive re-computation. Despite empirical successes, a unified theory for its effectiveness under heterogeneous finetuning hyperparameters (e.g., varying learning rates, batch sizes) remains missing. Existing federated learning theories focus purely on optimization, which fails to explain model merging and inherently leads to theoretical paradoxes. To address this challenge, we pioneer the integration of $L_2$-Stability theory into heterogeneous environments to rigorously decouple the excess risk of the merged model $\boldsymbol{x}_{avg}$ into optimization and generalization errors. This comprehensive analysis yields three main contributions: (i) We mathematically establish the fundamental \textit{Optimization-Generalization Trade-off}, explicitly resolving the paradox of why over-trained experts lead to catastrophic merging collapse. (ii) \textit{A unified theoretical framework} is provided to explain not only linear merging algorithms (e.g., TA, AdaMerging) but also state-of-the-art \textit{non-linear} merging algorithms (e.g., TIES, DARE), proving how sparsification operators strictly tighten the generalization bound by suppressing task heterogeneity. (iii) Rather than heuristic guidelines, we derive \textit{Quantitative Scaling Laws} that theoretically predict the precise impact of hyperparameter choices, enabling practitioners to strategically construct ``merge-friendly'' experts. Extensive experiments on the ResNet and ViT architectures across 20 visual classification tasks, involving thousands of finetuning models, robustly confirm that our theoretical scaling laws accurately predict the empirical generalization behaviors of $\boldsymbol{x}_{avg}$.
Submission history
From: Qinglun Li [view email][v1] Thu, 29 Jan 2026 13:22:06 UTC (244 KB)
[v2] Thu, 19 Mar 2026 06:54:16 UTC (1,183 KB)
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
