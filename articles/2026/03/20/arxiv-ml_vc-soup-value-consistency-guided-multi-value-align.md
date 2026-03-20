---
title: "VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18113"
published: "2026-03-20"
fetched: "2026-03-20T12:08:07.855255"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Language Models
View PDF HTML (experimental)Abstract:As large language models (LLMs) increasingly shape content generation, interaction, and decision-making across the Web, aligning them with human values has become a central objective in trustworthy AI. This challenge becomes even more pronounced when aligning multiple, potentially conflicting human values. Although recent approaches, such as reward reweighting, prompt-based supervised fine-tuning, and model merging, attempt to tackle multi-value alignment, they still face two major limitations: (1) training separate models for each value combination is prohibitively expensive; (2) value conflicts substantially degrade alignment performance. These limitations make it difficult to achieve favorable trade-offs across diverse human values. To address these challenges, we revisit multi-value alignment from the perspective of value consistency in data and propose VC-soup, a data filtering and parameter merging framework grounded in value-consistent learning. We first design a value consistency metric based on the cosine similarity between the reward-gap vector of each preference pair and an all-ones vector, which quantifies its cross-value coherence. We then filter out low-consistency preference pairs in each value dataset and train on the remaining data to obtain smooth, value-consistent policy models that better preserve linear mode connectivity. Finally, we linearly combine these policies and apply Pareto filtering across values to obtain solutions with balanced multi-value performance. Extensive experiments and theoretical analysis demonstrate that VC-soup effectively mitigates conflicts and consistently outperforms existing multi-value alignment methods.
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
