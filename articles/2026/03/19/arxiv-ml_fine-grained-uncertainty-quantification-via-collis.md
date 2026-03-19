---
title: "Fine-Grained Uncertainty Quantification via Collisions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2411.12127"
published: "2026-03-19"
fetched: "2026-03-19T13:18:14.580283"
---

Computer Science > Machine Learning
[Submitted on 18 Nov 2024 (v1), last revised 18 Mar 2026 (this version, v5)]
Title:Fine-Grained Uncertainty Quantification via Collisions
View PDF HTML (experimental)Abstract:We propose a new and intuitive metric for aleatoric uncertainty quantification (UQ), the prevalence of class collisions defined as the same input being observed in different classes. We use the rate of class collisions to define the collision matrix, a novel and uniquely fine-grained measure of uncertainty. For a classification problem involving $K$ classes, the $K\times K$ collision matrix $S$ measures the inherent difficulty in distinguishing between each pair of classes. We discuss several applications of the collision matrix, establish its fundamental mathematical properties, and show its relationship with existing UQ methods, including the Bayes error rate (BER). We also address the new problem of estimating the collision matrix using one-hot labeled data by proposing a series of innovative techniques to estimate $S$. First, we learn a pair-wise contrastive model which accepts two inputs and determines if they belong to the same class. We then show that this contrastive model (which is PAC learnable) can be used to estimate the row Gramian matrix of $S$, defined as $G=SS^T$. Finally, we show that under reasonable assumptions, $G$ can be used to uniquely recover $S$, a new result on non-negative matrices which could be of independent interest. With a method to estimate $S$ established, we demonstrate how this estimate of $S$, in conjunction with the contrastive model, can be used to estimate the posterior class probability distribution of any point. Experimental results are also presented to validate our methods of estimating the collision matrix and class posterior distributions on several datasets.
Submission history
From: Jesse Friedbaum [view email][v1] Mon, 18 Nov 2024 23:41:27 UTC (2,824 KB)
[v2] Mon, 24 Feb 2025 19:31:27 UTC (3,583 KB)
[v3] Tue, 20 May 2025 17:03:47 UTC (3,789 KB)
[v4] Thu, 24 Jul 2025 00:06:46 UTC (2,302 KB)
[v5] Wed, 18 Mar 2026 04:37:50 UTC (2,424 KB)
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
