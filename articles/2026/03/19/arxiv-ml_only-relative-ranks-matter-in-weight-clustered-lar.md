---
title: "Only relative ranks matter in weight-clustered large language models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17917"
published: "2026-03-19"
fetched: "2026-03-19T12:18:07.059135"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:Only relative ranks matter in weight-clustered large language models
View PDF HTML (experimental)Abstract:Large language models (LLMs) contain billions of parameters, yet many exact values are not essential. We show that what matters most is the relative rank of weights-whether one connection is stronger or weaker than another-rather than precise magnitudes. To reduce the number of unique weight values, we apply weight clustering to pretrained models, replacing every weight matrix with K shared values from K-means. For Llama 3.1-8B-Instruct and SmolLM2-135M, reducing each matrix to only 16-64 distinct values preserves strong accuracy without retraining, providing a simple, training-free method to compress LLMs on disk. Optionally fine-tuning only the cluster means (centroids) recovers 30-40 percent of the remaining accuracy gap at minimal cost. We then systematically randomize cluster means while keeping assignments fixed. Scrambling the relative ranks of the clusters degrades quality sharply-perplexity can increase by orders of magnitude-even when global statistics such as mean and variance are preserved. In contrast, rank-preserving randomizations cause almost no loss at mid and late layers. On the other hand, when many layers are perturbed simultaneously, progressive layer-by-layer replacement reveals that scale drift-not rank distortion-is the dominant collapse mechanism; however, an affine correction w' = aw + b with a > 0 (which preserves both rank order and overall weight distribution) can substantially delay this drift. This rank-based perspective offers a new lens on model compression and robustness.
Submission history
From: Borja Aizpurua Altuna [view email][v1] Wed, 18 Mar 2026 16:55:13 UTC (167 KB)
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
