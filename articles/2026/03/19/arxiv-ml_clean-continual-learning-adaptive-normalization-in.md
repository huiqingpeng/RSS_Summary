---
title: "CLeAN: Continual Learning Adaptive Normalization in Dynamic Environments"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17548"
published: "2026-03-19"
fetched: "2026-03-19T12:13:22.055991"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:CLeAN: Continual Learning Adaptive Normalization in Dynamic Environments
View PDF HTML (experimental)Abstract:Artificial intelligence systems predominantly rely on static data distributions, making them ineffective in dynamic real-world environments, such as cybersecurity, autonomous transportation, or finance, where data shifts frequently. Continual learning offers a potential solution by enabling models to learn from sequential data while retaining prior knowledge. However, a critical and underexplored issue in this domain is data normalization. Conventional normalization methods, such as min-max scaling, presuppose access to the entire dataset, which is incongruent with the sequential nature of continual learning. In this paper we introduce Continual Learning Adaptive Normalization (CLeAN), a novel adaptive normalization technique designed for continual learning in tabular data. CLeAN involves the estimation of global feature scales using learnable parameters that are updated via an Exponential Moving Average (EMA) module, enabling the model to adapt to evolving data distributions. Through comprehensive evaluations on two datasets and various continual learning strategies, including Resevoir Experience Replay, A-GEM, and EwC we demonstrate that CLeAN not only improves model performance on new data but also mitigates catastrophic forgetting. The findings underscore the importance of adaptive normalization in enhancing the stability and effectiveness of tabular data, offering a novel perspective on the use of normalization to preserve knowledge in dynamic learning environments.
Submission history
From: Davide Evangelista [view email][v1] Wed, 18 Mar 2026 09:52:31 UTC (334 KB)
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
