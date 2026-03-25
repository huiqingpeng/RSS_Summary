---
title: "Bounding Box Anomaly Scoring for simple and efficient Out-of-Distribution detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22660"
published: "2026-03-25"
fetched: "2026-03-26T07:16:05.951030"
---

Computer Science > Machine Learning
[Submitted on 24 Mar 2026]
Title:Bounding Box Anomaly Scoring for simple and efficient Out-of-Distribution detection
View PDF HTML (experimental)Abstract:Out-of-distribution (OOD) detection aims to identify inputs that differ from the training distribution in order to reduce unreliable predictions by deep neural networks. Among post-hoc feature-space approaches, OOD detection is commonly performed by approximating the in-distribution support in the representation space of a pretrained network. Existing methods often reflect a trade-off between compact parametric models, such as Mahalanobis-based scores, and more flexible but reference-based methods, such as k-nearest neighbors. Bounding-box abstraction provides an attractive intermediate perspective by representing in-distribution support through compact axis-aligned summaries of hidden activations. In this paper, we introduce Bounding Box Anomaly Scoring (BBAS), a post-hoc OOD detection method that leverages bounding-box abstraction. BBAS combines graded anomaly scores based on interval exceedances, monitoring variables adapted to convolutional layers, and decoupled clustering and box construction for richer and multi-layer representations. Experiments on image-classification benchmarks show that BBAS provides robust separation between in-distribution and out-of-distribution samples while preserving the simplicity, compactness, and updateability of the bounding-box approach.
Submission history
From: Mohamed Bahi Yahiaoui [view email][v1] Tue, 24 Mar 2026 00:25:26 UTC (5,254 KB)
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
