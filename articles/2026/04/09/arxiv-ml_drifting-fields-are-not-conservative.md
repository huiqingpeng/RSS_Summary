---
title: "Drifting Fields are not Conservative"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06333"
published: "2026-04-09"
fetched: "2026-04-10T07:04:56.691133"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:Drifting Fields are not Conservative
View PDF HTML (experimental)Abstract:Drifting models generate high-quality samples in a single forward pass by transporting generated samples toward the data distribution using a vector valued drift field. We investigate whether this procedure is equivalent to optimizing a scalar loss and find that, in general, it is not: drift fields are not conservative - they cannot be written as the gradient of any scalar potential. We identify the position-dependent normalization as the source of non-conservatism. The Gaussian kernel is the unique exception where the normalization is harmless and the drift field is exactly the gradient of a scalar function. Generalizing this, we propose an alternative normalization via a related kernel (the sharp kernel) which restores conservatism for any radial kernel, yielding well-defined loss functions for training drifting models. While we identify that the drifting field matching objective is strictly more general than loss minimization, as it can implement non-conservative transport fields that no scalar loss can reproduce, we observe that practical gains obtained utilizing this flexibility are minimal. We thus propose to train drifting models with the conceptually simpler formulations utilizing loss functions.
Submission history
From: Sebastian Hoffmann [view email][v1] Tue, 7 Apr 2026 18:14:37 UTC (1,806 KB)
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
