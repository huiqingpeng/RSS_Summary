---
title: "Preconditioned Attention: Enhancing Efficiency in Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27153"
published: "2026-03-31"
fetched: "2026-04-01T07:22:05.916073"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Preconditioned Attention: Enhancing Efficiency in Transformers
View PDF HTML (experimental)Abstract:Central to the success of Transformers is the attention block, which effectively models global dependencies among input tokens associated to a dataset. However, we theoretically demonstrate that standard attention mechanisms in transformers often produce ill-conditioned matrices with large condition numbers. This ill-conditioning is a well-known obstacle for gradient-based optimizers, leading to inefficient training. To address this issue, we introduce preconditioned attention, a novel approach that incorporates a conditioning matrix into each attention head. Our theoretical analysis shows that this method significantly reduces the condition number of attention matrices, resulting in better-conditioned matrices that improve optimization. Conditioned attention serves as a simple drop-in replacement for a wide variety of attention mechanisms in the literature. We validate the effectiveness of preconditioned attention across a diverse set of transformer applications, including image classification, object detection, instance segmentation, long sequence modeling and language modeling.
Submission history
From: Hemanth Saratchandran [view email][v1] Sat, 28 Mar 2026 06:30:45 UTC (918 KB)
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
