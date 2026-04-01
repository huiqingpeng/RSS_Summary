---
title: "Task Scarcity and Label Leakage in Relational Transfer Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29914"
published: "2026-04-01"
fetched: "2026-04-02T07:21:04.841818"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Task Scarcity and Label Leakage in Relational Transfer Learning
View PDF HTML (experimental)Abstract:Training relational foundation models requires learning representations that transfer across tasks, yet available supervision is typically limited to a small number of prediction targets per database. This task scarcity causes learned representations to encode task-specific shortcuts that degrade transfer even within the same schema, a problem we call label leakage. We study this using K-Space, a modular architecture combining frozen pretrained tabular encoders with a lightweight message-passing core. To suppress leakage, we introduce a gradient projection method that removes label-predictive directions from representation updates. On RelBench, this improves within-dataset transfer by +0.145 AUROC on average, often recovering near single-task performance. Our results suggest that limited task diversity, not just limited data, constrains relational foundation models.
Submission history
From: Francisco Galuppo Azevedo [view email][v1] Tue, 31 Mar 2026 15:55:33 UTC (361 KB)
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
