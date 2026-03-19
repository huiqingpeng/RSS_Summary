---
title: "The MCC approaches the geometric mean of precision and recall as true negatives approach infinity"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2305.00594"
published: "2026-03-19"
fetched: "2026-03-19T16:23:14.490623"
---

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 30 Apr 2023 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:The MCC approaches the geometric mean of precision and recall as true negatives approach infinity
View PDF HTML (experimental)Abstract:The performance of a binary classifier is described by a confusion matrix with four entries: the number of true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN). The Matthews Correlation Coefficient (MCC), F1, and Fowlkes-Mallows (FM) scores are scalars that summarize a confusion matrix. Both the F1 and FM scores are based on only three of the four entries in a confusion matrix (they ignore TN). Unlike F1 and FM, the MCC depends on all four entries of the confusion matrix, which can make it attractive in some cases.
However, in some open world settings, measuring the number of true negatives is not straightforward. Object detection is such a case because the number of candidate negative boxes is effectively unbounded. This motivates the question: what is the limit of the MCC as the number of true negatives tends to infinity?
Put plainly, as the true negative count grows, the MCC converges to the FM score, which is the geometric mean of precision and recall. This result was previously noted in the ecology literature in terms of the phi-coefficient and the Ochiai index, but we discuss it in the context of binary classifiers. Furthermore, we provide a full proof of the result, including a Lean formalization. We also briefly comment on the emerging role of LLMs in proof assistance and in locating prior work.
Submission history
From: Jonathan Crall [view email][v1] Sun, 30 Apr 2023 22:36:47 UTC (77 KB)
[v2] Sun, 9 Jul 2023 21:49:30 UTC (22 KB)
[v3] Tue, 17 Mar 2026 21:12:10 UTC (30 KB)
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
