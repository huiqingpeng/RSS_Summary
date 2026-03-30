---
title: "Maintaining Difficulty: A Margin Scheduler for Triplet Loss in Siamese Networks Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26389"
published: "2026-03-30"
fetched: "2026-03-31T07:23:49.480038"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:Maintaining Difficulty: A Margin Scheduler for Triplet Loss in Siamese Networks Training
View PDF HTML (experimental)Abstract:The Triplet Margin Ranking Loss is one of the most widely used loss functions in Siamese Networks for solving Distance Metric Learning (DML) problems. This loss function depends on a margin parameter {\mu}, which defines the minimum distance that should separate positive and negative pairs during training. In this work, we show that, during training, the effective margin of many triplets often exceeds the predefined value of {\mu}, provided that a sufficient number of triplets violating this margin is observed. This behavior indicates that fixing the margin throughout training may limit the learning process. Based on this observation, we propose a margin scheduler that adjusts the value of {\mu} according to the proportion of easy triplets observed at each epoch, with the goal of maintaining training difficulty over time. We show that the proposed strategy leads to improved performance when compared to both a constant margin and a monotonically increasing margin scheme. Experimental results on four different datasets show consistent gains in verification performance.
Submission history
From: Paulo Ricardo Lisboa De Almeida [view email][v1] Fri, 27 Mar 2026 13:15:34 UTC (530 KB)
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
