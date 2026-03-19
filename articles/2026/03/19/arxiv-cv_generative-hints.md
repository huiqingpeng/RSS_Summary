---
title: "Generative Hints"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.02933"
published: "2026-03-19"
fetched: "2026-03-19T16:27:15.749994"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 4 Nov 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Generative Hints
View PDF HTML (experimental)Abstract:Data augmentation is widely used in vision to introduce variation and mitigate overfitting, by enabling models to learn invariant properties. However, augmentation only indirectly captures these properties and does not explicitly constrain the learned function to satisfy them beyond the empirical training set. We propose generative hints, a training methodology that directly enforces known functional invariances over the input distribution. Our approach leverages a generative model trained on the training data to approximate the input distribution and to produce unlabeled synthetic images, which we refer to as virtual examples. On these virtual examples, we impose hint objectives that explicitly constrain the model's predictions to satisfy known invariance properties, such as spatial invariance. Although the original training dataset is fully labeled, generative hints train the model in a semi-supervised manner by combining the standard classification objective on real data with an auxiliary hint objectives applied to unlabeled virtual examples. Across multiple datasets, architectures, invariance types, and loss functions, generative hints consistently outperform standard data augmentation, achieving accuracy improvements of up to 2.10% on fine-grained visual classification benchmarks and an average gain of 1.29% on the CheXpert medical imaging dataset.
Submission history
From: Andy Dimnaku [view email][v1] Tue, 4 Nov 2025 19:31:36 UTC (2,624 KB)
[v2] Wed, 18 Mar 2026 04:25:05 UTC (2,621 KB)
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
