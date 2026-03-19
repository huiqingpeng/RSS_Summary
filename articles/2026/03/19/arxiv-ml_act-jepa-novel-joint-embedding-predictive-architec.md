---
title: "ACT-JEPA: Novel Joint-Embedding Predictive Architecture for Efficient Policy Representation Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2501.14622"
published: "2026-03-19"
fetched: "2026-03-19T13:18:24.482727"
---

Computer Science > Machine Learning
[Submitted on 24 Jan 2025 (v1), last revised 17 Mar 2026 (this version, v4)]
Title:ACT-JEPA: Novel Joint-Embedding Predictive Architecture for Efficient Policy Representation Learning
View PDF HTML (experimental)Abstract:Learning efficient representations for decision-making policies is a challenge in imitation learning (IL). Current IL methods require expert demonstrations, which are expensive to collect. Additionally, they are not explicitly trained to understand the environment. Consequently, they have underdeveloped world models. Self-supervised learning (SSL) offers an alternative, as it can learn a world model from diverse, unlabeled data. However, most SSL methods are inefficient because they operate in raw input space. In this work, we propose ACT-JEPA, a novel architecture that unifies IL and SSL to enhance policy representations. It is trained end-to-end to jointly predict 1) action sequences and 2) latent observation sequences. To learn in latent space, we utilize Joint-Embedding Predictive Architecture, which allows the model to filter out irrelevant details and learn a robust world model. We evaluate ACT-JEPA in different environments and across multiple tasks. Our results show that it outperforms the strongest baseline in all environments. ACT-JEPA achieves up to 40% improvement in world model understanding and up to 10% higher task success rate. Finally, we show that predicting latent observation sequences effectively generalizes to predicting action sequences. This work demonstrates how integrating IL and SSL leads to efficient policy representation learning, an improved world model, and a higher task success rate.
Submission history
From: Aleksandar Vujinovic [view email][v1] Fri, 24 Jan 2025 16:41:41 UTC (412 KB)
[v2] Mon, 27 Jan 2025 16:39:40 UTC (539 KB)
[v3] Wed, 2 Apr 2025 11:15:15 UTC (536 KB)
[v4] Tue, 17 Mar 2026 21:06:45 UTC (83 KB)
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
