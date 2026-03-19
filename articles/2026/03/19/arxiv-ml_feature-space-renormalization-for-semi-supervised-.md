---
title: "Feature Space Renormalization for Semi-supervised Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2311.04055"
published: "2026-03-19"
fetched: "2026-03-19T13:17:31.658091"
---

Computer Science > Machine Learning
[Submitted on 7 Nov 2023 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Feature Space Renormalization for Semi-supervised Learning
View PDFAbstract:Semi-supervised learning (SSL) has been proven to be a powerful method for leveraging unlabeled data to alleviate models'dependence on large labeled datasets. The common framework among recent approaches is to train the model on a large amount of unlabeled data with consistency regularization to constrain the model predictions to be invariant to input perturbation. This paper proposes a feature space renormalizati-on (FSR) mechanism for SSL, which imposes consistency on feature representations rather than on labels to enable the model to learn better discriminative features. In order to apply this mechanism to SSL, we design a dual-branch FSR module consisting of a dual-branch header and an FSR block. This module can be seamlessly plugged and played into existing SSL frameworks to enhance the performance of the base SSL. The experimental results show that our proposed FSR module helps the base SSL framework (e.g. CRMatch and FreeMatch), achieve better performance on a variety of standard SSL benchmark datasets, without incurring additional overhead in terms of computation time and GPU memory.
Submission history
From: Jun Sun [view email][v1] Tue, 7 Nov 2023 15:07:02 UTC (1,232 KB)
[v2] Wed, 18 Mar 2026 15:24:35 UTC (1,314 KB)
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
