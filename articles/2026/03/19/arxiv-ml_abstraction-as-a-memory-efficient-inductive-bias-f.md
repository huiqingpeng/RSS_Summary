---
title: "Abstraction as a Memory-Efficient Inductive Bias for Continual Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17198"
published: "2026-03-19"
fetched: "2026-03-19T12:08:46.106900"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Abstraction as a Memory-Efficient Inductive Bias for Continual Learning
View PDF HTML (experimental)Abstract:The real world is non-stationary and infinitely complex, requiring intelligent agents to learn continually without the prohibitive cost of retraining from scratch. While online continual learning offers a framework for this setting, learning new information often interferes with previously acquired knowledge, causes forgetting and degraded generalization. To address this, we propose Abstraction-Augmented Training (AAT), a loss-level modification encouraging models to capture the latent relational structure shared across examples. By jointly optimizing over concrete instances and their abstract representations, AAT introduces a memory-efficient inductive bias that stabilizes learning in strictly online data streams, eliminating the need for a replay buffer. To capture the multi-faceted nature of abstraction, we introduce and evaluate AAT on two benchmarks: a controlled relational dataset where abstraction is realized through entity masking, and a narrative dataset where abstraction is expressed through shared proverbs. Our results show that AAT achieves performance comparable to or exceeding strong experience replay (ER) baselines, despite requiring zero additional memory and only minimal changes to the training objective. This work highlights structural abstraction as a powerful, memory-free alternative to ER.
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
