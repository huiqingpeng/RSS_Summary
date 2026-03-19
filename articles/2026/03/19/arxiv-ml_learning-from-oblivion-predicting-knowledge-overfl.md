---
title: "Learning from Oblivion: Predicting Knowledge Overflowed Weights via Retrodiction of Forgetting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2508.05059"
published: "2026-03-19"
fetched: "2026-03-19T14:04:50.146669"
---

Computer Science > Machine Learning
[Submitted on 7 Aug 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Learning from Oblivion: Predicting Knowledge Overflowed Weights via Retrodiction of Forgetting
View PDF HTML (experimental)Abstract:Pre-trained weights have become a cornerstone of modern deep learning, enabling efficient knowledge transfer and improving downstream task performance, especially in data-scarce scenarios. However, a fundamental question remains: how can we obtain better pre-trained weights that encapsulate more knowledge beyond the given dataset? In this work, we introduce KNowledge-Overflowed Weights (KNOW) prediction, a novel strategy that leverages structured forgetting and its inversion to synthesize knowledge-enriched weights. Our key insight is that sequential fine-tuning on progressively downsized datasets induces a structured forgetting process, which can be modeled and reversed to recover knowledge as if trained on a larger dataset. We construct a dataset of weight transitions governed by this controlled forgetting and employ meta-learning to model weight prediction effectively. Specifically, our KNowledge-Overflowed Weights Nowcaster (KNOWN) acts as a hyper-model that learns the general evolution of weights and predicts enhanced weights with improved generalization. Extensive experiments across diverse datasets and architectures demonstrate that KNOW prediction consistently outperforms Naive fine-tuning and simple weight prediction, leading to superior downstream performance. Our work provides a new perspective on reinterpreting forgetting dynamics to push the limits of knowledge transfer. The code and pre-trained model are available at this https URL
Submission history
From: Jinhyeok Jang [view email][v1] Thu, 7 Aug 2025 06:23:07 UTC (4,250 KB)
[v2] Wed, 18 Mar 2026 12:44:46 UTC (4,246 KB)
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
