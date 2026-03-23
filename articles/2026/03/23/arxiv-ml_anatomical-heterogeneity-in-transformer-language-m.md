---
title: "Anatomical Heterogeneity in Transformer Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19348"
published: "2026-03-23"
fetched: "2026-03-24T07:17:49.103569"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Anatomical Heterogeneity in Transformer Language Models
View PDF HTML (experimental)Abstract:Current transformer language models are trained with uniform computational budgets across all layers, implicitly assuming layer homogeneity. We challenge this assumption through empirical analysis of SmolLM2-135M, a 30-layer, 135M-parameter causal language model, using five diagnostic metrics: weight predictability (R2), ablation degradation, recovery speed, weight manipulation robustness, and structural analysis. We find profound anatomical heterogeneity: (1) Layer weights follow strong mathematical regularity (R2 = 0.91) with a universal oscillatory delta pattern (correlation ~= -0.50), yet predicted weights cause catastrophic failure due to nonlinear error accumulation. (2) Layer importance spans a 10^7 range, from a critical core (L8-11, up to +63,419% PPL degradation) to anti-layers (L14, L17) whose removal improves performance. (3) Recovery speed correlates with layer importance, indicating differential training requirements. (4) Only weight scaling (alpha = 0.9) preserves model quality among five tested manipulation strategies. (5) Growth Transformer Training, allocating budget by layer importance, achieves ~54% cost reduction. A proof-of-concept experiment confirms this: 4.7x lower validation loss than uniform training at identical parameter count, while being 13% faster.
Submission history
From: Tomasz Wietrzykowski [view email][v1] Thu, 19 Mar 2026 16:59:17 UTC (13 KB)
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
