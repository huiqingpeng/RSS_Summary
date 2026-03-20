---
title: "Inverse classification with logistic and softmax classifiers: efficient optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2309.08945"
published: "2026-03-20"
fetched: "2026-03-20T14:03:47.602592"
---

Computer Science > Machine Learning
[Submitted on 16 Sep 2023 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Inverse classification with logistic and softmax classifiers: efficient optimization
View PDF HTML (experimental)Abstract:In recent years, a certain type of problems have become of interest where one wants to query a trained classifier. Specifically, one wants to find the closest instance to a given input instance such that the classifier's predicted label is changed in a desired way. Examples of these "inverse classification" problems are counterfactual explanations, adversarial examples and model inversion. All of them are fundamentally optimization problems over the input instance vector involving a fixed classifier, and it is of interest to achieve a fast solution for interactive or real-time applications. We focus on solving this problem efficiently with the squared Euclidean distance for two of the most widely used classifiers: logistic regression and softmax classifier. Owing to special properties of these models, we show that the optimization can be solved in closed form for logistic regression, and iteratively but extremely fast for the softmax classifier. This allows us to solve either case exactly (to nearly machine precision) in a runtime of milliseconds to around a second even for very high-dimensional instances and many classes.
Submission history
From: Miguel Á. Carreira-Perpiñán [view email][v1] Sat, 16 Sep 2023 10:34:40 UTC (799 KB)
[v2] Thu, 19 Mar 2026 05:22:20 UTC (797 KB)
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
