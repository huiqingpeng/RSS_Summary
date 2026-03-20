---
title: "Representation Finetuning for Continual Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.11201"
published: "2026-03-20"
fetched: "2026-03-20T14:12:57.334605"
---

Computer Science > Machine Learning
[Submitted on 11 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Representation Finetuning for Continual Learning
View PDF HTML (experimental)Abstract:The world is inherently dynamic, and continual learning aims to enable models to adapt to ever-evolving data streams. While pre-trained models have shown powerful performance in continual learning, they still require finetuning to adapt effectively to downstream tasks. However, prevailing Parameter-Efficient Fine-Tuning (PEFT) methods operate through empirical, black-box optimization at the weight level. These approaches lack explicit control over representation drift, leading to sensitivity to domain shifts and catastrophic forgetting in continual learning scenarios. In this work, we introduce Continual Representation Learning (CoRe), a novel framework that for the first time shifts the finetuning paradigm from weight space to representation space. Unlike conventional methods, CoRe performs task-specific interventions within a low-rank linear subspace of hidden representations, adopting a learning process with explicit objectives, which ensures stability for past tasks while maintaining plasticity for new ones. By constraining updates to a low-rank subspace, CoRe achieves exceptional parameter efficiency. Extensive experiments across multiple continual learning benchmarks demonstrate that CoRe not only preserves parameter efficiency but also significantly outperforms existing state-of-the-art methods. Our work introduces representation finetuning as a new, more effective and interpretable paradigm for continual learning.
Submission history
From: Haihua Luo [view email][v1] Wed, 11 Mar 2026 18:15:31 UTC (700 KB)
[v2] Thu, 19 Mar 2026 06:17:22 UTC (700 KB)
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
